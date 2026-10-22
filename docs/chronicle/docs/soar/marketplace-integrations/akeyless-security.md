---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/akeyless-security/
title: Integrate Akeyless with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:29.788075+00:00
---

# Integrate Akeyless with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/akeyless-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Akeyless with Google SecOps 

This document explains how to integrate Akeyless with Google Security Operations.

**Note:** In the Google SecOps platform, the integration for Akeyless is called _Akeyless Security_.

## Use cases

The **Akeyless** integration uses Google SecOps capabilities to support the following use cases:

  * **Synchronize integration credentials** : Automatically update credentials and sensitive parameters across Google SecOps integration instances, connectors, and jobs using secrets stored in Akeyless.

  * **Retrieve secrets in playbooks** : Fetch static secrets or specific secret versions from Akeyless on demand during playbook execution to authenticate with external services.

  * **Automate credential rotation** : Propagate rotated API keys, tokens, and passwords from Akeyless to Google SecOps integrations, connectors, and jobs by mapping parameters to the `latest` secret version, preventing disruptions caused by expired credentials.

  * **Control credential updates with version pinning** : Pin integration, connector, or job parameters to a specific secret version in Akeyless to validate credential changes or roll back to a previous version when needed.

  * **Eliminate hardcoded secrets in workflows** : Centralize sensitive credentials in Akeyless instead of embedding them directly in playbook inputs or custom scripts, reducing credential exposure across SOC workflows.




## Before you begin

Before you configure the integration in the Google SecOps platform, verify that you have the following:

  * **API key credentials** : An Akeyless **Access ID** and **Access Key** for authentication.

For more information, see [Akeyless API Key Authentication](https://docs.akeyless.io/docs/auth-with-api-key).

  * **Access permissions** : Read permissions granted to your authentication method for the secrets that Google SecOps retrieves.

For more information, see [Akeyless Role-Based Access Control (RBAC)](https://docs.akeyless.io/docs/rbac).

  * **Network connectivity** : Network access from your Google SecOps instance or remote agent to your Akeyless API Gateway URL.




## Integration parameters

The **Akeyless** integration requires the following parameters:

Parameter | Description  
---|---  
`API Gateway URL` | Optional. The URL of your Akeyless API Gateway. The default value is `https://api.akeyless.io`.  
`Access ID` | Required. The access ID for your Akeyless API key authentication method.  
`Access Key` | Required. The access key associated with your Akeyless access ID.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Akeyless server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Get Secret Value

Use the **Get Secret Value** action to retrieve a secret value from Akeyless for use in playbooks.

This action doesn't run on Google SecOps entities. 

**Note:** To protect sensitive data, the case wall widget displays only the secret name and version. To use the retrieved secret value in subsequent playbook steps, access the `secret_value` field from the action's JSON result.

#### Action inputs

The **Get Secret Value** action requires the following parameters:

Parameter | Description  
---|---  
`Secret Name` | Required. The name or path of the secret to retrieve from Akeyless. To retrieve the latest version, enter `SECRET_NAME` or `SECRET_NAME:latest`. To retrieve a specific version, enter `SECRET_NAME:VERSION_NUMBER`, where `VERSION_NUMBER` is a positive integer (for example, `/prod/api-key:2`).  
  
#### Action outputs

The **Get Secret Value** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Secret Value** action:
    
    
    {
      "secret_name": "/secops/integrations/example-api-key",
      "version": "latest",
      "secret_value": "EXAMPLE_SECRET_VALUE"
    }
    

##### Output messages

On the **Case Wall** , the **Get Secret Value** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully retrieved secret 'SECRET_NAME' (version: 'SECRET_VERSION') from Akeyless Security.` | The action succeeded.  
`Failed to retrieve secret 'SECRET_NAME' (version: 'SECRET_VERSION') from Akeyless Security. Reason: ERROR_REASON` | The action failed. Verify that the secret path and version exist in Akeyless and that your authentication credentials have read access to the secret.  
`Error executing action 'Get Secret Value'. Reason: Invalid credential mapping format for value 'SECRET_NAME'. Expected format: 'secret_name' or 'secret_name:version' (where version is a positive integer or 'latest').` | The action failed. Verify the format of the `Secret Name` parameter.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Secret Value** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Ping

Use the **Ping** action to test connectivity to the Akeyless server.

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

On the **Case Wall** , the **Ping** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Akeyless server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Akeyless server! Reason: ERROR_REASON` | The action failed. Verify your `API Gateway URL`, `Access ID`, `Access Key`, and SSL settings.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
## Jobs

For more information on jobs, see [ Configure a new job](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#configure-a-new-job) and [ Advanced scheduling](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#advanced-scheduling). 

### Sync Integration Credentials Job

Use the **Sync Integration Credentials Job** to automatically synchronize secrets stored in Akeyless with your configured Google SecOps integration instances, connectors, and jobs.

#### Job parameters

The **Sync Integration Credentials Job** requires the following parameters:

Parameter | Description  
---|---  
`API Gateway URL` | Optional. The URL of your Akeyless API Gateway. The default value is `https://api.akeyless.io`.  
`Access ID` | Required. The access ID for your Akeyless API key authentication method.  
`Access Key` | Required. The access key associated with your Akeyless access ID.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Akeyless server. Enabled by default.  
`Environment Name` | Required. The Google SecOps environment where the target integration instances, connectors, and jobs are configured. The default value is `Default Environment`.  
`Credential Mapping` | Required. A JSON or YAML dictionary that maps target integration instances, connectors, and jobs to the Akeyless secrets containing their parameter values. Include at least one mapped parameter under the `integration_instances`, `connectors`, or `jobs` keys. When mapping a parameter, you must reference versions in one of the following ways:

  * **Latest version (`SECRET_NAME` or `SECRET_NAME:latest`)** : Retrieves the latest secret value from Akeyless and updates the mapped parameter each time the job runs.Use this format for secrets that rotate regularly.
  * **Specific version (`SECRET_NAME:VERSION_NUMBER`)** : Retrieves a specific version of the secret, where ` VERSION_NUMBER` is a positive integer (for example, `/secops/prod/jira-api-token:2`).After the parameter is updated to that version, subsequent job runs skip updating the parameter unless you change the mapped secret or version.

To see an example, see Example `Credential Mapping`. The default value is `{"integration_instances": {"Integration_Instance_Name": {"Parameter_Name": "Secret_Name"}}}`.  
  
#### Example `Credential Mapping`

The following example shows how to map parameters for integration instances, connectors, and jobs in the `Credential Mapping` parameter:
    
    
    {
      "integration_instances": {
        "VirusTotal_Prod": {
          "API Key": "/secops/prod/virustotal-api-key"
        },
        "Jira_Instance_1": {
          "API Token": "/secops/prod/jira-api-token:2"
        }
      },
      "connectors": {
        "CrowdStrike Falcon Alerts Connector": {
          "Client Secret": "/secops/prod/crowdstrike-client-secret:latest"
        }
      },
      "jobs": {
        "ServiceNow Sync Closed Cases": {
          "Password": "/secops/prod/servicenow-password:1"
        }
      }
    }
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
