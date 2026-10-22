---
url: https://docs.cloud.google.com/apigee/docs/apihub/manage-monitoring-conditions-multi-gateway/
title: Manage monitoring conditions for multiple Apigee organizations and gateways \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:47:19.173652+00:00
---

# Manage monitoring conditions for multiple Apigee organizations and gateways  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/manage-monitoring-conditions-multi-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage monitoring conditions for multiple Apigee organizations and gateways Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This page describes how to create and manage monitoring conditions for your [Apigee Advanced API Security add-on](https://docs.cloud.google.com/apigee/docs/apihub/advanced-api-security-multi-gateway) in API hub.

Monitoring conditions allow you to track and analyze the security posture of your API deployments, using [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).

Use monitoring conditions for:

  * Continuous visibility: Gain real-time and historical insights into your API security posture across different gateways.
  * Proactive regression detection: Identify any drops in security scores, which might indicate new vulnerabilities or misconfigurations.
  * Trend analysis: Analyze security score trends over time to understand the effectiveness of your security policies and remediation efforts.
  * Centralized monitoring and alerting: Utilize Cloud Monitoring to consolidate security metrics with other operational data. You can also configure alerts to notify you when security scores deviate from your expectations. 



## Before you begin

  * Enable and configure the Apigee Advanced API Security add-on for your API hub instance. For more information, see [Configure Apigee Advanced API Security for multiple Apigee organizations and gateways](https://docs.cloud.google.com/apigee/docs/apihub/configure-advanced-api-security-multi-gateway). 
  * Grant the required IAM roles and permissions to your principal account. For more information, see [IAM roles and permissions](https://docs.cloud.google.com/apigee/docs/apihub/advanced-api-security-multi-gateway#iam-roles). 
  * In addition to the IAM roles and permissions, if you will be managing monitoring conditions and alerts, you must have the additional permissions or follow the steps for managing monitoring conditions and alerts described in [Required roles for risk assessment](https://docs.cloud.google.com/apigee/docs/api-security/enable-security#required-roles-for-risk-assessment)
  * Learn about Cloud Monitoring features and functionality. See the [Cloud Monitoring overview](https://docs.cloud.google.com/monitoring/docs/monitoring-overview). 
  * If you are using the APIs to manage monitoring conditions, see the API Reference documentation at [organizations.securityMonitoringConditions](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.securityMonitoringConditions). 



## List monitoring conditions

You can view the list of all monitoring conditions that exist for your APIs in your API hub instance. 

### Console

To view the list of existing monitoring condition configurations, go to the **API hub > Risk assessment** page and select the **Monitoring conditions** tab.

Select the gateway for which you want to view the list of monitoring conditions from the **Gateway** selector at the top of the page.

To view the details of a specific monitoring condition, including which deployments are monitored, click the **Monitored deployments/total deployed** value in the row for that security profile. The following monitoring condition details display: 

  * **Gateway:** the gateway or gateways where the monitoring condition applies. This field also shows your Apigee project name.
  * **Security profile:** the monitored security profile.
  * **Fetched data time:** the local date and time when the monitoring data was fetched.
  * **Deployments:** the monitored deployments. 
    * **Deployment:** the deployment name.
    * **Source environment:** the environment where the proxy is deployed.
    * **Status:** the status of the deployment. If a deployment is monitored, it has a `Monitored` status. Otherwise, it has a `Not Monitored` status.



### REST

To view the list of configured monitoring conditions, make a `GET` request to the `securityMonitoringConditions` API. 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/APIGEE_ORG/securityMonitoringConditions?risk_assessment_type=API_HUB" \
      -X GET \
      -H "Authorization: Bearer $TOKEN"
        

To view the list of monitoring conditions for a specific gateway, send a `GET` request as follows: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/APIGEE_ORG/securityMonitoringConditions?risk_assessment_type=API_HUB&filter=api_hub_gateway%3DGATEWAY_ID" \
      -X GET \
      -H "Authorization: Bearer $TOKEN"
        

To view the list of monitoring conditions for a specific security profile, send a `GET` request as follows: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/APIGEE_ORG/securityMonitoringConditions?risk_assessment_type=API_HUB&filter=profile%3DPROFILE_ID" \
      -X GET \
      -H "Authorization: Bearer $TOKEN"
        

To see details on a specific monitoring condition, use the following `GET` request: 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/APIGEE_ORG/securityMonitoringConditions/CONDITION_ID?risk_assessment_type=API_HUB" \
      -X GET \
      -H "Authorization: Bearer $TOKEN"
        

Replace the following: 

  * `APIGEE_ORG`: Name of the Apigee organization provisioned in your Google Cloud project.
  * `GATEWAY_ID`: The name of the gateway. One of: `apigee-x`, `apigee-hybrid`, `apigee-edge-cloud`, `apigee-edge-private-cloud`.
  * `PROFILE_ID`: The name of the security profile.
  * `CONDITION_ID`: The ID of the monitoring condition.



## Create a monitoring condition

Create monitoring conditions on your security profiles to track and analyze API deployments. 

### Console

To create a monitoring condition: 

  1. In the Google Cloud console, go to the **API hub > Risk assessment** page. 

[Go to Risk assessment](https://console.cloud.google.com/apigee/api-hub/api-security/risk-assessment)

  2. In the **Risk assessment** page, click the **Monitoring conditions** tab.
  3. Select the gateway for which you want to create the monitoring condition from the **Gateway** selector at the top of the page.
  4. Click add_box **Create monitoring condition**. The **Create monitoring condition** panel appears. 
  5. The **Gateway** field shows the gateway or gateways where the monitoring condition will apply. This field also shows your Apigee project name. The **Gateway** field is auto-populated based on your **Gateway** selection in the main page and is not editable. 
  6. Select a **Security profile**. **Note:** Only one monitoring condition can be created per security profile. If a monitoring condition already exists for the selected security profile, you can't create another one.
  7. In the **Deployments to monitor** section, select whether to include all deployments or selected deployments: 
     * **Monitor all deployments (current and future):** selects all current and future deployments in the Apigee project.
     * **Monitor specific deployments:** monitors only the deployments you select from the list.
  8. Click **Create** to save your changes or **Close** to exit without saving changes. 

The monitoring condition is created and you are returned to the **Monitoring conditions** tab. 




### REST

To create a monitoring condition, make a `POST` request to the `securityMonitoringConditions` API. When creating a monitoring condition, you must set `risk_assessment_type` to `API_HUB`. 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/APIGEE_ORG/securityMonitoringConditions?security_monitoring_condition_id=CONDITION_ID" \
      -X POST \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "profile": "PROFILE_ID",
        "risk_assessment_type": "API_HUB",
        "api_hub_gateway": "GATEWAY_NAME",
        "include_all_resources": {}
      }'
    

Replace the following: 

  * `APIGEE_ORG`: Name of the Apigee organization provisioned in your Google Cloud project.
  * `CONDITION_ID`: The ID of the monitoring condition.
  * `PROFILE_ID`: The name of the security profile.
  * `GATEWAY_NAME`: The full resource name of the gate (plugin instance). For example, `projects/sense-staging-test/locations/us-west1/plugins/system-apigee-x-and-hybrid/instances/2b355bf9-4466-484b-afbe-e50916940762`.



## Edit a monitoring condition

You can edit an existing monitoring condition to update its monitored deployments. 

### Console

To edit a monitoring condition, do the following: 

  1. Go to the **API hub > Risk assessment** page. 

[Go to Risk assessment](https://console.cloud.google.com/apigee/api-hub/api-security/risk-assessment)

  2. In the **Risk assessment** page, click the **Monitoring conditions** tab.
  3. Select the gateway for which you want to edit the monitoring condition from the **Gateway** selector at the top of the page.
  4. Find the monitoring condition that you want to edit in the table shown.
  5. In the row for the monitoring condition, select **Edit** in the **Actions** menu.
  6. In the **Edit monitoring condition** panel, make the required edits to the assessment configurations. Only the selected deployments can be edited. If you need to edit other settings such as the security profile, create a new monitoring condition instead of editing.
  7. Click **Save** to save your changes.



### REST

To edit a monitoring condition, make a `PATCH` request to the `securityMonitoringConditions` API. You can use `update_mask` to specify which field to update. The `update_mask` could be empty (which defaults to all non-empty fields set in the request), or one of the following: `include`, `include_all_resources`, or `*` (everything). This example uses an update mask to update a monitoring condition so that it includes specific deployments instead of all deployments. 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/APIGEE_ORG/securityMonitoringConditions/CONDITION_ID?update_mask=include" \
      -X PATCH \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-Type: application/json" \
      -d '{
        "risk_assessment_type": "API_HUB",
        "include": {
          "resources": [
            {
              "type": "API_HUB_DEPLOYMENT",
              "name": "DEPLOYMENT_ID_1"
            },
            {
              "type": "API_HUB_DEPLOYMENT",
              "name": "DEPLOYMENT_ID_2"
            }
          ]
        }
      }'
    

Replace the following: 

  * `APIGEE_ORG`: Name of the Apigee organization provisioned in your Google Cloud project.
  * `CONDITION_ID`: The ID of the monitoring condition. Obtain the condition ID by using List monitoring conditions.
  * `DEPLOYMENT_ID_1`, `DEPLOYMENT_ID_2`: The names of the deployments to monitor.



## View Cloud Monitoring for a monitoring condition

Once you've created a monitoring condition, you can load the Google Cloud Cloud Monitoring Metrics Explorer for the monitored condition.

Follow these steps to view Cloud Monitoring for a monitoring condition:

  1. Go to the **API hub > Risk assessment** page. 

[ Go to Risk assessment](https://console.cloud.google.com/apigee/api-hub/api-security/risk-assessment)

  2. In the **Risk assessment** page, click the **Monitoring conditions** tab.
  3. Select the gateway with your monitoring condition from the **Gateway** selector at the top of the page.
  4. In the **Deployment monitoring conditions** table, find the monitoring condition. If you need to create the monitoring condition, see Create a monitoring condition.
  5. Click **View** under **Cloud Monitoring** in the row for the monitoring condition. This loads the Cloud Monitoring dashboard.



## Delete a monitoring condition

Deleting a monitoring condition stops the monitored metrics from publishing to Cloud Monitoring. 

**Warning:** Deleting a monitoring condition stops the publishing of new score metrics to Cloud Monitoring for the security profile and gateway. However, deleting the monitoring condition doesn't delete any alerts you have created in Cloud Monitoring. You must remove those separately. 

### Console

To delete a monitoring condition, do the following: 

  1. Go to the **API hub > Risk assessment** page. 

[Go to Risk assessment](https://console.cloud.google.com/apigee/api-hub/api-security/risk-assessment)

  2. In the **Risk assessment** page, click the **Monitoring conditions** tab.
  3. Select the gateway for which you want to delete the monitoring condition from the **Gateway** selector at the top of the page.
  4. In the row for the monitoring condition that you want to delete, select **Delete** in the **Actions** menu.
  5. Verify the security profile name associated with the monitoring condition and click **Confirm** to confirm the deletion.



### REST

To delete a monitoring condition, make a `DELETE` request to the `securityMonitoringConditions` API. 
    
    
    curl "https://apigee.googleapis.com/v1/organizations/APIGEE_ORG/securityMonitoringConditions/CONDITION_ID?risk_assessment_type=API_HUB" \
      -X DELETE \
      -H "Authorization: Bearer $TOKEN"
    

Replace the following: 

  * `APIGEE_ORG`: Name of the Apigee organization provisioned in your Google Cloud project.
  * `CONDITION_ID`: The ID of the monitoring condition. Obtain the condition ID by using List monitoring conditions.



## Configure monitoring alerts

Create and manage monitoring alerts from your API hub.

To configure monitoring alerts, do the following:

  1. Create the monitoring condition to create alerts from, if not already created. See Create a monitoring condition.
  2. Go to the **API hub > Risk assessment** page. 

[ Go to Risk assessment](https://console.cloud.google.com/apigee/api-hub/api-security/risk-assessment)

  3. In the **Risk assessment** page, click the **Monitoring conditions** tab.
  4. Select the gateway where the monitoring condition you want to configure monitoring alerts from the **Gateway** selector at the top of the page.
  5. Click **Create monitoring alert** in the **Actions** menu in the row for the existing monitoring alert.
  6. This loads the **Create alerting policy** page in Google Cloud console, with related metrics pre-populated for you. Follow the instructions in [Alerting policies overview](https://docs.cloud.google.com/monitoring/alerts) to create and manage alerting policies.



## Limitations

The following limitations apply to monitoring conditions: 

  * Only one monitoring condition can exist for a security profile and gateway combination. If a profile is already part of an existing monitoring condition for the gateway selected, you can't create a new condition on the same security profile.
  * Only deployed APIs are monitored. If a proxy that is included in a monitoring condition is undeployed, it isn't monitored and doesn't show as monitored in the monitoring condition details. On redeploy, the proxy is automatically monitored and shows as monitored in the monitoring condition details.
  * You can create a maximum of 200 security monitoring conditions per organization.
  * New scores that are tracked by a security monitoring condition might take up to 5 minutes to show in Cloud Monitoring.
  * Security scores are available in Cloud Monitoring for up to 6 weeks. See [Data retention](https://docs.cloud.google.com/monitoring/quotas#data_retention_policy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
