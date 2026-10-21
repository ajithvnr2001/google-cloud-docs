---
url: https://docs.cloud.google.com/recommender/docs/recent-change-recommendations/
title: Recent change recommendations \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:02:19.147733+00:00
---

# Recent change recommendations  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/recent-change-recommendations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Reference ](https://docs.cloud.google.com/recommender/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Recent change recommendations

**Preview — Recent change recommendations**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Recent change recommendations automatically flag risky changes made recently to cloud resources identified as important based on their usage and other signals to help detect and mitigate issues, like service outages, caused by misconfigurations of those important cloud resources. For example, if you deleted a highly used project, recent change recommendations can help identify unintended issues by proactively warning you about the risks associated with a given change.

## Scope

The recent change recommendations only support the resources and actions listed in the following table.

Resource | Action | Recommendation Scope/Level | Surfaces | Criteria used to determine resource importance  
---|---|---|---|---  
Project | Deletion | Organization | 
* Google Cloud CLI
* Recommender API
* Cloud Logging (opt-in)
| 
* Project usage (API calls, networking traffic, and Google Cloud services usage)
* Billing
* Usage within the last 30 days  
Service account | Deletion | Project | 
* Google Cloud CLI
* Recommender API
* Cloud Logging (opt-in)
| 
* Number of authentications
* Usage within the last 90 days  
  
To provide feedback on this capability overall or request additional resources and actions you'd like to see supported in future releases, see Troubleshooting, feedback and support.

## Before you begin

  1. [Enable the Recommender API](https://docs.cloud.google.com/recommender/docs/enable-api) on a single billing project. You can then use this same billing project to retrieve recommendations and insights for other projects, the entire organization or the billing account, using the billing-project functionality of gcloud/API.

  2. Grant permissions on the user or service account that you will be used for accessing this feature.




## Permissions

To view the recommendations for recent change recommendations, you must have the specific permissions for the recent change recommender.

  * `recommender.cloudRecentChangeRecommendations.get`
  * `recommender.cloudRecentChangeRecommendations.list`
  * `recommender.cloudRecentChangeInsights.get`
  * `recommender.cloudRecentChangeInsights.list`



You can also grant [roles/recommender.viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.viewer) role to cover these permissions.

## View recent change recommendations

The following sections describe how to view recent change recommendations for supported actions.

### Project deletion

### API

  * ListRecommendation:
        
        curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "x-goog-user-project: PROJECT_ID " \
        "https://recommender.googleapis.com/v1/organizations/ORGANIZATION_ID /locations/global/\
        recommenders/google.cloud.RecentChangeRecommender/recommendations"
        

Replace the following:

    * `PROJECT_ID `: The project ID of a project where you've enabled the Recommender API.
    * `ORGANIZATION_ID `: The organization ID of organization you want to see the recent change risk recommendations.
  * ListInsight:
        
        curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "x-goog-user-project: PROJECT_ID " \
        "https://recommender.googleapis.com/v1/organizations/ORGANIZATION_ID /locations/global/insightTypes/google.cloud.RecentChangeInsight/insights"
        

Replace the following:

    * `PROJECT_ID `: The project ID of a project where you've enabled the Recommender API.
    * `ORGANIZATION_ID `: The organization ID of organization you want to see the recent change risk recommendations.



###  Google Cloud CLI 

  * ListRecommendation:
        
        gcloud recommender recommendations list --recommender=google.cloud.RecentChangeRecommender \
          --organization=ORGANIZATION_ID  --location=global --format=yaml
        

Replace the following:

    * `ORGANIZATION_ID `: The organization ID of organization you want to see the recent change risk recommendations.
  * ListInsight
        
        gcloud recommender insights list --insight-type=google.cloud.RecentChangeInsight \
          --organization=ORGANIZATION_ID  --location=global --format=yaml
        

Replace the following:

    * `ORGANIZATION_ID `: The organization ID of organization you want to see the recent change risk recommendations.



### Service account deletion

### API

  * ListRecommendation:
        
        curl -H "Authorization: Bearer $(gcloud auth print-access-token)"\
        "https://recommender.googleapis.com/v1/projects/PROJECT_ID /locations/global/\
        recommenders/google.cloud.RecentChangeRecommender/recommendations"
        

Replace the following:

    * `PROJECT_ID `: The project ID of a project where you've enabled the Recommender API.
  * ListInsight:
        
        curl -H "Authorization: Bearer $(gcloud auth print-access-token)"\
        -H "x-goog-user-project: BILLING_PROJECT_ID "\
        "https://recommender.googleapis.com/v1/projects/PROJECT_ID /locations/global/insightTypes/google.cloud.RecentChangeInsight/insights"
        

Replace the following:

    * `PROJECT_ID `: The project ID of a project where you've enabled the Recommender API.
    * `BILLING_PROJECT_ID `: The billing project ID.



###  Google Cloud CLI 

  * ListRecommendation:
        
        gcloud recommender recommendations list --recommender=google.cloud.RecentChangeRecommender \
          --project=PROJECT_ID  --location=global --format=yaml
        

Replace the following:

    * `PROJECT_ID `: The project ID of a project where you've enabled the Recommender API.
  * ListInsight
        
        gcloud recommender insights list --insight-type=google.cloud.RecentChangeInsight \
          --project=PROJECT_ID  --location=global --format=yaml
        

Replace the following:

    * `PROJECT_ID `: The project ID of a project where you've enabled the Recommender API.



## Understand the response

The following tables provide a description of the fields present in the recommendation and insight objects.

### Recommendations

Field name | Type | description  
---|---|---  
`associatedInsights` | string | Insight that is associated with this recommendation.  
`asset` | object | Contains the asset name and asset type of the associated resource.  
`etag` | string | Fingerprint of the RecommenderConfig. Provides optimistic locking when updating.  
`lastRefreshTime` | string | Timestamp of the last time when the recommendation was updated.  
A timestamp in RFC 3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2022-01-10T22:47:38.421626Z".   
  
### Insights

Field name | Type | description  
---|---|---  
`associatedRecommendations` | string | Recommendation that is associated with this recommendation.  
`projects/[project_number]/locations/global/recommenders/google.cloud.RecentChangeRecommender/recommendations/[recommendation_id]`  
`importance` | object | Contains the reasons why we determined this resource to be important.  
`risk` | object | Contains some miscellaneous data that was relevant in discovering the importance of the resource.  
`lastRefreshTime` | string | Timestamp of the last time when the recommendation was updated.  
A timestamp in RFC 3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2022-01-10T22:47:38.421626Z".   
  
## Log recent change recommendations

Optionally, you can use [Cloud Logging](https://docs.cloud.google.com/logging) to create a log whenever a new recent change recommendation occurs. Note that these logs are [platform logs](https://docs.cloud.google.com/logging/docs/api/platform-logs), so additional charges apply for such logs. The logging is turned off by default. You must enable logging using the recommender config to generate logs.

Recommendation type | Logging Scope  
---|---  
Risky project deletion | Organization level  
Risky service account deletion | Project level  
  
The logging scope for a recommendation corresponds to the recommendation scope. You can enable logging for an organization or a project separately. The recommendation logging config is not inherited from an organization to a project for this feature. To generate service account deletion recommendations logging, you must enable logging for the corresponding project.

To viewCloud Logging (if enabled) you need [Logs Viewer](https://docs.cloud.google.com/logging/docs/access-control#logging.viewer) permissions.

### Logging configuration

To view and update recommender configuration, you must have the following permissions:

  * `recommender.cloudRecentChangeRecommenderConfig.get`
  * `recommender.cloudRecentChangeRecommenderConfig.list`
  * `recommender.cloudRecentChangeRecommenderConfig.update`



### Enable logging

Use the `--project` flag to enable logging for a project or the `--organization` flag to enable logging for an organization. The following examples show how to enable logging for a project.

  1. Check `enable_creation_logs` param in the `recommenderGenerationConfig`:
         
         gcloud recommender recommender-config describe google.cloud.RecentChangeRecommender \
           --project=PROJECT_ID  --location=global
         

Replace the following:

     * `PROJECT_ID `: The project ID of a project where you've enabled the Recommender API.

The output is similar to the following:
    
    <pre class="console">
    etag: '"******"'
    recommenderGenerationConfig:
      params:
        enable_creation_logs: false
    …
    </pre>
    

  2. Create a `config.txt`` file that contains the following lines:
         
         {
           "params": {
             "enable_creation_logs": true
           }
         }
         

  3. Update the param:
         
         gcloud recommender recommender-config update google.cloud.RecentChangeRecommender \
           --project=PROJECT_ID  --location=global --config-file=config.txt \
           --etag="ETAG "
         

Replace the following:

     * `PROJECT_ID `: The project ID of a project where you've enabled the Recommender API.
     * `ETAG `: Where ETAG is the value from the previous describe command.



## Troubleshooting, feedback, and support

Email active-assist-feedback@google.com in case of technical issues, questions or feedback.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
