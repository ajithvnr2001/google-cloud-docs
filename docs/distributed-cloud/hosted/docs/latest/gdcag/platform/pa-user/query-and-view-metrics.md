---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/query-and-view-metrics/
title: Query and view metrics \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:00:21.055056+00:00
---

# Query and view metrics  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/query-and-view-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Query and view metrics Stay organized with collections  Save and categorize content based on your preferences. 

After [collecting metrics](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/collect-metrics) from your deployed workloads in Google Distributed Cloud (GDC) air-gapped, you can start analyzing them. To analyze metrics, you can visualize and filter them on informative Grafana dashboards or access them directly from Cortex using the `curl` tool for flexible scripting and automation.

This page provides detailed instructions on how to query and visualize your metrics using both the Grafana user interface and the `curl` tool for the Cortex endpoint to gain insights into your workload performance.

You can access your metrics in one of the following two methods:

  * **Grafana dashboards** : Explore trends and identify anomalies with intuitive visualizations of key metrics like CPU utilization, storage consumption, and network activity. Grafana provides a user-friendly interface for filtering and analyzing your workload data in dashboards.
  * **Cortex endpoint** : For more advanced use cases, query your project's Cortex instance directly using the `curl` tool on a command line. Cortex stores your project's Prometheus metrics and provides an HTTP endpoint for programmatic access. This access lets you export data, automate tasks, and build custom integrations.



## Before you begin

To get the permissions that you need to query and visualize metrics on Grafana dashboards, ask your Organization IAM Admin or Project IAM Admin to grant you one of the predefined Organization Grafana Viewer or Project Grafana Viewer roles. Depending on the level of access and permissions you need, you might obtain Grafana roles in an organization or a project.

Alternatively, to get the permissions that you need to query metrics from the Cortex endpoint, ask your Project IAM Admin to grant you the Project Cortex Prometheus Viewer role in your project namespace.

The following table summarizes the `Role` requirements for the PA and AO personas.

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
`EMAIL_ADDRESS` | The identifier for the user being granted the role. This is often an email address. For example, `infrastructure-operator@example.com`.  
`ROLE` | The name of the `Role` that contains the permissions you want to grant to the user. Look for the roles available in the previous table  
`GROUP_NAME` | The name of the `Group` to which PA/AO user belongs to. For example, `pa-group`.  
`ZONE` | Name of the Zone  
**Important:** Before committing configuration, ensure the `kustomization.yaml` file exists in the folder where you are create the yaml file.

###  Config 1 

This configuration grants permissions to a user group to access PA/AO Grafana in `org` cluster. After setting up this configuration, refer to the [grafana dashboards](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/query-and-view-metrics#grafana-endpoint) section of this document to view metrics on Grafana.

  * **Kubectl Command**

This is the generic command format:
        
        kubectl --kubeconfig `KUBECONFIG` create rolebinding `RULE_NAME` -n platform-obs --group=`GROUP_NAME` --role=project-grafana-viewer
        

**Example:**
        
        kubectl --kubeconfig <path-to-kubeconfig> create rolebinding project-grafana-viewers-binding --role=project-grafana-viewer --group=my-team --namespace=platform-obs
        

  * **IAC File path**
        
        /infrastructure/zonal/zones/`ZONE`/org-admin/rolebindings/`GROUP_NAME`/<YAML_FILE>
        

  * **Yaml File**
        
        apiVersion: rbac.authorization.k8s.io/v1
        kind: RoleBinding
        metadata:
          name: RULE_NAME
          namespace: platform-obs
        subjects:
        - kind: Group
          name: GROUP_NAME
          apiGroup: rbac.authorization.k8s.io
        roleRef:
          kind: Role
          name: project-grafana-viewer
          apiGroup: rbac.authorization.k8s.io
        




###  Config 2 

This configuration grants permissions to a user group to be able to programmatically access PA/AO metrics in `org` cluster. After setting up this configuration, refer to the [cortex endpoint](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/query-and-view-metrics#cortex-endpoint-sz) section of this document to programmatically query the metrics.

  * **Kubectl Command**

This is the generic command format:
        
        kubectl --kubeconfig `KUBECONFIG` create rolebinding `RULE_NAME` -n platform-obs --group=`GROUP_NAME` --role=project-cortex-prometheus-viewer
        

**Example:**
        
        kubectl --kubeconfig <path-to-kubeconfig> create rolebinding project-cortex-prometheus-viewer-binding --role=project-cortex-prometheus-viewer --group=my-team --namespace=platform-obs
        

  * **IAC File path**
        
        /infrastructure/zonal/zones/`ZONE`/org-admin/rolebindings/`GROUP_NAME`/<YAML_FILE>
        

  * **Yaml File**
        
        apiVersion: rbac.authorization.k8s.io/v1
        kind: RoleBinding
        metadata:
          name: RULE_NAME
          namespace: platform-obs
        subjects:
        - kind: Group
          name: GROUP_NAME
          apiGroup: rbac.authorization.k8s.io
        roleRef:
          kind: Role
          name: project-cortex-prometheus-viewer
          apiGroup: rbac.authorization.k8s.io
        




###  Config 3 

This configuration grants permissions to a user to access PA/AO Grafana in `org` cluster. After setting up this configuration, refer to the [grafana dashboards](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/query-and-view-metrics#grafana-endpoint) section of this document to view metrics on Grafana.

  * **Kubectl Command**

This is the generic command format:
        
        kubectl --kubeconfig `KUBECONFIG` create rolebinding `RULE_NAME` -n platform-obs --user=`EMAIL_ADDRESS` --role=project-grafana-viewer
        

**Example:**
        
        kubectl --kubeconfig <path-to-kubeconfig> create rolebinding project-grafana-viewers-binding --role=project-grafana-viewer --user=my-email@example.com --namespace=platform-obs
        

  * **IAC File path**
        
        /infrastructure/zonal/zones/`ZONE`/org-admin/rolebindings/`EMAIL_ADDRESS`/<YAML_FILE>
        

  * **Yaml File**
        
        apiVersion: rbac.authorization.k8s.io/v1
        kind: RoleBinding
        metadata:
          name: RULE_NAME
          namespace: platform-obs
        subjects:
        - kind: User
          name: EMAIL_ADDRESS
          apiGroup: rbac.authorization.k8s.io
        roleRef:
          kind: Role
          name: project-grafana-viewer
          apiGroup: rbac.authorization.k8s.io
        




###  Config 4 

This configuration grants permissions to a user to be able to programmatically access PA/AO metrics in `org` cluster. After setting up this configuration, refer to the [cortex endpoint](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/query-and-view-metrics#cortex-endpoint-sz) section of this document to programmatically query the metrics.

  * **Kubectl Command**

This is the generic command format:
        
        kubectl --kubeconfig `KUBECONFIG` create rolebinding `RULE_NAME` -n platform-obs --user=`EMAIL_ADDRESS` --role=project-cortex-prometheus-viewer
        

**Example:**
        
        kubectl --kubeconfig <path-to-kubeconfig> create rolebinding project-cortex-prometheus-viewer-binding --role=project-cortex-prometheus-viewer --user=my-email@example.com --namespace=platform-obs
        

  * **IAC File path**
        
        /infrastructure/zonal/zones/`ZONE`/org-admin/rolebindings/`EMAIL_ADDRESS`/<YAML_FILE>
        

  * **Yaml File**
        
        apiVersion: rbac.authorization.k8s.io/v1
        kind: RoleBinding
        metadata:
          name: RULE_NAME
          namespace: platform-obs
        subjects:
        - kind: User
          name: EMAIL_ADDRESS
          apiGroup: rbac.authorization.k8s.io
        roleRef:
          kind: Role
          name: project-cortex-prometheus-viewer
          apiGroup: rbac.authorization.k8s.io
        




For more information about these roles, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/obs-iam-permissions).

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

  4. On the user interface, click explore **Explore** from the navigation menu to open the **Explore** page.

  5. From the menu at the **Explore** bar, select a data source to retrieve metrics, according to your universe type:

     * **Single-zone universes** : Select **prometheus** to display metrics from the single zone of your universe.

     * **Multi-zone universes** : Grafana can connect to different zones and show cross-zone data. Select **Metrics ZONE_NAME** to display metrics from any zone of your universe, regardless of the zone you are signed in.

Additionally, to have cross-zone data visualizations in a single dashboard and add multiple zones to your query, select **Mixed** as the data source.

  6. Enter a query to search for metrics using [PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/) (Prometheus Query Language) expressions. You can do this step in either of the following ways:

     * Select a metric and a label for your query from the **Metric** and **Label filters** menus. Click add **Add** to add more labels to your query. Then, click **Run query**.
     * Enter your query directly in the **Metrics** text field and press `Shift+Enter` to run the query.

The page displays the metrics matching your query.

![The prometheus option is selected on the Explore page to obtain metrics.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/images/metrics-ui.png)

**Figure 1.** Menu option to query metrics from the Grafana user interface.

In figure 1, the **prometheus** option displays the interface that lets you build queries from Grafana to retrieve metrics.

For value examples of labels that you can use to query metrics, see Sample queries and labels.




###  Cortex endpoint - single zone

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

  1. [Download and install the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview).
  2. [Set](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-config-set) the gdcloud `core/organization_console_url` property:
         
         gdcloud config set core/organization_console_url
         https://GDC_URL
         

  3. [Sign in with the configured identity provider](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth#sign-in-with-idp):
         
         gdcloud auth login
         

  4. Use your username and password to authenticate and sign in.

When the login is successful, you can use the authorization header in your curl request through the `gdcloud auth print-identity-token` command. For more information, see [gdcloud auth](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-auth).




#### Call the Cortex endpoint

Complete the following steps to reach the Cortex endpoint using the `curl` tool:

  1. Authenticate the `curl` request.
  2. Use `curl` to call the Cortex endpoint and extend the URL using the Querying HTTP API Format to query metrics.

The following is an example of a `curl` request:
         
         curl https://GDC_URL/PROJECT_NAME/cortex/prometheus/api/v1/query?query=my_metric{cluster="my-cluster"}&time=2015-07-01T20:10:51.781Z \
         -H "Authorization: Bearer $(gdcloud auth print-identity-token \
         --audiences=https://GDC_URL)"
         

You obtain the output following the command. The API response is in JSON format.

**Note:** Add the `api/v1/query` endpoint to query metrics from the URL. You can include optional parameters for your API call after a _question mark_ (`?`) at the end of the URL. Separate these parameters with _ampersand_ (`&`) symbols as in the example of the `curl` request from the last step.



###  Cortex endpoint - multizone

This section describes how to access your metrics using Cortex.

#### Identify your Cortex endpoint

The following URL is the endpoint of the Cortex instance of your project for multizone query:
    
    
      https://GDC_URL/PROJECT_NAMESPACE/cortex/metrics
    

Replace the following:

  * `GDC_URL`: the URL of your organization in GDC.

    * Example for org-1, zone1: `console.org-1.zone1.google.gdch.test`
    * Replace organization and zone for your application.
  * `PROJECT_NAMESPACE`: your project namespace.

For example, the Cortex endpoint for the `project-1` project in the `org-1` organization is `https://console.org-1.zone1.google.gdch.test/project-1/cortex/metrics.`.

**Note:** You can directly open the URL in a web browser to query metrics. The instructions in the following sections use the `curl` command to call the endpoint, but the same applies to a web browser. For querying multizone metrics, use any zone URL.



#### Authenticate the `curl` request

  1. [Download and install the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview).
  2. [Set](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-config-set) the gdcloud `core/organization_console_url` property:
         
         gdcloud config set core/organization_console_url
         https://GDC_URL
         

  3. [Sign in with the configured identity provider](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth#sign-in-with-idp):
         
         gdcloud auth login
         

  4. Use your username and password to authenticate and sign in.

When the login is successful, you can use the authorization header in your curl request through the `gdcloud auth print-identity-token` command. For more information, see [gdcloud auth](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-auth).




#### Call the Cortex endpoint

Complete the following steps to reach the Cortex endpoint using the `curl` tool:

  1. Authenticate the `curl` request.
  2. Use `curl` to call the Cortex endpoint and extend the URL using the Querying HTTP API Format to query metrics.
  3. In addition to Prometheus URL query parameters, include location parameter to provide list of zones to query for. \- location={string}: list of zones separated by `|` \- If not provided, the query will be executed on all available zones.

The following is an example of a `curl POST` request:
         
         curl POST \
          https://GDC_URL/PROJECT_NAME/cortex/metrics/api/v1/query_range" \
         -H 'Content-Type: application/x-www-form-urlencoded' \
         --data-urlencode 'query=pod_cpu_usage_total' \
         --data-urlencode 'start=2025-07-21T16:00:00Z' \
         --data-urlencode 'end=2025-07-21T16:15:00Z' \
         --data-urlencode 'step=60s' \
         --data-urlencode 'location=zone1|zone2' \
         -H "Authorization: Bearer $(gdcloud auth print-identity-token \
         --audiences=https://GDC_URL)"
         

The following is an example of a `curl GET` request:
         
         curl -X GET \
          https://GDC_URL/PROJECT_NAME/cortex/metrics/api/v1/query_range?query=pod_cpu_usage_total&start=2025-07-21T16:00:00Z&end=2025-07-21T16:15:00Z&step=1s&location=zone1|zone2" \
         -H "Authorization: Bearer $(gdcloud auth print-identity-token \
         --audiences=https://GDC_URL)"
         

You obtain the output, following the command. The API response is in JSON format.

**Note:** Add the `api/v1/query` endpoint to query metrics from the URL. You can include optional parameters for your API call after a _question mark_ (`?`) at the end of the URL. Separate these parameters with _ampersand_ (`&`) symbols as in the example of the `curl` request from the last step.



## Sample queries and labels

You can query metrics using the metric name and key-value pairs for labels. A PromQL query has the following syntax:
    
    
    metric_name{label_one="value", label_two="value"}
    

Labels let you differentiate the characteristics of a metric. In this way, container authors make their workloads generate metrics and add tags to filter those metrics.

For example, you can have an `api_http_requests_total` metric to count the number of HTTP requests received. Then, you can add a `request_method` label on this metric, which takes a `POST`, `GET`, or `PUT` value. Consequently, you create three metric streams for each request type you might receive. In this case, to find the number of HTTP `GET` requests, you run the following query:
    
    
    api_http_requests_total{request_method="GET"}
    

See Metrics and Label Naming for more information about metrics and labels.

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
  
The following code sample shows the use of key-value pairs for labels to query different metrics to view the CPU usage collected in a Kubernetes cluster:
    
    
    pod_cpu_usage_total{cluster="CLUSTER_NAME"}
    

Use the metrics relabeling tool to add labels not exposed initially by the scrapped containers and rename produced metrics. You must configure the `MonitoringTarget` custom resource to add labels on the metrics it collects. Specify those labels in the `metricsRelabelings` field of the custom resource. For more information, see [Label metrics](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/label-metrics).

The following is an example of a response received from a cortex metrics endpoint:
    
    
              {
        "zone1": {
          "status": "success",
          "data": {
            "resultType": "matrix",
            "result": [
              {
                "metric": {
                  "__name__": "pod_cpu_usage_total",
                  "_gdch_project": "project-1",
                  "cluster": "root-admin",
                  "container_name": "otel-collector",
                  "exported_instance": "localhost:2112",
                  "exported_job": "workload-0",
                  "ha_cluster": "root-admin-shard1",
                  "instance": "172.192.1.74:3113",
                  "job": "metrics-server-exporter.mon-system",
                  "namespace": "mon-system",
                  "namespace_name": "mon-system",
                  "pod": "cortex-0",
                  "pod_name": "metrics-server-exporter-695c9f848b-swzgq",
                  "zone_id": "zone1"
                },
                "values": [
                  [
                    1753261200,
                    "2.258621991"
                  ],
                  [
                    1753261800,
                    "1.029301454"
                  ]
                ]
              }
            ]
          }
        },
        "zone2": {
          "status": "success",
          "data": {
            "resultType": "matrix",
            "result": [
              {
                "metric": {
                  "__name__": "pod_cpu_usage_total",
                  "_gdch_project": "project-1",
                  "cluster": "root-admin",
                  "container_name": "otel-collector",
                  "exported_instance": "localhost:2112",
                  "exported_job": "workload-0",
                  "ha_cluster": "root-admin-shard1",
                  "instance": "172.196.3.208:3113",
                  "job": "metrics-server-exporter.mon-system",
                  "namespace": "mon-system",
                  "namespace_name": "mon-system",
                  "pod": "cortex-0",
                  "pod_name": "metrics-server-exporter-695c9f848b-kchfv",
                  "zone_id": "zone2"
                },
                "values": [
                  [
                    1753261200,
                    "1.814027424"
                  ],
                  [
                    1753261800,
                    "2.7767060260000003"
                  ]
                ]
              }
            ]
          }
        }
      }
    

## Querying HTTP API

### Format overview

The API responses are consistently formatted in JSON. Successful requests will always receive a 2xx status code.

For invalid requests, the API handlers will return a JSON error object along with one of the following HTTP status codes:

  * 400 Bad Request: If essential parameters are either missing or incorrectly provided.
  * 503 Service Unavailable: If queries exceed their time limit or are aborted.



Any data that was successfully collected will be included in the "data" field of the response.

The JSON response envelope format is as follows:
    
    
    {
      "status": "success" | "error",
      "data": <data>,
    
      // Only set if status is "error". The data field may still hold
      // additional data.
      "errorType": "<string>",
      "error": "<string>",
    
      // Only set if there were warnings while executing the request.
      // There will still be data in the data field.
      "warnings": ["<string>"],
      // Only set if there were info-level annotations while executing the request.
      "infos": ["<string>"]
    }
    

### Instant queries

The following endpoint evaluates an instant query at a single point in time:
    
    
    GET /api/v1/query
    POST /api/v1/query
    

The following URL query parameters are available for Prometheus expression queries:

  * `query=<string>`: The Prometheus expression query string.
  * `time=<rfc3339 | unix_timestamp>`: An optional evaluation timestamp, specified as an RFC 3339 string or Unix timestamp. If omitted, the current server time is used.
  * `timeout=<duration>`: An optional evaluation timeout. Defaults to and is limited by the query.timeout flag's value.
  * `limit=<number>`: An optional maximum number of series to return. This truncates series for matrixes and vectors but does not affect scalars or strings. A value of 0 disables this limit.
  * `lookback_delta=<number>`: An optional parameter to override the lookback period specifically for this query.



The current server time is used if the time parameter is omitted.

For larger queries that might exceed URL character limits, you can submit these parameters using the POST method. Ensure the request body is URL-encoded and the Content-Type header is set to application/x-www-form-urlencoded.

The data section of the query result has the following format:
    
    
    {
      "resultType": "matrix" | "vector" | "scalar" | "string",
      "result": <value>
    }
    

`<value>` refers to the query result data, which has varying formats depending on the resultType.

The following example evaluates the expression up at the time 2015-07-01T20:10:51.781Z:
    
    
    curl 'http://localhost:9090/api/v1/query?query=up&time=2015-07-01T20:10:51.781Z'
    
    
    
    {
       "status" : "success",
       "data" : {
          "resultType" : "vector",
          "result" : [
             {
                "metric" : {
                   "__name__" : "up",
                   "job" : "prometheus",
                   "instance" : "localhost:9090"
                },
                "value": [ 1435781451.781, "1" ]
             },
             {
                "metric" : {
                   "__name__" : "up",
                   "job" : "node",
                   "instance" : "localhost:9100"
                },
                "value" : [ 1435781451.781, "0" ]
             }
          ]
       }
    }
    

### Range queries

The following endpoint evaluates an expression query over a range of time:
    
    
    GET /api/v1/query_range
    POST /api/v1/query_range
    

The following URL query parameters are available for Prometheus expression queries:

  * `query=<string>`: The Prometheus expression query string.
  * `start=<rfc3339 | unix_timestamp>`: Start timestamp, inclusive.
  * `end=<rfc3339 | unix_timestamp>`: End timestamp, inclusive.
  * `step=<duration | float>`: Query resolution step width in duration format or float number of seconds.
  * `timeout=<duration>`: An optional evaluation timeout. Defaults to and is limited by the query.timeout flag's value.
  * `limit=<number>`: An optional maximum number of series to return. This truncates series for matrixes and vectors but does not affect scalars or strings. A value of 0 disables this limit.
  * `lookback_delta=<number>`: An optional parameter to override the lookback period specifically for this query.



For larger queries that might exceed URL character limits, you can submit these parameters using the POST method. Ensure the request body is URL-encoded and the Content-Type header is set to application/x-www-form-urlencoded.

The data section of the query result has the following format:
    
    
    {
      "resultType": "matrix",
      "result": <value>
    }
    

The following example evaluates the expression up over a 30-second range with a query resolution of 15 seconds.
    
    
    curl 'http://localhost:9090/api/v1/query_range?query=up&start=2015-07-01T20:10:30.781Z&end=2015-07-01T20:11:00.781Z&step=15s'
    
    
    
    {
       "status" : "success",
       "data" : {
          "resultType" : "matrix",
          "result" : [
             {
                "metric" : {
                   "__name__" : "up",
                   "job" : "prometheus",
                   "instance" : "localhost:9090"
                },
                "values" : [
                   [ 1435781430.781, "1" ],
                   [ 1435781445.781, "1" ],
                   [ 1435781460.781, "1" ]
                ]
             },
             {
                "metric" : {
                   "__name__" : "up",
                   "job" : "node",
                   "instance" : "localhost:9091"
                },
                "values" : [
                   [ 1435781430.781, "0" ],
                   [ 1435781445.781, "0" ],
                   [ 1435781460.781, "1" ]
                ]
             }
          ]
       }
    }
    

## Metrics and Label Naming

### Metric Naming Guidelines

When defining metric names, consider the following principles:

  * A metric name SHOULD include a single-word application prefix, which client libraries sometimes refer to as a "namespace." This prefix identifies the domain to which the metric belongs. For application-specific metrics, the application's name is typically used as the prefix.

Examples:

    * prometheus_notifications_total (specific to the Prometheus server)
    * process_cpu_seconds_total (exported by many client libraries)
    * http_request_duration_seconds (for all HTTP requests)
  * A metric name MUST represent a single unit (e.g., avoid mixing seconds with milliseconds, or seconds with bytes).

  * A metric name SHOULD use base units (e.g., seconds, bytes, meters) rather than derived units (e.g., milliseconds, megabytes, kilometers).

  * A metric name SHOULD include a plural unit suffix. For accumulating counts, the suffix "total" should be used in addition to the unit suffix if applicable.

Examples:

    * http_request_duration_seconds
    * node_memory_usage_bytes
    * http_requests_total (for a unit-less accumulating count)
    * process_cpu_seconds_total (for an accumulating count with unit)
    * foobar_build_info (for a pseudo-metric providing metadata about the running binary)
  * A metric name MAY order its components to facilitate convenient grouping when sorted lexicographically, provided all other rules are followed. Related metrics often have common name components placed first to ensure they sort together.

Examples:

    * prometheus_tsdb_head_truncations_closed_total
    * prometheus_tsdb_head_truncations_established_total
    * prometheus_tsdb_head_truncations_failed_total
    * prometheus_tsdb_head_truncations_total
  * A metric name SHOULD consistently represent the same logical "thing-being-measured" across all label dimensions.

Examples:

    * request duration
    * bytes of data transfer
    * instantaneous resource usage as a percentage



### Label Naming Guidelines

When measuring something, use labels to distinguish its characteristics. For example:

  * For total API HTTP requests (`api_http_requests_total`), differentiate by operation type, for example `create`, `update`, `delete` (request types: `operation="create|update|delete"`).
  * For API request duration in seconds (`api_request_duration_seconds`), differentiate by request stage, for example `extract`, `transform`, `load` (request stages: `stage="extract|transform|load"`).



Avoid including label names in the metric name itself, as this creates redundancy and can lead to confusion if those labels are later aggregated.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
