---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows/
title: Manage Apigee instance maintenance windows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:12.609455+00:00
---

# Manage Apigee instance maintenance windows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage Apigee instance maintenance windows Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This section has procedures for finding and setting maintenance windows for Apigee resources. To learn more about how and why Apigee performs maintenance, see [Maintenance overview](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance).

## Set a preferred window for maintenance

If a resource is already undergoing maintenance or has a scheduled maintenance event, any changes you make to the maintenance window setting (including changing the day/time, changing the update order, or clearing the settings) do not apply to the pending event. The scheduled maintenance proceeds as planned, and your changes apply only to future maintenance rollouts.

If you've opted in to maintenance notifications, then Apigee sends you notifications after a resource has been scheduled for maintenance, with the exact date and time when the maintenance is scheduled to happen. Apigee sends these notifications based on your resource maintenance window order of update settings, as follows:

**Note:** "Week 1" and "Week 2" refer to the rollout phases and notification lead times (1 week versus 2 weeks). They do **not** refer to the first or second calendar week of the month. For example, a "Week 2" rollout does not necessarily happen in the second week of a calendar month. It happens one week after the "Week 1" rollout for that specific release.

  * If the order of update setting is set to Week 1, then Apigee sends maintenance notifications at least one week in advance.
  * If the order of update setting is set to Week 2, then Apigee sends maintenance notifications at least two weeks in advance.



You can only specify one maintenance window per Apigee instance. Requests with more than one maintenance window will be rejected.

If you would like to set maintenance windows for multiple instances in the same organization you should ensure at least 12 hours between the maintenance windows to avoid overlapping maintenance operations.

When updating the maintenance window, the previous window will be overwritten.

To perform this task, you must have the [Apigee Organization Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee) role (`roles/apigee.admin`) or a role that includes the `apigee.instances.update` permission.
    
    
    AUTH="Authorization: Bearer $(gcloud auth print-access-token)"
    curl -X PATCH \
      -H "$AUTH" \
      -H "Content-Type: application/json" \
      -d '{
        "maintenanceUpdatePolicy": {
          "maintenanceWindows": [
            {
              "day": "SUNDAY",
              "startTime": {
                "hours": 23
              }
            }
          ],
          "maintenanceChannel": "WEEK1"
        }
      }' \
      "https://apigee.googleapis.com/v1/organizations/ORGANIZATION_ID/instances/INSTANCE_ID?updateMask=maintenanceUpdatePolicy.maintenanceWindows,maintenanceUpdatePolicy.maintenanceChannel"
    
    

Where: 

  * Maintenance `startTime` is configured in UTC.
  * `maintenanceChannel`: The maintenance channel/order of update setting (e.g., `WEEK1` or `WEEK2`).
  * **ORGANIZATION_ID** is your Apigee organization ID.
  * **INSTANCE_ID** is your Apigee instance ID.



## Find existing maintenance settings and maintenance schedules

You can retrieve your current maintenance settings and view any upcoming maintenance by checking the `maintenanceUpdatePolicy` and `scheduledMaintenance` fields, as shown in the following API example:

To perform this task, you must have a role that includes the `apigee.instances.get` permission.
    
    
    AUTH="Authorization: Bearer $(gcloud auth print-access-token)"
    curl -H "$AUTH" \
      "https://apigee.googleapis.com/v1/organizations/ORGANIZATION_ID/instances/INSTANCE_ID"
    
    

Where: 

  * **ORGANIZATION_ID** is your Apigee organization ID.
  * **INSTANCE_ID** is your Apigee instance ID.



Example output
    
    
    {
      ...
      "scheduledMaintenance": {
        "startTime": "2025-01-28T23:00:00Z"
      },
      "maintenanceUpdatePolicy": {
        "maintenanceWindows": [
          {
            "day": "SUNDAY",
            "startTime": {
              "hours": 23
            }
          }
        ],
        "maintenanceChannel": "WEEK1"
      }
    }

## Clear maintenance settings

If you no longer require maintenance settings you can clear them by following the instructions below.

To perform this task, you must have the [Apigee Organization Admin](https://cloud.google.com/iam/docs/roles-permissions/apigee) role (`roles/apigee.admin`) or a role that includes the `apigee.instances.update` permission.
    
    
    AUTH="Authorization: Bearer $(gcloud auth print-access-token)"
    curl -X PATCH \
      -H "$AUTH" \
      -H "Content-Type: application/json" \
      -d '{
        "maintenanceUpdatePolicy": null
      }' \
      "https://apigee.googleapis.com/v1/organizations/ORGANIZATION_ID/instances/INSTANCE_ID?updateMask=maintenanceUpdatePolicy"
    
    

Where: 

  * **ORGANIZATION_ID** is your Apigee organization ID.
  * **INSTANCE_ID** is your Apigee instance ID.



## Opt-in to maintenance notifications

Before you opt-in for maintenance notifications, you must  set a preferred window for maintenance on a resource.

  1. In the Google Cloud console, go to the **User preferences > Communication** page.

[Go to Communications](https://console.cloud.google.com/user-preferences/communication)

  2. In the row for **Apigee, Maintenance window** , select the radio button under **Email** to turn it **On**.



Each user that needs to receive notifications must opt in separately by following the above instructions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
