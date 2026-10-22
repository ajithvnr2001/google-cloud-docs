---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/query-and-view-metrics/
title: Query and view metrics \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:11.976888+00:00
---

# Query and view metrics  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/query-and-view-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Query and view metrics Stay organized with collections  Save and categorize content based on your preferences. 

After [collecting metrics](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/collect-metrics) from your deployed workloads in Google Distributed Cloud (GDC) air-gapped appliance, you can start analyzing them. To analyze metrics, you can visualize and filter them on informative Grafana dashboards or access them directly from Cortex using the `curl` tool for flexible scripting and automation.

You can access your metrics in one of the following two methods:

  * **Grafana dashboards** : Explore trends and identify anomalies with intuitive visualizations of key metrics like CPU utilization, storage consumption, and network activity. Grafana provides a user-friendly interface for filtering and analyzing your workload data in dashboards.
  * **Cortex endpoint** : For more advanced use cases, query your project's Cortex instance directly using the `curl` tool on a command line. Cortex stores your project's Prometheus metrics and provides an HTTP endpoint for programmatic access. This access lets you export data, automate tasks, and build custom integrations.



## Before you begin

To get the permissions that you need to query and visualize metrics on Grafana dashboards, ask your Organization IAM Admin or Project IAM Admin to grant you one of the predefined Organization Grafana Viewer or Project Grafana Viewer roles. Depending on the level of access and permissions you need, you might obtain Grafana roles in an organization or a project.

Alternatively, to get the permissions that you need to query metrics from the Cortex endpoint, ask your Project IAM Admin to grant you the Project Cortex Prometheus Viewer role in your project namespace.

For more information about these roles, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/obs-iam-permissions).

The following table summarizes the `Role` requirements for `PA and AO persona`.

Persona | Object | Cluster | Role | Namespace | Group/User | Config  
---|---|---|---|---|---|---  
PA | grafana | org-admin | `project-grafana-viewer` | platform-obs | Group | 1  
PA | cortex | org-admin | `project-cortex-prometheus-viewer` | platform-obs | Group | 2  
PA | grafana | org-admin | `project-grafana-viewer` | platform-obs | User | 3  
PA | cortex | org-admin | `project-cortex-prometheus-viewer` | platform-obs | User | 4  
AO | grafana | org-admin | `project-grafana-viewer` | PROJECT_NAMESPACE | Group | 1  
AO | cortex | org-admin | `project-cortex-prometheus-viewer` | PROJECT_NAMESPACE | Group | 2  
AO | grafana | org-admin | `project-grafana-viewer` | PROJECT_NAMESPACE | User | 3  
AO | cortex | org-admin | `project-cortex-prometheus-viewer` | PROJECT_NAMESPACE | User | 4  
  
Replace the following variables appropriately:

Variable | Description  
---|---  
`KUBECONFIG` | You will need the kubeconfig for the specific cluster that contains the NAMESPACE where this RoleBinding will be applied.  
`RULE_NAME` | The unique name for this `RoleBinding` resource within the namespace. For example, `io-root-cortex-prometheus-viewer`.  
`NAMESPACE` | The Kubernetes namespace where this `RoleBinding` will be created and apply. Look for the `Namespace` column in the previous table.  
`EMAIL_ADDRESS` | The identifier for the user being granted the role. This is often an email address. For example, `platform-administrator@example.com`.  
`ROLE` | The name of the `Role` that contains the permissions you want to grant to the user. Look for the roles available in the previous table  
`GROUP_NAME` | The name of the `Group` to which PA/AO user belongs to. For example, `pa-group`.  
`ZONE` | Name of the Zone  
**Important:** Before committing configuration, ensure the `kustomization.yaml` file exists in the folder where you are create the yaml file.

###  Config 1 

This configuration grants permissions to a user group to access PA/AO Grafana in `org` cluster. After setting up this configuration, refer [grafana dashboards](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/query-and-view-metrics#grafana-dashboards) section of this document to view metrics on Grafana.

  * **Kubectl Command**

This is the generic command format:
        
        kubectl --kubeconfig `KUBECONFIG` create rolebinding `RULE_NAME` -n `NAMESPACE` --group=`GROUP_NAME` --role=project-grafana-viewer
        

**Example:**
        
        kubectl --kubeconfig <path-to-kubeconfig> create rolebinding project-grafana-viewers-binding --role=project-grafana-viewer --group=my-team --namespace=platform-obs
        

  * **Yaml File**
        
        apiVersion: rbac.authorization.k8s.io/v1
        kind: RoleBinding
        metadata:
          name: RULE_NAME
          namespace: NAMESPACE
        subjects:
        - kind: Group
          name: GROUP_NAME
          apiGroup: rbac.authorization.k8s.io
        roleRef:
          kind: Role
          name: project-grafana-viewer
          apiGroup: rbac.authorization.k8s.io
        




###  Config 2 

This configuration grants permissions to a user group to be able to programmatically access PA/AO metrics in `org` cluster. After setting up this configuration, refer [cortex endpoint](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/query-and-view-metrics#cortex-endpoint) section of this document to programmatically query the metrics.

  * **Kubectl Command**

This is the generic command format:
        
        kubectl --kubeconfig `KUBECONFIG` create rolebinding `RULE_NAME` -n `NAMESPACE` --group=`GROUP_NAME` --role=project-cortex-prometheus-viewer
        

**Example:**
        
        kubectl --kubeconfig <path-to-kubeconfig> create rolebinding project-cortex-prometheus-viewer-binding --role=project-cortex-prometheus-viewer --group=my-team --namespace=platform-obs
        

  * **Yaml File**
        
        apiVersion: rbac.authorization.k8s.io/v1
        kind: RoleBinding
        metadata:
          name: RULE_NAME
          namespace: NAMESPACE
        subjects:
        - kind: Group
          name: GROUP_NAME
          apiGroup: rbac.authorization.k8s.io
        roleRef:
          kind: Role
          name: project-cortex-prometheus-viewer
          apiGroup: rbac.authorization.k8s.io
        




###  Config 3 

This configuration grants permissions to a user to access PA/AO Grafana in `org` cluster. After setting up this configuration, refer [grafana dashboards](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/query-and-view-metrics#grafana-dashboards) section of this document to view metrics on Grafana.

  * **Kubectl Command**

This is the generic command format:
        
        kubectl --kubeconfig `KUBECONFIG` create rolebinding `RULE_NAME` -n `NAMESPACE` --user=`EMAIL_ADDRESS` --role=project-grafana-viewer
        

**Example:**
        
        kubectl --kubeconfig <path-to-kubeconfig> create rolebinding project-grafana-viewers-binding --role=project-grafana-viewer --user=my-email@example.com --namespace=platform-obs
        

  * **Yaml File**
        
        apiVersion: rbac.authorization.k8s.io/v1
        kind: RoleBinding
        metadata:
          name: RULE_NAME
          namespace: NAMESPACE
        subjects:
        - kind: User
          name: EMAIL_ADDRESS
          apiGroup: rbac.authorization.k8s.io
        roleRef:
          kind: Role
          name: project-grafana-viewer
          apiGroup: rbac.authorization.k8s.io
        




###  Config 4 

This configuration grants permissions to a user to be able to programmatically access PA/AO metrics in `org` cluster. After setting up this configuration, refer [cortex endpoint](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/query-and-view-metrics#cortex-endpoint) section of this document to programmatically query the metrics.

  * **Kubectl Command**

This is the generic command format:
        
        kubectl --kubeconfig `KUBECONFIG` create rolebinding `RULE_NAME` -n `NAMESPACE` --user=`EMAIL_ADDRESS` --role=project-cortex-prometheus-viewer
        

**Example:**
        
        kubectl --kubeconfig <path-to-kubeconfig> create rolebinding project-cortex-prometheus-viewer-binding --role=project-cortex-prometheus-viewer --user=my-email@example.com --namespace=platform-obs
        

  * **Yaml File**
        
        apiVersion: rbac.authorization.k8s.io/v1
        kind: RoleBinding
        metadata:
          name: RULE_NAME
          namespace: NAMESPACE
        subjects:
        - kind: User
          name: EMAIL_ADDRESS
          apiGroup: rbac.authorization.k8s.io
        roleRef:
          kind: Role
          name: project-cortex-prometheus-viewer
          apiGroup: rbac.authorization.k8s.io
        




For more information about these roles, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/obs-iam-permissions).

## Obtain and filter your metrics

Select one of the following methods to build queries, visualize trends, and filter metrics from your project workloads:

###  Grafana dashboards 

This section describes how to access your metrics using Grafana dashboards.

#### Identify your Grafana endpoint

The following URL is the endpoint of the Grafana instance of your project:
    
    
      https://GDC_URL/PROJECT_NAMESPACE/grafana
    

Replace the following:

  * `GDC_URL`: the URL of your organization in GDC.
  * `PROJECT_NAMESPACE`: your project namespace.

For example, the Grafana endpoint for the `platform-obs` project in the `org-1` organization is `https://org-1/platform-obs/grafana`.




#### View metrics in the Grafana user interface

Retrieve metrics in the Grafana user interface:

  1. In the GDC console, select your project.
  2. In the navigation menu, select **Operations** > **Monitoring**.
  3. Click **View all in Grafana**.

A new page opens your Grafana endpoint and displays the user interface.

  4. On the user interface,click explore **Explore** from the navigation menu to open the **Explore** page.

  5. From the menu at the **Explore** bar, select a data source to retrieve metrics, according to your universe type:

     * **Single-zone universes** : Select **prometheus** to display metrics from the single zone of your universe.
  6. Enter a query to search for metrics using [PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/) (Prometheus Query Language) expressions. You can do this step in either of the following ways:

     * Select a metric and a label for your query from the **Metric** and **Label filters** menus. Click add **Add** to add more labels to your query. Then, click **Run query**.
     * Enter your query directly in the **Metrics** text field and press `Shift+Enter` to run the query.

The page displays the metrics matching your query.

![The prometheus option is selected on the Explore page to obtain metrics.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/admin/images/metrics.png)

**Figure 1.** Menu option to query metrics from the Grafana user interface.

In figure 1, the **prometheus** option displays the interface that lets you build queries from Grafana to retrieve metrics.

For value examples of labels that you can use to query metrics, see Sample queries and labels.




###  Cortex endpoint 

This section describes how to access your metrics using Cortex.

#### Identify your Cortex endpoint

The following URL is the endpoint of the Cortex instance of your project:
    
    
      https://GDC_URL/PROJECT_NAMESPACE/cortex/prometheus/
    

Replace the following:

  * `GDC_URL`: the URL of your organization in GDC.
  * `PROJECT_NAMESPACE`: your project namespace.

For example, the Cortex endpoint for the `platform-obs` project in the `org-1` organization is `https://org-1/platform-obs/cortex/prometheus/`.

**Note:** You can directly open the URL in a web browser to query metrics. The instructions in the following sections use the `curl` command to call the endpoint, but the same applies to a web browser.



#### Authenticate the `curl` request

  1. [Download and install the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview).
  2. [Set](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-config-set) the gdcloud `core/organization_console_url` property:
         
         gdcloud config set core/organization_console_url
         https://GDC_URL
         

  3. [Sign in with the configured identity provider](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-auth#sign-in-with-idp):
         
         gdcloud auth login
         

  4. Use your username and password to authenticate and sign in.

When the login is successful, you can use the authorization header in your cURL request through the `gdcloud auth print-identity-token` command. For more information, see [gdcloud auth](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-auth).




#### Call the Cortex endpoint

Complete the following steps to reach the Cortex endpoint using the `curl` tool:

  1. Authenticate the `curl` request.
  2. Use `curl` to call the Cortex endpoint and extend the URL using the standard Prometheus HTTP API (<https://prometheus.io/docs/prometheus/latest/querying/api/>) to query metrics.

The following is an example of a `curl` request:
         
         curl https://GDC_URL/PROJECT_NAME/cortex/prometheus/api/v1/query?query=my_metric{cluster="my-cluster"}&time=2015-07-01T20:10:51.781Z \
         -H "Authorization: Bearer $(gdcloud auth print-identity-token \
         --audiences=https://GDC_URL)"
         

You obtain the output following the command. The API response is in JSON format.

**Note:** Add the `api/v1/query` endpoint to query metrics from the URL. You can include optional parameters for your API call after a _question mark_ (`?`) at the end of the URL. Separate these parameters with _ampersand_ (`&`) symbols as in the example of the `curl` request fromnthe last step.



## Sample queries and labels

You can query metrics using the metric name and key-value pairs for labels. A PromQL query has the following syntax:
    
    
    metric_name{label_one="value", label_two="value"}
    

Labels let you differentiate the characteristics of a metric. In this way, container authors make their workloads generate metrics and add tags to filter those metrics.

For example, you can have an `api_http_requests_total` metric to count the number of HTTP requests received. Then, you can add a `request_method` label on this metric, which takes a `POST`, `GET`, or `PUT` value. Consequently, you create three metric streams for each request type you might receive. In this case, to find the number of HTTP `GET` requests, you run the following query:
    
    
    api_http_requests_total{request_method="GET"}
    

See <https://prometheus.io/docs/practices/naming/> for more information about metrics and labels.

The following are some of the default labels that the `MonitoringTarget` custom resource adds. You can use these default labels to query metrics:

  * `_gdch_service`: the short name of the service.
  * `cluster`: the name of the cluster.
  * `container_name`: the name of the container within a pod.
  * `namespace_name`: your project namespace.
  * `pod_name`: the pod name prefix.



The following table describes the labels that Prometheus adds automatically:

Default labels **Metric label** | **Description**  
---|---  
`job` | The internal name of the scrape job used to collect the metric. Jobs created by the `MonitoringTarget` custom resource have a name with the following pattern:  
  
`obs-system/OBS_SHADOW_PROJECT_NAME/MONITORINGTARGET_NAME.MONITORINGTARGET_NAMESPACE/I/J`  
  
`I` and `J` are unique numbers determined internally to avoid name conflicts.  
`instance` | The `$IP:$PORT` of the scrapped service. If a workload resource has multiple replicas, use this field to differentiate them.  
  
The following code samples show the use of key-value pairs for labels to query different metrics:

  * View all the metric streams of the processed operations in your project:
        
        processed_ops_total
        

  * View the processed operations collected in a Kubernetes cluster:
        
        processed_ops_total{cluster="CLUSTER_NAME"}
        

  * View the CPU usage collected in a Kubernetes cluster:
        
        cpu_usage{cluster="CLUSTER_NAME"}
        




Use the metrics relabeling tool to add labels not exposed initially by the scrapped containers and rename produced metrics. You must configure the `MonitoringTarget` custom resource to add labels on the metrics it collects. Specify those labels in the `metricsRelabelings` field of the custom resource. For more information, see [Label metrics](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/label-metrics).

## Query metrics from the Cortex API

Cortex is the long-term storage for Prometheus metrics in GDC. The Observability platform exposes a Cortex HTTP API endpoint for querying and reading metrics, alerts, and other Prometheus time series data from your project.

Query metrics directly from the HTTP API to read and export metrics and other time series data to external tools, set up automated tasks, adapt responses, and build integrations according to your system monitoring use case. For example, insert the output into another command, export details to text file formats, or configure a Linux cron job. You can call the API from the command-line interface (CLI) or a web browser and use query language expressions as endpoint parameters to obtain the result in JSON format.

This section explains how to call the Cortex API endpoint from the CLI using the Prometheus API specification to query metrics for data observability..

### Before you begin

You must obtain authorization to query metrics from the CLI. To get the permissions you need to access the Cortex API endpoint, ask your Project IAM Admin to grant you the Project Cortex Prometheus Viewer (`project-cortex-prometheus-viewer`) role.

Create the following role bindings using the `kubectl` commands to Cortex prometheus for each persona:

  1. Infrastructure Operator (IO) Root-Admin - `Project Cortex Prometheus Viewer`:
         
         kubectl --kubeconfig $HOME/root-admin-kubeconfig create rolebinding 
         io-cortex-prometheus-viewer-binding -n infra-obs 
         --user=fop-infrastructure-operator@example.com 
         --role=project-cortex-prometheus-viewer
         

  2. Platform-Admin (PA) Root-Admin - `Project Cortex Prometheus Viewer`:
         
         kubectl --kubeconfig $HOME/root-admin-kubeconfig create rolebinding 
         pa-cortex-prometheus-viewer-binding -n platform-obs 
         --user=fop-platform-admin@example.com --role=project-cortex-prometheus-viewer
         

  3. Application Operator (AO) Root-Admin - `Project Cortex Prometheus Viewer` :
         
         kubectl --kubeconfig $HOME/root-admin-kubeconfig create rolebinding 
         project-cortex-prometheus-viewer-binding -n PROJECT_NAME 
         --user=USER_NAME --role=project-cortex-prometheus-viewer
         

Replace the following:

     * PROJECT_NAME: The name of your project.
     * USER_NAME: The account name of the user that requires the role binding.



After the role binding is created, you can access Prometheus API with your login username.

### HTTP API endpoint

The following URL is the HTTP API endpoint for accessing metrics in the `platform-obs` project:
    
    
    https://GDC_URL/PROJECT_NAME/cortex/prometheus/
    

Replace the following:

  * GDC_URL: The URL of your organization in GDC.
  * PROJECT_NAME: The name of your project.

**Note:** You can directly open the URL in a web browser to query metrics. The instructions in the following section use the `curl` command to call the API endpoint, but the same applies to a web browser.

### Call the API endpoint

Work through the following steps to reach the Cortex API endpoint from the CLI and query metrics:

  1. Ensure you meet the prerequisites.
  2. Open the CLI.
  3. Use the `curl` tool to call the Cortex endpoint and extend the URL using the standard <https://prometheus.io/docs/prometheus/latest/querying/api/> to query metrics. For example:
         
         curl https://console.org-1.zone1.google.gdch.test/alice/cortex/prometheus/api/v1/query?query=my_metric{cluster="org-1-system"}&time=2015-07-01T20:10:51.781Z
         




You obtain the output in the CLI following the command. The API response format is JSON.

**Note:** Add the `api/v1/query` endpoint to query metrics from the URL. You can include optional parameters for your API call after a _question mark_ (`?`) at the end of the URL. Separate these parameters with _ampersand_ (`&`) symbols as in the example of the query from the last step.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
