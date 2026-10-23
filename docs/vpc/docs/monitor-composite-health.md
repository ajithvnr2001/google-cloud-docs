---
url: https://docs.cloud.google.com/vpc/docs/monitor-composite-health/
title: Monitor Composite Health \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:13.634932+00:00
---

# Monitor Composite Health  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/monitor-composite-health/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor Composite Health

This page shows how to monitor the health of published services that use Composite Health. You can do the following:

  * **Monitor current health states** : Check the real-time health state of a published service or an individual backend service.
  * **View logs for health state transitions** : Use Cloud Logging to view log entries that record changes in health states for monitored resources.



You monitor published services through their associated composite health checks, and you monitor individual backend services through their associated health sources. Service consumers can view logs for Private Service Connect NEGs that connect to published services that use Composite Health.

Composite Health uses the following states to represent the health of published services and backend services.

Health state | Monitored resource | Description  
---|---|---  
`HEALTHY` | Health source | The associated backend service is healthy as defined by its health aggregation policy.  
Composite health check | The published service is healthy because each of its associated health sources is healthy.  
Private Service Connect NEG | The associated published service is healthy as defined by the producer's composite health check.  
`UNHEALTHY` | Health source | The backend service does not meet the criteria defined by its health aggregation policy.  
Composite health check | The published service is unhealthy because one or more of the associated health sources are unhealthy.  
Private Service Connect NEG | The associated published service is unhealthy as defined by the producer's composite health check; this status can trigger cross-region failover.  
`UNKNOWN` | Health source | The health state is not available yet. This is a transient state that occurs when resources are newly created or configured.  
Composite health check | No associated health sources are unhealthy, but one or more health sources are unknown.  
Private Service Connect NEG | The health state of the associated published service is not available yet.  
  
## Before you begin

You must [configure Composite Health](https://docs.cloud.google.com/vpc/docs/configure-composite-health-failover) before you can use it to monitor the health of published services.

### Required roles

To get the permissions that you need to monitor Composite Health, ask your administrator to grant you the following IAM roles on your project: 

  * Check the health state of health sources or composite health checks: [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`) 
  * View Composite Health logging: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Check the health state of a single health source

This section shows how to retrieve the following information about a health source:

  * The overall health state
  * The number of healthy endpoints compared to the total number of endpoints in each instance group or NEG that is associated with the health source's backend service



If the health source is associated with the backend service of an internal passthrough Network Load Balancer that has multiple forwarding rules, the health state is calculated independently for each of the load balancer's forwarding rules. In this case, the health state details include a `forwardingRule` field to identify the forwarding rule that is being evaluated.

###  Console 

  1. In the Google Cloud console, go to the **Composite Health** page:

[Go to Composite Health](https://console.cloud.google.com/net-services/service-health/list)

  2. Click **Health sources**.

  3. Click the name of the health source that you want to view.

  4. To view more details, in the **Health status** section, click the arrow_rightexpander arrow next to the backend service that you want to view. If forwarding rules are displayed, click the expander arrow next to a forwarding rule to view the status of the associated backends.




###  gcloud 

Use the [`gcloud compute health-sources get-health` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-sources/get-health).
    
    
    gcloud compute health-sources get-health HEALTH_SOURCE \
        --region=REGION
    

Replace the following:

  * `HEALTH_SOURCE`: the name of the health source
  * `REGION`: the region of the health source



###  API 

Send a request to the [`regionHealthSources.getHealth` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthSources/getHealth).

HTTP method and URL:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/healthSources/HEALTH_SOURCE/getHealth
    

Replace the following:

  * `PROJECT_ID`: the ID of your project
  * `REGION`: the region of the health source
  * `HEALTH_SOURCE`: the name of the health source



## Check the health state of a composite health check

This section shows how to check the health state of a composite health check, including the following information:

  * The overall health state of the monitored regional published service
  * The individual health state of each health source that is associated with the composite health check




###  Console 

  1. In the Google Cloud console, go to the **Composite Health** page:

[Go to Composite Health](https://console.cloud.google.com/net-services/service-health/list)

  2. Click the name of the composite health check that you want to view.

  3. To view more details, in the **Health status** section, click the arrow_rightexpander arrow next to the composite health check that you want to view.




###  gcloud 

Use the [`gcloud compute composite-health-checks get-health` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/composite-health-checks/get-health).
    
    
    gcloud compute composite-health-checks get-health COMPOSITE_CHECK_NAME \
        --region=REGION
    

Replace the following:

  * `COMPOSITE_CHECK_NAME`: the name of the composite health check
  * `REGION`: the region of the composite health check



###  API 

Send a request to the [`regionCompositeHealthChecks.getHealth` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionCompositeHealthChecks/getHealth).

HTTP method and URL:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/compositeHealthChecks/COMPOSITE_CHECK_NAME/getHealth
    

Replace the following:

  * `PROJECT_ID`: the ID of your project
  * `REGION`: the region of the composite health check
  * `COMPOSITE_CHECK_NAME`: the name of the composite health check



## View Composite Health logs

You can use [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) to track changes in health states. These logs are generated each time a health state changes (for example, from `HEALTHY` to `UNHEALTHY`).

Logging is enabled by default for health sources, composite health checks, and Private Service Connect NEGs that connect to published services that are configured to use Composite Health.

For more information about querying and analyzing log data, see [Analyze logs using Logs Explorer and Observability Analytics](https://docs.cloud.google.com/logging/docs/log-analytics).

###  Console 

To view Composite Health logs, do the following.

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. If you don't see the query editor field in the **Query** pane, click the **Show query** toggle.

  3. In the query editor field:

     * To view logs for producer resources (health sources and composite health checks), enter the following query:
           
           logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Fcompositehealth"
           

     * To view logs for consumer resources (Private Service Connect NEGs connected to published services that use composite health checks), enter the following query:
           
           logName="projects/PROJECT_ID/logs/compute.googleapis.com%2Fservicehealthchecks"
           

Replace `PROJECT_ID` with your project ID.

  4. Click **Run query**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
