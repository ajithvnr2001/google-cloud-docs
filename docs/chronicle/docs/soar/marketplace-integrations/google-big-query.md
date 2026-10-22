---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-big-query/
title: Integrate BigQuery with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:05.387193+00:00
---

# Integrate BigQuery with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-big-query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate BigQuery with Google SecOps

This document explains how to integrate BigQuery with Google Security Operations.

**Important:** In the Google SecOps platform, the integration for BigQuery is called _Google BigQuery_.

## Use cases

The **BigQuery** integration uses Google SecOps capabilities to support the following use cases:

  * **Threat intelligence enrichment** : Automatically enrich security alerts with threat intelligence data stored in BigQuery to assess the severity and credibility of potential threats.

  * **User behavior analysis** : Identify anomalous user activity by analyzing historical logs stored in BigQuery to detect insider threats and compromised accounts.

  * **Security data lake analysis** : Use BigQuery querying capabilities to analyze large volumes of security data aggregated from various sources to improve threat hunting.

  * **Advanced ML/AI analytics** : Build custom models for predictive defense and automated risk scoring using historical security data and BigQuery ML.

  * **Long-term data retention** : Archive resolved incident data into BigQuery for cost-effective long-term storage, supporting compliance and forensic audits.




## Before you begin

Before you configure the **BigQuery** integration in Google SecOps, complete the following prerequisite steps:

  1. Grant the necessary Identity and Access Management roles to your service account.

  2. Create a service account.

  3. Choose and configure one of the following authentication methods:

     * **Option 1:Workload Identity (recommended)**: This method uses short-lived, temporary access tokens using service account impersonation.

     * **Option 2:Service account JSON key**: This method relies on a static, long-lived secret key file.




### Grant IAM roles

Granting the necessary permissions to your service account lets the integration run jobs and access your data. The following standard roles are managed by Google Cloud and automatically update if API requirements change. To assign these roles to your service account, complete the following steps:

  1. In the Google Cloud console, go to [**IAM**](https://console.cloud.google.com/iam-admin/iam).

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Locate your service account in the list of principals and click **Edit principal** (edit).

  3. Click **Add another role** and select the following:

     * **BigQuery User** (`roles/bigquery.user`): Lets the integration run jobs, including queries, within the project.

     * **BigQuery Data Viewer** (`roles/bigquery.dataViewer`): Lets the integration read data and metadata from datasets and tables.

     * **Service Usage Consumer** (`roles/serviceusage.serviceUsageConsumer`): This is mandatory if you configure `Quota Project ID` in the integration settings.

  4. Click **Save**.




### Create a service account

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click **add Create service account**.

  3. Provide a name and description and click **Create and continue**.

  4. In the **Grant this service account access to project** step, add the roles identified in the previous step.

  5. Click **Done**. Take a note of the service account's **Email address**.




### Configure Workload Identity credentials

Workload Identity is the recommended approach as it uses short-lived access tokens using service account impersonation.

#### Identify the unique instance identity

Establishing a connection requires granting your Google SecOps instance permission to impersonate your service account.

  1. In Google SecOps, go to **Content Hub > Response Integrations**.

  2. Select the **BigQuery** integration and enter your service account email in the `Workload Identity Email` field.

  3. Click **Save > Test**. The test is expected to fail. 

  4. Click the close_small button next to **Test** and locate the identity email beginning with `gke-init-python@...` or `soar-python@...`.

  5. Copy this unique email address.




#### Authorize the instance identity in Google Cloud

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select the target service account and go to **Permissions > Grant Access**.

  3. Paste the unique email address into the **New principals** field and assign the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`).




### Configure a JSON key

Static, long-lived secret key files require manual rotation. Use this method only if Workload Identity authentication isn't available.

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts** and select your service account.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Go to the **Keys** tab and click **Add key > Create new key**.

  3. Select **JSON** and click **Create**. The file automatically downloads to your computer.




#### Configure manual individual parameters

If you choose to enter credentials manually, keep the downloaded JSON key file open in a text editor to copy the individual values required in the integration settings.

## Integration parameters

To establish a connection between Google SecOps and BigQuery, you must configure the following parameters. The integration supports three distinct authentication paths. Choose one of the following methods to provide credentials.

  * **Workload Identity** : Uses `Workload Identity Email` and `Quota Project ID`.

  * **Service account JSON file** : Uses `Service Account Json File Content` to provide the entire key at once.

  * **Manual individual parameters** : Uses separate fields manually copied from a JSON key.


Parameter | Description  
---|---  
`API Root` | Optional. The API root of the BigQuery instance (for example, `https://bigquery.googleapis.com`).  
`Workload Identity Email` | Optional. The client email address of your service account. Use this for Workload Identity authentication.  
`Service Account Json File Content` | Optional. The full content of the service account key JSON file. If you configure this parameter, the integration ignores individual credential parameters.  
`Quota Project ID` | Optional. The project ID used for API usage and billing. This parameter is required when using Workload Identity authentication.  
`Project ID` | Optional. The project ID to target in BigQuery.  
`Verify SSL` | Required. Validates the SSL certificate for the connection. Enabled by default.  
  
### Individual credential parameters

Only use the following parameters if you're manually entering credentials rather than using the full JSON file content or a Workload Identity.

Parameter | Description  
---|---  
`Account Type` | Optional.The value found in the `type` field of your JSON key (typically `service_account`).  
`Private Key ID` | Optional.The value found in the `private_key_id` field of your JSON key.  
`Private Key` | Optional.The value found in the `private_key` field of your JSON key.  
`Client Email` | Optional.The value found in the `client_email` field of your JSON key.  
`Client ID` | Optional.The value found in the `client_id` field of your JSON key.  
`Auth URI` | Optional.The value found in the `auth_uri` field of your JSON key. The default value is `https://accounts.google.com/o/oauth2/auth`.  
`Token URI` | Optional.The value found in the `token_uri` field of your JSON key. The default value is `https://oauth2.googleapis.com/token`.  
`Auth Provider X509 URL` | Optional.The value found in the `auth_provider_x509_cert_url` field of your JSON key.  
`Client X509 URL` | Optional.The value found in the `client_x509_cert_url` field of your JSON key.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Use the **Ping** action to test connectivity to the BigQuery.

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
`Successfully connected to the Google BigQuery server with the provided connection parameters!` | Action succeeded.  
`Failed to connect to the Google BigQuery server! Error is ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Run Custom Query

Use the **Run Custom Query** action to execute custom queries in BigQuery.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Run Custom Query** action requires the following parameters:

Parameters | Description  
---|---  
`Query` | Required.The SQL query to execute.  
`Max Results To Return` | Optional.The number of results to return for every response. The default value is `50`.  
  
#### Action outputs

The **Run Custom Query** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Run Custom Query** action:
    
    
    {
        "Airport_Code": "CODE",
        "Airport_Name": "NAME",
        "Time_Label": "2015/05",
        "Time_Month": 5,
        "Time_Month_Name": "May",
        "Time_Year": 2015,
        "Statistics___of_Delays_Carrier": 351,
        "Statistics___of_Delays_Late_Aircraft": 546,
        "Statistics___of_Delays_National_Aviation_System": 292,
        "Statistics___of_Delays_Security": 2,
        "Statistics___of_Delays_Weather": 100,
        "Statistics_Carriers_Names": "Example Air Lines Inc., Example Airlines Co.",
        "Statistics_Carriers_Total": 3,
        "Statistics_Flights_Cancelled": 88,
        "Statistics_Flights_Delayed": 1289,
        "Statistics_Flights_Diverted": 32,
        "Statistics_Flights_On_Time": 6182,
        "Statistics_Flights_Total": 7591,
        "Statistics_Minutes_Delayed_Carrier": 19332,
        "Statistics_Minutes_Delayed_Late_Aircraft": 34376,
        "Statistics_Minutes_Delayed_National_Aviation_System": 12346,
        "Statistics_Minutes_Delayed_Security": 48,
        "Statistics_Minutes_Delayed_Total": 76163,
        "Statistics_Minutes_Delayed_Weather": 100061
    }
    

##### Output messages

The **Run Custom Query** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully executed query in Google BigQuery!` | Action succeeded.  
`Error executing action "Run Custom Query". Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Run Custom Query** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Run SQL Query

Use the **Run SQL Query** action to execute queries in BigQuery.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Run SQL Query** action requires the following parameters:

Parameters | Description  
---|---  
`Dataset Name` | Required.The name of the dataset to use when executing queries.  
`Query` | Required.The SQL query to execute.  
`Max Results To Return` | Optional.The number of results to return for every response. The default value is `50`.  
  
#### Action outputs

The **Run SQL Query** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Run SQL Query** action:
    
    
    {
        "Airport_Code": "CODE",
        "Airport_Name": "NAME",
        "Time_Label": "2015/05",
        "Time_Month": 5,
        "Time_Month_Name": "May",
        "Time_Year": 2015,
        "Statistics___of_Delays_Carrier": 351,
        "Statistics___of_Delays_Late_Aircraft": 546,
        "Statistics___of_Delays_National_Aviation_System": 292,
        "Statistics___of_Delays_Security": 2,
        "Statistics___of_Delays_Weather": 100,
        "Statistics_Carriers_Names": "Example Airlines Inc.,Example Airlines Co.",
        "Statistics_Carriers_Total": 3,
        "Statistics_Flights_Cancelled": 88,
        "Statistics_Flights_Delayed": 1289,
        "Statistics_Flights_Diverted": 32,
        "Statistics_Flights_On_Time": 6182,
        "Statistics_Flights_Total": 7591,
        "Statistics_Minutes_Delayed_Carrier": 19332,
        "Statistics_Minutes_Delayed_Late_Aircraft": 34376,
        "Statistics_Minutes_Delayed_National_Aviation_System": 12346,
        "Statistics_Minutes_Delayed_Security": 48,
        "Statistics_Minutes_Delayed_Total": 76163,
        "Statistics_Minutes_Delayed_Weather": 100061
    }
    

##### Output messages

The **Run SQL Query** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully executed query in the BigQuery dataset DATASET_NAME.` | Action succeeded.  
`Error executing action "Run SQL Query". Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Run SQL Query** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
