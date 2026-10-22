---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cyberark-credential-provider/
title: Integrate CyberArk Credential Provider with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:18.093124+00:00
---

# Integrate CyberArk Credential Provider with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cyberark-credential-provider/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate CyberArk Credential Provider with Google SecOps

This document explains how to integrate CyberArk Credential Provider with Google Security Operations (Google SecOps).

## Before you begin

To configure this integration, you must install the CyberArk Credential Provider on a Linux host.

Before you configure the CyberArk Credential Provider integration for Google SecOps, complete the following prerequisites:

  * Install the CyberArk Credential Provider on a Linux host.

  * If you're using a Docker container for the Google SecOps remote agent:

    * Configure the Docker container.

    * Generate an SSH key to securely communicate with the host.




## Integration parameters

The CyberArk Credential Provider integration requires the following parameters:

Parameter | Description  
---|---  
`Path to clipasswordsdk` | Required. The full path to the CLI Application Password SDK. The default value is `/opt/CARKaim/sdk/clipasswordsdk`.  
`Username for Credential Provider for Linux` | Required. The username for the remote agent to authenticate when deployed in a Docker container. The default value is `secopssuser`.  
`Docker Gateway IP Address` | Required. The IP address of the Docker gateway. The default value is `172.17.0.1`.  
`Host Public Key` | Required. The host machine's public key to ensure a secure connection to the correct server and to prevent unauthorized access.  
`SSH Private Key Path` | Optional. The full path to the SSH private key. This is the recommended method for authentication, and if chosen, this parameter is required.  
`Password for Credential Provider for Linux` | Optional. The password for the remote agent to authenticate when deployed in a Docker container.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Use the **Ping** action to test the connectivity to Credential Provider.

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
`Successfully connected to the CyberArk Credential Provider with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the CyberArk Credential Provider! Error is ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Application Password Value

Use the **Get Application Password Value** action to retrieve the application password value from CyberArk Credential Provider.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Application Password Value** action requires the following parameters:

Parameter | Description  
---|---  
`Application` | Required. The application ID from which to retrieve the password value.  
`Safe Name` | Required. The name of the Safe from which to retrieve the password.  
`Folder Name` | Required. The name of the folder from which to retrieve the password.  
`Object Name` | Required. The name of the object from which to retrieve the password.  
`Output` | Required. A comma-separated list of output fields to specify the data to retrieve. The default value is `Password`.  
  
#### Action outputs

The **Get Application Password Value** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Application Password Value** action:
    
    
    {
        "result": "YYYY"
    }
    

##### Output messages

The **Get Application Password Value** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully fetched password value for the application ID APPLICATION_ID.` `The password value for the application ID APPLICATION_ID was not found in the CyberArk Credential Provider.` | The action succeeded.  
`Error executing action "Get Application Password Value": ERROR_REASON.` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Application Password Value** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Run CLI Application Password SDK Command

Use the **Run CLI Application Password SDK Command** action to run a command directly on the CyberArk Credential Provider using the `CLI Application Password SDK` parameter.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Run CLI Application Password SDK Command** action requires the following parameters:

Parameter | Description  
---|---  
`clipasswdsdk Command` | Required. The command for the CLI Application Password SDK to run. Example: `APPID=Application-Password-SDK user=admin safe=safe folder=folder object=object`  
  
#### Action outputs

The **Run CLI Application Password SDK Command** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Run CLI Application Password SDK Command** action:
    
    
    {
       "output_value": "COMMAND_OUTPUT"
    }
    

##### Output messages

The **Run CLI Application Password SDK Command** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully executed the following CLI Application Password SDK command: COMMAND.` | The action succeeded.  
`Error executing the following command: COMMAND.` `Error executing action "Run CLI Application Password SDK Command". Reason: ERROR_REASON.` | The action failed.Check the command syntax, the connection to the server, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Run CLI Application Password SDK Command** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
## Jobs

### Sync Integration Credentials Job

Use the **Sync Integration Credentials Job** to synchronize CyberArk Credential Provider secret manager entries and automatically update integration, connector, and job configurations.

#### Job inputs

The **Sync Integration Credentials Job** requires the following parameters:

Parameter | Description  
---|---  
`Environment Name` | Required. Name of the environment, where to search for credentials. For Shared Environments, provide `*`. The default value is `Default Environment`.  
`Credential Mapping` | Required. A JSON object specifying the component display names, parameter names, and CyberArk Secret Manager entry lookup strings for the credentials you want to synchronize. The target integration instances, connectors, or jobs must already be configured on the platform before running the job. Secret Manager entries use the following format: `AppDescs.AppID=<app_id>;Safe=<safe_name>;Object=<object_name>[;Folder=<folder_name>]` **Generic structure:**
    
    
    {
      "integration_instances": {
        "<integration_instance_display_name>": {
          "<parameter_name>": "AppDescs.AppID=<app_id>;Safe=<safe_name>;Object=<object_name>[;Folder=<folder_name>]"
        }
      },
      "connectors": {
        "<connector_display_name>": {
          "<parameter_name>": "AppDescs.AppID=<app_id>;Safe=<safe_name>;Object=<object_name>[;Folder=<folder_name>]"
        }
      },
      "jobs": {
        "<job_display_name>": {
          "<parameter_name>": "AppDescs.AppID=<app_id>;Safe=<safe_name>;Object=<object_name>[;Folder=<folder_name>]"
        }
      }
    }

**Example configuration:**
    
    
    {
      "integration_instances": {
        "MicrosoftGraphMail_1": {
          "Tenant": "AppDescs.AppID=<app_id>;Safe=<safe_name>;Object=<object_name>;Folder=<folder_name>"
        }
      },
      "connectors": {
        "Microsoft Graph Mail Connector": {
          "Tenant": "AppDescs.AppID=<app_id>;Safe=<safe_name>;Object=<object_name>;Folder=<folder_name>"
        }
      },
      "jobs": {
        "Sync Mail Job": {
          "Tenant": "AppDescs.AppID=<app_id>;Safe=<safe_name>;Object=<object_name>;Folder=<folder_name>"
        }
      }
    }

Note: Integration instance display names are specific to the selected environment and must be unique per environment. Connectors and jobs are independent of environments.  
`Path to clipasswordsdk` | Required. The full path to the CLI Application Password SDK. The default value is `/opt/CARKaim/sdk/clipasswordsdk`.  
`Username for Credential Provider for Linux` | Required. The username for the remote agent to authenticate when deployed in a Docker container. The default value is `secopsuser`.  
`Docker Gateway IP Address` | Required. The IP address of the Docker gateway. The default value is `172.17.0.1`.  
`Host Public Key` | Required. The host machine's public key to ensure a secure connection to the correct server and to prevent unauthorized access.  
`SSH Private Key Path` | Optional. The full path to the SSH private key. This is the recommended method for authentication, and if chosen, this parameter is required.  
`Password for Credential Provider for Linux` | Optional. The password for the remote agent to authenticate when deployed in a Docker container.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
