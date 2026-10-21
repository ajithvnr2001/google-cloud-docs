---
url: https://docs.cloud.google.com/monitoring/synthetic-monitors/manage/
title: Manage synthetic monitors \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:57.108328+00:00
---

# Manage synthetic monitors  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/synthetic-monitors/manage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Manage synthetic monitors Stay organized with collections  Save and categorize content based on your preferences. 

To keep your synthetic tests aligned with your services as they evolve, you can list, inspect, edit, copy, and delete your synthetic monitors, and update or delete their underlying functions. You can perform these management tasks by using the Google Cloud console, the Google Cloud CLI, or the Cloud Monitoring API.

To view the execution results, metrics, logs, and traces for a synthetic monitor, see [Explore synthetic monitor results](https://docs.cloud.google.com/monitoring/synthetic-monitors/explore).

## Before you begin

Complete the following in the Google Cloud project that stores your synthetic monitor. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.

  * To get the permissions that you need to view and modify synthetic monitors by using the Google Cloud console, ask your administrator to grant you the following IAM roles on your project: 

    * [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`)
    * [Cloud Functions Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer) (`roles/cloudfunctions.developer`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * The API instructions on this page are for the APIs Explorer. However, you can also issue a curl command. The APIs Explorer provides the curl syntax.

  * Select the interface you plan to use:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## List synthetic monitors

###  Console 

To list the synthetic monitors in your Google Cloud project, do the following:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/uptime-check-icon.png) **Synthetic monitoring** page: 

[Go to **Synthetic monitoring**](https://console.cloud.google.com/monitoring/synthetic-monitoring)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Optional: To restrict which synthetic monitors are listed, add filters.

Each filter is composed of a name and a value. You can set the value to be an exact match for a synthetic monitor name or a partial match. Matches aren't case sensitive. For example, to list all synthetic monitors whose name contains `default`, do the following:

     * Click **Filter table** and select **Display name**.
     * Enter `default` and then press the return key.

If you have multiple filters, then the filters are automatically joined by a logical `AND` unless you insert an `OR` filter.




The **Synthetic monitors** page displays the following for each synthetic monitor:

  * Status of the most recent execution.
  * A link to detailed information about that synthetic monitor.
  * The success rate and average execution time.
  * The number of alerting policies.
  * A _more_vert_ **More options** menu that lets you edit, copy, or delete the synthetic monitor, and create an alerting policy.



###  gcloud

To list your uptime checks and synthetic monitors, run the [`gcloud monitoring uptime list-configs`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/uptime/list-configs) command:
    
    
    gcloud monitoring uptime list-configs --project=PROJECT_ID
    

Before you run the previous command, replace the following:

  * PROJECT_ID: The identifier of the project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.



The returned data includes the following:

  * Name and display name.
  * Check identifier.
  * Monitored resource.
  * Period between checks.



You can configure the Google Cloud CLI command to filter and sort the results.

###  REST 

To list the synthetic monitors in your Google Cloud project, including uptime checks, call the [`projects.uptimeCheckConfigs.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/list) method:

  1. Click [`projects.uptimeCheckConfigs.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/list).
  2. Use the APIs Explorer.

Set the **parent** to the name of the project. Ensure that you use the following format:
         
         projects/PROJECT_ID
         

In the previous expression, `PROJECT_ID` is your Google Cloud project ID. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.




For a synthetic monitor, the result contains a field labeled `syntheticMonitor`.

## View details of a synthetic monitor

###  Console 

To view the details of a synthetic monitor in your Google Cloud project, do the following:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/uptime-check-icon.png) **Synthetic monitoring** page: 

[Go to **Synthetic monitoring**](https://console.cloud.google.com/monitoring/synthetic-monitoring)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. To open the **Synthetic monitor details** page, locate the synthetic monitor that you want to view, and then click its name.

If you want to view your Cloud Run function from the **Function details** page provided by Cloud Run functions, then select the **Code** tab and then click the function's name. The **Function details** page opens in a new window. The tabs on this page let you view metrics, logs, and configuration information.




###  gcloud 

To list the details of an uptime check or synthetic monitor, run the [`gcloud monitoring uptime describe`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/uptime/describe) command:
    
    
    gcloud monitoring uptime describe CHECK_ID --project=PROJECT_ID
    

Before you run the previous command, replace the following:

  * PROJECT_ID: The identifier of the project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.
  * CHECK_ID: The identifier of the uptime check or synthetic monitor. You can find the identifier by running the `gcloud monitoring uptime list-configs` command and examining the **name** field. For more information, see Find the unique identifier of a synthetic monitor.



The data returned for the uptime check includes the following:

  * Name and display name.
  * Check identifier.
  * Monitored resource.
  * Period between checks.



###  REST 

To list the details of a specific synthetic monitor in your Google Cloud project, call the [`projects.uptimeCheckConfigs.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/get) method:

  1. Click [`projects.uptimeCheckConfigs.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/get).
  2. Use the APIs Explorer.

Set the **name** to the identifier of the synthetic monitor. Ensure that you use the following format:
         
         projects/PROJECT_ID/uptimeCheckConfigs/CHECK_ID
         

In the previous expression:

     * PROJECT_ID is your Google Cloud project ID. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.
     * CHECK_ID is the ID of the synthetic monitor.

For example, the value of the **name** field might be:
    
    projects/my-project/uptimeCheckConfigs/10863117100295372627
    

To find the value of the CHECK_ID, you can issue the [`projects.uptimeCheckConfigs.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/list) method. To reduce the number of returned results, include a filter. For example, add the filter `displayName="MySyntheticMonitor"`.




## Edit a synthetic monitor or Cloud Run function

###  Console 

**Note:** If you only want to modify the Cloud Run function, then you can use the **Function details** page or the **Synthetic monitor details** page. In both cases, you must select the edit option, make your changes, and then deploy the modified Cloud Run function.

To edit a synthetic monitor or its Cloud Run function by using the **Synthetic monitor details** page, do the following:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/uptime-check-icon.png) **Synthetic monitoring** page: 

[Go to **Synthetic monitoring**](https://console.cloud.google.com/monitoring/synthetic-monitoring)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Locate the synthetic monitor that you want to edit, click _more_vert_ **More options** , and then select **Edit**.
  4. Optional: To edit the Cloud Run function, click **Edit function** , make your changes, and then click **Apply function**.

For broken-link checkers, to modify the origin URI or the options that define which links are tested, edit the Cloud Run function, and then update the `options` object in the `index.js` file. For information about the fields and syntax for this object, see [`broken-links-ok/index.js`](https://github.com/GoogleCloudPlatform/synthetics-sdk-nodejs/blob/main/samples/broken-links-ok/index.js).

  5. To retain your modifications, click **Save**. Otherwise, click **Cancel**.




###  gcloud 

To modify an uptime check or synthetic monitor, run the [`gcloud monitoring uptime update`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/uptime/update) command:
    
    
    gcloud monitoring uptime update CHECK_ID OPTIONAL_FLAGS --project=PROJECT_ID
    

Before you run the previous command, replace the following:

  * PROJECT_ID: The identifier of the project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.
  * CHECK_ID: The identifier of the uptime check or synthetic monitor. You can find the identifier by running the `gcloud monitoring uptime list-configs` command and examining the **name** field. For more information, see Find the unique identifier of a synthetic monitor.

  * Define which fields you want to modify. For synthetic monitors, you can only update the following fields:

    * Period
    * Display name
    * Timeout
    * User labels



For example, to set the period of a synthetic monitor to be 10 minutes, run the following command:
    
    
    gcloud monitoring uptime update CHECK_ID --period=10 --project=PROJECT_ID
    

###  REST 

Alerting policies and functions aren't contained by a synthetic monitor, and therefore they can't be edited by the procedure described in this section:

  * To modify an alerting policy, use the Google Cloud console or call the [`alertPolicies.patch`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/patch) method. For more information, see [Manage alerting policies by API](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api).

  * To modify a Cloud Run function, after you update the function source, you must redeploy the function. For more information, see [Deploy a Cloud Run function](https://docs.cloud.google.com/functions/docs/deploy).




To edit a synthetic monitor, call the [`projects.uptimeCheckConfigs.patch`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/patch) method:

  1. Click [`projects.uptimeCheckConfigs.patch`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/patch).
  2. Use the APIs Explorer.

     1. Set the **name** to the identifier of the synthetic monitor. The identifier has the following format:
            
            projects/PROJECT_ID/uptimeCheckConfigs/CHECK_ID
            

In the previous expression:

        * PROJECT_ID is your project ID. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.
        * CHECK_ID is the ID of the synthetic monitor.

To find the value of the CHECK_ID, you can issue the [`projects.uptimeCheckConfigs.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/list) method. To reduce the number of returned results, include a filter. For example, add the filter `displayName="MySyntheticMonitor"`.

     2. Set the query parameter, **updateMask** , to identify which fields in the object are being modified. For example, to update the value of the `displayName`, the query parameter is as follows:
            
            updateMask=displayName
            




## Copy a synthetic monitor

###  Console 

To copy a synthetic monitor in your Google Cloud project, do the following:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/uptime-check-icon.png) **Synthetic monitoring** page: 

[Go to **Synthetic monitoring**](https://console.cloud.google.com/monitoring/synthetic-monitoring)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Locate the synthetic monitor that you want to copy, click _more_vert_ **More options** , and then select **Copy**.

The **Copy Synthetic Check** dialog opens with fields prepopulated, including a copy of the Cloud Run function.

  4. Click **Create function** , update the function as necessary, and then click **Apply function**.

  5. To retain your modifications, click **Create**. Otherwise, click **Cancel**.

When you click **Create** , your Cloud Run function is created and deployed, and then the synthetic monitor is created.




###  gcloud 

There is no Google Cloud CLI method that lets you copy a synthetic monitor.

###  REST 

There is no API method that lets you copy a synthetic monitor. However, you can make a copy by performing the following steps:

  1. Call the [`projects.uptimeCheckConfigs.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/get) method and save the response. For more information, see View details of a synthetic monitor.
  2. Edit the response.
  3. Call the [`projects.uptimeCheckConfigs.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/create) method and pass to the method the edited response.



## Delete a synthetic monitor

###  Console 

**Note:** When you delete an uptime check or synthetic monitor by using the Google Cloud console, you also delete associated alerting policies. However, deleting a synthetic monitor doesn't delete the Cloud Run function.

To delete a synthetic monitor and any associated alerting policies, do the following:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/uptime-check-icon.png) **Synthetic monitoring** page: 

[Go to **Synthetic monitoring**](https://console.cloud.google.com/monitoring/synthetic-monitoring)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Locate the synthetic monitor that you want to delete, and then click the name.

  4. Optional: If you want to delete the Cloud Run function, then select the **Code** tab and then click the function's name. The **Function details** page opens in a new window.

  5. In the **Synthetic monitor details** page, click delete **Delete** , and then complete the dialog.

You've now deleted the synthetic monitor.

  6. To delete the Cloud Run function, go to the **Function details** page, click delete **Delete** , and then complete the dialog.




###  gcloud 

**Note:** You can't delete an uptime check or a synthetic monitor by using the Google Cloud CLI or the Cloud Monitoring API when there is an alerting policy associated with that uptime check or synthetic monitor. You must delete the alerting policy first. Deleting a synthetic monitor doesn't delete the Cloud Run function.

To delete an uptime check or synthetic monitor, run the [`gcloud monitoring uptime delete`](https://docs.cloud.google.com/sdk/gcloud/reference/monitoring/uptime/delete) command:
    
    
    gcloud monitoring uptime delete CHECK_ID --project=PROJECT_ID
    

Before you run the previous command, replace the following:

  * PROJECT_ID: The identifier of the project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.
  * CHECK_ID: The identifier of the uptime check or synthetic monitor. You can find the identifier by running the `gcloud monitoring uptime list-configs` command and examining the **name** field. For more information, see Find the unique identifier of a synthetic monitor.



###  REST 

**Note:** You can't delete an uptime check or a synthetic monitor by using the Google Cloud CLI or the Cloud Monitoring API when there is an alerting policy associated with that uptime check or synthetic monitor. You must delete the alerting policy first. Deleting a synthetic monitor doesn't delete the Cloud Run function.

To delete a synthetic monitor, call the [`projects.uptimeCheckConfigs.delete`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/delete) method:

  1. Click [`projects.uptimeCheckConfigs.delete`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/delete).
  2. Use the APIs Explorer.

Set the **name** to the identifier of the synthetic monitor. Ensure that you use the following format:
         
         projects/PROJECT_ID/uptimeCheckConfigs/CHECK_ID
         

In the previous expression:

     * PROJECT_ID is your project ID. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.
     * CHECK_ID is the ID of the synthetic monitor.

To find the value of the CHECK_ID, you can issue the [`projects.uptimeCheckConfigs.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs/list) method. To reduce the number of returned results, include a filter. For example, add the filter `displayName="MySyntheticMonitor"`.




## Find the unique identifier of a synthetic monitor

When your synthetic monitor is created, Monitoring assigns it an identifier. This identifier is embedded in the resource name for the synthetic monitor and has the form:
    
    
    projects/PROJECT_ID/uptimeCheckConfigs/CHECK_ID
    

The CHECK_ID is included in the response of the Google Cloud CLI and Cloud Monitoring API methods that create or list synthetic monitors.

## What's next

  * [Create a synthetic monitor](https://docs.cloud.google.com/monitoring/synthetic-monitors/create)
  * [Explore synthetic monitor results](https://docs.cloud.google.com/monitoring/synthetic-monitors/explore)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
