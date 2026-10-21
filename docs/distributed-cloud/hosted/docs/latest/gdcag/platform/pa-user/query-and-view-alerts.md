---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/query-and-view-alerts/
title: Query and view open alerts \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:44:05.577021+00:00
---

# Query and view open alerts  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/query-and-view-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Query and view open alerts Stay organized with collections  Save and categorize content based on your preferences. 

This page provides detailed instructions on how to query and visualize open alerts using both the GDC console and the `curl` tool for the Cortex endpoint to gain issue awareness and resolve problems.

After [creating alert rules](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-alert-rules) based on logs and metrics from Google Distributed Cloud (GDC) air-gapped environments, you can start monitoring open alerts from your project. You can visualize and filter alerts that your system events trigger on the GDC console or access them directly from Cortex using the `curl` tool for flexible scripting and automation.

You can access open alerts in one of the following two methods:

  * **GDC console** : Visualize alerting data in integrated panels containing information like the number of alerts for a specific data source, the severity level, duration, status, message, and labels. The GDC console provides a user-friendly interface for filtering and analyzing alerts from your system components.
  * **Cortex Alertmanager endpoint** : For more advanced use cases, query your project's Cortex instance directly using the `curl` tool on a command line. Cortex stores your project's Alertmanager alerts and provides an HTTP endpoint for programmatic access. This access lets you export data, automate tasks, configure cron jobs, and build custom integrations.



## Before you begin

To get the permissions that you need to query and visualize alerts, ask your Project IAM Admin to grant you one of the associated Project Cortex Alertmanager roles in your project namespace. Depending on the level of access and permissions you need, you might obtain editor or viewer roles for this resource in a project.

The following table summarizes the `Role` requirements for `PA and AO persona`.

Persona | Object | Cluster | Role | Namespace | Group/User | Config  
---|---|---|---|---|---|---  
PA | grafana | org-admin | `project-cortex-alertmanager-viewer` | platform-obs | Group | 1  
PA | grafana | org-admin | `project-cortex-alertmanager-viewer` | platform-obs | User | 2  
AO | alertmanager | org-admin | `project-cortex-alertmanager-viewer` | PROJECT_NAMESPACE | Group | 1  
AO | alertmanager | org-admin | `project-cortex-alertmanager-viewer` | PROJECT_NAMESPACE | User | 2  
  
Replace the following variables appropriately:

Variable | Description  
---|---  
`KUBECONFIG` | You will need the kubeconfig for the specific cluster that contains the NAMESPACE where this RoleBinding will be applied.  
`RULE_NAME` | The unique name for this `RoleBinding` resource within the namespace. For example, `pa-cortex-alertmanager-viewer`.  
`NAMESPACE` | The Kubernetes namespace where this `RoleBinding` will be created and apply. Look for the `Namespace` column in the previous table.  
`EMAIL_ADDRESS` | The identifier for the user being granted the role. This is often an email address. For example, `infrastructure-operator@example.com`.  
`ROLE` | The name of the `Role` that contains the permissions you want to grant to the user. Look for the roles available in the previous table  
`GROUP_NAME` | The name of the `Group` to which PA/AO user belongs to. For example, `pa-group`.  
`ZONE` | Name of the Zone  
**Important:** Before committing configuration, ensure the `kustomization.yaml` file exists in the folder where you are create the yaml file.

###  Config 1 

This configuration grants permissions to a user group to access PA/AO alerts in `org` cluster. After setting up this configuration, refer [console](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/query-and-view-alerts#console) section of this document to view alerts on the GDC console.

  * **Kubectl Command**

This is the generic command format:
        
        kubectl --kubeconfig `KUBECONFIG` create rolebinding `RULE_NAME` -n `NAMESPACE` --group=`GROUP_NAME` --role=project-cortex-alertmanager-viewer
        

**Example:**
        
        kubectl --kubeconfig <path-to-kubeconfig> create rolebinding project-cortex-alertmanager-viewer-binding --role=project-cortex-alertmanager-viewer --group=my-team --namespace=platform-obs
        

  * **IAC File path**
        
        /infrastructure/zonal/zones/`ZONE`/org-admin/rolebindings/`GROUP_NAME`/<YAML_FILE>
        

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

This configuration is for the `PA` persona, targeting the `grafana` object in the `org-admin` cluster. It grants the `project-cortex-alertmanager-viewer` role within the `platform-obs` namespace to a `User`.

  * **Kubectl Command**

This is the generic command format:
        
        kubectl --kubeconfig `KUBECONFIG` create rolebinding `RULE_NAME` -n platform-obs --user=`EMAIL_ADDRESS` --role=project-cortex-alertmanager-viewer
        

**Example:**
        
        kubectl --kubeconfig <path-to-kubeconfig> create rolebinding project-cortex-alertmanager-viewer-binding --role=project-cortex-alertmanager-viewer --user=my-email@example.com --namespace=platform-obs
        

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
          name: project-cortex-alertmanager-viewer
          apiGroup: rbac.authorization.k8s.io
        

For more information about these roles, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/obs-iam-permissions).




## View and filter open alerts

Select one of the following methods to query and filter open alerts from your project namespace:

###  Console 

View the open alerts in a project from the GDC console:

  1. [Sign in to the GDC console](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in).
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
  2. Use `curl` to call the Cortex endpoint and extend the URL using the standard Alertmanager API specification (<https://prometheus.io/docs/prometheus/latest/querying/api/#alertmanagers>) to query alerts.

The following is an example of a `curl` request:
         
         curl https://GDC_URL/PROJECT_NAME/cortex/alertmanager/api/v1/alertmanagers \
           -H "Authorization: Bearer $(gdcloud auth print-identity-token \
           --audiences=https://GDC_URL)"
         

You obtain the output following the command. The API response is in JSON format.

**Note:** Add the `api/v1/alertmanagers` endpoint to query active and eliminated alerts from the URL.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
