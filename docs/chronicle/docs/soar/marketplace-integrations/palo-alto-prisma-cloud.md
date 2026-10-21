---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/palo-alto-prisma-cloud/
title: Palo Alto Networks Prisma Cloud \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:59:38.831530+00:00
---

# Palo Alto Networks Prisma Cloud  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/palo-alto-prisma-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Palo Alto Networks Prisma Cloud

This document provides guidance on how to integrate Palo Alto Networks Prisma Cloud with the SOAR module of Google Security Operations. In Google SecOps platform, the integration for Palo Alto Networks Prisma Cloud is called _Palo Alto Prisma Cloud_.

## Before you begin

Before configuring the integration in the Google SecOps platform, verify that you have the following:

  * **Prisma Cloud Access Key**: Generate the required API key for connection and communication.

  * **Required Permissions**: Ensure the service account has the necessary security roles assigned in Prisma Cloud.




### Prisma Cloud Access Key generation

To enable Google SecOps to securely communicate with your Prisma Cloud environment, you must first generate an Access Key. This key is used for API authentication.

For more information on how to generate the key, see [how to create access keys](https://docs.prismacloud.io/en/enterprise-edition/content-collections/administration/create-access-keys).

### Grant required permissions in Prisma Cloud

The Access Key you generate must be associated with a service account or role that has the necessary permissions to pull and manage alert and asset data from Prisma Cloud.

Ensure the service account or custom role used for this integration is granted the following minimum permissions:

  * `Asset Inventory.Overview`
  * `Alerts.Overview`
  * `Alerts.Snooze/Dismiss`
  * `Alerts.Remediation`
  * `Investigate.Asset`



## Integrate Prisma Cloud with Google SecOps

The integration requires the following parameters:

Parameter | Description  
---|---  
`API Root` | _Required_ The API root of the Prisma Cloud instance. Default value is `https://api3.prismacloud.io`.  
`Access Key ID` | _Required_ The access key ID of the Prisma Cloud account.  
`Secret Access Key` | _Required_ The secret access key of the Prisma Cloud account.  
`Verify SSL` | _Required_ If selected, Google SecOps verifies that the SSL certificate for the connection to the Prisma Cloud server is valid.Selected by default.  
  
You can make changes at a later stage, if necessary. After you configure a Prisma Cloud instance, you can use the instance in playbooks. For information on configuring and supporting Prisma Cloud multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

For instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

The following is the list of actions available in the Prisma Cloud integration:

  * Enrich Assets
  * Ping
  * Respond To Alert



### Enrich Assets

Use Prisma Cloud to enrich information about a resource.

This action doesn't run on Google SecOps entities. For more information about supported entities, see [What entity types do we support](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/what-entity-types-do-we-support).

#### Action inputs

The action requires the following parameters:

Parameter | Description  
---|---  
`Asset Identifiers` | _Required_ A comma-separated list of asset identifiers that you want to fetch the details for.An asset identifier is either an asset ID or an asset Restricted Resource Name (RRN).  
  
#### Action outputs

The action provides the following outputs:

Action output type | Action output availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
Output messages | Available  
  
##### JSON result

The following example describes the JSON result output received when using the Enrich Assets action:
    
    
    {
        "id":"2dcffa4a51d892bcf48ed80652e75650",
        "externalAssetId":"5115585594921894848",
        "cloudType":"gcp",
        "createdTs":1707216238063,
        "insertTs":1707216238063,
        "dynamicData":null,
        "data":{
            "id":"5115585594921894848",
            "kind":"compute#instance",
            "name":"example-name-rgmn",
            "tags":{
                "items":[
                    "example-name"
                ],
                "fingerprint":"ycXN3kijHZc="
            },
            "zone":"https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/zones/us-central1-a",
            "disks":[
                {
                    "boot":true,
                    "kind":"compute#attachedDisk",
                    "mode":"READ_WRITE",
                    "type":"PERSISTENT",
                    "index":0,
                    "source":"https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/zones/us-central1-a/disks/example-name-rgmn",
                    "licenses":[
                        "https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/global/licenses/LICENSE_ID"
                    ],
                    "interface":"SCSI",
                    "autoDelete":true,
                    "deviceName":"persistent-disk-0",
                    "diskSizeGb":"30",
                    "architecture":"X86_64",
                    "guestOsFeatures":[
                        {
                            "type":"GVNIC"
                        },
                        {
                            "type":"SEV_CAPABLE"
                        },
                        {
                            "type":"UEFI_COMPATIBLE"
                        },
                        {
                            "type":"VIRTIO_SCSI_MULTIQUEUE"
                        }
                    ],
                    "shieldedInstanceInitialState":{
                        "dbxs":[
                        ]
                    }
                }
            ],
            "labels":{
                "goog-ccm":"true",
                "goog-solutions-console-solution-id":"java-application",
                "goog-solutions-console-deployment-name":"java-application"
            },
            "status":"RUNNING",
            "metadata":{
                "kind":"compute#metadata",
                "items":[
                    {
                        "key":"created-by",
                        "value":"projects/PROJECT_ID/regions/us-central1/instanceGroupManagers/example-name"
                    },
                    {
                        "key":"instance-template",
                        "value":"projects/PROJECT_ID/global/instanceTemplates/xwiki-us-central1-a-temp"
                    },
                    {
                        "key":"startup-script",
                        "value":"#! /bin/bash\n\nsed -i \"s/$(echo JGROUP_BUCKET | sed -e 's/\\([[\/.*]\\|\\]\\)/\\\\&/g')/$(echo xwiki-jgroup-PROJECT_ID-gce | sed -e 's/[\/&]/\\\\&/g')/g\" /usr/lib/xwiki/WEB-INF/observation/remote/jgroups/tcp.xml\nsed -i \"s/$(echo ACCESS_KEY | sed -e 's/\\([[\/.*]\\|\\]\\)/\\\\&/g')/$(echo GOOG1E | sed -e 's/[\/&]/\\\\&/g')/g\" /usr/lib/xwiki/WEB-INF/observation/remote/jgroups/tcp.xml\nsed -i \"s/$(echo SECRET_KEY | sed -e 's/\\([[\/.*]\\|\\]\\)/\\\\&/g')/$(echo IvgTtIJJq+68sI9XISo2qMXGyONmFDf7U9QuegN/ | sed -e 's/[\/&]/\\\\&/g')/g\" /usr/lib/xwiki/WEB-INF/observation/remote/jgroups/tcp.xml\n\nDB_PASS=\"$(gcloud secrets versions access --secret xwiki-db-password latest --project PROJECT_NAME)\"\n\nbash /home/xwiki_startup.sh \"203.0.113.2\" \"xwiki\" \"${DB_PASS}\" \"203.0.113.242\"\nbash /home/xwiki_deploy_flavor.sh \"203.0.113.2\" \"xwiki\" \"${DB_PASS}\" \"203.0.113.242\"\n"
                    }
                ],
                "fingerprint":"_s0ui1yxFME="
            },
            "selfLink":"https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/zones/us-central1-a/instances/example-name-rgmn",
            "scheduling":{
                "preemptible":false,
                "automaticRestart":true,
                "onHostMaintenance":"MIGRATE",
                "provisioningModel":"STANDARD"
            },
            "cpuPlatform":"Intel Cascade Lake",
            "fingerprint":"YBMt5z3lxpI=",
            "machineType":"https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/zones/us-central1-a/machineTypes/n2-standard-2",
            "minCpuPlatform":"Intel Cascade Lake",
            "serviceAccounts":[
                {
                    "email":"example@developer.gserviceaccount.com",
                    "scopes":[
                        "https://www.googleapis.com/auth/cloud-platform",
                        "https://www.googleapis.com/auth/compute",
                        "https://www.googleapis.com/auth/devstorage.full_control",
                        "https://www.googleapis.com/auth/devstorage.read_only",
                        "https://www.googleapis.com/auth/logging.write",
                        "https://www.googleapis.com/auth/monitoring.write",
                        "https://www.googleapis.com/auth/service.management.readonly",
                        "https://www.googleapis.com/auth/servicecontrol",
                        "https://www.googleapis.com/auth/trace.append"
                    ]
                }
            ],
            "startRestricted":false,
            "labelFingerprint":"Cy_Kdpu4cz8=",
            "creationTimestamp":"2024-02-05T16:28:31.856-08:00",
            "networkInterfaces":[
                {
                    "kind":"compute#networkInterface",
                    "name":"nic0",
                    "network":"https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/global/networks/NETWORK_ID",
                    "networkIP":"203.0.113.2",
                    "stackType":"IPV4_ONLY",
                    "subnetwork":"https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/regions/us-central1/subnetworks/SUBNETWORK_ID",
                    "fingerprint":"lpKHF5wzhv4="
                }
            ],
            "deletionProtection":false,
            "lastStartTimestamp":"2024-02-05T16:28:47.038-08:00",
            "shieldedInstanceConfig":{
                "enableVtpm":true,
                "enableSecureBoot":false,
                "enableIntegrityMonitoring":true
            },
            "shieldedInstanceIntegrityPolicy":{
                "updateAutoLearnPolicy":true
            }
        },
        "name":"example-name-rgmn",
        "regionId":"us-central1",
        "regionName":"US",
        "riskGrade":"B",
        "stateId":null,
        "url":"https://console.cloud.google.com/compute/instancesDetail/zones/us-central1-a/instances/example-name-rgmn?project=PROJECT_NAME",
        "vpcId":null,
        "vpcName":null,
        "relationshipCounts":1,
        "vulnerabilityCounts":{
            "critical":17,
            "high":38,
            "knownExploits":{
                "critical":0,
                "high":0,
                "low":0,
                "medium":0
            },
            "low":31,
            "medium":59,
            "old":{
                "critical":0,
                "high":0,
                "low":0,
                "medium":0
            },
            "patchable":{
                "critical":17,
                "high":38,
                "low":5,
                "medium":26
            }
        },
        "vpcExternalAssetId":null,
        "tags":{
            "goog-ccm":true,
            "xwiki-us-central1-autoscale":"",
            "goog-solutions-console-deployment-name":"java-application",
            "goog-solutions-console-solution-id":"java-application"
        },
        "assetType":"Google Compute Engine VM Instance",
        "serviceName":"Google Compute Engine",
        "resourceType":"Google Compute Engine VM Instance",
        "accountGroup":"account",
        "accountName":"Example-Name",
        "assetClassId":"compute",
        "assetClass":"Compute",
        "deleted":false,
        "problem":[
            
        ],
        "alertsCount":[
            {
                "count":5,
                "severity":"high"
            },
            {
                "count":3,
                "severity":"critical"
            },
            {
                "count":2,
                "severity":"low"
            }
        ],
        "attributes":{
            "altAssetId":"example-name-rgmn.us-central1-a.c.PROJECT_NAME.internal",
            "name":"example-name-rgmn.us-central1-a.c.PROJECT_NAME.internal",
            "provider":"gcp",
            "accountID":"example-account",
            "region":"us-central1-a",
            "resourceName":"5115585594921894848",
            "osRelease":"focal",
            "osDistro":"ubuntu",
            "distro":"Ubuntu 20.04.5 LTS",
            "scannedBy":"Agentless",
            "docker":"",
            "kubernetes":"",
            "cluster":"",
            "vmImage":"hsa-xwiki-vm-img-latest",
            "collections":[
                "All"
            ],
            "scanPassed":true,
            "stage":"run",
            "lastScanTime":"2024-02-12T18:25:39.39Z"
        },
        "alertCountBySeverity":[
            {
                "severity":"high",
                "count":5
            },
            {
                "severity":"critical",
                "count":3
            },
            {
                "severity":"low",
                "count":2
            }
        ]
    }
    

##### Script result

The following table describes the values for the script result output when using the Enrich Assets action:

Script result name | Value  
---|---  
is_success | True or False  
  
##### Output messages

On a Case Wall, the Enrich Assets action provides the following output messages:

Output message | Message description  
---|---  
`Successfully enriched the following resources using information from Palo Alto Prisma Cloud: ASSET_ID` `Action wasn't able to enrich the following assets using information from Palo Alto Prisma Cloud: ASSET_ID` `None of the provided assets were enriched.` | Action succeeded.  
`Error executing action "Enrich Assets". Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### Ping

Use this action to test connectivity to the Prisma Cloud server.

#### Action inputs

None.

#### Action outputs

The action provides the following outputs:

Action output type | Action output availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
Output messages | Available  
  
##### Script result

The following table describes the values for the script result output when using the Ping action:

Script result name | Value  
---|---  
is_success | True or False  
  
##### Output messages

On a Case Wall, the Ping action provides the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Palo Alto Prisma Cloud server with the provided connection parameters!` | Action succeeded.  
`Failed to connect to the Palo Alto Prisma Cloud server! Error is ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### Respond To Alert

Use Prisma Cloud to respond to an alert.

This action doesn't run on Google SecOps entities. For more information about supported entities, see [What entity types do we support](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/what-entity-types-do-we-support).

#### Action inputs

The action requires the following parameters:

Parameter | Description  
---|---  
`Alert ID` | _Required_ ID of the response alert.  
`Response Type` | _Optional_ An alert status.If the `Snooze` value is selected, the **Snooze Time** parameter is required. Possible values:

  * Dismiss
  * Snooze
  * Reopen
  * Remediate

  
`Snooze Time` | _Optional_ The snooze time in hours.  
`Dismiss Note` | _Optional_ A note to justify a dismissal.  
  
#### Action outputs

The action provides the following outputs:

Action output type | Action output availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
Output messages | Available  
  
##### JSON result

The following example describes the JSON result output received when using the Respond To Alert action:
    
    
    {
    "response_status": {"Reopened", "Snoozed", "Dismissed", "Remediated", "No Remediation Applied."} 
    }
    

##### Script result

The following table describes the values for the script result output when using the Respond to Alert action:

Script result name | Value  
---|---  
is_success | True or False  
  
##### Output messages

On a Case Wall, the Ping action provides the following output messages:

Output message | Message description  
---|---  
`Successfully responded to an alert with ID ALERT_ID in Palo Alto Prisma Cloud.` | Action succeeded.  
`Error executing action "Respond To Alert". Reason: Alert with ID ALERT_ID wasn't found in Palo Alto Prisma Cloud. Please check the spelling.` | Action failed.Alert is not found. Check the spelling.  
`Error executing action "Respond To Alert". Reason: The Response Type parameter is misconfigured. Select a valid value for the Response Type parameter.` | Action failed.Check the **Response Type** parameter value.  
`Error executing action "Respond To Alert". Reason: Action couldn't respond to alert with ID ALERT_ID in Palo Alto Prisma Cloud. Please check the action configuration parameters.` | Action failed.Check the input parameter values.  
`Error executing action "Respond To Alert". Reason: The Response Type parameter was set to "Snooze". Make sure that the Snooze Time parameter value is configured and valid.` | Action failed.Check the **Snooze Time** parameter value.   
`Error executing action "Respond To Alert". Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
## Connectors

For detailed instructions about configuring a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

### Palo Alto Prisma Cloud — Alerts Connector

Use this connector to pull alerts from Prisma Cloud.

The dynamic list works with the **policy.name** parameter as shown in the following example:
    
    
    "filters": [
     {
         "operator": "=",
         "name": "policy.name",
         "value": "Google Cloud VM instance that is internet reachable with unrestricted access (203.0.113.0/24)"
     },
     {
         "operator": "=",
         "name": "policy.name",
         "value": "Compute Engine with IAM write access level"
     }
    ]
    

#### Connector inputs

The connector requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | _Required_ The source field name to retrieve the product field name.The default value is `policy_policyType`.  
`Event Field Name` | _Required_ The source field name to retrieve the event field name.Default value is `resource_cloudType`.  
`Environment Field Name` | _Optional_ The name of the field where the environment name is stored.If the environment field isn't found, the environment is set to the default environment.  
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic.Use the default value `.*` to retrieve the required raw `Environment Field Name` value.If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`API Root` | _Required_ The API root of the Prisma Cloud instance.Default value is `https://api3.prismacloud.io`.  
`Access Key ID` | _Required_ The access key ID of the Prisma Cloud account.  
`Secret Access Key` | _Required_ The secret access key of the Prisma Cloud account.  
`Lowest Severity to Fetch` | _Optional_ The lowest severity of the alerts to fetch.If you provide no value, the connector ingests alerts with all severities.Possible values: 

  * Critical
  * High
  * Medium
  * Low
  * Informational

  
`Max Hours Backwards` | _Optional_ The number of hours before the connector first starts retrieving incidents. This parameter applies only once to the initial connector iteration after you enable the connector for the first time.The default value is 1 hour.  
`Max Alerts To Fetch` | _Optional_ The number of alerts to process in one connector iteration. The default value is 100. The maximum value is 1000.  
`Use dynamic list as a blocklist` | _Required_ If selected, the dynamic list is used as a blocklist. Not selected by default.  
`Verify SSL` | _Required_ If selected, Google SecOps verifies that the SSL certificate for the connection to the Prisma Cloud server is valid.Not selected by default.  
`Proxy Server Address` | _Optional_ Address of the proxy server to use.  
`Proxy Username` | _Optional_ Proxy username to authenticate with.  
`Proxy Password` | _Optional_ Proxy password to authenticate with.  
  
#### Connector events

The following is an example of a connector event:
    
    
    {
     "id": "ID",
     "status": "open",
     "reason": "NEW_ALERT",
     "firstSeen": 1706971601230,
     "lastSeen": 1706971601230,
     "alertTime": 1706971601230,
     "lastUpdated": 1707806767098,
     "saveSearchId": "b1ccf7df-d2c8-4588-8d06-b62738fd9745",
     "policy": {
         "policyId": "45488d62-6abe-4938-9b7a-aaa44858540e",
         "name": "Data destruction risk due to a publicly exposed and vulnerable Google Cloud VM instance with delete permissions",
         "policyType": "attack_path",
         "systemDefault": true,
         "description": "This policy idnces as soon as possible.",
         "severity": "critical",
         "recommendation": "The followinge vulnerabilities quickly.",
         "labels": [
             "Prisma_Cloud"
         ],
         "lastModifiedOn": 1702006359544,
         "lastModifiedBy": "user@example.com",
         "deleted": false,
         "findingTypes": [],
         "remediable": false
     },
     "alertRules": [
         {
             "policyScanConfigId": "9612cba4-4f76-44ec-b11f-9c01ba9a4c04",
             "name": "Default Alert Rule",
             "enabled": true,
             "scanAll": true,
             "target": {
                 "accountGroups": [],
                 "excludedAccounts": [],
                 "regions": [],
                 "tags": []
             },
             "createdBy": "example@example.com",
             "alertRuleNotificationConfig": [],
             "allowAutoRemediate": false,
             "notifyOnOpen": true,
             "notifyOnSnoozed": false,
             "notifyOnDismissed": false,
             "notifyOnResolved": false
         }
     ],
     "resource": {
         "id": "ID",
         "name": "gke-gke-pc-pool-1-4e52a225-12id",
         "account": "Example-Account",
         "accountId": "ACCOUNT_ID",
         "cloudAccountGroups": [
             "Default Account Group"
         ],
         "region": "US",
         "regionId": "us-central1",
         "resourceType": "INSTANCE",
         "resourceApiName": "gcloud-compute-instances-list",
         "cloudServiceName": "Google Compute Engine",
         "data": {},
         "cloudType": "gcp",
         "resourceTs": 1706915178410,
         "internalResourceId": "INTERNAL_RESOURCE_ID",
         "cloudAccountOwners": [
             "user1@example.com",
             "user2@example.com"
         ],
         "unifiedAssetId": "393924d2b306c07490b19615c6e1a265",
         "resourceConfigJsonAvailable": false,
         "resourceDetailsAvailable": true
     },
     "networkAnomaly": false
    }
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
