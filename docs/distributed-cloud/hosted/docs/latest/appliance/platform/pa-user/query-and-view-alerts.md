---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/query-and-view-alerts/
title: Query and view open alerts \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:21:48.946752+00:00
---

# Query and view open alerts  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/query-and-view-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Query and view open alerts Stay organized with collections  Save and categorize content based on your preferences. 

This page provides detailed instructions on how to query and visualize open alerts using both the GDC console and the `curl` tool for the Cortex endpoint to gain issue awareness and resolve problems.

After [creating alert rules](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-alert-rules) based on logs and metrics from Google Distributed Cloud (GDC) air-gapped appliance environments, you can start monitoring open alerts from your project. You can visualize and filter alerts that your system events trigger on the GDC console or access them directly from Cortex using the `curl` tool for flexible scripting and automation.

You can access open alerts in one of the following two methods:

  * **GDC console** : Visualize alerting data in integrated panels containing information like the number of alerts for a specific data source, the severity level, duration, status, message, and labels. The GDC console provides a user-friendly interface for filtering and analyzing alerts from your system components.
  * **Cortex Alertmanager endpoint** : For more advanced use cases, query your project's Cortex instance directly using the `curl` tool on a command line. Cortex stores your project's Alertmanager alerts and provides an HTTP endpoint for programmatic access. This access lets you export data, automate tasks, configure cron jobs, and build custom integrations.



## Before you begin

To get the permissions that you need to query and visualize alerts, ask your Project IAM Admin to grant you one of the associated Project Cortex Alertmanager roles in your project namespace. Depending on the level of access and permissions you need, you might obtain editor or viewer roles for this resource in a project.

To get the permissions that you need to export logs, ask your Project IAM Admin to grant you the Project Grafana Viewer (`project-grafana-viewer`) role. This role-based access control process lets you access data visualizations safely. For more information about these roles, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/obs-iam-permissions).

The following table summarizes the `Role` requirements for `PA and AO persona`.

Persona | Object | Cluster | Role | Namespace | Group/User | Config  
---|---|---|---|---|---|---  
PA | alertmanager | org-admin | `project-cortex-alertmanager-viewer` | platform-obs | Group | 1  
PA | alertmanager | org-admin | `project-cortex-alertmanager-viewer` | platform-obs | User | 2  
AO | alertmanager | org-admin | `project-cortex-alertmanager-viewer` | PROJECT_NAMESPACE | Group | 1  
AO | alertmanager | org-admin | `project-cortex-alertmanager-viewer` | PROJECT_NAMESPACE | User | 2  
  
Replace the following variables appropriately:

Variable | Description  
---|---  
`KUBECONFIG` | You will need the kubeconfig for the specific cluster that contains the NAMESPACE where this RoleBinding will be applied.  
`RULE_NAME` | The unique name for this `RoleBinding` resource within the namespace. For example, `pa-cortex-alertmanager-viewer`.  
`NAMESPACE` | The Kubernetes namespace where this `RoleBinding` will be created and apply. Look for the `Namespace` column in the previous table.  
`EMAIL_ADDRESS` | The identifier for the user being granted the role. This is often an email address. For example, `platform-administrator@example.com`.  
`ROLE` | The name of the `Role` that contains the permissions you want to grant to the user. Look for the roles available in the previous table  
`GROUP_NAME` | The name of the `Group` to which PA/AO user belongs to. For example, `pa-group`.  
`ZONE` | Name of the Zone  
**Important:** Before committing configuration, ensure the `kustomization.yaml` file exists in the folder where you are create the yaml file.

###  Config 1 

This configuration grants permissions to a user group to access PA/AO alerts in `org` cluster. After setting up this configuration, refer [console](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/query-and-view-alerts#console) section of this document to view alerts on the GDC console.

  * **Kubectl Command**

This is the generic command format:
        
        kubectl --kubeconfig `KUBECONFIG` create rolebinding `RULE_NAME` -n `NAMESPACE` --group=`GROUP_NAME` --role=project-cortex-alertmanager-viewer
        

**Example:**
        
        kubectl --kubeconfig <path-to-kubeconfig> create rolebinding project-cortex-alertmanager-viewer-binding --role=project-cortex-alertmanager-viewer --group=my-team --namespace=platform-obs
        

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
          name: project-cortex-alertmanager-viewer
          apiGroup: rbac.authorization.k8s.io
        




###  Config 2 

This configuration grants permissions to a user to access PA/AO alerts in `org` cluster. After setting up this configuration, refer [console](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/query-and-view-alerts#console) section of this document to view alerts on the GDC console.

  * **Kubectl Command**

This is the generic command format:
        
        kubectl --kubeconfig `KUBECONFIG` create rolebinding `RULE_NAME` -n `NAMESPACE` --user=`EMAIL_ADDRESS` --role=project-cortex-alertmanager-viewer
        

**Example:**
        
        kubectl --kubeconfig <path-to-kubeconfig> create rolebinding project-cortex-alertmanager-viewer-binding --role=project-cortex-alertmanager-viewer --user=my-email@example.com --namespace=platform-obs
        

  * **IAC File path**
        
        /infrastructure/zonal/zones/`ZONE`/org-admin/rolebindings/`EMAIL_ADDRESS`/<YAML_FILE>
        

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
          name: project-cortex-alertmanager-viewer
          apiGroup: rbac.authorization.k8s.io
        

For more information about these roles, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/obs-iam-permissions)




### Grafana endpoint

**For Application Operator (AO):**

Open the following URL to access the endpoint of your project:
    
    
    https://GDC_URL/PROJECT_NAMESPACE/grafana
    

Replace the following:

  * GDC_URL: The URL of your organization in GDC.
  * PROJECT_NAMESPACE: The namespace of your project.



The project's UI contains default dashboards such as the **Alerts - Overview** dashboard with information about alerts. Querying alerts from the UI lets you visually retrieve alerting information from your project and get an integrated view of resources for awareness and quick resolution of problems.

**For Platform Admin (PA):**

Open the following URL to access the endpoint of your `platform-obs` project:
    
    
    https://GDC_URL/platform-obs/grafana
    

Replace GDC_URL with the URL of your organization in GDC.

The user interface (UI) of the system monitoring instance contains default dashboards such as the **Alerts - Overview** dashboard with information about alerts for data observability. Querying alerts from the UI lets you visually retrieve alerting information from your project and get an integrated view of resources for awareness and quick resolution of problems.

![The Alerts - Overview dashboard shows information about the number of alerts for a specific data source and a line graph of the alerts history, showing the number of alerts open per hour for the data source.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/admin/images/alerts.png)

**Figure 1.** The **Alerts - Overview** dashboard on the Grafana UI.

## View and filter open alerts

Select one of the following methods to query and filter open alerts from your project namespace:

###  Console 

View the open alerts in a project from the GDC console:

  1. [Sign in to the GDC console](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in).
  2. In the GDC console, select your project.
  3. In the navigation menu, select **Operations** > **Alerting**.
  4. Select the **Alerts** tab.
  5. View the list of alerts.
  6. On the **Alerts opened** section, click **Filter** to only display open alerts. You can also filter alerts by other property names or values.
  7. Click an alert name to view the alert details.



###  Cortex endpoint 

This section describes how to access alerts using your Cortex Alertmanager endpoint.

#### Identify your Cortex endpoint

The following URL is the endpoint of the Cortex instance of your project:
    
    
      https://GDC_URL/PROJECT_NAMESPACE/cortex/alertmanager/
    

Replace the following:

  * `GDC_URL`: the URL of your organization in GDC.
  * `PROJECT_NAMESPACE`: your project namespace.

For example, the Cortex endpoint for the `platform-obs` project in the `org-1` organization is `https://org-1/platform-obs/cortex/alertmanager/`.

**Note:** You can directly open the URL in a web browser to query alerts. The instructions in the following sections use the `curl` command to call the endpoint, but the same applies to a web browser.



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
  2. Use `curl` to call the Cortex endpoint and extend the URL using the standard Alertmanager API specification (<https://prometheus.io/docs/prometheus/latest/querying/api/#alertmanagers>) to query alerts.

The following is an example of a `curl` request:
         
         curl https://GDC_URL/PROJECT_NAME/cortex/alertmanager/api/v1/alertmanagers \
           -H "Authorization: Bearer $(gdcloud auth print-identity-token \
           --audiences=https://GDC_URL)"
         

You obtain the output following the command. The API response is in JSON format.

**Note:** Add the `api/v1/alertmanagers` endpoint to query active and eliminated alerts from the URL.



## Alertmanager

Alertmanager lets you monitor alert notifications from client applications. You can inspect and silence alerts using Alertmanager, and filter or group alerts:

![Ignore Loki rejection audit logs alerts in the root admin cluster](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/admin/images/alert-manager.png)

**Figure 2.** Menu option to query audit logs from the Alertmanager.

### Predefined alerting policies

The following table lists the pre-installed alerting rules in Prometheus:

**Name** | **Description**  
---|---  
KubeAPIDown (critical) | KubeAPI has disappeared from Prometheus target discovery for 15 minutes.  
KubeClientErrors (warning) | Kubernetes API server client errors ratio > 0.01 for 15 minutes.  
KubeClientErrors (critical) | Kubernetes API server client errors ratio > 0.1 for 15 minutes.  
KubePodCrashLooping (warning) | Pod has been in a crash looping state for longer than 15 minutes.  
KubePodNotReady (warning) | Pod has been in a non-ready state for longer than 15 minutes.  
KubePersistentVolumeFillingUp (critical) | Free bytes of a claimed PersistentVolume < 0.03.  
KubePersistentVolumeFillingUp (warning) | Free bytes of a claimed PersistentVolume < 0.15.  
KubePersistentVolumeErrors (critical) | The persistent volume is in the Failed or Pending phase for five minutes.  
KubeNodeNotReady (warning) | Node has been unready for more than 15 minutes.  
KubeNodeCPUUsageHigh (critical) | Node CPU usage is > 80%.  
KubeNodeMemoryUsageHigh (critical) | Node memory usage is > 80%.  
NodeFilesystemSpaceFillingUp (warning) | Node file system usage is > 60%.  
NodeFilesystemSpaceFillingUp (critical) | Node file system usage is > 85%.  
CertManagerCertExpirySoon (warning) | A certificate is expiring in 21 days.  
CertManagerCertNotReady (critical) | A certificate is not ready to serve traffic after 10 minutes.  
CertManagerHittingRateLimits (critical) | A rate limit has been hit creating and renewing certificates for five minutes.  
DeploymentNotReady (critical). | A Deployment on the org admin cluster has been in a non-ready state for longer than 15 minutes.  
  
### Sample alertmanagerConfigurationConfigmaps

Syntax of configs in ConfigMaps that `alertmanagerConfigurationConfigmaps` lists must follow <https://prometheus.io/docs/alerting/latest/configuration/>
    
    
    apiVersion: observability.gdc.goog/v1alpha1
    kind: ObservabilityPipeline
    metadata:
      # Choose namespace that matches the project's namespace
      namespace: kube-system
      name: observability-config
    # Configure Alertmanager
     alerting:
      # Storage size for alerting data within organization
      # Permission: PA
      localStorageSize: 1Gi
    
      # Permission: PA & AO
      # alertmanager config must be under the key "alertmanager.yml" in the configMap
      alertmanagerConfig: <configmap-for-alertmanager-config>
    
      # Permission: PA
      volumes:
        - <volume referenced in volumeMounts>
    
      # Permission: PA
      volumeMounts:
        - <volumeMount referenced in alertmanagerConfig>
    

### Sample rule configuration
    
    
    # Configures either an alert or a target record for precomputation
    apiVersion: monitoring.gdc.goog/v1alpha1
    kind: MonitoringRule
    metadata:
      # Choose namespace that contains the metrics that rules are based on
      # Note: alert/record will be produced in the same namespace
      namespace: g-fleetns-a
      name: alerting-config
    spec:
      # Rule evaluation interval
      interval: <duration>
    
      # Configure limit for number of alerts (0: no limit)
      # Optional, Default: 0 (no limit)
      limit: <int>
    
      # Configure record rules
      recordRules:
        # Define which timeseries to write to (must be a valid metric name)
      - record: <string>
    
        # Define PromQL expression to evaluate for this rule
        expr: <string>
    
        # Define labels to add or overwrite
        # Optional, Map of {key, value} pairs
        labels:
          <labelname>: <labelvalue>
    
      # Configure alert rules
      alertRules:
        # Define alert name 
      - alert: <string>
    
        # Define PromQL expression to evaluate for this rule
        # https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/
        expr: <string>
    
        # Define when an active alert moves from pending to firing
        # Optional, Default: 0s
        for: <duration>
    
        # Define labels to add or overwrite
        # Required, Map of {key, value} pairs
        # Required labels: 
        #     severity: [error, critical, warning, info]
        #     code: 
        #     resource: component/service/hardware related to alert
        #     additional labels are optional
        labels:
          severity: <enum: [error, critical, warning, info]>
          code: 
          resource: <Short name of the related operable component>
          <labelname>: <tmpl_string>
    
        # Define annotations to add
        # Optional, Map of {key, value} pairs
        # Recommended annotations:
        #     message: value of Message field in UI
        #     expression: value of Rule field in UI
        #     runbookurl: URL for link in Actions to take field in UI
        annotations:
          <labelname>: <tmpl_string>
    
    
    
    # Configures either an alert or a target record for precomputation
    apiVersion: logging.gdc.goog/v1alpha1
    kind: LoggingRule
    metadata:
      # Choose namespace that contains the logs that rules are based on
      # Note: alert/record will be produced in the same namespace
      namespace: g-fleetns-a
      name: alerting-config
    spec:
      # Choose which log source to base alerts on (Operational/Audit/Security Logs)
      # Optional, Default: Operational
      source: <string>
    
      # Rule evaluation interval
      interval: <duration>
    
      # Configure limit for number of alerts (0: no limit)
      # Optional, Default: 0 (no limit)
      limit: <int>
    
      # Configure record rules
      recordRules:
        # Define which timeseries to write to (must be a valid metric name)
      - record: <string>
    
        # Define LogQL expression to evaluate for this rule
        # https://grafana.com/docs/loki/latest/rules/
        expr: <string>
    
        # Define labels to add or overwrite
        # Optional, Map of {key, value} pairs
        labels:
          <labelname>: <labelvalue>
    
      # Configure alert rules
      alertRules:
        # Define alert name
      - alert: <string>
    
        # Define LogQL expression to evaluate for this rule
        expr: <string>
    
        # Define when an active alert moves from pending to firing
        # Optional, Default: 0s
        for: <duration>
    
        # Define labels to add or overwrite
        # Required, Map of {key, value} pairs
        # Required labels: 
        #     severity: [error, critical, warning, info]
        #     code: 
        #     resource: component/service/hardware related to alert
        #     additional labels are optional
        labels:
          severity: <enum: [error, critical, warning, info]>
          code:
          resource: <Short name of the related operable component>
          <labelname>: <tmpl_string>
    
        # Define annotations to add
        # Optional, Map of {key, value} pairs
        # Recommended annotations:
        #     message: value of Message field in UI
        #     expression: value of Rule field in UI
        #     runbookurl: URL for link in Actions to take field in UI
        annotations:
          <labelname>: <tmpl_string>
    

## Query alerts from the HTTP API

The Observability platform exposes an HTTP API endpoint for querying and reading metrics, alerts, and other time series data from your project for system monitoring. 

Query alerts directly from the Observability HTTP API to set up automated tasks, adapt responses, and build integrations according to your use case. For example, insert the output into another command, export details to text file formats, or configure a Linux cron job. You can call the Observability HTTP API from the command-line interface (CLI) or a web browser and obtain the result in JSON format.

This section explains how to call the Observability HTTP API endpoint from the CLI using the API specification to query alerts.

Query alerts directly from the Observability HTTP API to set up automated tasks, adapt responses, and build integrations according to your use case. For example, insert the output into another command, export details to text file formats, or configure a Linux cron job. You can call the Observability HTTP API from the command-line interface (CLI) or a web browser and obtain the result in JSON format.

This section explains how to call the Observability HTTP API endpoint from the CLI using the Alertmanager API specification to query metrics.

### Before you begin

To get the permissions you need to access the Observability HTTP API endpoint, ask your Project IAM Admin to grant you the Project Cortex Alertmanager Viewer (`project-cortex-alertmanager-viewer`) role in your project namespace.

The Project IAM Admin can grant you access by creating a role binding:

a. Infrastructure Operator (IO) Root-Admin - `Project Cortex Alertmanager Viewer`:
    
    
    kubectl --kubeconfig $HOME/root-admin-kubeconfig create rolebinding 
    io-cortex-alertmanager-viewer-binding -n infra-obs 
    --user=fop-infrastructure-operator@example.com 
    --role=project-cortex-alertmanager-viewer
    

b. Platform-Admin (PA) Root-Admin - `Project Cortex Alertmanager Viewer`:
    
    
    kubectl --kubeconfig $HOME/root-admin-kubeconfig create rolebinding
    pa-cortex-alertmanager-viewer-binding -n platform-obs 
    --user=fop-platform-admin@example.com 
    --role=project-cortex-alertmanager-viewer
    

c. Application Operator (AO) Root-Admin - Project Cortex Alertmanager Viewer: Project: $AO_PROJECT AO User Name: $AO_USER
    
    
    kubectl --kubeconfig $HOME/root-admin-kubeconfig create rolebinding 
    project-cortex-alertmanager-viewer-binding -n $AO_PROJECT 
    --user=$AO_USER 
    --role=project-cortex-alertmanager-viewer
    

After the role binding is created, you can access corresponding Alertmanager with your login username.

### Verify the role binding
    
    
    kubectl --kubeconfig $HOME/org-1-admin-kubeconfig get rolebinding -n platform-obs
    

For information about setting role bindings from the GDC console, see [Grant access to resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/set-up-role-bindings#set-up-role-bindings).

### Cortex endpoint

The following URL is the Cortex endpoint for accessing alerts:
    
    
    https://GDC_URL/PROJECT_NAME/cortex/alertmanager/
    

Replace the following:

  * GDC_URL: The URL of your organization in GDC.
  * PROJECT_NAME: The name of your project.



### Call the API endpoint

Follow these steps to reach the Cortex API endpoint from the CLI and query alerts:

  1. Ensure you meet the prerequisites.
  2. Open the CLI.
  3. Use the `curl` tool to call the Cortex endpoint URL and extend the URL using the standard <https://prometheus.io/docs/prometheus/latest/querying/api/#alertmanagers> to query alerts. For example:
         
         curl https://console.org-1.zone1.google.gdch.test/alice/cortex/alertmanager/api/v1/alertmanagers
         




You obtain the output in the CLI following the command. The API response format is JSON.

**Note:** Add the `api/v1/alertmanagers` endpoint to query active and dropped Alertmanager alerts from the URL.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
