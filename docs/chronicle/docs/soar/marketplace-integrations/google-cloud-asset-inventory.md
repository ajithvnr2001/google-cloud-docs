---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-cloud-asset-inventory/
title: Integrate Cloud Asset Inventory with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:17.593461+00:00
---

# Integrate Cloud Asset Inventory with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-cloud-asset-inventory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Cloud Asset Inventory with Google SecOps 

This document explains how to integrate Cloud Asset Inventory with Google Security Operations.

**Note:** In the Google SecOps platform, the integration for Cloud Asset Inventory is called _Google Cloud Asset Inventory_.

## Use cases

The **Cloud Asset Inventory** integration uses Google SecOps capabilities to support the following use cases:

  * **Enrich Google Cloud resources** : Automatically fetch detailed metadata for cloud resources using full resource names to provide context for security alerts.

  * **Retrieve resource snapshots** : Get a point-in-time view of resource configurations and status to aid in forensic investigations and change analysis.

  * **Audit service account permissions** : List roles and unique permissions associated with service accounts to identify over-privileged identities and maintain the principle of least privilege.

  * **Inventory multi-cloud assets** : Access resource details across Google Cloud and connected external environments to centralize your asset visibility within investigations.




## Before you begin

Before you configure the Cloud Asset Inventory integration in Google SecOps, complete the following prerequisite steps:

**Note:** For new deployments provisioned starting in Q4 2025, we recommend configuring all service accounts in the same project as your Google SecOps instance.

  1. Create a service account.

  2. Create a custom IAM role.

  3. Grant the necessary roles to your service account.

  4. Choose and configure one of the following authentication methods:

     * **Option 1:Workload Identity (recommended)**: This method uses short-lived, temporary access tokens using service account impersonation, eliminating the need to store any secrets.

     * **Option 2:Service account JSON key**: This method relies on a static, long-lived secret key file. Use this method only if Workload Identity isn't available in your environment.




### Create a service account

To create a service account, complete the following steps:

  1. In the Google Cloud console, go to **Credentials**.

[Go to Credentials](https://console.cloud.google.com/apis/credentials)

  2. From the **Create credentials** menu, select **Service account**.

  3. Enter a name in the **Service account name** field and click **Create and continue**.

  4. Skip the optional role assignment and principal access screens by clicking **Continue > Done**.

  5. Copy the service account email address for use in the configuration steps.




### Create a custom IAM role

To provide the integration with required search capabilities, create a custom role:

  1. In the Google Cloud console, go to **IAM & Admin > Roles**.

[Go to Roles](https://console.cloud.google.com/iam-admin/roles)

  2. Click **Create role** and provide a **Title** (such as "SecOps Asset Searcher") and a unique **ID**.

  3. Set the **Role launch stage** to **General Availability**.

  4. Click **Add Permissions** and add `cloudasset.assets.searchAllResources`.

  5. Click **Create**.




### Grant roles to your service account

To let the integration access your resources, grant the following roles to your service account:

  1. In the Google Cloud console, go to [**IAM & Admin > IAM**](https://console.cloud.google.com/iam-admin/iam).

  2. Locate your service account and click **edit Edit principal**.

  3. Click **Add another role** and select the following:

     * The custom IAM role created in the previous step.

     * **Cloud Asset Viewer**.

     * **Service Usage Consumer** (only required if you use a `Quota Project ID`).

  4. Click **Save**.




### Configure Workload Identity credentials

Choose this method or the JSON key method to authenticate the integration. Workload Identity is the recommended and more secure approach because it uses short-lived, temporary access tokens using service account impersonation, eliminating the need to store or rotate long-lived secrets.

#### Identify the unique instance identity

To authenticate using a Workload Identity, you must grant your Google SecOps instance permission to impersonate your service account. This lets the instance securely access Google Cloud resources.

  1. In Google SecOps, go to **Content Hub > Response Integrations**.

  2. Select the **Cloud Asset Inventory** integration, and enter your service account email in `Workload Identity Email`.

  3. Click **Save > Test**. The test is expected to fail. 

  4. Click close_small to the right of **Test** and search the error message for the identity email beginning with `gke-init-python@...` or `soar-python@...`.

  5. Copy this unique email address.




#### Authorize the instance identity in Google Cloud

Once you have retrieved the unique identity for your Google SecOps instance, you must authorize it to access your Google Cloud resources. This step enables service account impersonation, allowing the platform to generate short-lived tokens and act on your behalf without the need for static keys.

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select the target service account and go to **Permissions > Grant Access**.

  3. Paste the unique email address into the **New principals** field and assign the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`).




#### Grant quota project access

When authenticating with a Workload Identity, you must specify a `Quota Project ID` in the integration settings to track API usage and billing. 

To authorize this, you must grant your service account the following role on the designated quota project:

  1. In the Google Cloud console, go to **IAM & Admin > IAM** and select your project.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Locate your service account in the list of principals and click **edit(Edit principal)** for that account.

  3. Click **Add another role** and select the **Service Usage Consumer** role (`roles/serviceusage.serviceUsageConsumer`).

  4. Click **Save**.




### Configure a JSON key

Choose this method or the Workload Identity method to authenticate the integration. Use the JSON key method only if Workload Identity isn't available in your environment. Workload Identity is the recommended and more secure approach. This method relies on a static, long-lived secret key file that requires manual management and rotation.

Use the following procedure to generate the JSON key file required to authenticate the integration:

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts** and select the service account you created.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Go to the **Keys** tab.

  3. Click **Add key > Create new key**.

  4. Select `JSON` as the key type and click **Create**. The JSON file downloads to your computer.

  5. Copy the entire content of this file and paste it into `User's Service Account` during integration configuration.




## Integration parameters

The Cloud Asset Inventory integration requires the following parameters:

Parameter | Description  
---|---  
`API Root` | _Required_ The API root of the Cloud Asset Inventory instance. The default value is `https://cloudasset.googleapis.com`.  
`Organization ID` | _Optional_ The organization ID to use in the Cloud Asset Inventory integration.  
`Project ID` | _Optional_ The project ID to use for the Cloud Asset Inventory integration. If no value is provided, the integration retrieves theproject ID from the JSON file content provided in the `User's Service Account` parameter.  
`User's Service Account` | _Required_ The full content of the service account JSON key file. **Important:** To authenticate, you must provide either this field or `Workload Identity Email`. Don't populate this field if you intend to authenticate using a Workload Identity, because providing both causes authentication conflicts.   
`Quota Project ID` | _Optional_ The Google Cloud project ID that you use for Google Cloud APIs and billing. This parameter requires you to grant the `Service Usage Consumer` role to your service account. If no value is provided, the integration retrieves the project ID from your Google Cloud service account.  
`Workload Identity Email` | _Optional._ The client email address of the service account used for Workload Identity impersonation. **Important:** Don't populate this field if you intend to authenticate using a JSON key. Providing both causes authentication conflicts. To prevent `Permission Denied` errors, grant the **Service Account Token Creator** role to the Google SecOps instance service account for the email address provided in this field.  
`Verify SSL` | _Required_ If selected, the integration validates the SSL certificate when connecting to the Cloud Asset Inventory server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Enrich Resource

Use the **Enrich Resource** action to enrich information about a Google Cloud resource using Cloud Asset Inventory.

This action doesn't run on Google SecOps entities. 

#### Action inputs

To configure the **Enrich Resource** action, use the following parameters:

Parameter | Description  
---|---  
`Resource Names` | _Required_ A comma-separated list containing resource names of resources to fetch details for.To configure this parameter, enter the full metadata resource name in the following format: `//cloudresourcemanager.googleapis.com/projects/PROJECT_ID`.  
`Fields To Return` | _Optional_ A comma-separated list of fields to return.The default value is `*`.Examples of values are as follows: `assetType`, `project`, `folders`, `organization`, `displayName`, `description`, `location`, `labels`, `networkTags`, `kmsKeys`, `createTime`, `updateTime`, `state`, `additionalAttributes`, `parentFullResourceName`, `parentAssetType`. The action always returns the `displayName` field. There is also an option to configure advanced filters. For example, to return a specific key from `additionalAttributes`, enter `additionalAttributes.{key}`. To exclude a specific key from `additionalAttributes`, enter `-additionalAttributes.{key}`.  
  
#### Action outputs

The **Enrich Resource** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Enrich Resource** action:
    
    
    [
      {
        "Entity": "//iam.googleapis.com/projects/PROJECT/serviceAccounts/SERVICE_ACCOUNT/keys/KEY_ID",
        "EntityResult": {
          "additionalAttributes": {
            "email": "email@example.iam.gserviceaccount.com",
            "uniqueId": 123456789
          },
          "name": "//iam.googleapis.com/projects/PROJECT/serviceAccounts/SERVICE_ACCOUNT/keys/KEY_ID",
          "assetType": "iam.googleapis.com/ServiceAccountKey",
          "project": "projects/PROJECT",
          "displayName": "projects/PROJECT/serviceAccounts/SERVICE_ACCOUNT@PROJECT.iam.gserviceaccount.com/keys/KEY_ID",
          "createTime": "2022-05-26T17:35:07Z",
          "versionedResources": [
            {
              "version": "v1",
              "resource": {
                "keyAlgorithm": "KEY_ALG_RSA_2048",
                "keyOrigin": "GOOGLE_PROVIDED",
                "keyType": "USER_MANAGED",
                "name": "projects/PROJECT/serviceAccounts/SERVICE_ACCOUNT@PROJECT.iam.gserviceaccount.com/keys/KEY_ID",
                "validAfterTime": "2022-05-26T17:35:07Z",
                "validBeforeTime": "9999-12-31T23:59:59Z"
              }
            }
          ],
          "organization": "organizations/ORGANIZATION",
          "parentFullResourceName": "//iam.googleapis.com/projects/PROJECT/serviceAccounts/SERVICE_ACCOUNT@PROJECT.iam.gserviceaccount.com",
          "parentAssetType": "iam.googleapis.com/ServiceAccount"
        }
      }
    ]
    

##### Output messages

The **Enrich Resource** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully enriched the following resources using information from Google Cloud Asset Inventory: ASSET_IDENTIFIER` `Action wasn't able to enrich the following resources using information from Google Cloud Asset Inventory: ASSET_IDENTIFIER` `None of the provided resources were enriched.` | The action succeeded.  
`Error executing action "Enrich resources". Reason: ERROR_REASON` | The action failed.Check connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Enrich Resource** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Resource Snapshot

Use the **Get Resource Snapshot** action to get information about the resource using Cloud Asset Inventory.

This action doesn't run on Google SecOps entities. 

#### Action inputs

To configure the **Get Resource Snapshot** action, use the following parameters:

Parameter | Description  
---|---  
`Resource Names` | _Required_ A comma-separated list of resources to fetch details for.To configure this parameter, enter the full metadata resource name in the following format: `//cloudresourcemanager.googleapis.com/projects/PROJECT_ID`.  
`Fields To Return` | _Optional_ A comma-separated list of fields to return. Input every field in the following format: `assets.FIELD` Examples of values are as follows: `assets.asset.name, assets.asset.assetType, assets.asset.resource.data`. The action always returns the `assets.asset.name` field. The default value is `*`.  
  
#### Action outputs

The **Get Resource Snapshot** action provides the following outputs:

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

The following examples show the JSON result outputs received when using the **Get Resource Snapshot** action:

##### JSON result for Google Cloud
    
    
        [
     {
       "Entity": "//compute.googleapis.com/projects/example-project/zones/us-central1-a/instances/example-instance",
       "EntityResult": {
         "window": {
           "startTime": "2023-08-14T19:43:41.805828Z",
           "endTime": "2262-04-11T23:47:16.854775807Z"
         },
         "asset": {
           "name": "//compute.googleapis.com/projects/example-project/zones/us-central1-a/instances/example-instance",
           "assetType": "compute.googleapis.com/Instance",
           "resource": {
             "version": "v1",
             "discoveryDocumentUri": "https://www.googleapis.com/discovery/v1/apis/compute/v1/rest",
             "discoveryName": "Instance",
             "parent": "//cloudresourcemanager.googleapis.com/projects/example-project-id",
             "data": {
               "description": "",
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
               "lastStartTimestamp": "2022-05-26T01:44:52.756-07:00",
               "deletionProtection": false,
               "name": "example-name",
               "keyRevocationActionType": "NONE_ON_KEY_REVOCATION",
               "canIpForward": false,
               "shieldedInstanceIntegrityPolicy": {
                 "updateAutoLearnPolicy": true
               },
               "zone": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a",
               "resourceStatus": {},
               "scheduling": {
                 "onHostMaintenance": "MIGRATE",
                 "preemptible": false,
                 "provisioningModel": "STANDARD",
                 "automaticRestart": true
               },
               "machineType": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/machineTypes/e2-micro",
               "confidentialInstanceConfig": {
                 "enableConfidentialCompute": false
               },
               "selfLink": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/instances/example-instance",
               "id": "example-id",
               "fingerprint": "example-fingerprint",
               "startRestricted": false,
               "networkInterfaces": [
                 {
                   "network": "https://www.googleapis.com/compute/v1/projects/example-project/global/networks/example-network",
                   "stackType": "IPV4_ONLY",
                   "name": "example",
                   "subnetwork": "https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1/subnetworks/example-network-subnet",
                   "accessConfigs": [
                     {
                       "type": "ONE_TO_ONE_NAT",
                       "name": "External NAT",
                       "natIP": "192.0.2.1",
                       "networkTier": "PREMIUM"
                     }
                   ],
                   "fingerprint": "example-fingerprint",
                   "networkIP": "203.0.113.2"
                 }
               ],
               "allocationAffinity": {
                 "consumeAllocationType": "ANY_ALLOCATION"
               },
               "labelFingerprint": "example-label",
               "shieldedInstanceConfig": {
                 "enableSecureBoot": false,
                 "enableVtpm": true,
                 "enableIntegrityMonitoring": true
               },
               "cpuPlatform": "Intel Broadwell",
               "creationTimestamp": "2022-05-26T01:44:40.323-07:00",
               "status": "RUNNING",
               "disks": [
                 {
                   "guestOsFeatures": [
                     {
                       "type": "VIRTIO_SCSI_MULTIQUEUE"
                     },
                     {
                       "type": "SEV_CAPABLE"
                     },
                     {
                       "type": "UEFI_COMPATIBLE"
                     },
                     {
                       "type": "GVNIC"
                     }
                   ],
                   "interface": "SCSI",
                   "shieldedInstanceInitialState": {
                     "dbxs": [
                       {
                         "content": "2gcDBhMRFQAAAAAAAAAAABENAAAAAvEOndK",
                         "fileType": "BIN"
                       }
                     ],
                     "dbx": [
                       {
                         "fileType": "BIN",
                         "content": "2gcDBhMRFQAAAAAAAAAAABENAAAAAvEOndK"
                       }
                     ]
                   },
                   "diskSizeGb": "10",
                   "deviceName": "example-device-name",
                   "type": "PERSISTENT",
                   "source": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/disks/example-instance",
                   "boot": true,
                   "licenses": [
                     "https://www.googleapis.com/compute/v1/projects/example-project/global/licenses"
                   ],
                   "index": 0,
                   "autoDelete": true,
                   "mode": "READ_WRITE"
                 }
               ],
               "tags": {
                 "items": [
                   "http-server"
                 ],
                 "fingerprint": "example-fingerprint"
               },
               "displayDevice": {
                 "enableDisplay": false
               },
               "reservationAffinity": {
                 "consumeReservationType": "ANY_ALLOCATION"
               }
             },
             "location": "us-central1-a"
           },
           "ancestors": [
             "projects/example-project-id",
             "organizations/example-org-id"
           ],
           "updateTime": "2023-08-14T19:43:41.805828Z"
         }
       }
     },
     {
       "Entity": "//iam.googleapis.com/projects/example-project/serviceAccounts/example-account-id",
       "EntityResult": {
         "window": {
           "startTime": "2023-12-22T13:37:50Z",
           "endTime": "2262-04-11T23:47:16.854775807Z"
         },
         "asset": {
           "name": "//iam.googleapis.com/projects/example-project/serviceAccounts/example-account-id",
           "assetType": "iam.googleapis.com/ServiceAccount",
           "resource": {
             "version": "v1",
             "discoveryDocumentUri": "https://iam.googleapis.com/$discovery/rest",
             "discoveryName": "ServiceAccount",
             "parent": "//cloudresourcemanager.googleapis.com/projects/example-project-id",
             "data": {
               "name": "projects/example-project/serviceAccounts/cloud-asset-inventory-auto@example-project.iam.gserviceaccount.com",
               "projectId": "example-project",
               "email": "cloud-asset-inventory-auto@example-project.iam.gserviceaccount.com",
               "uniqueId": "example-account-id",
               "displayName": "Cloud Asset Inventory Automation",
               "oauth2ClientId": "example-account-id"
             }
           },
           "ancestors": [
             "projects/example-project-id",
             "organizations/example-org-id"
           ],
           "updateTime": "2023-12-22T13:37:50Z"
         }
       }
     }
    ]

##### JSON result for AWS
    
    
    [
       {
           "Entity": "//cloudasset.googleapis.com/organizations/example-org-id/otherCloudConnections/aws/arn:aws:s3:::aps-max-test-bucket",
           "EntityResult": {
               "assets": [
                   {
                       "window": {
                           "startTime": "2024-01-24T17:51:03.412233028Z",
                           "endTime": "2262-04-11T23:47:16.854775807Z"
                       },
                       "asset": {
                           "name": "//cloudasset.googleapis.com/organizations/example-org-id/otherCloudConnections/aws/arn:aws:s3:::aps-max-test-bucket",
                           "assetType": "cloudasset.googleapis.com/AWS::S3::Bucket",
                           "resource": {
                               "version": "v1",
                               "discoveryDocumentUri": "n/a",
                               "discoveryName": "n/a",
                               "data": {
                                   "dataSourceProvider": "AMAZON_WEB_SERVICES",
                                   "supplementaryConfigurations": {
                                       "PublicAccessBlockConfiguration": {
                                           "BlockPublicPolicy": true,
                                           "RestrictPublicBuckets": true,
                                           "BlockPublicAcls": true,
                                           "IgnorePublicAcls": true
                                       },
                                       "TagSet": [
                                           {
                                               "Key": "my-key2",
                                               "Value": "my-value2"
                                           },
                                           {
                                               "Key": "my-key1",
                                               "Value": "my-value1"
                                           }
                                       ],
                                       "ServerSideEncryptionConfiguration": {
                                           "Rules": [
                                               {
                                                   "ApplyServerSideEncryptionByDefault": {
                                                       "SSEAlgorithm": "AES256"
                                                   },
                                                   "BucketKeyEnabled": true
                                               }
                                           ]
                                       },
                                       "AccessControlPolicy": {
                                           "Grants": [
                                               {
                                                   "Grantee": {
                                                       "DisplayName": "example",
                                                       "ID": "example-id",
                                                       "Type": "CanonicalUser"
                                                   },
                                                   "Permission": "FULL_CONTROL"
                                               }
                                           ],
                                           "Owner": {
                                               "DisplayName": "example",
                                               "ID": "example-id"
                                           }
                                       }
                                   },
                                   "configuration": {
                                       "Name": "aps-max-test-bucket",
                                       "CreationDate": "2023-12-04T15:29:50+00:00"
                                   },
                                   "tags": {
                                       "my-key2": "my-value2",
                                       "my-key1": "my-value1"
                                   },
                                   "originalResourceName": "arn:aws:s3:::aps-max-test-bucket",
                                   "awsAccount": "arn:aws:organizations::example-id:account/example-account/example-account-id"
                               },
                               "location": "global"
                           },
                           "ancestors": [
                               "organizations/example-org-id"
                           ],
                           "updateTime": "2024-01-24T17:51:03.412233028Z"
                       }
                   }
               ]
           }
       }
    ]

##### Output messages

The **Get Resource Snapshot** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned information about the following resources using Google Cloud Asset Inventory:  ASSET_IDENTIFIER` `Action wasn't able to return information about the following resources using Google Cloud Asset Inventory:  ASSET_IDENTIFIER.` `No information was found for the provided resources.` | The action succeeded.  
`Error executing action "Get Resource Snapshot". Reason: ERROR_REASON` | The action failed.Check connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Resource Snapshot** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List Service Account Roles

Use the **List Service Account Roles** action to list roles that are related to the Google Cloud service account using Cloud Asset Inventory.

This action doesn't run on Google SecOps entities. 

#### Action inputs

To configure the **List Service Account Roles** action, use the following parameters:

Parameter | Description  
---|---  
`Service Accounts` | _Required_ A comma-separated list of service accounts to fetch details for.  
`Check Roles` | _Optional_ A comma-separated list of roles to check in relation to service account, such as `roles/cloudasset.owner`.  
`Check Permissions` | _Optional_ A comma-separated list of permission to check in relation to service account, such as `cloudasset.assets.listResource `.  
`Expand Permissions` | _Optional_ If selected, the action returns information about all unique permissions related to the resource. Not selected by default.  
`Max Roles To Return` | _Required_ The number of roles related to service account to return.The default value is 100.  
`Max Permissions To Return` | _Required_ The number of permissions related to the service account to return.  
  
#### Action outputs

The **List Service Account Roles** action provides the following outputs:

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

The following example shows the JSON result output received when using the **List Service Account Roles** action:
    
    
    {
       "roles": ["role1", "role2"],
       "unique_permissions": ["permission1", "permission2"]
    }
    

##### Output messages

The **List Service Account Roles** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully enriched for the following service accounts using information from Google Cloud Asset Inventory: ASSET_IDENTIFIER` `Action wasn't able to enrich the following service accounts using information from Google Cloud Asset Inventory: ASSET_IDENTIFIER` `None of the service accounts were enriched.` | The action succeeded.  
`Error executing action "List Service Account Roles". Reason: ERROR_REASON` | The action failed.Check connection to the server, input parameters, or credentials.  
  
### Ping

Use the **Ping** action to test the connectivity to Cloud Asset Inventory.

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
`Successfully connected to the Google Cloud Asset Inventory server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Google Cloud Asset Inventory server! ` | The action failed.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
