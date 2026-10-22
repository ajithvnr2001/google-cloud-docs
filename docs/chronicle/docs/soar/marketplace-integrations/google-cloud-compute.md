---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-cloud-compute/
title: Integrate Compute Engine with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:16.725118+00:00
---

# Integrate Compute Engine with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-cloud-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Compute Engine with Google SecOps

This document explains how to integrate Compute Engine with Google Security Operations.

**Important:** In the Google SecOps platform, the integration for Compute Engine is called _Google Cloud Compute_.

## Use cases

The Compute Engine integration uses Google SecOps capabilities to support the following use cases:

  * **Automated incident response** : Automatically isolate a compromised Compute Engine instance from the network. Automated containment limits the attack's spread, accelerates response time, and reduces security team workload. 

  * **Threat hunting and investigation** : Automate the collection of logs and security telemetry from Compute Engine instances across multiple projects. Analyzing this consolidated data enables proactive threat hunting and speeds up investigations by automating data collection.

  * **Vulnerability management** : Integrate vulnerability scanning tools with Google SecOps to automatically scan Compute Engine instances for known vulnerabilities. Generate remediation tickets or patch vulnerabilities directly to reduce exploitation risk and improve security posture.

  * **Compliance automation** : Automate the collection of audit logs and configuration data from Compute Engine instances to comply with regulatory requirements. Generate reports and dashboards for auditors to simplify compliance reporting and reduce manual effort.

  * **Security orchestration** : Orchestrate security workflows across multiple Google Cloud services, including Compute Engine. For example, trigger the creation of a new firewall rule in response to a security event detected on an instance, leading to a more coordinated and automated security posture.




### Before you begin

Before you configure the **Compute Engine** integration in Google SecOps, complete the following prerequisite steps:

  1. Create and configure a custom Identity and Access Management role.

  2. Create a service account.

  3. Choose and configure one of the following authentication methods:

     * **Option 1:Workload Identity (recommended)**: This method uses short-lived, temporary access tokens using service account impersonation.

     * **Option 2:Service account JSON key**: This method relies on a static, long-lived secret key file.




### Create a custom IAM role

To provide the integration with the specific permissions required to manage your instances, create a custom role:

  1. In the Google Cloud console, go to **IAM & Admin > Roles**.

[Go to Roles](https://console.cloud.google.com/iam-admin/roles)

  2. Click **add Create custom role**.

  3. Provide a **Title** (for example, `SecOps Compute Engine Integration`), **Description** , and a unique **ID**.

  4. Set the **Role Launch Stage** to **General Availability**.

  5. Click **Add Permissions** and add the following:

     * `compute.instances.list`
     * `compute.instances.start`
     * `compute.instances.stop`
     * `compute.instances.delete`
     * `compute.instances.setLabels`
     * `compute.instances.getIamPolicy`
     * `compute.instances.setIamPolicy`
     * `compute.instances.get`
     * `compute.zones.list`
  6. Click **Create**.




### Create a service account

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click **add Create Service Account**.

  3. Enter a name and description, and click **Create and Continue**.

  4. In the **Grant this service account access to project** step, assign the custom role you created.

  5. Click **Done**. Note the service account's **Email address**.




### Configure Workload Identity credentials

Workload Identity is the recommended approach because it uses short-lived access tokens that use service account impersonation.

#### Identify the unique instance identity

Establishing a connection requires granting your Google SecOps instance permission to impersonate your service account.

  1. In Google SecOps, go to **Content Hub > Response Integrations**.

  2. Select the **Compute Engine** integration and enter your service account email in `Workload Identity Email`.

  3. Click **Save > Test**. The test is expected to fail. 

  4. Click the close_small button next to **Test** and locate the identity email beginning with `gke-init-python@...` or `soar-python@...`.

  5. Copy this unique email address.




#### Authorize the instance identity in Google Cloud

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select the target service account and go to **Permissions > Grant Access**.

  3. Paste the unique email address into the **New principals** field and assign the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`).




### Configure a JSON key

Static, long-lived secret key files require manual rotation. Use this method only if Workload Identity authentication isn't available.

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts** and select your service account.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Go to the **Keys** tab and click **Add key > Create new key**.

  3. Select **JSON** and click **Create**. The file automatically downloads to your computer.




#### Configure manual individual parameters

If you choose to enter credentials manually, keep the downloaded JSON key file open in a text editor to copy the individual values required in the integration settings.

## Integration parameters

To establish a connection between Google SecOps and Compute Engine, you must configure the following parameters. The integration supports three distinct authentication paths. Choose one of the following methods to provide credentials:

  * **Workload Identity** : Uses `Workload Identity Email`.
  * **Service account JSON file** : Uses `Service Account Json File Content` to provide the entire key at once.
  * **Manual individual parameters** : Uses separate fields manually copied from a JSON key.

Parameter | Description  
---|---  
`API Root` | Optional. The base URL for the Compute Engine API. The default value is `https://compute.googleapis.com`.  
`OS Config API Root` | Optional. The base URL for the Cloud OS Config API. The default value is `https://osconfig.googleapis.com`.  
`Workload Identity Email` | Optional. The client email address of your service account. Use this for Workload Identity authentication.  
`Service Account Json File Content` | Optional. The full content of the service account key JSON file. If configured, the integration ignores individual credential parameters.  
`Project ID` | Optional. The ID of the Google Cloud project to target. If no value is provided, the integration retrieves the ID from the service account credentials.  
`Verify SSL` | Required. Validates the SSL certificate for the connection. Enabled by default.  
  
### Individual credential parameters

Only use the following parameters if you're manually entering credentials rather than using the full JSON file content or a Workload Identity.

Parameter | Description  
---|---  
`Account Type` | Optional.The value found in the `type` field of your JSON key (typically `service_account`).  
`Private Key ID` | Optional.The value found in the `private_key_id` field of your JSON key.  
`Private Key` | Optional.The value found in the `private_key` field of your JSON key.  
`Client Email` | Optional.The value found in the `client_email` field of your JSON key.  
`Client ID` | Optional.The value found in the `client_id` field of your JSON key.  
`Auth URI` | Optional.The value found in the `auth_uri` field of your JSON key. The default value is `https://accounts.google.com/o/oauth2/auth`.  
`Token URI` | Optional.The value found in the `token_uri` field of your JSON key. The default is `https://oauth2.googleapis.com/token`.  
`Auth Provider X509 URL` | Optional.The value found in the `auth_provider_x509_cert_url` field of your JSON key.  
`Client X509 URL` | Optional.The value found in the `client_x509_cert_url` field of your JSON key.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Add IP To Firewall Rule

Use the **Add IP Range to Firewall Rule** action to append an IP range to an existing firewall rule within a Compute Engine instance.

This action doesn't run on Google SecOps entities. 

**Note:** This action runs asynchronously. Adjust the script timeout value in the Google SecOps IDE as needed to ensure the action has sufficient time to complete the request.

#### Action inputs

The **Add IP To Firewall Rule** action requires the following parameters:

Parameter | Description  
---|---  
`Resource Name` | Optional. The full resource name of the Compute Engine instance, in the format `/projects/PROJECT_ID/global/ firewallsFIREWALL`. This parameter takes priority over `Project ID` and `Firewall Rule`.  
`Project ID` | Optional. The project name associated with the Compute Engine instance. If no value is provided, the action uses the project ID from the integration configuration.  
`Firewall Rule` | Optional. The name of the specific firewall rule to update.  
`Type` | Required. The direction of the traffic for the IP range being added. The possible values are as follows:

  * `Source`
  * `Destination`

The default value is `Source`.  
`IP Ranges` | Required. A comma-separated list of IP address ranges (CIDR notation) to add to the firewall rule.  
  
#### Action outputs

The **Add IP To Firewall Rule** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Add IP To Firewall Rule** action:
    
    
    {
      "kind": "compute#operation",
      "id": "0000000000000000000",
      "name": "operation-1716223324528-618e5619d1f93-174eac81-6b38200d",
      "operationType": "patch",
      "targetLink": "https://www.googleapis.com/compute/v1/projects/project-id/global/firewalls/firewall-name",
      "targetId": "7886634413370691799",
      "status": "DONE",
      "user": "compute-admin@project-id.iam.gserviceaccount.com",
      "progress": 100,
      "insertTime": "2024-05-20T09:42:05.150-07:00",
      "startTime": "2024-05-20T09:42:05.164-07:00",
      "endTime": "2024-05-20T09:42:09.381-07:00",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/project-id/global/operations/operation-1234567890",
      "firewall": {
        "kind": "compute#firewall",
        "id": "6297155974506248217",
        "creationTimestamp": "2023-09-13T07:28:06.690-07:00",
        "name": "firewall-name",
        "description": "",
        "network": "https://www.googleapis.com/compute/v1/projects/project-id/global/networks/vpc-network",
        "priority": 1000,
        "sourceRanges": [
          "0.0.0.0/0"
        ],
        "destinationRanges": [
          "0.0.0.0/21"
        ],
        "allowed": [
          {
            "IPProtocol": "tcp",
            "ports": [
              "22"
            ]
          }
        ],
        "direction": "INGRESS",
        "logConfig": {
          "enable": false
        },
        "disabled": false,
        "selfLink": "https://www.googleapis.com/compute/v1/projects/project-id/global/firewalls/firewall-name"
      }
    }
    

##### Output messages

The **Add IP To Firewall Rule** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully updated firewall rule in Google Cloud Compute.` `Waiting for the operation to finish execution on the RESOURCE_PATH instance in Google Cloud Compute.` | The action succeeded.  
`Error executing action "Add IP To Firewall Rule". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add IP To Firewall Rule** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Add Labels to Instance

Use the **Add Labels to Instance** action to add or update labels on a specific Compute Engine instance.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Add Labels to Instance** action requires the following parameters:

Parameter | Description  
---|---  
`Resource Name` | Optional. The full resource name of the Compute Engine instance, in the format `/project/PROJECT_ID/zone/ ZONE_ID/instances/ INSTANCE_ID`. This parameter takes priority over `Project ID`, `Instance Zone`, and `Instance ID`.  
`Project ID` | Optional. The ID of the project associated with the Compute Engine instance. If no value is provided, the action retrieves the project ID from the integration configuration.  
`Instance Zone` | Optional. The specific zone where the instance is located. This parameter is required if you're identifying the instance using `Instance Zone` and `Instance ID`.  
`Instance ID` | Optional. The unique ID of the Compute Engine instance. This parameter is required if you're identifying the instance using `Instance Zone` and `Instance ID`.  
`Instance Labels` | Required. A comma-separated list of labels to apply to the instance, in the `key:value` format (such as `vm_label_key:label1`).  
  
#### Action outputs

The **Add Labels to Instance** action provides the following outputs:

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

The following example describes the JSON result output received when using the **Add Labels to Instance** action:
    
    
    {
       "id": "ID",
       "name": "operation-OPERATION_ID",
       "zone": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-a",
       "operationType": "setLabels",
       "targetLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-a/instances/INSTANCE_ID",
       "targetId": "INSTANCE_ID",
       "status": "RUNNING",
       "user": "user@example.com",
       "progress": 0,
       "insertTime": "2021-04-28T23:01:29.395-07:00",
       "startTime": "2021-04-28T23:01:29.397-07:00",
       "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-a/operations/operation-OPERATION_ID",
       "kind": "compute#operation"
    }
    

##### Output messages

The **Add Labels to Instance** action can return the following output messages:

Output message | Message description  
---|---  
`Labels LABEL_LIST were successfully added to Compute Engine instance INSTANCE_ID.` `Provided instance zone ZONE_ID is not valid.` `Provided instance ID is not valid.` ` Labels were not added because provided label LABEL_ID has the key that already exist for the Compute Engine instance INSTANCE_ID.` | The action succeeded.  
`Error executing action "Add Labels to Instance". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add Labels to Instance** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Add Network Tags

Use the **Add Network Tags** action to append one or more network tags to a specific Compute Engine instance.

This action doesn't run on Google SecOps entities. 

**Note:** This action runs asynchronously. Adjust the script timeout value in the Google SecOps IDE as needed to ensure the action has sufficient time to complete the request.

#### Action inputs

The **Add Network Tags** action requires the following parameters:

Parameter | Description  
---|---  
`Resource Name` | Optional. The full resource name of the Compute Engine instance, in the format `/project/PROJECT_ID/zone/ ZONE_ID/instances/ INSTANCE_ID`. This parameter takes priority over `Project ID`, `Instance Zone`, and `Instance ID`.  
`Project ID` | Optional. The ID of the project associated with the Compute Engine instance. If no value is provided, the action retrieves the project ID from the integration configuration.  
`Instance Zone` | Optional. The specific zone where the instance is located. This parameter is required if you're identifying the instance using `Instance Zone` and `Instance ID`.  
`Instance ID` | Optional. The unique ID of the Compute Engine instance. This parameter is required if you're identifying the instance using `Instance Zone` and `Instance ID`.  
`Network Tags` | Required. A comma-separated list of network tags to add to the instance. All tags must only contain lowercase letters, numbers, and hyphens.  
  
#### Action outputs

The **Add Network Tags** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Add Network Tags** action:
    
    
    {
      "kind": "compute#instance",
      "id": "1459671903146615834",
      "creationTimestamp": "2023-09-13T04:20:21.993-07:00",
      "name": "instance-2",
      "description": "",
      "tags": {
        "items": [
          "another-tag",
          "tag"
        ],
        "fingerprint": "BCeEINC7Ths="
      },
      "machineType": "https://www.googleapis.com/compute/v1/projects/project-id/zones/us-central1-a/machineTypes/e2-micro",
      "status": "RUNNING",
      "zone": "https://www.googleapis.com/compute/v1/projects/project-id/zones/us-central1-a",
      "canIpForward": false,
      "networkInterfaces": [
        {
          "kind": "compute#networkInterface",
          "network": "https://www.googleapis.com/compute/v1/projects/project-id/global/networks/default",
          "subnetwork": "https://www.googleapis.com/compute/v1/projects/project-id/regions/us-central1/subnetworks/default",
          "networkIP": "10.128.0.3",
          "name": "nic0",
          "fingerprint": "-ZnnV7hiDfs=",
          "stackType": "IPV4_ONLY"
        }
      ],
      "disks": [
        {
          "kind": "compute#attachedDisk",
          "type": "PERSISTENT",
          "mode": "READ_WRITE",
          "source": "https://www.googleapis.com/compute/v1/projects/project-id/zones/us-central1-a/disks/instance-2",
          "deviceName": "instance-2",
          "index": 0,
          "boot": true,
          "autoDelete": true,
          "licenses": [
            "https://www.googleapis.com/compute/v1/projects/centos-cloud/global/licenses/centos-7"
          ],
          "interface": "SCSI",
          "guestOsFeatures": [
            { "type": "UEFI_COMPATIBLE" },
            { "type": "GVNIC" }
          ],
          "diskSizeGb": "20",
          "architecture": "X86_64"
        }
      ],
      "metadata": {
        "kind": "compute#metadata",
        "fingerprint": "NBmH4-7Jw9U=",
        "items": []
      },
      "serviceAccounts": [
        {
          "email": "1111111111-compute@developer.gserviceaccount.com",
          "scopes": [
            "https://www.googleapis.com/auth/devstorage.read_only",
            "https://www.googleapis.com/auth/logging.write",
            "https://www.googleapis.com/auth/monitoring.write",
            "https://www.googleapis.com/auth/servicecontrol",
            "https://www.googleapis.com/auth/service.management.readonly",
            "https://www.googleapis.com/auth/trace.append"
          ]
        }
      ],
      "selfLink": "https://www.googleapis.com/compute/v1/projects/project-id/zones/us-central1-a/instances/instance-2",
      "scheduling": {
        "onHostMaintenance": "MIGRATE",
        "automaticRestart": true,
        "preemptible": false,
        "provisioningModel": "STANDARD"
      },
      "cpuPlatform": "Intel Broadwell",
      "deletionProtection": false,
      "shieldedInstanceConfig": {
        "enableSecureBoot": false,
        "enableVtpm": true,
        "enableIntegrityMonitoring": true
      }
    }
    

##### Output messages

The **Add Network Tags** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added network tags to the instance RESOURCE_PATH in Compute Engine.` `Waiting for the operation to finish execution on the RESOURCE_PATH instance in Compute Engine.` | The action succeeded.  
`Error executing action "Add Network Tags". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add Network Tags** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Delete Instance

Use the **Delete Instance** action to delete Compute Engine instances.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Delete Instance** action requires the following parameters:

Parameter | Description  
---|---  
`Resource Name` | Optional. The full resource name of the Compute Engine instance, in the format `/project/PROJECT_ID/zone/ ZONE_ID/instances/ INSTANCE_ID`. This parameter takes priority over `Project ID`, `Instance Zone`, and `Instance ID`.  
`Project ID` | Optional. The ID of the project associated with the Compute Engine instance. If no value is provided, the action retrieves the project ID from the integration configuration.  
`Instance Zone` | Optional. The specific zone where the instance is located. This parameter is required if you're identifying the instance using `Instance Zone` and `Instance ID`.  
`Instance ID` | Optional. The unique ID of the instance you want to start. You can retrieve this value using the List Instances action. This parameter is required if you're identifying the instance using `Instance Zone` and `Instance ID`.  
  
#### Action outputs

The **Delete Instance** action provides the following outputs:

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

The following example describes the JSON result output received when using the **Delete Instance** action:
    
    
    {
       "id": "ID",
       "name": "operation-OPERATION_ID",
       "zone": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-a",
       "operationType": "delete",
       "targetLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-a/instances/INSTANCE_ID",
       "targetId": "INSTANCE_ID",
       "status": "RUNNING",
       "user": "user@example.com",
       "progress": 0,
       "insertTime": "2021-04-28T23:01:29.395-07:00",
       "startTime": "2021-04-28T23:01:29.397-07:00",
       "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-a/operations/operation-OPERATION_ID",
       "kind": "compute#operation"
    }
    

##### Output messages

The **Delete Instance** action can return the following output messages:

Output message | Message description  
---|---  
`Compute Engine instance INSTANCE_ID was deleted successfully.` `Provided instance zone ZONE_ID is not valid.` `Provided instance ID is not valid.` | The action succeeded.  
`Error executing action "Start Instance". Reason: ERROR_REASON` `Provided resource RESOURCE_PATH is not valid` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Delete Instance** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Enrich Entities

Use the **Enrich Entities** action to enrich Google SecOps `IP Address` entities with the instance information from Compute Engine.

This action runs on the following Google SecOps entities:

  * `IP Address`



#### Action inputs

The **Enrich Entities** action requires the following parameters:

Parameters | Description  
---|---  
`Project ID` | Optional. The ID of the project associated with the Compute Engine instance. If no value is provided, the action retrieves the project ID from the integration configuration.  
`Instance Zone` | Optional. The specific zone where the instance is located.  
  
#### Action outputs

The **Enrich Entities** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

After completing execution, the **Enrich Entities** action provides the following table:

Table name: **ENTITY Enrichment Table**

Columns:

  * **Entity Field**
  * **Value**



##### Enrichment table

The **Enrich Entities** action supports the following entity enrichment:

Enrichment field | Source (JSON key) | Logic  
---|---|---  
`Google_Compute_instance_id` | `id` | Not available  
`Google_Compute_creation_timestamp` | `creationTimestamp` | Not available  
`Google_Compute_instance_name` | `name` | Not available  
`Google_Compute_description` | `description` | Not available  
`Google_Compute_tags` | `tags` | Provide the tags in a CSV list  
`Google_Compute_machine_type` | `machineType` | Not available  
`Google_Compute_instance_status` | `status` | Not available  
`Google_Compute_instance_zone` | `zone` | Not available  
`Google_Compute_can_ip_forward` | `canIpForward` | Not available  
`Google_Compute_instance_network_interfaces_name_INDEX` | `networkInterfaces.name` | Expand if there are more network interfaces available  
`Google_Compute_instance_network_interfaces_name_access_configs_type_INDEX` | `networkInterfaces.accessConfigs.type` | Expand if there are more network interfaces available  
`Google_Compute_instance_network_interfaces_name_access_configs_name_INDEX` | `networkInterfaces.accessConfigs.name` | Expand if there are more network interfaces available  
`Google_Compute_instance_network_interfaces_name_access_configs_natIP_INDEX` | `networkInterfaces.accessConfigs.natIP` | Expand if there are more network interfaces available  
`Google_Compute_instance_metadata` | `metadata` | CSV list of values from instance metadata  
`Google_Compute_service_account_INDEX ` | `serviceAccounts.email` | Expand if there are more service accounts available  
`Google_Compute_service_account_scopes_INDEX ` | `serviceAccounts.scopes` | Expand if there are more service accounts available  
`Google_Compute_link_to_Google_Compute` | `selfLink` | Not available  
`Google_Compute_labels` | `labels` | Provide a CSV list of values  
`Google_Compute_instance_last_start_timestamp` | `lastStartTimestamp` | Not available  
`Google_Compute_instance_last_stop_timestamp` | `lastStopTimestamp` | Not available  
  
##### JSON result

The following example describes the JSON result output received when using the **Enrich Entities** action:
    
    
    {
        "id": "ID",
        "creationTimestamp": "2021-04-28T21:34:57.369-07:00",
        "name": "instance-1",
        "description": "",
        "tags": {
            "fingerprint": "VALUE"
        },
        "machineType": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-a/machineTypes/f1-micro",
        "status": "RUNNING",
        "zone": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-a",
        "canIpForward": false,
        "networkInterfaces": [
            {
                "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/default",
                "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/subnetworks/default",
                "networkIP": "203.0.113.2",
                "name": "example",
                "accessConfigs": [
                    {
                        "type": "ONE_TO_ONE_NAT",
                        "name": "External NAT",
                        "natIP": "198.51.100.59",
                        "networkTier": "PREMIUM",
                        "kind": "compute#accessConfig"
                    }
                ],
                "fingerprint": "VALUE",
                "kind": "compute#networkInterface"
            }
        ],
        "disks": [
            {
                "type": "PERSISTENT",
                "mode": "READ_WRITE",
                "source": "https://www.googleapis.com/compute/v1/PROJECT_ID/zones/us-central1-a/disks/instance-1",
                "deviceName": "instance-1",
                "index": 0,
                "boot": true,
                "autoDelete": true,
                "licenses": [
                    "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/licenses/LICENSE"
                ],
                "interface": "SCSI",
                "guestOsFeatures": [
                    {
                        "type": "UEFI_COMPATIBLE"
                    },
                    {
                        "type": "VIRTIO_SCSI_MULTIQUEUE"
                    }
                ],
                "diskSizeGb": "10",
                "kind": "compute#attachedDisk"
            }
        ],
        "metadata": {
            "fingerprint": "VALUE",
            "kind": "compute#metadata"
        },
        "serviceAccounts": [
            {
                "email": "user@example.com",
                "scopes": [
                    "https://www.googleapis.com/auth/devstorage.read_only",
                    "https://www.googleapis.com/auth/logging.write",
                    "https://www.googleapis.com/auth/monitoring.write",
                    "https://www.googleapis.com/auth/servicecontrol",
                    "https://www.googleapis.com/auth/service.management.readonly",
                    "https://www.googleapis.com/auth/trace.append"
                ]
            }
        ],
        "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-a/instances/instance-1",
        "scheduling": {
            "onHostMaintenance": "MIGRATE",
            "automaticRestart": true,
            "preemptible": false
        },
        "cpuPlatform": "Intel Haswell",
        "labels": {
            "vm_test_tag": "tag1"
        },
        "labelFingerprint": "VALUE",
        "startRestricted": false,
        "deletionProtection": false,
        "reservationAffinity": {
            "consumeReservationType": "ANY_RESERVATION"
        },
        "displayDevice": {
            "enableDisplay": false
        },
        "shieldedInstanceConfig": {
            "enableSecureBoot": false,
            "enableVtpm": true,
            "enableIntegrityMonitoring": true
        },
        "shieldedInstanceIntegrityPolicy": {
            "updateAutoLearnPolicy": true
        },
        "confidentialInstanceConfig": {
            "enableConfidentialCompute": false
        },
        "fingerprint": "VALUE",
        "lastStartTimestamp": "2021-04-28T21:35:07.865-07:00",
        "kind": "compute#instance"
    }
    

##### Output messages

The **Enrich Entities** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully enriched entities: ENTITY_ID.` `Provided instance zone ZONE_ID is not valid.` `Action was not able to find a match Compute Engine to enrich provided entities: ENTITY_ID.` `No entities were enriched.` | The action succeeded.  
`Error executing action "Enrich Entities". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Enrich Entities** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Execute VM Patch Job

Use the **Execute VM Patch Job** action to execute a VM patch job on Compute Engine instances.

This action doesn't run on Google SecOps entities. 

**Note:** This action runs asynchronously. Adjust the script timeout value in the Google SecOps IDE as needed to ensure the action has sufficient time to complete the request.**Important:** The **Execute VM Patch Job** action requires you to enable the [OS Config API](https://docs.cloud.google.com/compute/docs/osconfig/rest).

#### Action inputs

The **Execute VM Patch Job** action requires the following parameters:

Parameter | Description  
---|---  
`Instance Filter Object` | Required. The JSON object used to target specific instances for patching. The default value targets all instances:
    
    
    {
      "all": "true"
    }
          
  
`Name` | Required. The unique name for the patching job.  
`Description` | Optional. A brief description of the patching job's purpose.  
`Patching Config Object` | Optional. A JSON object that defines the specific update steps and configurations for different operating systems. If no value is provided, the action uses the following default value:
    
    
    {
      "rebootConfig": "DEFAULT",
      "apt": {
        "type": "DIST"
      },
      "yum": {
        "security": true
      },
      "zypper": {
        "withUpdate": true
      },
      "windowsUpdate": {
        "classifications": ["CRITICAL", "SECURITY"]
      }
    }
          
  
`Patch Duration Timeout` | Required. The maximum time, in minutes, allowed for the patching job to run. The default value is `60`.  
`Rollout Strategy` | Optional. The method used to deploy the patch across multiple zones. The possible values are as follows:

  * `Zone By Zone`: Patches are applied to one zone at a time to minimize risk.
  * `Concurrent Zones`: Patches are applied to all targeted zones simultaneously to reduce the total maintenance window.

The default value is `Zone By Zone`.  
`Disruption Budget` | Required. The number or percentage of instances that can be offline at the same time (for example, `5` or `10%`). The default value is `10%`.  
`Wait For Completion` | Required. If selected, the action remains active until the patching job finishes. Enabled by default.  
`Fail If Completed With Errors` | Required. If selected, the action fails if the job status is `Completed with errors` or if it reaches the timeout limit. This parameter is ignored if `Wait For Completion` is disabled. Enabled by default.  
  
#### Action outputs

The **Execute VM Patch Job** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Execute VM Patch Job** action:
    
    
    {
                "name": "projects/PROJECT_ID/patchJobs/JOB_ID",
                "createTime": "2024-09-24T16:00:43.354907Z",
                "updateTime": "2024-09-24T16:00:44.626050Z",
                "state": "PATCHING",
                "patchConfig": {
                    "rebootConfig": "DEFAULT",
                    "apt": {
                        "type": "UPGRADE"
                    },
                    "yum": {},
                    "zypper": {},
                    "windowsUpdate": {}
                },
                "duration": "3600s",
                "instanceDetailsSummary": {
                    "startedInstanceCount": "1"
                },
                "percentComplete": 20,
                "instanceFilter": {
                    "instances": [
                        "zones/us-central1-a/instances/INSTANCE_ID"
                    ]
                },
                "displayName": "test",
                "rollout": {
                    "mode": "ZONE_BY_ZONE",
                    "disruptionBudget": {
                        "percent": 25
                    }
                }
            }
    

##### Output messages

The **Execute VM Patch Job** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully executed VM patching job in Google Cloud Compute.` `Successfully executed and completed VM patching job in Google Cloud Compute.` `The executed patching job was canceled in Google Cloud Compute.` `The executed patching job was completed, but with errors in Compute Engine. Errors: ERROR_DESCRIPTION` `` | The action succeeded.  
`Error executing action "Execute VM Patch Job". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Execute VM Patch Job** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Instance IAM Policy

Use the **Get Instance IAM Policy** action to retrieve the Identity and Access Management (iam_name_short) access control policy for a specific Compute Engine resource.

This action doesn't run on Google SecOps entities. 

**Note:** If no policy has been explicitly defined for the resource, the action returns an empty policy object.

#### Action inputs

The **Get Instance IAM Policy** action requires the following parameters:

Parameter | Description  
---|---  
`Resource Name` | Optional. The full resource name of the Compute Engine instance, in the format `/project/PROJECT_ID/zone/ ZONE_ID/instances/ INSTANCE_ID`. This parameter takes priority over `Project ID`, `Instance Zone`, and `Instance ID`.  
`Project ID` | Optional. The ID of the project associated with the Compute Engine instance. If no value is provided, the action retrieves the project ID from the integration configuration.  
`Instance Zone` | Optional. The specific zone where the instance is located. This parameter is required if you're identifying the instance using `Instance Zone` and `Instance ID`.  
`Instance ID` | Optional. The unique ID of the instance you want to start. You can retrieve this value using the List Instances action. This parameter is required if you're identifying the instance using `Instance Zone` and `Instance ID`.  
  
#### Action outputs

The **Get Instance IAM Policy** action provides the following outputs:

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

The following example describes the JSON result output received when using the **Get Instance IAM Policy** action:
    
    
    {
        "version": 1,
        "etag": "BwXBfsc47MI=",
        "bindings": [
            {
                "role": "roles/compute.networkViewer_withcond_2f0c00",
                "members": [
                    "user:user@example.com"
                ]
            }
        ]
    }
    

##### Output messages

The **Get Instance IAM Policy** action can return the following output messages:

Output message | Message description  
---|---  
`Compute Engine instance INSTANCE_ID IAM policy was fetched successfully.` `Provided instance zone ZONE_ID is not valid.` `Provided instance ID is not valid.` | The action succeeded.  
`Error executing action "Get Instance IAM Policy". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Instance IAM Policy** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### List Instances

Use the **List Instances** action to list Compute Engine instances based on specified search criteria.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **List Instances** action requires the following parameters:

Parameter | Description  
---|---  
`Project ID` | Optional. The ID of the project from which to list instances. If no value is provided, the action retrieves the project ID from the Google Cloud service account used in the integration configuration.  
`Instance Zone` | Optional. The specific zone to search for instances in. If no value is provided, the action searches across all available zones.  
`Instance Name` | Optional. A name of the instance to search for. This parameter accepts multiple values as a comma-separated string.  
`Instance Status` | Optional. The current state of the instances to include in the search results, such as `RUNNING` or `TERMINATED`. This parameter accepts multiple values as a comma-separated string.  
`Instance Labels` | Optional. The labels used to filter the instance results, provided in `key:value` format (such as `env:production`). This parameter accepts multiple values as a comma-separated string.  
`Max Rows to Return` | Optional. The maximum number of instances to return in the results. The default value is `50`.  
  
#### Action outputs

The **List Instances** action provides the following outputs:

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

The **List Instances** action provides the following table:

Table name: **Compute Engine Instances**

Table columns:

  * **Instance Name**
  * **Instance ID**
  * **Instance Creation Time**
  * **Instance Description**
  * **Instance Type**
  * **Instance Status**
  * **Instance Labels**



##### JSON result

The following example describes the JSON result output received when using the **List Instances** action:
    
    
    { "id": "projects/PROJECT_ID/zones/us-central1-a/instances",
       "items": [
           {
               "id": "ID",
               "creationTimestamp": "2021-04-28T21:34:57.369-07:00",
               "name": "instance-1",
               "description": "",
               "tags": {
                   "fingerprint": "VALUE"
               },
               "machineType": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-a/machineTypes/f1-micro",
               "status": "RUNNING",
               "zone": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-a",
               "canIpForward": false,
               "networkInterfaces": [
                   {
                       "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/default",
                       "subnetwork": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/subnetworks/default",
                       "networkIP": "192.0.2.2",
                       "name": "example",
                       "accessConfigs": [
                           {
                               "type": "ONE_TO_ONE_NAT",
                               "name": "External NAT",
                               "natIP": "203.0.113.59",
                               "networkTier": "PREMIUM",
                               "kind": "compute#accessConfig"
                           }
                       ],
                       "fingerprint": "VALUE",
                       "kind": "compute#networkInterface"
                   }
               ],
               "disks": [
                   {
                       "type": "PERSISTENT",
                       "mode": "READ_WRITE",
                       "source": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-a/disks/instance-1",
                       "deviceName": "instance-1",
                       "index": 0,
                       "boot": true,
                       "autoDelete": true,
                       "licenses": [
                           "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/licenses/LICENSE"
                       ],
                       "interface": "SCSI",
                       "guestOsFeatures": [
                           {
                               "type": "UEFI_COMPATIBLE"
                           },
                           {
                               "type": "VIRTIO_SCSI_MULTIQUEUE"
                           }
                       ],
                       "diskSizeGb": "10",
                       "kind": "compute#attachedDisk"
                   }
               ],
               "metadata": {
                   "fingerprint": "VALUE",
                   "kind": "compute#metadata"
               },
               "serviceAccounts": [
                   {
                       "email": "user@example.com",
                       "scopes": [
                           "https://www.googleapis.com/auth/devstorage.read_only",
                           "https://www.googleapis.com/auth/logging.write",
                           "https://www.googleapis.com/auth/monitoring.write",
                           "https://www.googleapis.com/auth/servicecontrol",
                           "https://www.googleapis.com/auth/service.management.readonly",
                           "https://www.googleapis.com/auth/trace.append"
                       ]
                   }
               ],
               "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_IDzones/us-central1-a/instances/instance-1",
               "scheduling": {
                   "onHostMaintenance": "MIGRATE",
                   "automaticRestart": true,
                   "preemptible": false
               },
               "cpuPlatform": "Intel Haswell",
               "labels": {
                   "vm_test_tag": "tag1"
               },
               "labelFingerprint": "VALUE",
               "startRestricted": false,
               "deletionProtection": false,
               "reservationAffinity": {
                   "consumeReservationType": "ANY_RESERVATION"
               },
               "displayDevice": {
                   "enableDisplay": false
               },
               "shieldedInstanceConfig": {
                   "enableSecureBoot": false,
                   "enableVtpm": true,
                   "enableIntegrityMonitoring": true
               },
               "shieldedInstanceIntegrityPolicy": {
                   "updateAutoLearnPolicy": true
               },
               "confidentialInstanceConfig": {
                   "enableConfidentialCompute": false
               },
               "fingerprint": "VALUE",
               "lastStartTimestamp": "2021-04-28T21:35:07.865-07:00",
               "kind": "compute#instance"
           }
       ]
    }
    

##### Output messages

The **List Instances** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully fetched Compute Engine instances.` `Provided instance zone  ZONE_ID is not valid.` `No instances were found in Compute Engine.` | The action succeeded.  
`Error executing action "List Instances". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **List Instances** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Ping

Use the **Ping** action to test the connectivity to Compute Engine.

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
`Successfully connected to the Compute Engine service with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Compute Engine service! Error is ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Remove External IP Addresses

Use the **Remove External IP Addresses** action to remove external IP addresses on a Compute Engine instance.

This action doesn't run on Google SecOps entities. 

**Note:** This action runs asynchronously. Adjust the script timeout value in the Google SecOps IDE as needed to ensure the action has sufficient time to complete the request.

#### Action inputs

The **Remove External IP Addresses** action requires the following parameters:

Parameters | Description  
---|---  
`Resource Name` | Optional. The full resource name of the Compute Engine instance, in the format `/project/PROJECT_ID/zone/ ZONE_ID/instances/ INSTANCE_ID`. This parameter takes priority over `Project ID`, `Instance Zone`, and `Instance ID`.  
`Project ID` | Optional. The ID of the project associated with the Compute Engine instance. If no value is provided, the action retrieves the project ID from the integration configuration.  
`Instance Zone` | Optional. The specific zone where the instance is located. This parameter is required if you're identifying the instance using `Instance Zone` and `Instance ID`.  
`Instance ID` | Optional. The unique ID of the instance you want to start. You can retrieve this value using the List Instances action. This parameter is required if you're identifying the instance using `Instance Zone` and `Instance ID`.  
`Network Interfaces` | Optional. A comma-separated list of the specific network interfaces to modify. If no value is provided or if you use the `*` wildcard, the action updates all network interfaces. The default value is `*`.  
  
#### Action outputs

The **Remove External IP Addresses** action provides the following outputs:

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

The following example describes the JSON result output received when using the **Remove External IP Addresses** action:
    
    
    [
        {
            "endTime": "2024-05-21T04:28:05.371-07:00",
            "id": "ID",
            "insertTime": "2024-05-21T04:28:04.176-07:00",
            "kind": "compute#operation",
            "name": "operation-OPERATION_ID",
            "operationType": "updateNetworkInterface",
            "progress": 100,
            "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/operations/operation-OPERATION_ID",
            "startTime": "2024-05-21T04:28:04.190-07:00",
            "status": "DONE",
            "targetId": "TARGET_ID",
            "targetLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/instances/INSTANCE_ID",
            "user": "user@example.com",
            "zone": "us-west1-a",
            "networkInterface": "example"
        },
        {
            "endTime": "2024-05-21T04:28:06.549-07:00",
            "id": "2531200345768541098",
            "insertTime": "2024-05-21T04:28:05.419-07:00",
            "kind": "compute#operation",
            "name": "operation-OPERATION_ID",
            "operationType": "deleteAccessConfig",
            "progress": 100,
            "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/operations/operation-OPERATION_ID",
            "startTime": "2024-05-21T04:28:05.430-07:00",
            "status": "DONE",
            "targetId": "3905740668247239013",
            "targetLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-west1-a/instances/INSTANCE_ID",
            "user": "user@example.com",
            "zone": "us-west1-a",
            "networkInterface": "example"
        }
    ]
    

##### Output messages

The **Remove External IP Addresses** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully removed external IP addresses from RESOURCE_PATH instance in INTEGRATION_NAME.` `Waiting for the operation to finish execution on the RESOURCE_PATH instance in INTEGRATION_NAME.` | The action succeeded.  
`Error executing action "Remove External IP Addresses". Reason: ERROR_REASON` `Action ran into a timeout during execution. Pending operations: PENDING_OPERATIONS. Please increase the timeout in IDE.` `The following network interfaces were not found: INTERFACES on the RESOURCE_PATH in INTEGRATION_NAME. Please check the spelling.` `Provided instance zone is not valid.` `Provided instance ID is not valid.` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Remove External IP Addresses** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Remove IP From Firewall Rule

Use the **Remove IP From Firewall Rule** action to delete specific IP address ranges from an existing Compute Engine firewall rule.

This action doesn't run on Google SecOps entities. 

**Note:** This action runs asynchronously. Adjust the script timeout value in the Google SecOps IDE as needed to ensure the action has sufficient time to complete the request.

#### Action inputs

The **Remove IP From Firewall Rule** action requires the following parameters:

Parameter | Description  
---|---  
`Resource Name` | Optional. The full resource name of the Compute Engine instance, in the format `/projects/PROJECT_ID/global/ firewallsFIREWALL`. This parameter takes priority over `Project ID` and `Firewall Rule`.  
`Project ID` | Optional. The ID of the project associated with the Compute Engine instance. If no value is provided, the action retrieves the project ID from the integration configuration.  
`Firewall Rule` | Optional. The name of the specific firewall rule to update.  
`Type` | Required. The direction of the traffic for the IP range being added. The possible values are as follows:

  * `Source`
  * `Destination`

The default value is `Source`.  
`IP Ranges` | Required. A comma-separated list of IP address ranges (CIDR notation) to add to the firewall rule.  
  
#### Action outputs

The **Remove IP From Firewall Rule** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Remove IP From Firewall Rule** action:
    
    
    {
      "kind": "compute#operation",
      "id": "9160761312385876914",
      "name": "operation-1716223324528-618e5619d1f93-174eac81-6b38200d",
      "operationType": "patch",
      "targetLink": "https://www.googleapis.com/compute/v1/projects/project-id/global/firewalls/firewall-name",
      "targetId": "7886634413370691799",
      "status": "DONE",
      "user": "compute-admin@project-id.iam.gserviceaccount.com",
      "progress": 100,
      "insertTime": "2024-05-20T09:42:05.150-07:00",
      "startTime": "2024-05-20T09:42:05.164-07:00",
      "endTime": "2024-05-20T09:42:09.381-07:00",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/project-id/global/operations/operation-1716223324528-618e5619d1f93-174eac81-6b38200d",
      "firewall": {
        "kind": "compute#firewall",
        "id": "6297155974506248217",
        "creationTimestamp": "2023-09-13T07:28:06.690-07:00",
        "name": "firewall-name",
        "description": "",
        "network": "https://www.googleapis.com/compute/v1/projects/project-id/global/networks/vpc-network",
        "priority": 1000,
        "sourceRanges": [
          "0.0.0.0/0"
        ],
        "destinationRanges": [
          "0.0.0.0/21"
        ],
        "allowed": [
          {
            "IPProtocol": "tcp",
            "ports": [
              "22"
            ]
          }
        ],
        "direction": "INGRESS",
        "logConfig": {
          "enable": false
        },
        "disabled": false,
        "selfLink": "https://www.googleapis.com/compute/v1/projects/project-id/global/firewalls/firewall-name"
      }
    }
    

##### Output messages

The **Remove IP From Firewall Rule** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully updated firewall rule in Google Cloud Compute.` `Waiting for the operation to finish execution on the RESOURCE_PATH instance in Google Cloud Compute.` | The action succeeded.  
`Error executing action "Remove IP From Firewall Rule". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Remove IP From Firewall Rule** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Remove Network Tags

Use the **Remove Network Tags** action to remove network tags from the Compute Engine instance.

This action doesn't run on Google SecOps entities. 

**Note:** This action runs asynchronously. Adjust the script timeout value in the Google SecOps IDE as needed to ensure the action has sufficient time to complete the request.

#### Action inputs

The **Remove Network Tags** action requires the following parameters:

Parameter | Description  
---|---  
`Resource Name` | Optional. The full resource name of the Compute Engine instance, in the format `/project/PROJECT_ID/zone/ ZONE_ID/instances/ INSTANCE_ID`. This parameter takes priority over `Project ID`, `Instance Zone`, and `Instance ID`.  
`Project ID` | Optional. The ID of the project associated with the Compute Engine instance. If no value is provided, the action retrieves the project ID from the integration configuration.  
`Instance Zone` | Optional. The specific zone where the instance is located. This parameter is required if you're identifying the instance using `Instance Zone` and `Instance ID`.  
`Instance ID` | Optional. The unique ID of the instance you want to start. You can retrieve this value using the List Instances action. This parameter is required if you're identifying the instance using `Instance Zone` and `Instance ID`.  
`Network Tags` | Required. A comma-separated list of network tags to add to the instance. All tags must only contain lowercase letters, numbers, and hyphens.  
  
#### Action outputs

The **Remove Network Tags** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Example** action:
    
    
    {
      "kind": "compute#instance",
      "id": "1459671903146615834",
      "creationTimestamp": "2023-09-13T04:20:21.993-07:00",
      "name": "instance-2",
      "description": "",
      "tags": {
        "items": [
          "another-tag",
          "tag"
        ],
        "fingerprint": "BCeEINC7Ths="
      },
      "machineType": "https://www.googleapis.com/compute/v1/projects/project-id/zones/us-central1-a/machineTypes/e2-micro",
      "status": "RUNNING",
      "zone": "https://www.googleapis.com/compute/v1/projects/project-id/zones/us-central1-a",
      "canIpForward": false,
      "networkInterfaces": [
        {
          "kind": "compute#networkInterface",
          "network": "https://www.googleapis.com/compute/v1/projects/project-id/global/networks/default",
          "subnetwork": "https://www.googleapis.com/compute/v1/projects/project-id/regions/us-central1/subnetworks/default",
          "networkIP": "10.128.0.3",
          "name": "nic0",
          "fingerprint": "-ZnnV7hiDfs=",
          "stackType": "IPV4_ONLY"
        }
      ],
      "disks": [
        {
          "kind": "compute#attachedDisk",
          "type": "PERSISTENT",
          "mode": "READ_WRITE",
          "source": "https://www.googleapis.com/compute/v1/projects/project-id/zones/us-central1-a/disks/instance-2",
          "deviceName": "instance-2",
          "index": 0,
          "boot": true,
          "autoDelete": true,
          "licenses": [
            "https://www.googleapis.com/compute/v1/projects/centos-cloud/global/licenses/centos-7"
          ],
          "interface": "SCSI",
          "guestOsFeatures": [
            {
              "type": "UEFI_COMPATIBLE"
            },
            {
              "type": "GVNIC"
            }
          ],
          "diskSizeGb": "20",
          "architecture": "X86_64"
        }
      ],
      "metadata": {
        "kind": "compute#metadata",
        "fingerprint": "NBmH4-7Jw9U=",
        "items": []
      },
      "serviceAccounts": [
        {
          "email": "1111111111-compute@developer.gserviceaccount.com",
          "scopes": [
            "https://www.googleapis.com/auth/devstorage.read_only",
            "https://www.googleapis.com/auth/logging.write",
            "https://www.googleapis.com/auth/monitoring.write",
            "https://www.googleapis.com/auth/servicecontrol",
            "https://www.googleapis.com/auth/service.management.readonly",
            "https://www.googleapis.com/auth/trace.append"
          ]
        }
      ],
      "selfLink": "https://www.googleapis.com/compute/v1/projects/project-id/zones/us-central1-a/instances/instance-2",
      "scheduling": {
        "onHostMaintenance": "MIGRATE",
        "automaticRestart": true,
        "preemptible": false,
        "provisioningModel": "STANDARD"
      },
      "cpuPlatform": "Intel Broadwell",
      "deletionProtection": false,
      "shieldedInstanceConfig": {
        "enableSecureBoot": false,
        "enableVtpm": true,
        "enableIntegrityMonitoring": true
      }
    }
    

##### Output messages

The **Remove Network Tags** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully removed network tags from the instance RESOURCE_PATH in Compute Engine.` `Waiting for the operation to finish execution on the RESOURCE_PATH instance in Compute Engine.` | The action succeeded.  
`Error executing action "Remove Network Tags". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Remove Network Tags** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Set Instance IAM Policy

Use the **Set Instance IAM Policy** action to sets the access control policy for the specified resource. The policy that you provide in the action replaces any existing policy.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Set Instance IAM Policy** action requires the following parameters:

Parameters | Description  
---|---  
`Resource Name` | Optional. The full resource name of the Compute Engine instance, in the format `/project/PROJECT_ID/zone/ ZONE_ID/instances/ INSTANCE_ID`. This parameter takes priority over `Project ID`, `Instance Zone`, and `Instance ID`.  
`Project ID` | Optional. The ID of the project associated with the Compute Engine instance. If no value is provided, the action retrieves the project ID from the integration configuration.  
`Instance Zone` | Optional. The specific zone where the instance is located. This parameter is required if you're identifying the instance using `Instance Zone` and `Instance ID`.  
`Instance ID` | Optional. The unique ID of the instance you want to start. You can retrieve this value using the List Instances action. This parameter is required if you're identifying the instance using `Instance Zone` and `Instance ID`.  
`Policy` | Required. The IAM policy document to apply to the instance, provided as a JSON object.  
  
#### Action outputs

The **Set Instance IAM Policy** action provides the following outputs:

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

The following example describes the JSON result output received when using the **Set Instance IAM Policy** action:
    
    
    {
        "version": 1,
        "etag": "BwXBftu99FE=",
        "bindings": [
            {
                "role": "roles/compute.networkViewer",
                "members": [
                    "user:user@example.com"
                ]
            }
        ]
    }
    

##### Output messages

The **Set Instance IAM Policy** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully set new IAM policy for the Compute Engine instance INSTANCE_ID.` `Provided instance zone ZONE_ID is not valid.` `Provided instance ID INSTANCE_ID is not valid.` `Provided policy JSON document POLICY is not valid.` | The action succeeded.  
`Error executing action "Set Instance IAM Policy". Reason: ERROR_REASON` `Provided resource RESOURCE is not valid.` `Error executing action "Set Instance IAM Policy". Reason: "Resource Name" or "Instance Zone" **and** "Instance ID" needs to be provided. ` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Set Instance IAM Policy** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Start Instance

Use the **Start Instance** action to power on a Compute Engine instance that is in a stopped or terminated state.

This action doesn't run on Google SecOps entities. 

**Note:** This action runs asynchronously. Adjust the script timeout value in the Google SecOps IDE as needed to ensure the action has sufficient time to complete the request.

#### Action inputs

The **Start Instance** action requires the following parameters:

Parameters | Description  
---|---  
`Resource Name` | Optional. The full resource name of the Compute Engine instance, in the format `/project/PROJECT_ID/zone/ ZONE_ID/instances/ INSTANCE_ID`. This parameter takes priority over `Project ID`, `Instance Zone`, and `Instance ID`.  
`Project ID` | Optional. The ID of the project associated with the Compute Engine instance. If no value is provided, the action retrieves the project ID from the integration configuration.  
`Instance Zone` | Optional. The specific zone where the instance is located. This parameter is required if you're identifying the instance using `Instance Zone` and `Instance ID`.  
`Instance ID` | Optional. The unique ID of the instance you want to start. You can retrieve this value using the List Instances action. This parameter is required if you're identifying the instance using `Instance Zone` and `Instance ID`.  
  
#### Action outputs

The **Start Instance** action provides the following outputs:

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

The following example describes the JSON result output received when using the **Start Instance** action:
    
    
    {
       "id": "ID",
       "name": "operation-OPERATION_ID",
       "zone": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-a",
       "operationType": "start",
       "targetLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-a/instances/INSTANCE_ID",
       "targetId": "INSTANCE_ID",
       "status": "DONE",
       "user": "user@example.com",
       "progress": 100,
       "insertTime": "2021-04-28T23:01:29.395-07:00",
       "startTime": "2021-04-28T23:01:29.397-07:00",
       "endTime": "2021-04-28T23:01:29.397-07:00",
       "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-a/operations/operation-OPERATION_ID",
       "kind": "compute#operation"
    }
    

##### Output messages

The **Start Instance** action can return the following output messages:

Output message | Message description  
---|---  
`Compute Engine instance RESOURCE_PATH was started successfully.` `Provided instance zone ZONE_ID is not valid.` `Provided instance ID is not valid.` | The action succeeded.  
`Error executing action "Start Instance". Reason: ERROR_REASON` `Error executing action "Start Instance". Reason: You should provide either "Resource name" or "Instance Zone" and "Instance ID" parameters.` `Error executing action "Start Instance". Reason: Given resource name string does not match expected pattern.` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Start Instance** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Stop Instance

Use the **Stop Instance** action to shut down a running Compute Engine instance. You can restart a stopped instance at any time.

Stopping an instance stops VM usage charges, but charges continue to apply for associated resources such as persistent disks and static IP addresses unless those resources are deleted.

This action doesn't run on Google SecOps entities. 

**Note:** This action runs asynchronously. Adjust the script timeout value in the Google SecOps IDE as needed to ensure the action has sufficient time to complete the request.

#### Action inputs

The **Stop Instance** action requires the following parameters:

Parameters | Description  
---|---  
`Resource Name` | Optional. The full resource name of the Compute Engine instance, in the format `/project/PROJECT_ID/zone/ ZONE_ID/instances/ INSTANCE_ID`. This parameter takes priority over `Project ID`, `Instance Zone`, and `Instance ID`.  
`Project ID` | Optional. The ID of the project associated with the Compute Engine instance. If no value is provided, the action retrieves the project ID from the integration configuration.  
`Instance Zone` | Optional. The specific zone where the instance is located. This parameter is required if you're identifying the instance using `Instance Zone` and `Instance ID`.  
`Instance ID` | Optional. The unique ID of the instance you want to start. You can retrieve this value using the List Instances action. This parameter is required if you're identifying the instance using `Instance Zone` and `Instance ID`.  
  
#### Action outputs

The **Stop Instance** action provides the following outputs:

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

The following example describes the JSON result output received when using the **Stop Instance** action:
    
    
    {
       "id": "ID",
       "name": "operation-OPERATION_ID",
       "zone": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-a",
       "operationType": "stop",
       "targetLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-a/instances/INSTANCE_ID",
       "targetId": "INSTANCE_ID",
       "status": "RUNNING",
       "user": "user@example.com",
       "progress": 100,
       "insertTime": "2021-04-28T23:01:29.395-07:00",
       "startTime": "2021-04-28T23:01:29.397-07:00",
       "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/us-central1-a/operations/operation-OPERATION_ID",
       "kind": "compute#operation"
    }
    

##### Output messages

The **Stop Instance** action can return the following output messages:

Output message | Message description  
---|---  
`Compute Engine instance INSTANCE_ID was stopped successfully.` `Provided instance zone ZONE_ID is not valid.` `Provided instance ID is not valid.` | The action succeeded.  
`Error executing action "Stop Instance". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Stop Instance** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Update Firewall Rule

Use the **Update Firewall Rule** action to modify the configuration of an existing Compute Engine firewall rule. This action lets you update specific parameters while maintaining the rule's identity.

This action doesn't run on Google SecOps entities. 

**Note:** This action runs asynchronously. Adjust the script timeout value in the Google SecOps IDE as needed to ensure the action has sufficient time to complete the request.

#### Action inputs

The **Update Firewall Rule** action requires the following parameters:

Parameters | Description  
---|---  
`Firewall Rule` | Optional. The name of the specific firewall rule to update.  
`Project ID` | Optional. The ID of the project associated with the Compute Engine instance. If no value is provided, the action retrieves the project ID from the integration configuration.  
`Resource Name` | Optional. The full resource name of the Compute Engine instance, in the format `/projects/PROJECT_ID/global/ firewallsFIREWALL`. This parameter takes priority over `Project ID` and `Firewall Rule`.  
`Source IP Ranges` | Optional. A comma-separated list of the source IP address ranges for the firewall rule. If the `none` value is set, the action deletes all existing source IP ranges from the rule. If no value is provided, the existing values remain unchanged.  
`Source Tags` | Optional. A comma-separated list of source network tags to apply to the rule. If the `none` value is set, the action deletes all existing source tags from the rule. If no value is provided, the existing values remain unchanged.  
`Source Service Accounts` | Optional. A comma-separated list of source service accounts to apply to the rule. If the `none` value is set, the action deletes all existing source service accounts from the rule. If no value is provided, the existing values remain unchanged.  
`TCP Ports` | Optional. A comma-separated list of TCP ports or port ranges to allow or deny. This parameter supports the `all` and `none` values. If configured, the action updates the firewall rule's protocol and port list with this value.  
`UDP Ports` | Optional. A comma-separated list of UDP ports or port ranges to allow or deny. This parameter supports the `all` and `none` values. If configured, the action updates the firewall rule's protocol and port list with this value.  
`Other Protocols` | Optional. A comma-separated list of protocols other than TCP and UDP to include in the rule. If the `none` value is set, the action updates the firewall rule's protocol list with this value.  
`Destination IP Ranges` | Optional. A comma-separated list of the destination IP address ranges for the firewall rule. If the `none` value is set, the action deletes all existing destination IP ranges from the rule. If no value is provided, the existing values remain unchanged.  
  
#### Action outputs

The **Update Firewall Rule** action provides the following outputs:

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

The following example describes the JSON result output received when using the **Update Firewall Rule** action:
    
    
    {
      "kind": "compute#operation",
      "id": "9160761312385876914",
      "name": "operation-1716223324528-618e5619d1f93-174eac81-6b38200d",
      "operationType": "patch",
      "targetLink": "https://www.googleapis.com/compute/v1/projects/project-id/global/firewalls/firewall-name",
      "targetId": "7886634413370691799",
      "status": "DONE",
      "user": "compute-admin@project-id.iam.gserviceaccount.com",
      "progress": 100,g
      "insertTime": "2024-05-20T09:42:05.150-07:00",
      "startTime": "2024-05-20T09:42:05.164-07:00",
      "endTime": "2024-05-20T09:42:09.381-07:00",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/project-id/global/operations/operation-1716223324528-618e5619d1f93-174eac81-6b38200d",
      "firewall": {
        "kind": "compute#firewall",
        "id": "6297155974506248217",
        "creationTimestamp": "2023-09-13T07:28:06.690-07:00",
        "name": "firewall-name",
        "description": "",
        "network": "https://www.googleapis.com/compute/v1/projects/project-id/global/networks/vpc-network",
        "priority": 1000,
        "sourceRanges": [
          "0.0.0.0/0"
        ],
        "destinationRanges": [
          "0.0.0.0/21"
        ],
        "allowed": [
          {
            "IPProtocol": "tcp",
            "ports": [
              "22"
            ]
          }
        ],
        "direction": "INGRESS",
        "logConfig": {
          "enable": false
        },
        "disabled": false,
        "selfLink": "https://www.googleapis.com/compute/v1/projects/project-id/global/firewalls/firewall-name"
      }
    }
    

##### Output messages

The **Update Firewall Rule** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully updated firewall rule in Cloud Compute.` `Updating firewall rule in Cloud Compute.` | The action succeeded.  
`Error executing action "Update Firewall Rule". Reason: ERROR_REASON` `Provided firewall name is not valid.` `Action ran into a timeout during execution. Please increase the timeout in IDE.` `You must provide at least some parameter to update the firewall rule with.` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Update Firewall Rule** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
