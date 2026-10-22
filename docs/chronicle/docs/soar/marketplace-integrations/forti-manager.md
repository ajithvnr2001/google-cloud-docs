---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/forti-manager/
title: Integrate FortiManager with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:00.769217+00:00
---

# Integrate FortiManager with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/forti-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate FortiManager with Google SecOps 

This document explains how to integrate FortiManager with Google Security Operations.

## Before you begin

Before you configure the integration in the Google SecOps platform, verify that you have the following:

  * **FortiManager API credentials** : A valid username and password with the necessary permissions to manage the Administrative Domains (ADOMs).

  * **FortiManager ADOM license** : A valid ADOM subscription license. This license is mandatory for "write" operations, such as updating firewall policies, managing address groups, or locking and unlocking ADOMs.

    * **Optional workaround** : If you don't have an ADOM license, you can manage your firewalls by connecting to them directly rather than through the manager. 

To implement this alternative, complete the following steps:

      1. Install the **FortiGate** integration from the Content Hub.

      2. Generate a **REST API Admin Key** on the local FortiGate device.

      3. Update your playbooks to use **FortiGate** actions instead of FortiManager actions using the following mapping table.

FortiManager action (Requires ADOM license) | Equivalent FortiGate action (Direct control)  
---|---  
`Add IP to Group` | `[Add Entities To Address Group](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fortigate#add_entities_to_address_group)`  
`Remove IP from Group` | `[Remove Entities from Address Group](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fortigate#remove_entities_from_address_group)`  
`Add URL to URL Filter` | `[Add Entities To Policy](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fortigate#add_entities_to_policy)`  
`Remove URL From URL Filter` | `[Remove Entities From Policy](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fortigate#remove_entities_from_policy)`  
  



## Integration parameters

The FortiManager integration requires the following parameters:

Parameter | Description  
---|---  
`Verify SSL` | Optional. If selected, the integration validates the SSL certificate when connecting to FortiManager.Selected by default.  
`Workflow Mode` | Optional. If selected, the integration uses workflow sessions to execute API requests if FortiManager is configured in workflow mode. Not selected by default.  
`API Root` | Required. The API root of the FortiManager instance, such as `https://IP_ADDRESS/jsonrpc`. The default value is `https://x.x.x.x/jsonrpc`.  
`Username` | Required. The username of the FortiManager account.  
`Password` | Required. The password of the FortiManager account.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action).

### Add IP to Group

Use the **Add IP To Group** action to create a firewall address object and add it to a suitable address group.

This action runs on the Google SecOps `IP Address` entity.

**Important:** This action requires a valid ADOM subscription license. If you don't have this license, use the [FortiGate integration](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fortigate) and its corresponding actions as a workaround.

#### Action inputs

The **Add IP To Group** action requires the following parameters:

Parameter | Description  
---|---  
`ADOM Name` | Required. The administrative domain (ADOM) name to use. The default value is `root`.  
`Address Group Name` | Required. The address group name to add the address object.  
  
#### Action outputs

The **Add IP To Group** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Add IP To Group** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Add URL to URL Filter

Use the **Add URL to URL Filter** action to add a new block record to a URL filter.

This action runs on the Google SecOps `URL` entity.

**Important:** This action requires a valid ADOM subscription license. If you don't have this license, use the [FortiGate integration](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fortigate) and its corresponding actions as a workaround.

#### Action inputs

The **Add URL to URL Filter** action requires the following parameters:

Parameter | Description  
---|---  
`ADOM Name` | Required. The ADOM name to use.The default value is `root`.  
`Url Filter Name` | Required. The URL filter name to add a URL.  
  
#### Action outputs

The **Add URL to URL Filter** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Add URL to URL Filter** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Execute Script

Use the **Execute Script** action to execute an existing script on a device group. To run this action on a single device, provide the virtual domain (VDOM).

This action runs on all Google SecOps entities.

#### Action inputs

The **Execute Script** action requires the following parameters:

Parameter | Description  
---|---  
`ADOM Name` | Required. The ADOM name to execute the script.  
`Policy Package Name` | Required. The full name of the policy package to execute the script, including the package name and any parent folders.  
`Script Name` | Required. The name of the script to execute in FortiManager.  
`Device Name` | Required. The name of the device on which to execute the script.  
`VDOM` | Optional. The VDOM of the device in which to execute the script.  
  
#### Action outputs

The **Execute Script** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Execute Script** action:

Script result name | Value  
---|---  
`task_id` | `TASK_ID`  
  
### Get Task Information

Use the **Get Task Information** action to obtain the task information using the task ID.

This action runs on all Google SecOps entities.

#### Action inputs

The **Get Task Information** action requires the following parameters:

Parameter | Description  
---|---  
`Task ID` | Required. The ID of the FortiManager task for which to retrieve information.  
  
#### Action outputs

The **Get Task Information** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Get Task Information** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test the connectivity to FortiManager.

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
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Remove IP From Group

Use the **Remove IP From Group** action to remove a firewall address object from an address group and delete the firewall address object.

This action runs on the Google SecOps `IP Address` entity.

**Important:** This action requires a valid ADOM subscription license. If you don't have this license, use the [FortiGate integration](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fortigate) and its corresponding actions as a workaround.

#### Action inputs

The **Remove IP From Group** action requires the following parameters:

Parameter | Description  
---|---  
`ADOM Name` | Required. The name of the ADOM to run the action. The default value is `root`.  
`Address Group Name` | Required. The name of the address group from which to remove the address object.  
  
#### Action outputs

The **Remove IP From Group** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Remove IP From Group** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Remove URL From URL Filter

Use the **Remove URL From URL Filter** action to remove a block record from a URL filter.

This action runs on the Google SecOps `URL` entity.

**Important:** This action requires a valid ADOM subscription license. If you don't have this license, use the [FortiGate integration](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fortigate) and its corresponding actions as a workaround.

#### Action inputs

The **Remove URL From URL Filter** action requires the following parameters:

Parameter | Description  
---|---  
`ADOM Name` | Required. The name of the ADOM to run the action. The default value is `root`.  
`Url Filter Name` | Required. The name of the URL filter from which to remove the URL.  
  
#### Action outputs

The **Remove URL From URL Filter** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Remove URL From URL Filter** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
