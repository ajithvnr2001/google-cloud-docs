---
url: https://docs.cloud.google.com/apigee/docs/apihub/view-security-scores-multi-gateway/
title: View security scores for multiple Apigee organizations and gateways \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:55:04.700258+00:00
---

# View security scores for multiple Apigee organizations and gateways  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/view-security-scores-multi-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  View security scores for multiple Apigee organizations and gateways Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This page describes how to view security scores for multiple Apigee organizations and gateways. 

## Before you begin

Before you can view security scores across gateways, ensure that you have completed the following: 

  * Enable and configure the Apigee Advanced API Security add-on for your API hub instance. For more information, see [Configure Apigee Advanced API Security for multiple Apigee organizations and gateways](https://docs.cloud.google.com/apigee/docs/apihub/configure-advanced-api-security-multi-gateway). 
  * Grant the required IAM roles and permissions to your principal account. For more information, see [IAM roles and permissions](https://docs.cloud.google.com/apigee/docs/apihub/advanced-api-security-multi-gateway#iam-roles). 
  * Optional: Create a security profile to use for filtering deployments. For more information, see [Manage security profiles for multi-gateway assessments](https://docs.cloud.google.com/apigee/docs/apihub/manage-security-profiles-multi-gateway).

**Key terms:** Before you begin, you should be familiar with the following terms: 

  * **Gateway** : An umbrella term representing a specific API hub plugin instance, combining the plugin type and instance name (for example, `Apigee X - instance_name`). 
  * **Gateway type** : The type of API hub plugin (for example, `Apigee X`). 
  * **Gateway name** : The specific instance name or ID of the API hub plugin (for example, `instance_name`). For Apigee gateways, the instance name corresponds to the Apigee organization name. 
  * **Deployment** : Represents a specific API proxy deployment. You can have multiple deployments (using the same name) for a single API proxy. API hub creates a new deployment for each new API version. 



## View security scores across gateways

The **Security scores** tab in the API hub **Risk assessment** page provides information about all the risk assessments and security scores for your Apigee organizations, environments, and gateways. 

### Console

To view the security scores for API deployments across different Apigee organizations, environments, and gateways, do the following: 

  1. In the Google Cloud console, go to the **API hub > Risk assessment** page. 

[Go to Risk assessment](https://console.cloud.google.com/apigee/api-hub/api-security/risk-assessment)

  2. In the **Risk assessment** page, click the **Security scores** tab.
  3. Click the **Gateway** drop-down and select a gateway for which you want to view the security scores. You can only select **1** gateway at a time. 

The drop-down only lists the runtime projects that you have configured in your Advanced API Security add-on. 

**Note:** The drop-down list only displays the runtime projects that you have configured for your Advanced API Security add-on in your API hub instance. For information about how to add more runtime projects to your Advanced API Security add-on, see [Manage runtime projects and environments for Advanced API Security](https://docs.cloud.google.com/apigee/docs/apihub/configure-advanced-api-security-multi-gateway#manage-api-security-hub). 
  4. Click the **Security profile** drop-down and select the profile which is relevant to your security assessment. For information about creating and managing security profiles, see [Manage security profiles for multi-gateway assessments](https://docs.cloud.google.com/apigee/docs/apihub/manage-security-profiles-multi-gateway). 

The **Security scores** tab displays the security score assessment details and recommendations for the selected gateway and security profile. 




### REST

To get the security scores of your API deployments in different gateways, make a `POST` request to the `securityAssessmentResults:batchCompute` API. 

The following request returns the security scores for all resources in the selected gateway and security profile. 
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)"
    "https://apihub.googleapis.com/v1/organizations/APIGEE_ORG/securityAssessmentResults:batchCompute"
    -X POST -H "Content-Type: application/json" -d '
    {
      "profile": "PROFILE_ID",
      "api_hub_gateways": {
        "gateways": ["GATEWAYS"]
      },
      "include_all_resources": {}
    }'
    

The following request returns the security scores for the selected resource in the selected gateway and security profile. 
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)"
    "https://apihub.googleapis.com/v1/organizations/APIGEE_ORG/securityAssessmentResults:batchCompute"
    -X POST -H "Content-Type: application/json" -d '
    {
      "profile": "PROFILE_ID",
      "api_hub_gateways": {
        "gateways": ["GATEWAYS"]
      },
      "include": {
        "resources": [
          {
            "type": "API_HUB_DEPLOYMENT",
            "name": "DEPLOYMENT_ID"
          }
        ]
      }
    }'
    

Replace the following: 

  * `APIGEE_ORG`: Name of the Apigee organization provisioned in your Google Cloud project.
  * `PROFILE_ID`: The name of the security profile.
  * `GATEWAYS`: The full resource names of the gateways (plugin instances) for which you want to view the security scores. You can only specify 1 gateway using the following format: `projects/API_HUB_HOST_PROJECT/locations/API_HUB_LOCATION/plugins/API_HUB_PLUGIN/instances/API_HUB_INSTANCE`. 
  * `DEPLOYMENT_ID`: The UUID of the API deployment.



## Security score assessment details

The **Security scores** tab aggregates the assessment results for the selected gateway and security profile into three sections: 

  * Deployments by severity
  * Assessment details
  * API deployments



### Deployments by severity

The **Deployments by severity** section displays the total number of API deployments in the selected gateway and security profile grouped by severity. The severity for an API deployment is a direct mapping of the score range of the deployment against the selected security profile. For example, if an API deployment has a calculated security score of 45%, it falls into the 0% - 50% range, and its severity is classified as High. 

The following table shows the severity and score range mapping for the **Deployments by severity** section:

Severity | Score range | Meaning  
---|---|---  
**High** | 0% - 50% | Indicates significant configuration issues or severe risk.  
**Medium** | 51% - 90% | Indicates moderate compliance with the profile.  
**Low** | 91% - 99% | Indicates near full compliance with the profile.  
**Minimal** | 100% | Indicates full compliance with the profile.  
  
The following image shows the **Deployments by severity** section for the **Security scores** tab:

![Deployments by severity screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/risk-assessment/severity.png)![Deployments by severity screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/risk-assessment/severity.png)

### Assessment details

The **Assessment details** section displays the total number of API deployments that are included in the selected gateway and security profile along with the assessment date and time. 

The following image shows the **Assessment details** section for the **Security scores** tab:

![Assessment details screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/risk-assessment/assessment_details.png)![Assessment details screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/risk-assessment/assessment_details.png)

### API deployments

The **API deployments** section displays the following assessment details for each deployed API proxy in the selected gateway and security profile: 

Assessment | Description  
---|---  
**Deployment** | Represents a specific API proxy deployment. You can have multiple deployments (using the same name) for a single API proxy. API hub creates a new deployment for each new API version.  
**Gateway type** | The type of gateway hosting the deployment (for example, `Apigee X`).  
**Gateway name** | The specific instance name or ID of the gateway hosting the deployment (for example, `instance_name`). For Apigee gateways, the instance name corresponds to the Apigee organization name.  
**Severity** | The risk level of the deployment.  
**Score** | The compliance percentage of the deployment against the selected security profile.  
**Failed assessment by weight** | A breakdown showing the number of assessment checks that failed, grouped by their assigned significance.  **Major** failures carry approximately 15 points, **Moderate** failures carry approximately 5 points, and **Minor** failures carry approximately 1 point towards the weighted score calculation.  **Note:** The weight points assigned to each failure may vary based on the number of assessment checks in your security profile.   
**Recommendations** | The count of specific, actionable steps needed to fix identified security vulnerabilities and improve the score.  
  
The following image shows the **API deployments** section for the **Security scores** tab:

![API deployments screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/risk-assessment/api_deployments.png)![API deployments screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/risk-assessment/api_deployments.png)

## View recommendations

To view recommendations for improving your API proxy security scores, do the following: 

  1. In the **Security scores** tab, go to the **API deployments** section.
  2. For the API deployment for which you want to view the recommendations, click the count displayed under the **Recommendations** column. 

The **Recommendations** pane displays the specific recommendations along with the number of API proxies that are affected by the recommendation. 

  3. Optional: Click **Edit proxy** to open the Apigee UI and modify the deployment (proxy) to address the security issues identified by the recommendation. **Note:** The **Edit proxy** button is only available for Apigee X and Apigee hybrid deployments. For other environments, do the following: 
     * **Apigee Edge Public Cloud:** Log in to the Apigee Edge Management Console and directly edit the deployment (proxy).
For more information on deploying proxies, see [Deploy API proxies using the UI](https://docs.apigee.com/api-platform/deploy/deploying-proxies-ui). 

The following image shows the **Recommendations** pane for the **Security scores** tab:

![Recommendations screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/risk-assessment/recommendations.png)![Recommendations screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/risk-assessment/recommendations.png)




## Limitations

  * Security scores are only generated if an environment has deployed proxies.
  * The maximum number of gateways per security score calculation: 
    * Using the API: 3
    * Using the Google Cloud console: 1
  * Newly deployed proxies and newly enabled organizations and environments don't immediately show scores. See [Data delays](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#data-delays) for information.



## Considerations

  * Security score calculations may take a few minutes to complete depending on the number of API deployments in the selected gateway and security profile. 



## What's next

  * Learn how to [manage security profiles](https://docs.cloud.google.com/apigee/docs/apihub/manage-security-profiles-multi-gateway) for your multi-gateway setup. 
  * Learn how to view security scores for a given API across its deployments in gateways, see [View security scores for APIs](https://docs.cloud.google.com/apigee/docs/apihub/view-api-security-scores).
  * Learn how to [manage runtime projects and environments for Advanced API Security](https://docs.cloud.google.com/apigee/docs/apihub/configure-advanced-api-security-multi-gateway#manage-api-security-hub).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
