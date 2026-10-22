---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/wiz/
title: Integrate Wiz with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:19.751578+00:00
---

# Integrate Wiz with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/wiz/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Wiz with Google SecOps

This document explains how to integrate Wiz with Google Security Operations (Google SecOps).

## Before you begin

To use the integration, you need an API Root, Client ID, and Client Secret. 

For more information on how to generate these credentials, see [Service Accounts settings](https://docs.wiz.io/docs/service-accounts-settings).

### Required Service Account permissions and scopes

Ensure that your Wiz Service Account is granted the appropriate API permission scopes for the operations you intend to run in Google SecOps.

#### Read & Query Operations

Operation / Purpose | Used By | Required Permissions / Scopes  
---|---|---  
**Test Connectivity** | Ping Action | `read:issues`  
**Get Issue Details** | Get Issue Details Action | `read:issues`  
`read:posture_issues`  
`read:threat_issues`  
`read:comments`  
**List Resource Vulnerability Findings** | List Resource Vulnerability Findings Action | `read:vulnerabilities`  
**Get Blue Agent Analysis** | Get Blue Agent Analysis Action | `read:threat_issues`  
  
#### Write & Modify Operations (Mutations)

Operation / Purpose | Used By | Required Permissions / Scopes  
---|---|---  
**Reopen Issue** | Reopen Issue Action | `write:issue_status`  
`update:posture_issue_status`  
`write:threat_issue_status`  
**Resolve Issue** | Resolve Issue Action | `write:threat_issue_status`  
`write:threat_issues`  
**Ignore Issue** | Ignore Issue Action | `update:posture_issue_ignore`  
`write:issue_ignore`  
**Add Comment To Issue** | Add Comment To Issue Action | `write:issue_comments`  
`write:threat_issue_comments`  
`write:comments`  
**Note:** If granular scoping is not required by your organization's security policy, a Wiz administrator can alternatively grant the broad permissions `read:all`, `write:all`, and `update:all` to cover all integration operations.

## Integration parameters

The Wiz integration requires the following parameters:

Parameter | Description  
---|---  
`API Root` | Required. The GraphQL API endpoint URL for your Wiz tenant. The endpoint must follow the format `https://api.<region>.app.wiz.io/graphql` (or `https://api.<region>.app.wiz.us/graphql` for Wiz for Gov), where `<region>` represents your assigned Wiz data center region (such as `us1`, `us2`, `eu1`, or `eu2`). Refer to your Wiz tenant details to obtain your exact endpoint URL. Don't use generic, unnumbered regional URLs.  
`Authentication URL` | Optional. The authentication URL used to generate OAuth access tokens. For Commercial environments, use `https://auth.app.wiz.io`. For Wiz for Gov (FedRAMP) environments, use `https://auth.app.wiz.us`. The default value is `https://auth.app.wiz.io`.  
`Client ID` | Required. The client ID associated with your Wiz API credentials.  
`Client Secret` | Required. The client secret associated with your Wiz API credentials.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Wiz server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Use the **Ping** action to test the connectivity to Wiz.

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
Script result. | Available  
  
##### Output messages

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Wiz server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Wiz server! Error is ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Issue Details

Use the **Get Issue Details** action to obtain information about a specified issue in Wiz.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Issue Details** action requires the following parameters:

Parameter | Description  
---|---  
`Issue ID` | Required.The unique identifier of the Wiz issue to retrieve or act upon.  
  
#### Action outputs

The **Get Issue Details** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Issue Details** action:
    
    
    {
       "id": "f54e3fb9-a520-4e99-aacc-b99f6ae7f28d",
       "createdAt": "2025-07-26T11:47:43.94524Z",
       "updatedAt": "2025-07-31T07:34:54.445702Z",
       "status": "RESOLVED",
       "severity": "CRITICAL",
       "type": "TOXIC_COMBINATION",
       "description": "This container is using an image that contains a file identified as a high/critical severity malware by ReversingLabs.\n\nMalware can imply a malicious actor's presence in your environment. The malware can be used for crypto-mining, data leakage, lateral movement to other resources in your environment, etc.",
       "resolvedAt": "2025-07-31T07:34:54.445702Z",
       "entitySnapshot": {
           "cloudPlatform": "GCP",
           "id": "1971f945-3476-5b3d-a5a1-ab166c3e2eca",
           "name": "cluster-solr",
           "region": "us-central1",
           "subscriptionName": "Wiz-Labs",
           "type": "KUBERNETES_CLUSTER"
       },
       "projects": [
           {
               "id": "904cbc14-1c52-571c-a6b8-46fee263eb0f",
               "name": "GCP Lab"
           }
       ],
       "sourceRules": [
           {
               "id": "wc-id-1038",
               "name": "Container using an image infected with critical/high severity malware",
               "description": "This container is using an image that contains a file identified as a high/critical severity malware by ReversingLabs.\n\nMalware can imply a malicious actor's presence in your environment. The malware can be used for crypto-mining, data leakage, lateral movement to other resources in your environment, etc."
           }
       ]
    }
    

##### Output messages

The **Get Issue Details** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned details for the following issue using information from Wiz: ISSUE_ID` `The action wasn't able to return details for the following entities using information from Wiz: ISSUE_ID` | The action succeeded.  
`Error executing action "Get Issue Details". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Issue Details** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Reopen Issue

Use the **Reopen Issue** action to reopen a specified issue in Wiz.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Reopen Issue** action requires the following parameters:

Parameter | Description  
---|---  
`Issue ID` | Required.The unique identifier of the issue in Wiz to retrieve or update.  
  
#### Action outputs

The **Reopen Issue** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Reopen Issue** action:
    
    
    {
        "id": "41facd3f-29b0-4fcf-9a0c-e7fc40416aa0",
        "note": "",
        "status": "OPEN",
        "dueAt": null,
        "resolutionReason": null
    }
    

##### Output messages

The **Reopen Issue** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully reopened issue with ID ISSUE_ID` in Wiz. | The action succeeded.  
`Error executing action "Reopen Issue". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Reopen Issue** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ignore Issue

Use the **Ignore Issue** action to ignore a specified issue in Wiz.

This action doesn't run on Google SecOps entities. 

**Note:** This action only works on Graph Control or Cloud Configuration issues.

#### Action inputs

The **Ignore Issue** action requires the following parameters:

Parameter | Description  
---|---  
`Issue ID` | Required.The unique identifier of the issue in Wiz.  
`Resolution Reason` | Required.The reason for the resolution of the issue. The possible values are as follows:

  * `False Positive`
  * `Exception`
  * `Won't Fix~`

The default value is `False Positive`.  
`Resolution Note` | Optional.A note that gives additional context for the issue resolution.  
  
#### Action outputs

The **Ignore Issue** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Ignore Issue** action:
    
    
    {
        "id": "41facd3f-29b0-4fcf-9a0c-e7fc40416aa0",
        "note": "",
        "status": "REJECTED",
        "dueAt": null,
        "resolutionReason": "FALSE_POSITIVE"
    }
    

##### Output messages

The **Ignore Issue** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully ignored issue with ID ISSUE_ID` in Wiz. | The action succeeded.  
`Error executing action "Ignore Issue". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ignore Issue** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Resolve Issue

Use the **Resolve Issue** action to resolve a specified issue in Wiz.

This action doesn't run on Google SecOps entities. 

**Note:** This action only works on Threat Detection issues.

#### Action inputs

The **Resolve Issue** action requires the following parameters:

Parameter | Description  
---|---  
`Issue ID` | Required.The unique identifier of the issue in Wiz.  
`Resolution Reason` | Required.The reason for the resolution of the issue. The possible values are as follows:

  * `Malicious Threat`
  * `Not Malicious Threat`
  * `Security Test Threat`
  * `Planned Action Threat`
  * `Inconclusive Threat`

The default value is `Not Malicious Threat`.  
`Resolution Note` | Optional.A note that gives additional context about the resolution.  
  
#### Action outputs

The **Resolve Issue** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Resolve Issue** action:
    
    
    {
        "id": "0db2222f-7d1f-501a-9ad5-fe669c7da036",
        "resolutionNote": "",
        "status": "RESOLVED",
        "dueAt": null,
        "resolutionReason": "NOT_MALICIOUS_THREAT"
    }
    

##### Output messages

The **Resolve Issue** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully resolved issue with ID ISSUE_ID` in Wiz. | The action succeeded.  
`Error executing action "Resolve Issue". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Resolve Issue** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Add Comment To Issue

Use the **Add Comment To Issue** action to add a comment to a specified issue in Wiz.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Add Comment To Issue** action requires the following parameters:

Parameter | Description  
---|---  
`Issue ID` | Required.The unique identifier of the issue in Wiz.  
`Comment` | Required.The text of the comment to add to the issue.  
  
#### Action outputs

The **Add Comment To Issue** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Add Comment To Issue** action:
    
    
    {
      "createdAt": "2025-08-01T11:59:00.843434941Z", "id":
      "6f997da2-85a0-4be2-b205-83ea19e9b17a", "text": "testing"
    }
    

##### Output messages

The **Add Comment To Issue** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added a comment to the issue with ID ISSUE_ID` in Wiz. | The action succeeded.  
`Error executing action "Add Comment To Issue". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add Comment To Issue** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Blue Agent Analysis

Use the **Get Blue Agent Analysis** action to obtain analysis details from the Wiz blue agent for a specified threat.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Blue Agent Analysis** action requires the following parameters:

Parameter | Description  
---|---  
`Threat ID` | Required.The unique identifier of the Wiz threat ID.  
  
#### Action outputs

The **Get Blue Agent Analysis** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Blue Agent Analysis** action:
    
    
    {
      "id": "threat-12345",
      "threatType": "MALWARE_DETECTION",
      "status": "COMPLETED",
      "analysis": {
        "summary": "Blue Agent analysis details",
        "riskScore": "HIGH"
      }
    }
    

##### Output messages

The **Get Blue Agent Analysis** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully retrieved blue agent analysis for threat ID THREAT_ID` in Wiz. | The action succeeded.  
`Error executing action "Get Blue Agent Analysis". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Blue Agent Analysis** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
## Jobs

For more information on jobs, see [ Configure a new job](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#configure-a-new-job) and [ Advanced scheduling](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#advanced-scheduling). 

### Wiz and Google SecOps Bi-directional Sync Job

Use the **Wiz and Google SecOps Bi-directional Sync Job** to maintain continuous synchronization between Wiz Threats and Google SecOps cases.

**Note:** This job only supports Google SecOps cases with the `Wiz` tag.

#### Job parameters

The **Wiz and Google SecOps Bi-directional Sync Job** requires the following parameters:

Parameter | Description  
---|---  
`Environment Name` | Required. Name of the environment in which to sync cases. The default value is `Default Environment`.  
`Wiz API Root` | Required. The Wiz GraphQL API endpoint for your tenant. The endpoint must follow the format `https://api.<region>.app.wiz.io/graphql` (or `https://api.<region>.app.wiz.us/graphql` for Wiz for Gov), where `<region>` represents your assigned Wiz data center region (such as `us1`, `us2`, `eu1`, or `eu2`). Refer to your Wiz tenant details to obtain your exact endpoint URL. Don't use generic, unnumbered regional URLs. The default placeholder value is `https://api.<region>.app.wiz.io/graphql`. Replace `<region>` with your assigned Wiz data center region.  
`Wiz Authentication URL` | Optional. The authentication URL used to generate OAuth access tokens. For commercial environments, use `https://auth.app.wiz.io`. For Wiz for Gov (FedRAMP) environments, use `https://auth.app.wiz.us`. The default value is `https://auth.app.wiz.io`.  
`Wiz Client ID` | Required. Client ID for the Wiz API Service Account.  
`Wiz Client Secret` | Required. Client Secret for the Wiz API Service Account.  
`Max Hours Backwards` | Optional. Number of hours before the initial job iteration to retrieve updated cases from (range: 1 to 720, default: 24). This parameter applies to the first job run or as a fallback if the last run timestamp is reset.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Wiz server. Selected by default.  
`Fields to sync` | Required. A comma-separated list of items determining which fields should be synchronized. Only fields explicitly listed here will be synced. Possible values are: `Status`, `Comments`, `Product Link`, `Severity`. The default value is `Status, Comments, Product Link, Severity`.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
