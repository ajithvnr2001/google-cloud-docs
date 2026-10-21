---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-dashboards/
title: Create visualization dashboards \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:02:11.856519+00:00
---

# Create visualization dashboards  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Create visualization dashboards Stay organized with collections  Save and categorize content based on your preferences. 

Grafana dashboards let you visualize logs and metrics across Google Distributed Cloud (GDC) air-gapped appliance. These dashboards provide dynamic views of system health and performance through customizable panels.

A dashboard provides a dynamic visual representation of your system's performance. It consists of one or more customizable panels, each configured to query and display specific metrics from your GDC components. These panels let you do the following:

  * Visualize metrics through various graph types.
  * Define alert thresholds to trigger notifications based on metric values.
  * Customize display properties such as labels, units, and time ranges.
  * Set consistent time resolutions for accurate comparisons.



By effectively using Grafana dashboards, you can gain valuable insights into the performance and health of your GDC environment.

## Available dashboards

Assuming your environment is up and running, you immediately see a few metrics dashboards in the home page of the monitoring instance. For example, you can observe switch status and health of system components.

Use the switch and cluster dashboards for monitoring clusters and node metrics. 

![Home page with a list of available dashboards and recently viewed dashboards](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/platform/images/observability-ui-one.png)

The most relevant Platform Administrator (PA) metrics are the following:

  * **Kubernetes** / **API server** : Shows API server healthiness per cluster in the organization.
  * **Kubernetes** / **Compute Resources** / **Multi-Cluster** : Shows organization-wide resource utilization.
  * **Kubernetes** / **Compute Resources** / **Cluster** : Shows resource utilization per cluster.
  * **Kubernetes** / **Persistent Volumes** : Shows utilization of Kubernetes persistent volumes in each cluster.
  * **Node Status** : Shows resource usage on each node of each cluster.
  * **Pod Status** : Shows resource consumption of each pod in each cluster.



The following image shows an example for the **Kubernetes** / **Compute Resources** / **Multi-Cluster** dashboard.

![Line graph showing CPU usage and list of clusters showing CPU quotas](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/platform/images/observability-ui-two.png)

## Before you begin

To get the permissions that you need to access and view Grafana dashboards, ask your Organization IAM Admin or Project IAM Admin to grant you one of the predefined Grafana Viewer roles.

Additionally, to get the permissions that you need to manage the API objects required to create dashboards, ask your Organization IAM Admin or Project IAM Admin to grant you the associated `ConfigMap` and `Dashboard` roles.

Depending on the level of access and permissions you need, you might obtain creator, editor, or viewer roles for these resources in an organization or a project. For more information, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/obs-iam-permissions).

After obtaining the corresponding roles, follow these steps before creating dashboards:

  1. [Collect metrics from your workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/collect-metrics).
  2. Set the path of the kubeconfig file as an environment variable:
         
         export KUBECONFIG=KUBECONFIG_PATH
         

Replace `KUBECONFIG_PATH` with the path to the kubeconfig file for the Management API server where you want to create the dashboard.




## Identify your Grafana endpoint

The following URL is the endpoint of the Grafana instance of your project:
    
    
    https://GDC_URL/PROJECT_NAMESPACE/grafana
    

Replace the following:

  * `GDC_URL`: the URL of your organization in GDC.
  * `PROJECT_NAMESPACE`: your project namespace.



For example, the Grafana endpoint for the `platform-obs` project in the `org-1` organization is `https://org-1/platform-obs/grafana`.

## Create a custom dashboard

Follow these steps to create a Grafana dashboard and customize your settings:

  1. Open your Grafana endpoint to display the user interface.
  2. From the navigation menu, click add **Add**.
  3. From the drop-down menu, click **Dashboard**. Grafana creates an empty dashboard.
  4. On the empty dashboard, add all the panels you want.

  5. In the **Data source** menu of each panel, select the data source that you want for the panel, including metrics (`prometheus`), audit logs (`auditloki`), and operational logs (`oploki`).

For multi-zone universes, Grafana has zone-labeled data sources that you can use to create dashboard visualizations with metrics and logs from multiple zones. These data sources are named with the format `DATA_SOURCE-ZONE_ID`, where:

     * `DATA_SOURCE` can take one of the following values:

       * **Prometheus** (`prometheus` or `metrics`) to display metrics.
       * **Audit logs** (`auditloki`) to display audit logs.
       * **Operational logs** (`oploki`) to display operational logs.
     * `ZONE_ID` is the ID of the zone from which you want to display data in the dashboard.

Additionally, to create a visualization dashboard for cross-zone resources, the data source name is `--Mixed--`. This data source lets you add multiple queries per zone and have cross-zone data visualizations in a single dashboard. You can use this feature to make behaviour comparisons between, for example, a single metric or log query across multiple zones of your universe.

  6. Customize your details and edit your panels to supply your queries or make other updates.

**Tip:** When customizing your dashboard, implement best practices for your use case to facilitate the visualization and interpretation of observability data from your components. For example, establish acceptance thresholds, display useful signals, add labels to graphs, and choose a consistent time resolution.
  7. From the menu bar, click settings **Dashboard settings** to open the **Settings** page.

  8. From the navigation menu, select **JSON Model**.

  9. Copy the JSON model of the dashboard and paste it in a plain-text file for future use.




## Create a `ConfigMap` object

Follow these steps to create a `ConfigMap` object containing the JSON model of the dashboard:

  1. Open a terminal window.
  2. Create a `ConfigMap` object. In the `data` section of your `ConfigMap` object, paste the JSON model that you previously copied:
         
         apiVersion: v1
         kind: ConfigMap
         metadata:
           namespace: PROJECT_NAMESPACE
           name: CONFIGMAP_NAME
         data:
           JSON_FILE_NAME.json: |
             {
             JSON_MODEL
             }
         

Replace the following:

     * `PROJECT_NAMESPACE`: your project namespace.
     * `CONFIGMAP_NAME`: the name you want to give to your `ConfigMap` object.
     * `JSON_FILE_NAME`: the name you want to give to the file for the JSON model of the dashboard.
     * `JSON_MODEL`: the JSON model of your custom dashboard.

For an example of what this object must look like, see a `ConfigMap` example.

  3. Apply the `ConfigMap` object to the Management API server:
         
         kubectl --kubeconfig ${KUBECONFIG} apply -f CONFIGMAP_NAME.yaml
         




### A `ConfigMap` example

The following YAML file shows an example of the `ConfigMap` object of a dashboard in the `platform-obs` namespace:
    
    
      apiVersion: v1
      kind: ConfigMap
      metadata:
        namespace: platform-obs
        name: my-project-dashboard-configmap
      data:
        my-project-dashboard.json: |
          {
          "annotations": {
            "list": [
              {
                "builtIn": 1,
                "datasource": "--",
                "enable": true,
                "hide": true,
                "iconColor": "rgba(0, 211, 255, 1)",
                "name": "Annotations & Alerts",
                "type": "dashboard"
              }
            ]
          },
          "editable": true,
          "graphTooltip": 0,
          "id": null,
          "links": [],
          "panels": [],
          "schemaVersion": 27,
          "style": "dark",
          "tags": [],
          "templating": {
            "list": []
          },
          "time": {
            "from": "now-6h",
            "to": "now"
          },
          "timepicker": {},
          "timezone": "",
          "title": "Sample dashboard",
          "uid": null,
          "version": 0
          }
    

## Create a `Dashboard` custom resource

**Important:** Dashboards, metrics, and logs are isolated per project. To reuse a dashboard across multiple projects, deploy a `Dashboard` custom resource for each project and ensure the underlying data is accessible.

Follow these steps to create a `Dashboard` custom resource and import your custom dashboard to the Grafana instance of your project:

  1. Open a terminal window.
  2. Create a `Dashboard` custom resource and configure the file with the name you gave to the `ConfigMap` object:
         
         apiVersion: observability.gdc.goog/v1
         kind: Dashboard
         metadata:
           namespace: PROJECT_NAMESPACE
           name: DASHBOARD_NAME
         spec:
           configMapRef:
             name: CONFIGMAP_NAME
             namespace: PROJECT_NAMESPACE
             key: JSON_FILE_NAME.json
           foldername: Default
         

Replace the following:

     * `PROJECT_NAMESPACE`: your project namespace.
     * `DASHBOARD_NAME`: the name you want to give to your `Dashboard` custom resource.
     * `CONFIGMAP_NAME`: the name you gave to the `ConfigMap` object.
     * `JSON_FILE_NAME`: the name you gave to the file that contains the JSON model of the dashboard in the `ConfigMap` object.
**Note:** To organize dashboards in folders, specify the `foldername` in the `spec` section of the `Dashboard` resource. Omitting this field defaults to the `Default` folder. Folders are automatically created if they don't exist.
  3. Apply the `Dashboard` custom resource to the Management API server:
         
         kubectl --kubeconfig ${KUBECONFIG} apply -f DASHBOARD_NAME.yaml
         




The system monitors changes to both the `Dashboard` custom resource and the associated `ConfigMap` object. To update or delete a dashboard, modify these resources. Any modifications trigger an update to Grafana. You can't save any updates performed directly in the Grafana user interface.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
