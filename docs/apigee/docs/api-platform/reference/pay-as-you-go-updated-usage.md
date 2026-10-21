---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-usage/
title: View Pay-as-you-go and Subscription resource usage \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:32:00.528390+00:00
---

# View Pay-as-you-go and Subscription resource usage  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Resources ](https://docs.cloud.google.com/apigee/docs/release-notes)



Send feedback 

#  View Pay-as-you-go and Subscription resource usage Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

There are several tools you can use to view and monitor your Apigee resource use. This topic discusses how billing or organization administrators can: 

  * View resource usage in Metrics Explorer
  * Configure a Cloud Monitoring alert
  * View resource usage by billing account
  * Monitor resources with Cloud Audit Logging



To view organization resource usage and configure alerts, you need the following roles: 

  * **Apigee Organization Admin** (`roles/apigee.admin`)
  * **Logs Viewer** `(roles/logging.viewer`)
  * **Billing Account Viewer** (`roles/billing.viewer`)



## View resource usage in Metrics Explorer

You can use Metrics Explorer to view usage of the Apigee resources that are key attributes in determining cost in your Pay-as-you-go pricing plan. By selecting specific metrics and filters, you can generate a usage report for Apigee proxy/shared flow deployment units or Apigee active environments, or both.

For detailed information about the Apigee metrics and their possible values, see [apigee](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-apigee) on the Google Cloud metrics page.

**Note** : The instructions below describe how to view Apigee resource usage in Metrics Explorer for a single Google Cloud project. To view and monitor usage across multiple projects, including multiple projects in the same billing account, you can _configure a metrics scope_. For detailed instructions, see the following topics in the Cloud Monitoring documentation: 

  * [(Console) Configure a metrics scope](https://docs.cloud.google.com/monitoring/settings/multiple-projects)
  * [(API) Configure a metrics scope](https://docs.cloud.google.com/monitoring/settings/manage-api)



### Apigee proxy/shared flow deployment unit usage

### Metrics Explorer UI

To view Apigee proxy/shared flow deployment unit usage in Metrics Explorer, use the following steps: 

  1. Open the **Monitoring > Metrics Explorer** page in the Google Cloud console. 

[Go to Metrics Explorer](https://cloud.google.com/console/monitoring/metrics-explorer)

  2. In the **Select a metric** pane, expand the **Metric** menu and enter `Apigee` in the filter bar. 

Use the submenus to select the resource type, category, and metric: 

     1. In the **Active resources** menu, select **Apigee proxy**.
     2. In the **Active metric categories** menu, select **Proxy**.
     3. In the **Active metrics** menu, select **Apigee proxy details**.
  3. Click **Apply**.
  4. In the **Aggregation** section: 
     1. Use the **By** menu to group the data by **resource label**. Select both `proxy_deployment_type` and `env` from the list options to group the data by proxy deployment type and environment.
     2. Click **OK** to apply the filters.
  5. Select **Sum** from the **Grouping function** menu.



### PromQL

To view Apigee proxy/shared flow deployment unit usage with a PromQL query: 

  1. Open the **Monitoring > Metrics Explorer** page in the Google Cloud console. 

[Go to Metrics Explorer](https://cloud.google.com/console/monitoring/metrics-explorer)

  2. In the toolbar of the **Select a metric** pane, select **Code Editor**.
  3. To use PromQL: 
     1. Select **PromQL** in the **Language** toggle.
     2. Enter the following query into the query editor and click **Run Query** : 
            
            count(apigee_googleapis_com:proxy_details{monitored_resource="apigee.googleapis.com/Proxy"}) by (proxy_deployment_type, env)




### Apigee active environment usage

### Metrics Explorer UI

To view Apigee active environment usage in Metrics Explorer, use the following steps: 

  1. Open the **Monitoring > Metrics Explorer** page in the Google Cloud console. 

[Go to Metrics Explorer](https://cloud.google.com/console/monitoring/metrics-explorer)

  2. In the **Select a metric** pane, expand the **Metric** menu and enter `Apigee` in the filter bar. 

Use the submenus to select the resource type, category, and metric: 

     1. In the **Active resources** menu, select **Apigee environment**.
     2. In the **Active metric categories** menu, select **Environment**.
     3. In the **Active metrics** menu, select **Apigee active environment**.
  3. Click **Apply**.
  4. In the **Filters** section: 
     1. Use the **By** menu to group the data by **resource label**. Select `type` from the list options to group by environment type.
     2. Click **OK** to apply the filters.
  5. Select **Sum** from the **Grouping function** menu.



### PromQL

To view Apigee active environment usage with a PromQL query: 

  1. Open the **Monitoring > Metrics Explorer** page in the Google Cloud console. 

[Go to Metrics Explorer](https://cloud.google.com/console/monitoring/metrics-explorer)

  2. In the toolbar of the **Select a metric** pane, select **Code Editor**.
  3. To use PromQL: 
     1. Select **PromQL** in the **Language** toggle.
     2. Enter the following query into the query editor and click **Run Query** : 
            
            count(apigee_googleapis_com:environment_active{monitored_resource="apigee.googleapis.com/Environment"}) by (env, type)




### Standard and Extensible API calls

### Metrics Explorer UI

To view Standard and Extensible API calls by environment in Metrics Explorer, use the following steps: 

  1. Open the **Monitoring > Metrics Explorer** page in the Google Cloud console. 

[Go to Metrics Explorer](https://cloud.google.com/console/monitoring/metrics-explorer)

  2. In the **Select a metric** pane, expand the **Metric** menu and enter `Apigee` in the filter bar. 

Use the submenus to select the resource type, category, and metric: 

     1. In the **Active resources** menu, select **Apigee environment**.
     2. In the **Active metric categories** menu, select **Environment**.
     3. In the **Active metrics** menu, select **Apigee environment API call count**.
  3. Click **Apply**.
  4. In the **Filters** section: 
     1. Use the **By** menu to group by **resource label**. Select `proxy_deployment_type` from the list options to group by Environment type.
     2. Click **OK** to apply the filters.
  5. Select **Sum** from the **Grouping function** menu.



### PromQL

To view Standard and Extensible API calls by environment with a PromQL query: 

  1. Open the **Monitoring > Metrics Explorer** page in the Google Cloud console. 

[Go to Metrics Explorer](https://cloud.google.com/console/monitoring/metrics-explorer)

  2. In the toolbar of the **Select a metric** pane, select **Code Editor**.
  3. To use PromQL: 
     1. Select **PromQL** in the **Language** toggle.
     2. Enter the following query into the query editor and then click **Run query** : 
            
            sum(delta(apigee_googleapis_com:environment_api_call_count{monitored_resource="apigee.googleapis.com/Environment"}[1m])) by (proxy_deployment_type,env,location)




### Create a metrics dashboard

The graphical output of the Metrics Explorer on the **Chart** tab represents a _gauge_ metric. That is, each point on the graph records the resource utilization of your Apigee instance across all environments in each region at the time of measurement.

Once you have configured your view of the data using the **Resource & Metric** selection, you can save the data to a custom dashboard for future reference. To save your selected view: 

  1. Click the **Save Chart** button in the chart pane of the **Explorer** tab.
  2. In the **Save Chart** Dialog, enter the following information: 
     * **Chart title** field: Enter a name for the chart, or use the suggested title.
     * **Dashboard** drop-down: Select an existing dashboard or select **New Dashboard** to create and name a new dashboard. Your chart will be saved to the selected dashboard.
  3. Click **Save**.



Once saved, you can access your chart by navigating to the **Dashboards Overview** page in the Google Cloud console and viewing the dashboard you selected.

To learn more about creating and managing custom views using Cloud Monitoring, see [Dashboards and charts](https://docs.cloud.google.com/monitoring/dashboards).

## Configure a Cloud Monitoring alert

Once you have configured metrics reporting for your Apigee resource usage in Cloud Monitoring, you can enable _metric-based_ alerting policies. You can configure alerting policies to monitor resource usage relevant to your Pay-as-you-go plan and provide timely awareness of any potential problems. For more information, see [How alerting works](https://docs.cloud.google.com/monitoring/alerts#how_alerting_works).

You can add a metric-based alerting policy to your Google Cloud project by using the Google Cloud console, the [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/api/v3), or the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring/policies). When you use the Google Cloud console, you can enable recommended alerts or configure custom alerts from the [Alerting](https://cloud.google.com/console/monitoring/alerting) page of Cloud Monitoring. 

The general steps required to create a metric-based alerting policy are outlined in [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui). To configure an alerting policy specifically based on resource usage, you can follow the steps in [Create alerting policy](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#create-policy).

You can use the same metrics and filters used in the previous section to customize your alert for resource usage. For example, to create an alert based on Apigee proxy usage, use the following steps: 

  1. Open the **Monitoring > Alerting** page in the Google Cloud console. 

[Go to Alerting](https://cloud.google.com/console/monitoring/alerting)

  2. Click **\+ Create policy**. 
  3. In the **Select a metric** section of the **Create policy** pane, enter `Apigee` in the filter bar, and then use the submenus to select the resource type, category, and metric: 
     * In the **Active resources** menu, select **Apigee proxy**.
     * In the **Active metric categories** menu, select **Proxy**.
     * In the **Active metrics** menu, select **Apigee proxy details**.
  4. In the **Add Filters** section, use the **By** menu to group by **resource label**. Select both `proxy_deployment_type` and `env` from the list options to group by proxy deployment type and environment.



To create an alert based on Apigee active environment usage, select the metrics and filters used to View Apigee environment usage. 

## View resource usage by billing account

To view resource usage by billing account, follow these steps: 

  1. Open the **Billing** page in the Google Cloud console. 

[Go to Billing](https://cloud.google.com/console/billing)

  2. If you have more than one billing account, select **Go to linked billing account** to view the current project's billing account. To locate a different billing account, select **Manage billing accounts** and choose the account you'd like to view.
  3. Select **Reports**.
  4. Click **Show Filters** to access the **Filters** menu if it is not already open.
  5. In the **Time range** field, select **Usage date** to view a current snapshot of billing in a date range, or select **Invoice month** to view usage billed in a specific invoice. 
  6. Select **Group By > SKU**. 
  7. From the **Services** drop-down list, select **Apigee**. The list of SKUs included in your bill is displayed.
  8. To filter the list of SKUs, select the SKUs you want to view from the **SKUs** drop-down list. 

If your usage of any of these SKUs is **0** , they will not appear in the **Group By > SKU** pull-down menu.


**Note** : The billing report summarizes costs per region. If your environment is attached to multiple instances in a region, you will see an increase in the usage hours and cost accordingly. 

## Monitor resource usage with Cloud Audit Logging

You can use Cloud audit logs to monitor resource usage that will affect your Pay-as-you-go billing. Follow these steps to view the relevant audit logs: 

  1. Open the **Logs Explorer** page in the Cloud console. 

[Go to Logs Explorer](https://cloud.google.com/console/logs)

  2. On the **Query** , use the Search bar to search for any events impacting the following billable resources: 
     * Create instance with attached environment(s): `google.cloud.apigee.v1.InstanceService.CreateInstanceAndAttachments`
     * Update instance and it's attachments: `google.cloud.apigee.v1.InstanceService.UpdateInstanceAndAttachments`
     * Delete instance with attached environment(s): `google.cloud.apigee.v1.InstanceService.DeleteInstance`
     * Create instance attachment: `google.cloud.apigee.v1.InstanceAttachmentService.CreateInstanceAttachment`
     * Delete instance attachment: `google.cloud.apigee.v1.InstanceAttachmentService.DeleteInstanceAttachment`
     * Deploy a proxy: `google.cloud.apigee.v1.DeploymentService.DeployApiProxy`
     * Undeploy a proxy: `google.cloud.apigee.v1.DeploymentService.UndeployApiProxy`
     * Deploy a shared flow: `google.cloud.apigee.v1.DeploymentService.DeploySharedFlow`
     * Undeploy a shared flow: `google.cloud.apigee.v1.DeploymentService.UndeploySharedFlow`
     * Enable/disable the Apigee API Analytics or Advanced API Security add-on: `google.cloud.apigee.v1.EnvironmentAddons.SetAddonEnablement`

For example, you could enter the following sample query: 
    
    resource.type="audited_resource"
    resource.labels.method="google.cloud.apigee.v1.InstanceService.CreateInstanceAndAttachments"
    resource.labels.service="apigee.googleapis.com"

For more information on using Cloud Audit Logging to monitor Apigee resources, see [Apigee audit logging information](https://cloud.google.com/apigee/docs/api-platform/debug/audit-logging). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
