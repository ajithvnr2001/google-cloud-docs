---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-gke/
title: Integrate GKE with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:33:36.126202+00:00
---

# Integrate GKE with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate GKE with Google SecOps

This document explains how to configure and integrate Google Kubernetes Engine (GKE) with Google Security Operations.

**Important:** In the Google SecOps platform, the integration for GKE is called _Google Kubernetes Engine_.

## Use cases

The GKE integration uses Google SecOps capabilities to support the following use cases:

  * **Cluster inventory** : Automatically retrieve a list of all GKE clusters within a specified location. This helps security teams to maintain an up-to-date inventory of their Kubernetes infrastructure.

  * **Dynamic auto scaling** : Automatically adjust the size of node pools in response to security events or operational alerts, ensuring optimal performance.

  * **Label-based isolation** : Automatically apply labels to GKE clusters based on security policies or incident response procedures.

  * **Add-on configuration adjustment** : Automatically enable or disable GKE add-ons based on security best practices. Disabling insecure add-ons can reduce the attack surface.

  * **Operation status monitoring** : Automatically monitor the status of GKE operations that are triggered by security playbooks or incident response workflows. This lets security analysts monitor remediation progress and check the status of ongoing operations.




## Before you begin

Before you configure the **GKE** integration in Google SecOps, complete the following prerequisite steps:

  1. Create and configure a custom Identity and Access Management role.

  2. Create a service account.

  3. Choose and configure one of the following authentication methods:

     * **Option 1:Workload Identity (recommended)**: This method uses short-lived tokens via service account impersonation.

     * **Option 2:Service account JSON key**: This method relies on a static, long-lived secret key file.




### Create and configure an IAM role

To provide the integration with the necessary permissions, create a custom role in your project:

  1. In the Google Cloud console, go to **Roles**.

[Go to Roles](https://console.cloud.google.com/iam-admin/roles)

  2. Click **Create role**.

  3. Provide a **Title** (for example, `SecOps GKE Analyst`), **Description** , and a unique **ID**.

  4. Set the **Role Launch Stage** to **General Availability**.

  5. Add the following permissions to the role:

     * `container.clusters.list`
     * `container.clusters.update`
     * `container.clusters.get`
     * `container.operations.list`
     * `container.operations.get`
  6. Click **Create**.




### Create a service account

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click **add Create service account**.

  3. Provide a name and description, and click **Create and continue**.

  4. In the **Grant this service account access to project** step, assign the custom IAM role you created.

  5. Click **Done**. Take note of the service account's **Email address**.




### Configure Workload Identity credentials

Workload Identity is the recommended approach as it uses short-lived access tokens using service account impersonation.

#### Identify the unique instance identity

Establishing a connection requires granting your Google SecOps instance permission to impersonate your service account.

  1. In Google SecOps, go to **Content Hub > Response Integrations**.

  2. Select the **GKE** integration and enter your service account email in the `Workload Identity Email` field.

  3. Click **Save > Test**. The test is expected to fail. 

  4. Click the close_small button next to **Test** and locate the identity email beginning with `gke-init-python@...` or `soar-python@...`.

  5. Copy this unique email address.




#### Authorize the instance identity in Google Cloud

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select the target service account and navigate to **Permissions > Grant Access**.

  3. Paste the unique email address into the **New principals** field and assign the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`).




#### Grant quota project access

Authenticating with Workload Identity requires a `Quota Project ID` to track API usage and billing. 

  1. In the Google Cloud console, go to **IAM** for the project used as the quota project.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Locate your service account and click **Edit principal** (edit).

  3. Click **Add another role** and select **Service Usage Consumer** (`roles/serviceusage.serviceUsageConsumer`).

  4. Click **Save**.




### Configure a JSON key

Static, long-lived secret key files require manual rotation. Only use this method if Workload Identity authentication is unavailable.

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts** and select your service account.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Go to the **Keys** tab and click **Add key > Create new key**.

  3. Select **JSON** and click **Create**. The browser downloads the JSON file to your computer.




#### Configure manual individual parameters

If you choose to enter credentials manually, keep the downloaded JSON key file open in a text editor to copy the individual values required in the integration settings.

## Integration parameters

To establish a connection between Google SecOps and GKE, you must configure the following parameters. The integration supports three distinct authentication paths. Choose one of the following methods to provide credentials:

  * **Workload Identity** : Uses `Workload Identity Email` and `Quota Project ID`.

  * **Service account JSON file** : Uses `Service Account Json File Content` to provide the entire key file.

  * **Manual individual parameters** : Uses separate fields manually copied from a JSON key.


Parameter | Description  
---|---  
`API Root` | Required. The API root of the GKE instance. The default value is `https://container.googleapis.com`.  
`Workload Identity Email` | Optional. The client email address of your service account. Only configure this parameter if you're authenticating using a Workload Identity. If configured, you must also provide a `Quota Project ID` and `Service Account JSON File Content` is ignored.  
`Service Account Json File Content` | Optional. The full content of the service account key JSON file. Only configure this parameter if you're authenticating using a JSON key.  
`Project ID` | Optional. The project ID to target in GKE. If no value is provided, the integration retrieves the ID from the service account credentials.  
`Quota Project ID` | Optional. The project ID used for API usage and billing. This parameter is required when using Workload Identity authentication. If no value is provided, the integration retrieves the ID from the service account credentials.  
`Location ID` | Optional. The location ID used to scope cluster operations. The default value is `europe-central2-a`.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Google Cloud server. Enabled by default.  
  
### Individual credential parameters

Only configure the following parameters if you're manually entering credentials rather than using the full JSON file content or a Workload Identity.

Parameter | Description  
---|---  
`Account Type` | Optional.The value found in the `type` field of your JSON key (typically `service_account`).  
`Private Key ID` | Optional.The value found in the `private_key_id` field of your JSON key.  
`Private Key` | Optional.The value found in the `private_key` field of your JSON key.  
`Client Email` | Optional.The value found in the `client_email` field of your JSON key.  
`Client ID` | Optional.The value found in the `client_id` field of your JSON key.  
`Auth URI` | Optional.The value found in the `auth_uri` field of your JSON key. The default is `https://accounts.google.com/o/oauth2/auth`.  
`Token URI` | Optional.The value found in the `token_uri` field of your JSON key. The default is `https://oauth2.googleapis.com/token`.  
`Auth Provider X509 URL` | Optional.The value found in the `auth_provider_x509_cert_url` field of your JSON key.  
`Client X509 URL` | Optional.The value found in the `client_x509_cert_url` field of your JSON key.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Get Operation Status

Use the **Get Operation Status** action to retrieve the GKE operation status.

This action is asynchronous. Adjust the Google SecOps integrated development environment (IDE) for the action as needed.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Get Operation Status** action requires the following parameters:

Parameter | Description  
---|---  
`Location` | Required.A location to retrieve the operation statuses, such as `europe-central2-a`.  
`Operation Name` | Required.An operation to retrieve.  
`Wait for the operation to finish` | Optional.If selected, the action waits for the results of the operation.Not selected by default.  
  
#### Action outputs

The **Get Operation Status** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Get Operation Status** action:
    
    
    {
        "name": "operation-OPERATION_ID",
        "zone": "europe-central2-a",
        "operationType": "SET_NODE_POOL_SIZE",
        "status": "RUNNING",
        "selfLink": "https://container.googleapis.com/v1/projects/PROJECT_ID/zones/europe-central2-a/operations/operation-OPERATION_ID",
        "targetLink": "https://container.googleapis.com/v1/projects/PROJECT_ID/zones/europe-central2-a/clusters/cluster-test/nodePools/default-pool",
        "startTime": "2021-08-15T11:53:55.904254615Z"
    }
    

##### Output messages

The **Get Operation Status** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully fetched operation details.` `Failed to execute the action because API returned error, please see action logs LOG_SNIPPET.` `Operation  OPERATION_NAME is still in progress, current status: STATUS.` `Operation OPERATION_NAME successfully finished.` `Operation OPERATION_NAME failed to complete with the following status: STATUS.` | The action succeeded.  
`Provided cluster location CLUSTER_LOCATION does not exist.` `Provided operation name OPERATION_NAME was not found.` `Error executing action "Set Node Count". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Operation Status** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List Clusters

Use the **List Clusters** action to list GKE clusters based on the specified search criteria.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **List Clusters** action requires the following parameters:

Parameter | Description  
---|---  
`Cluster Location` | Required.The location to search for clusters, such as `europe-central2-a`.  
`Filter Logic` | Optional.The filter logic to apply.The filtering logic works with the `cluster name` field.The possible values are as follows:

  * `Not Specified`
  * `Equal`
  * `Contains`

The default value is `Not Specified`.  
`Filter Value` | Optional.The value to use for the filter.The filtering logic works with the `cluster name` field.If you set the `Filter Logic` parameter to `Equal`, the action searches for the `Filter Value` exact match among results. If you set the `Filter Logic` parameter to `Contains`, the action searches for results that contain the substring that you specify in this parameter. If you don't set a value, the action ignores the filter.  
`Max Records To Return` | Optional.The number of records to return. The default value is `50`.  
  
#### Action outputs

The **List Clusters** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **List Clusters** action can return the following table:

Table name: **Found Clusters**

Table columns:

  * **ID**
  * **Name**
  * **Description**
  * **Cluster Network**
  * **Cluster IPv4 CIDR**
  * **Labels**
  * **Cluster Endpoint**
  * **Status**
  * **Location**
  * **Zone**
  * **Initial Cluster Version**
  * **Current Master Version**
  * **Current Node Version**
  * **Create Time**



##### JSON result

The following example shows the JSON result output received when using the **List Clusters** action:
    
    
    {
               "name": "cluster-test",
               "description": "Requested by user",
               "nodeConfig": {
                   "machineType": "e2-micro",
                   "diskSizeGb": 15,
                   "oauthScopes": [
                       "https://www.googleapis.com/auth/devstorage.read_only",
                       "https://www.googleapis.com/auth/logging.write",
                       "https://www.googleapis.com/auth/monitoring",
                       "https://www.googleapis.com/auth/servicecontrol",
                       "https://www.googleapis.com/auth/service.management.readonly",
                       "https://www.googleapis.com/auth/trace.append"
                   ],
                   "metadata": {
                       "disable-legacy-endpoints": "true"
                   },
                   "imageType": "COS",
                   "tags": [
                       "pod-net-tag"
                   ],
                   "serviceAccount": "default",
                   "diskType": "pd-standard",
                   "shieldedInstanceConfig": {
                       "enableIntegrityMonitoring": true
                   }
               },
               "masterAuth": {
                   "clusterCaCertificate": "CERTIFICATE"
               }
    }
    

##### Output messages

The **List Clusters** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully found clusters for the provided criteria in GKE.` `No clusters were found for the provided criteria in GKE.` | The action succeeded.  
`Provided cluster location CLUSTER_LOCATION does not exist.` `Invalid value was provided for "Max Records to Return": MAX_RECORDS_TO_RETURN. Positive number should be provided.` `Error executing action "List Clusters". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **List Clusters** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List Node Pools

Use the **List Node Pools** action to list node pools for the GKE cluster based on the specified search criteria.

The filtering logic works with the `node pool name` field.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **List Node Pools** action requires the following parameters:

Parameter | Description  
---|---  
`Cluster Location` | Required.A location to search for clusters, such as `europe-central2-a`.  
`Cluster Name` | Required.The name of the cluster to search for.  
`Filter Logic` | Optional.The filter logic to apply.The filtering logic works with the `node pool name` field.The possible values are as follows:

  * `Not Specified`
  * `Equal`
  * `Contains`

The default value is `Not Specified`.  
`Filter Value` | Optional.The value to use for the filter.The filtering logic works with the `node pool name` field.If you set the `Filter Logic` parameter to `Equal`, the action searches for the `Filter Value` exact match among results. If you set the `Filter Logic` parameter to `Contains`, the action searches for results that contain the substring that you specify in this parameter. If you don't set a value, the action ignores the filter.  
`Max Records To Return` | Optional.The number of records to return. The default value is `50`.  
  
#### Action outputs

The **List Node Pools** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **List Node Pools** action can return the following table:

Table name: **Found Node Pools**

  * **Name**
  * **Status**
  * **Version**
  * **Machine Type**
  * **Tags**
  * **Service Account**
  * **Initial Node Count**
  * **Autoscaling**
  * **Max Pods Constraint**
  * **Locations**



##### JSON result

The following example shows the JSON result output received when using the **List Node Pools** action:
    
    
    {
        "nodePools": [
            {
                "name": "example-pool",
                "config": {
                    "machineType": "e2-micro",
                    "diskSizeGb": 15,
                    "oauthScopes": [
                        "https://www.googleapis.com/auth/devstorage.read_only",
                        "https://www.googleapis.com/auth/logging.write",
                        "https://www.googleapis.com/auth/monitoring",
                        "https://www.googleapis.com/auth/servicecontrol",
                        "https://www.googleapis.com/auth/service.management.readonly",
                        "https://www.googleapis.com/auth/trace.append"
                    ],
                    "metadata": {
                        "disable-legacy-endpoints": "true"
                    },
                    "imageType": "COS",
                    "tags": [
                        "pod-net-tag"
                    ],
                    "serviceAccount": "default",
                    "diskType": "pd-standard",
                    "shieldedInstanceConfig": {
                        "enableIntegrityMonitoring": true
                    }
                },
                "initialNodeCount": 3,
                "autoscaling": {},
                "management": {
                    "autoUpgrade": true,
                    "autoRepair": true
                },
                "maxPodsConstraint": {
                    "maxPodsPerNode": "8"
                },
                "podIpv4CidrSize": 28,
                "locations": [
                    "europe-central2-a"
                ],
                "networkConfig": {
                    "podRange": "gke-cluster-example-pods-ID",
                    "podIpv4CidrBlock": "192.0.2.0/24"
                },
                "selfLink": "https://container.googleapis.com/v1/projects/PROJECT_ID/zones/europe-central2-a/clusters/cluster-example/nodePools/example-pool",
                "version": "1.18.20-gke.900",
                "instanceGroupUrls": [
                    "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/europe-central2-a/instanceGroupManagers/gke-cluster-example-example-pool-ID-grp"
                ],
                "status": "RUNNING",
                "upgradeSettings": {
                    "maxSurge": 1
                }
            }
        ]
    }
    

##### Output messages

The **List Node Pools** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully found node pools for cluster CLUSTER_NAME for the provided criteria in GKE.` `No node pools were found for cluster CLUSTER_NAME for the provided criteria in GKE.` | The action succeeded.  
`Provided cluster location CLUSTER_LOCATION does not exist.` `Provided cluster name CLUSTER_NAME was not found.` `Invalid value was provided for "Max Records to Return": MAX_RECORDS_TO_RETURN. Positive number should be provided.` `Error executing action "List Node Pools". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **List Node Pools** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List Operations

Use the **List Operations** action to list GKE operations for a location based on the specified search criteria.

The filtering logic works with the `operation name` field.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **List Operations** action requires the following parameters:

Parameter | Description  
---|---  
`Cluster Location` | Required.The location to search for operations, such as `europe-central2-a`.  
`Filter Logic` | Optional.The filter logic to apply.The filtering logic works with the `cluster name` field.The possible values are as follows:

  * `Equal`
  * `Contains`

The default value is `Equal`.  
`Filter Value` | Optional.The value to use for the filter.The filtering logic works with the `cluster name` field.If you set the `Filter Logic` parameter to `Equal`, the action searches for the `Filter Value` exact match among results. If you set the `Filter Logic` parameter to `Contains`, the action searches for results that contain the substring that you specify in this parameter. If you don't set a value, the action ignores the filter.  
`Max Records To Return` | Optional.The number of records to return. The default value is `50`.  
  
#### Action outputs

The **List Operations** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **List Operations** action can return the following table:

Table name: **Found Operations**

Table columns:

  * **Name**
  * **Zone**
  * **Operation Type**
  * **Status**
  * **Start Time**
  * **End Time**
  * **Target Link**
  * **Self Link**



##### JSON result

The following example shows the JSON result output received when using the **List Operations** action:
    
    
    {
        "operations": [
            {
                "name": "operation-OPERATION_ID",
                "zone": "europe-central2-a",
                "operationType": "UPGRADE_MASTER",
                "status": "DONE",
                "selfLink": "https://container.googleapis.com/v1/projects/PROJECT_ID/zones/europe-central2-a/operations/operation-OPERATION_ID",
                "targetLink": "https://container.googleapis.com/v1/projects/PROJECT_ID/zones/europe-central2-a/clusters/cluster-example",
                "startTime": "2021-08-06T12:33:51.614562051Z",
                "endTime": "2021-08-06T12:38:55.038159801Z"
            },
        ]
    }
    

##### Output messages

The **List Operations** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully found operations for the provided criteria in GKE.` `No operations were found for the provided criteria in GKE.` | The action succeeded.  
`Provided cluster location CLUSTER_LOCATION does not exist.` `Error executing action "List Operations". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **List Operations** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test the connectivity to GKE.

This action doesn't run on Google SecOps entities. 

#### Action inputs

None.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the GKE service with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the GKE service! Error is ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Set Cluster Addons

Use the **Set Cluster Addons** action to set add-ons for the GKE cluster.

If the target cluster is already undergoing a configuration change, it cannot accept new configuration changes until the current configuration change is complete.

This action runs asynchronous. Adjust the Google SecOps IDE settings as needed.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Set Cluster Addons** action requires the following parameters:

Parameter | Description  
---|---  
`Cluster Location` | Required.A location to search for clusters, such as `europe-central2-a`.  
`Cluster Name` | Required.The name of the cluster to search for.  
`HTTP Load Balancing` | Optional.The value for the HTTP load balancing add-on. The possible values are as follows:

  * `Not Changed`
  * `Disabled`
  * `Enabled`

The default value is `Not Changed`.  
`Horizontal Pod Autoscaling` | Optional.The value for the horizontal Pod autoscaling add-on.The possible values are as follows:

  * `Not Changed`
  * `Disabled`
  * `Enabled`

The default value is `Not Changed`.  
`Network Policy Config` | Optional.The value for the network policy configuration add-on.The possible values are as follows:

  * `Not Changed`
  * `Disabled`
  * `Enabled`

The default value is `Not Changed`.  
`Cloud Run Config` | Optional.The value for the Cloud Run configuration add-on.The possible values are as follows:

  * `Not Changed`
  * `Disabled`
  * `Enabled, Load Balancer Type Unspecified`
  * `Enabled, Load Balancer Type External`
  * `Enabled, Load Balancer Type Internal`

The default value is `Not Changed`.  
`DNS Cache Config` | Optional.The value for the DNS cache configuration add-on. The possible values are as follows:

  * `Not Changed`
  * `Disabled`
  * `Enabled`

The default value is `Not Changed`.  
`Config Connector Config` | Optional.The value for the Config Connector configuration add-on.The possible values are as follows:

  * `Not Changed`
  * `Disabled`
  * `Enabled`

The default value is `Not Changed`.  
`Persistent Disk Csi Driver Config` | Optional.Specify the value for the Compute Engine persistent disk Container Storage Interface (CSI) Driver configuration add-on. The possible values are as follows:

  * `Not Changed`
  * `Disabled`
  * `Enabled`

The default value is `Not Changed`.  
`Wait for cluster configuration change operation to finish` | Optional.If selected, the action waits for the results of the cluster configuration change operation.Selected by default.  
  
#### Action outputs

The **Set Cluster Addons** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Set Cluster Addons** action:
    
    
    {
       "name": "operation-OPERATION_ID",
       "zone": "europe-central2-a",
       "operationType": "UPDATE_CLUSTER",
       "status": "RUNNING",
       "selfLink": "https://container.googleapis.com/v1/projects/PROJECT_ID/zones/europe-central2-a/operations/operation-OPERATION_ID",
       "targetLink": "https://container.googleapis.com/v1/projects/PROJECT_ID/zones/europe-central2-a/clusters/cluster-test",
       "startTime": "2021-08-15T11:34:43.051036236Z"
    }
    

##### Output messages

The **Set Cluster Addons** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully created cluster configuration change operation.` `Failed to execute the action because API returned error, please see action logs LOG_SNIPPET.` `Operation  OPERATION_NAME is still in progress, current status: STATUS.` `Operation OPERATION_NAME successfully finished.` `Operation OPERATION_NAME failed to complete with the following status: STATUS.` | The action succeeded.  
`Provided cluster location CLUSTER_LOCATION does not exist.` `Provided cluster name CLUSTER_NAME was not found.` `Error executing action "Set Cluster Addons". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Set Cluster Addons** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Set Cluster Labels

Use the **Set Cluster Labels** action to set labels for the GKE cluster. The action appends new labels to any existing cluster labels.

If the target cluster is already undergoing a configuration change, it cannot accept new configuration changes until the current configuration change is complete.

This action runs asynchronous. Adjust the Google SecOps IDE settings as needed.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Set Cluster Labels** action requires the following parameters:

Parameter | Description  
---|---  
`Cluster Location` | Required.A location to search for clusters, such as `europe-central2-a`.  
`Cluster Name` | Required.The name of the cluster to search for.  
`Cluster Labels` | Required.A JSON object that contains labels to add to the cluster. The action appends new labels to any existing cluster labels. The default value is as follows:
    
    
    {
          "key1":"value1",
          "key2":"value2"
          }
          
  
`Wait for cluster configuration change operation to finish` | Optional.If selected, the action waits for the results of the cluster configuration change operation.Not selected by default.  
  
#### Action outputs

The **Set Cluster Labels** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Set Cluster Labels** action:
    
    
    {
        "name": "operation-OPERATION_ID",
        "zone": "europe-central2-a",
        "operationType": "UPDATE_CLUSTER",
        "status": "RUNNING",
        "selfLink": "https://container.googleapis.com/v1/projects/PROJECT_ID/zones/europe-central2-a/operations/operation-OPERATION_ID",
        "targetLink": "https://container.googleapis.com/v1/projects/PROJECT_ID/zones/europe-central2-a/clusters/cluster-test",
        "startTime": "2021-08-15T11:53:55.904254615Z"
    }
    

##### Output messages

The **Set Cluster Labels** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully created cluster configuration change operation.` `Operation OPERATION_NAME is still in progress, current status: STATUS.` `Operation OPERATION_NAME successfully finished.` `Operation OPERATION_NAME failed to complete with the following status: STATUS.` `Operation OPERATION_NAME failed to complete with the following status: STATUS.` | The action succeeded.  
`Provided cluster location CLUSTER_LOCATION does not exist.` `Invalid value was provided for the cluster labels: CLUSTER_LABELS.` `Error executing action "Set Cluster Labels". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Set Cluster Labels** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Set Node Autoscaling

Use the **Set Node Autoscaling** action to set the node pool auto scaling configuration for the GKE cluster. The action is asynchronous.

If the target cluster is already undergoing a configuration change, it cannot accept new configuration changes until the current configuration change is complete.

This action runs asynchronous. Adjust the Google SecOps IDE settings as needed.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Set Node Autoscaling** action requires the following parameters:

Parameter | Description  
---|---  
`Cluster Location` | Required.A location to search for clusters, such as `europe-central2-a`.  
`Cluster Name` | Required.The name of the cluster to search for.  
`Node Pool Name` | Required.The node pool name for the cluster.  
`Autoscaling Mode` | Optional.The auto scaling mode status for the node pool. The possible values are as follows:

  * `Not Changed`
  * `Enabled`
  * `Disabled`

The default value is `Not Changed`.  
`Minimum Node Count` | Optional.The minimum number of nodes for the node pool configuration.  
`Maximum Node Count` | Optional.The maximum number of nodes for the node pool configuration.  
`Wait for cluster configuration change operation to finish` | Optional.If selected, the action waits for the results of the cluster configuration change operation.Not selected by default.  
  
#### Action outputs

The **Set Node Autoscaling** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Set Node Autoscaling** action:
    
    
    {
        "name": "operation-OPERATION_ID",
        "zone": "europe-central2-a",
        "operationType": "UPDATE_CLUSTER",
        "status": "RUNNING",
        "selfLink": "https://container.googleapis.com/v1/projects/PROJECT_ID/zones/europe-central2-a/operations/operation-OPERATION_ID",
        "targetLink": "https://container.googleapis.com/v1/projects/PROJECT_ID/zones/europe-central2-a/clusters/cluster-test",
        "startTime": "2021-08-15T11:53:55.904254615Z"
    }
    

##### Output messages

The **Set Node Autoscaling** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully created cluster node pool configuration change operation.` `Failed to execute the action because API returned error, please see action logs LOG_SNIPPET.` `Operation  OPERATION_NAME is still in progress, current status: STATUS.` `Operation OPERATION_NAME successfully finished.` `Operation OPERATION_NAME failed to complete with the following status: STATUS.` | The action succeeded.  
`Provided cluster location CLUSTER_LOCATION does not exist.` `Provided cluster name CLUSTER_NAME was not found.` `Error executing action "Set Node Autoscaling". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Set Node Autoscaling** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Set Node Pool Management

Use the **Set Node Pool Management** action to set the node pool management configuration for the GKE cluster.

This action runs asynchronous. Adjust the Google SecOps IDE settings as needed.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Set Node Pool Management** action requires the following parameters:

Parameter | Description  
---|---  
`Cluster Location` | Required.A location to search for clusters, such as `europe-central2-a`.  
`Cluster Name` | Required.The name of the cluster to search for.  
`Node Pool Name` | Required.The node pool name for the GKE cluster.  
`Auto Upgrade` | Optional.The status of the auto upgrade management feature.  
`Auto Repair` | Optional.The status of auto repair management feature.  
`Wait for cluster configuration change operation to finish` | Optional.If selected, the action waits for the results of the cluster configuration change operation.Not selected by default.  
  
#### Action outputs

The **Set Node Pool Management** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Set Node Pool Management** action:
    
    
    {
        "name": "operation-OPERATION_ID",
        "zone": "europe-central2-a",
        "operationType": "SET_NODE_POOL_MANAGEMENT",
        "status": "RUNNING",
        "selfLink": "https://container.googleapis.com/v1/projects/PROJECT_ID/zones/europe-central2-a/operations/operation-OPERATION_ID",
        "targetLink": "https://container.googleapis.com/v1/projects/PROJECT_ID/zones/europe-central2-a/clusters/cluster-test/nodePools/default-pool",
        "startTime": "2021-08-15T11:53:55.904254615Z"
    }
    

##### Output messages

The **Set Node Pool Management** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully created cluster node pool configuration change operation.` `Failed to execute the action because API returned error, please see action logs LOG_SNIPPET.` `Operation  OPERATION_NAME is still in progress, current status: STATUS.` `Operation OPERATION_NAME successfully finished.` `Operation OPERATION_NAME failed to complete with the following status: STATUS.` | The action succeeded.  
`Provided cluster location CLUSTER_LOCATION does not exist.` `Provided cluster name CLUSTER_NAME was not found.` `Provided node pool name NODE_POOL_NAME was not found.` `Error executing action "Set Node Pool Management". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Set Node Pool Management** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Set Node Count

Use the **Set Node Count** action to set the node count for the GKE cluster node pool.

This action runs asynchronous. Adjust the Google SecOps IDE settings as needed.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Set Node Count** action requires the following parameters:

Parameter | Description  
---|---  
`Cluster Location` | Required.A location to search for clusters, such as `europe-central2-a`.  
`Cluster Name` | Required.The name of the cluster to search for.  
`Node Pool Name` | Required.The node pool name for the GKE cluster.  
`Node Count` | Required.The number of nodes for the GKE cluster node pool.  
`Wait for cluster configuration change operation to finish` | Optional.If selected, the action waits for the results of the cluster configuration change operation.Not selected by default.  
  
#### Action outputs

The **Set Node Count** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Set Node Count** action:
    
    
    {
        "name": "operation-OPERATION_ID",
        "zone": "europe-central2-a",
        "operationType": "SET_NODE_POOL_SIZE",
        "status": "RUNNING",
        "selfLink": "https://container.googleapis.com/v1/projects/PROJECT_ID/zones/europe-central2-a/operations/operation-OPERATION_ID",
        "targetLink": "https://container.googleapis.com/v1/projects/PROJECT_ID/zones/europe-central2-a/clusters/cluster-test/nodePools/default-pool",
        "startTime": "2021-08-15T11:53:55.904254615Z"
    }
    

##### Output messages

The **Set Node Count** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully created cluster node pool configuration change operation.` `Failed to execute the action because API returned error, please see action logs LOG_SNIPPET.` `Operation  OPERATION_NAME is still in progress, current status: STATUS.` `Operation OPERATION_NAME successfully finished.` `Operation OPERATION_NAME failed to complete with the following status: STATUS.` | The action succeeded.  
`Provided cluster location CLUSTER_LOCATION does not exist.` `Provided cluster name CLUSTER_NAME was not found.` `Provided node pool name NODE_POOL_NAME was not found.` `Invalid value was provided for the node count: NODE_COUNT. The value should be a positive number.` `Error executing action "Set Node Count". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Set Node Count** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
