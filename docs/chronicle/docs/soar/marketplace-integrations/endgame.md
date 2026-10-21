---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/endgame/
title: Endgame \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:08:56.275770+00:00
---

# Endgame  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/endgame/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Endgame

**Important:** Endgame was acquired by Elastic and became part of Elastic Security.

This document describes how to integrate Endgame with Google Security Operations.

## Integrate Endgame with Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Enrich Entities

Enrich a Google SecOps Host and IP entities based on the information from Endgame.

#### Parameters

N/A

#### Use cases

The action can be used in the playbooks investigating activity on devices. If the device has the Endgame agent installed, then the action pulls Endgame information on device to enrich Google SecOps entities.

#### Run on

This action runs on the following entities:

  * Host
  * IP Address



#### Action results

##### Entity enrichment

Enrichment Field Name | Logic-When to apply  
---|---  
Endgame_Domain | Always  
Endgame_endpoint_id | Always  
Endgame_hostname | Always  
Endgame_sensors_status | Always  
Endgame_sensors_id | Always  
Endgame_sensors_status | Always  
Endgame_sensors_id | Always  
Endgame_policy_status | Always  
Endgame_policy_name | Always  
Endgame_policy_id | Always  
Endgame_is_isolated | Always  
  
##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
      "data": [
          {
              "domain": "InstallerInitiated",
              "updated_at": "2019-11-01T05:42:08.149079+00:00",
              "id": "1682418d-02ff-43cd-a730-bcae8215a514",
              "display_operating_system": "CentOS 7.6",
              "hostname": "example",
              "mac_address": "01:23:45:ab:cd:ef",
              "upgrade_status": "",
              "base_image": false,
              "isolation_updated_at": null,
              "status": "monitored",
              "ad_distinguished_name": "",
              "ad_hostname": "",
              "tags": [
                  {
                      "id": "a0927aeb-915a-466d-a5eb-5d7b6f9217c5",
                      "name": "BLUE TEAM"
                  },
                  {
                      "id": "bede2f24-593c-45e4-9863-9c2438f0f163",
                      "name": "SOC"
                  },
                  {
                      "id": "fc2dfcc8-9329-4f33-86a2-877bfb27575e",
                      "name": "CORE ENV"
                  }
              ],
              "isolation_request_status": null,
              "alert_count": 0,
              "investigation_count": 0,
              "groups": [
                  {
                      "is_dynamic": false,
                      "count": 4,
                      "id": "c1af3cd6-2638-4144-842d-adc9cfb67fb9",
                      "name": "SOC"
                  }
              ],
              "sensors": [
                  {
                      "status": "monitored",
                      "sensor_version": "3.52.12",
                      "policy_status": "successful",
                      "policy_name": "Lab (Detect-Only)",
                      "sensor_type": "hunt",
                      "id": "fbb87923-a833-5581-a160-7f4f85a21bd0",
                      "policy_id": "a1d72bce-1f61-4ba8-bcd4-dfa97148335f"
                  }
              ],
              "ip_address": "192.0.2.1",
              "is_isolated": false,
              "operating_system": "Linux 3.10.0-957.27.2.el7.x86_64",
              "name": "example",
              "status_changed_at": "2020-01-07T08:15:11.865854+00:00",
              "core_os": "linux",
              "created_at": "2019-03-19T05:07:50.598837+00:00",
              "error": null,
              "machine_id": "827255f4-53a2-1823-cac0-7c0f7730ca26"
          },
          {
              "domain": "InstallerInitiated",
              "updated_at": "2019-11-01T05:42:09.150756+00:00",
              "id": "12c3530d-657f-4ccd-835e-6df9affeed3d",
              "display_operating_system": "Ubuntu 18.04.3",
              "hostname": "example",
              "mac_address": "01:23:45:ab:cd:ef",
              "upgrade_status": "",
              "base_image": false,
              "isolation_updated_at": null,
              "status": "monitored",
              "ad_distinguished_name": "",
              "ad_hostname": "",
              "tags": [],
              "isolation_request_status": null,
              "alert_count": 0,
              "investigation_count": 0,
              "groups": [
                  {
                      "is_dynamic": false,
                      "count": 4,
                      "id": "c1af3cd6-2638-4144-842d-adc9cfb67fb9",
                      "name": "SOC"
                  }
              ],
              "sensors": [
                  {
                      "status": "monitored",
                      "sensor_version": "3.52.12",
                      "policy_status": "successful",
                      "policy_name": "Lab (Detect-Only)",
                      "sensor_type": "hunt",
                      "id": "dc2e35cc-0c87-5a60-8fc8-de23ef747d02",
                      "policy_id": "a1d72bce-1f61-4ba8-bcd4-dfa97148335f"
                  }
              ],
              "ip_address": "192.0.2.1",
              "is_isolated": false,
              "operating_system": "Linux 4.15.0-72-generic",
              "name": "example",
              "status_changed_at": "2020-01-07T08:15:16.875375+00:00",
              "core_os": "linux",
              "created_at": "2019-09-20T21:34:51.966863+00:00",
              "error": null,
              "machine_id": "5ae8ddd9-9339-ae4b-ccf7-5ed68f38b3a9"
          }
      ],
      "metadata": {
          "count": 38,
          "previous_url": null,
          "timestamp": "2020-01-07T18:09:43.765744",
          "next": null,
          "per_page": 50,
          "next_url": null,
          "transaction_id": "569cdc38-8c7a-4b93-af99-aaf907dc8dd6",
          "previous": null
      }
    }
    

### List Investigations

List Endgame investigations.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
OS | String | Solaris,Windows,MacOs,Linux | Specify for which OS you want to list investigations. Parameter can take multiple values as a comma-separated string.  
Fetch investigations for the last X hours | Int | N/A | Return investigations created for the specified timeframe in hours.  
Max Investigation to Return | Int | N/A | Specify how many investigation you want to query.  
  
#### Use cases

Investigations are used to hunt different objects of the endpoints, for example, processes, IP addresses, and files. This action allows the user to list investigations. Analysts may use this action to make sure that all of the required investigations are being performed on the system.

#### Run on

This action runs on all entities.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
      "data": [
          {
              "created_by_chat": false,
              "name": "Example User + 2020-01-08T13:47:51.334336_utc",
              "core_os": "windows",
              "created_at": "2020-01-08T13:47:51.340497+00:00",
              "task_completion": {
                  "completed_tasks": 1,
                  "total_tasks": 1
              },
              "archived": false,
              "created_by": {
                  "username": "admin",
                  "last_name": "User",
                  "is_active": true,
                  "is_editable": true,
                  "is_ldap": false,
                  "is_removable": false,
                  "timezone": null,
                  "id": "5ed3c5d7-f450-489d-8b5f-9430b18da4c1",
                  "first_name": "Example",
                  "last_viewed_alert": "2020-01-07T09:24:22.925000",
                  "is_sso": false,
                  "is_superuser": true,
                  "role": {
                      "role": "Admin",
                      "id": "37e9e54e-0bb8-5058-9bd4-50a0d0fbea35",
                      "permissions": {
                          "endpoints.scan": true,
                          "sensor.admin.view": true,
                          "sensor.admin.update": true,
                          "endpoints.delete": true,
                          "endpoints.respond": true,
                          "search.search": true,
                          "sensor.admin.create": true,
                          "alerts.admin.forwardalerts": true,
                          "endpoints.tag": true,
                          "user.delete": true,
                          "endpoints.deploy": true,
                          "user.update": true,
                          "search.save": true,
                          "investigation.create": true,
                          "endpoints.view": true,
                          "user.view": true,
                          "sensor.admin.download": true,
                          "alerts.view": true,
                          "alerts.update": true,
                          "search.delete": true,
                          "sensor.admin.delete": true,
                          "endpoints.uninstall": true,
                          "investigation.view": true,
                          "admin": true,
                          "investigation.update": true,
                          "endpoints.changeconfiguration": true,
                          "user.create": true
                      }
                  },
                  "type": "Local",
                  "email": null
              },
              "updated_at": "2020-01-08T13:47:51.379966+00:00",
              "created_by_user_display_name": "Example User",
              "canceled_by_user_id": null,
              "version": 2,
              "endpoint_count": 1,
              "assigned_to": {
                  "username": "admin",
                  "last_name": "User",
                  "is_active": true,
                  "is_editable": true,
                  "is_ldap": false,
                  "is_removable": false,
                  "timezone": null,
                  "id": "5ed3c5d7-f450-489d-8b5f-9430b18da4c1",
                  "first_name": "Example",
                  "last_viewed_alert": "2020-01-07T09:24:22.925000",
                  "is_sso": false,
                  "is_superuser": true,
                  "role": {
                      "role": "Admin",
                      "id": "37e9e54e-0bb8-5058-9bd4-50a0d0fbea35",
                      "permissions": {
                          "endpoints.scan": true,
                          "sensor.admin.view": true,
                          "sensor.admin.update": true,
                          "endpoints.delete": true,
                          "endpoints.respond": true,
                          "search.search": true,
                          "sensor.admin.create": true,
                          "alerts.admin.forwardalerts": true,
                          "endpoints.tag": true,
                          "user.delete": true,
                          "endpoints.deploy": true,
                          "user.update": true,
                          "search.save": true,
                          "investigation.create": true,
                          "endpoints.view": true,
                          "user.view": true,
                          "sensor.admin.download": true,
                          "alerts.view": true,
                          "alerts.update": true,
                          "search.delete": true,
                          "sensor.admin.delete": true,
                          "endpoints.uninstall": true,
                          "investigation.view": true,
                          "admin": true,
                          "investigation.update": true,
                          "endpoints.changeconfiguration": true,
                          "user.create": true
                      }
                  },
                  "type": "Local",
                  "email": null
              },
              "id": "e0ad7613-daf6-435f-98f6-ce40eae01acc",
              "canceled_by_user_display_name": null,
              "user_display_name": "Example User",
              "hunt_count": 1,
              "is_canceled": false
          }
      ],
     "metadata": {
          "count": 46,
          "previous_url": null,
          "timestamp": "2020-01-08T16:02:09.251511",
          "next": 2,
          "per_page": 1,
          "next_url": "/api/v1/investigations/?per_page=1&page=2",
          "previous": null
      }
    }
    

### Get Investigation Details

Get information on a specific Endgame investigation.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Investigation ID | String | N/A | Specify Endgame investigation ID to search for.  
  
#### Use cases

Investigations are used to hunt different objects of the endpoints, for example, processes, IP addresses, and files. This action allows the user to get more information about specific investigations. Analysts may use this action to make sure that all of the required tasks were performed on the system.

#### Run on

This action runs on all entities.

#### Action Results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "data": {
            "tasks": [
                "6500673c-d246-41a3-882d-d3a339f28497"
            ],
            "user_display_name": "Example User",
            "task_types": [
                "Process Survey"
            ],
            "task_completion": {
                "completed_tasks": 1,
                "total_tasks": 1
            },
            "updated_at": "2020-01-06T13:30:33.851816+00:00",
            "created_by_user_display_name": "Example User",
            "id": "54caeedc-d6b0-4ca0-8f64-8798d1c34d54",
            "task_completions_by_type": {
                "Process Survey": {
                    "completed_tasks": 1,
                    "task_type_id": "2fbf0c36-5160-5c31-99ec-0fa5880c6bd1",
                    "total_tasks": 1
                }
            },
            "archived": false,
            "user_id": "5ed3c5d7-f450-489d-8b5f-9430b18da4c1",
            "is_canceled": false,
            "created_by": {
                "username": "admin",
                "last_name": "User",
                "is_active": true,
                "is_editable": true,
                "is_ldap": false,
                "is_removable": false,
                "timezone": null,
                "id": "5ed3c5d7-f450-489d-8b5f-9430b18da4c1",
                "first_name": "Example",
                "last_viewed_alert": "2020-01-06T09:27:04.097000",
                "is_sso": false,
                "is_superuser": true,
                "role": {
                    "role": "Admin",
                    "id": "37e9e54e-0bb8-5058-9bd4-50a0d0fbea35",
                    "permissions": {
                        "endpoints.scan": true,
                        "sensor.admin.view": true,
                        "sensor.admin.update": true,
                        "endpoints.delete": true,
                        "endpoints.respond": true,
                        "search.search": true,
                        "sensor.admin.create": true,
                        "alerts.admin.forwardalerts": true,
                        "endpoints.tag": true,
                        "user.delete": true,
                        "endpoints.deploy": true,
                        "user.update": true,
                        "search.save": true,
                        "investigation.create": true,
                        "endpoints.view": true,
                        "user.view": true,
                        "sensor.admin.download": true,
                        "alerts.view": true,
                        "alerts.update": true,
                        "search.delete": true,
                        "sensor.admin.delete": true,
                        "endpoints.uninstall": true,
                        "investigation.view": true,
                        "admin": true,
                        "investigation.update": true,
                        "endpoints.changeconfiguration": true,
                        "user.create": true
                    }
                },
                "type": "Local",
                "email": null
            },
            "hunt_count": 1,
            "canceled_by_user_id": null,
            "version": 2,
            "endpoint_count": 1,
            "canceled_by_user_display_name": null,
            "created_by_user_id": "5ed3c5d7-f450-489d-8b5f-9430b18da4c1",
            "account_id": "c374bb8a-9a98-4823-b280-68e74c170a0e",
            "created_by_chat": false,
            "sensors": [
                "8eef6873-6db7-58ab-a1ca-68dc19b54117"
            ],
            "name": "Example User + 2020-01-06T13:30:33.808543_utc",
            "core_os": "windows",
            "created_at": "2020-01-06T13:30:33.813747+00:00",
            "assigned_to": {
                "username": "admin",
                "last_name": "User",
                "is_active": true,
                "is_editable": true,
                "is_ldap": false,
                "is_removable": false,
                "timezone": null,
                "id": "5ed3c5d7-f450-489d-8b5f-9430b18da4c1",
                "first_name": "Example",
                "last_viewed_alert": "2020-01-06T09:27:04.097000",
                "is_sso": false,
                "is_superuser": true,
                "role": {
                    "role": "Admin",
                    "id": "37e9e54e-0bb8-5058-9bd4-50a0d0fbea35",
                    "permissions": {
                        "endpoints.scan": true,
                        "sensor.admin.view": true,
                        "sensor.admin.update": true,
                        "endpoints.delete": true,
                        "endpoints.respond": true,
                        "search.search": true,
                        "sensor.admin.create": true,
                        "alerts.admin.forwardalerts": true,
                        "endpoints.tag": true,
                        "user.delete": true,
                        "endpoints.deploy": true,
                        "user.update": true,
                        "search.save": true,
                        "investigation.create": true,
                        "endpoints.view": true,
                        "user.view": true,
                        "sensor.admin.download": true,
                        "alerts.view": true,
                        "alerts.update": true,
                        "search.delete": true,
                        "sensor.admin.delete": true,
                        "endpoints.uninstall": true,
                        "investigation.view": true,
                        "admin": true,
                        "investigation.update": true,
                        "endpoints.changeconfiguration": true,
                        "user.create": true
                    }
                },
                "type": "Local",
                "email": null
            },
     "endpoints": [
                "b23c8a14-69e0-4966-b78a-c9fba4fdd934"
            ]
        },
        "metadata": {
            "timestamp": "2020-01-06T14:00:53.716517"
        }
    }
    

### Get Host Isolation Config

Get host isolation config defined in Endgame.

#### Parameters

N/A

#### Use cases

This action is used to get information about host isolation config. This config allows isolated hosts to connect to the IP addresses listed there. Analysts may use this action to verify that all of the required IP addresses are in the host isolation config.

#### Run on

This action runs on all entities.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
      "data": [
          {
              "id": "47999eeb-f076-5aca-a7cc-56bf7ac2b647",
              "comments": [
                  {
                      "comment": "Testing API",
                      "entity_id": "47999eeb-f076-5aca-a7cc-56bf7ac2b647",
                      "user_id": "5ed3c5d7-f450-489d-8b5f-9430b18da4c1",
                      "account_id": "c374bb8a-9a98-4823-b280-68e74c170a0e",
                      "entity_type": "whitelisted_ip",
                      "created_at": "2020-01-07T15:59:56Z",
                      "updated_at": "2020-01-07T15:59:56Z",
                      "id": 547,
                      "activity_type": "comment"
                  }
              ],
              "addr": "192.0.2.1/30"
          },
          {
              "id": "6ab5575c-718e-5e24-bd4d-77e0694ad6fc",
              "comments": [
                  {
                      "comment": "Testing API",
                      "entity_id": "6ab5575c-718e-5e24-bd4d-77e0694ad6fc",
                      "user_id": "5ed3c5d7-f450-489d-8b5f-9430b18da4c1",
                      "account_id": "c374bb8a-9a98-4823-b280-68e74c170a0e",
                      "entity_type": "whitelisted_ip",
                      "created_at": "2020-01-07T15:58:29Z",
                      "updated_at": "2020-01-07T15:58:29Z",
                      "id": 545,
                      "activity_type": "comment"
                  }
              ],
              "addr": "192.0.2.11/32"
          },
          {
              "id": "72bdf5d2-4cc6-5ccf-9787-a539fae9c517",
      "comments": [
                  {
                      "comment": "CIDR Test",
                      "entity_id": "72bdf5d2-4cc6-5ccf-9787-a539fae9c517",
                      "user_id": "5ed3c5d7-f450-489d-8b5f-9430b18da4c1",
                      "account_id": "c374bb8a-9a98-4823-b280-68e74c170a0e",
                      "entity_type": "whitelisted_ip",
                      "created_at": "2020-01-07T15:58:04Z",
                      "updated_at": "2020-01-07T15:58:04Z",
                      "id": 543,
                      "activity_type": "comment"
                  }
              ],
              "addr": "198.51.100.1/32"
          },
          {
              "id": "5aa89c8f-a535-5876-840c-af33a7ec1419",
              "comments": [
                  {
                      "comment": "Testing API",
                      "entity_id": "5aa89c8f-a535-5876-840c-af33a7ec1419",
                      "user_id": "5ed3c5d7-f450-489d-8b5f-9430b18da4c1",
                      "account_id": "c374bb8a-9a98-4823-b280-68e74c170a0e",
                      "entity_type": "whitelisted_ip",
                      "created_at": "2020-01-07T15:57:24Z",
                      "updated_at": "2020-01-07T15:57:24Z",
                      "id": 541,
                      "activity_type": "comment"
                  }
              ],
              "addr": "198.51.100.10"
          },
          {
              "id": "06461575-700b-596d-8662-7ea0aff28e9c",
              "comments": [
                  {
                      "comment": "Test Isolation",
                      "entity_id": "06461575-700b-596d-8662-7ea0aff28e9c",
                      "user_id": "5ed3c5d7-f450-489d-8b5f-9430b18da4c1",
                      "account_id": "c374bb8a-9a98-4823-b280-68e74c170a0e",
                      "entity_type": "whitelisted_ip",
                      "created_at": "2020-01-07T15:55:21Z",
                      "updated_at": "2020-01-07T15:55:21Z",
                      "id": 539,
                      "activity_type": "comment"
                  }
              ],
              "addr": "203.0.113.1"
          }
      ],
      "metadata": {
          "count": 5,
          "previous_url": null,
          "timestamp": "2020-01-07T16:00:19.754687",
          "next": null,
          "per_page": 10,
          "next_url": null,
          "previous": null
      }
    }
    

### Add IP Subnet to Host Isolation Config

Add an IP subnet to host isolation config defined in Endgame.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
IP Subnet | String | N/A | Enter the IPv4 Subnet that you want to add to Host Isolation Config.  
Description | String | N/A | Enter the description to the IP Subnet.  
Create Insight | Checkbox | unchecked | If enabled, creates Insight after successful execution of this action.  
  
#### Use cases

This action is used to get information about host isolation config. This config allows isolated hosts to connect to the IP subnets listed there. Analysts may use this action to add required IP subnets to the host isolation config.

#### Run On

This action runs on all entities.

#### Action Results

##### Insights

If an IP subnet was added to the host isolation config using Endgame, then create an insight to indicate this.

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### Remove IP Subnet From Host Isolation Config

Remove an IP subnet from host isolation config defined in Endgame.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
IP Subnet | String | N/A | Enter the IPv4 Subnet that you want to add to Host Isolation Config.  
Create Insight | Checkbox | unchecked | If enabled, creates Insight after successful execution of this action.  
  
#### Use cases

This action is used to get information about host isolation config. This config allows isolated hosts to connect to the IP subnets listed there. Analysts may use this action to remove IP subnets that are no longer required from the host isolation config.

#### Run on

This action runs on all entities.

#### Action results

##### Insights

If an IP subnet was removed from the host isolation config using Endgame, then create an insight to indicate this.

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### Collect Autoruns (Windows Only)

Collect autoruns from the Endgame endpoint.

#### Parameters

Parameter Display Name | Type | Default Value | Description  
---|---|---|---  
Max Items to Return | Integer | 1000 | Specify how many autoruns to return.  
  
  
Category "All" | Checkbox | Checked | If enabled, search for all autorun categories.  
Category "Network Provider" | Checkbox | Unchecked | If enabled, search for "Network Provider" autorun category.  
Category "Office" | Checkbox | Unchecked | If enabled, search for "Office" autorun category .  
Category "Driver" | Checkbox | Unchecked | If enabled, search for "Driver" autorun category.  
Category "App Init" | Checkbox | Unchecked | If enabled, search for "App Init" autorun category.  
Category "Winlogon" | Checkbox | Unchecked | If enabled, search for "Winlogon" autorun category.  
Category "Print Monitor" | Checkbox | Unchecked | If enabled, search for "Print Monitor" autorun category.  
Category "Ease of Access" | Checkbox | Unchecked | If enabled, search for "Ease of Access" autorun category.  
Category "WMI" | Checkbox | Unchecked | If enabled, search for "WMI" autorun category.  
Category "LSA Provider" | Checkbox | Unchecked | If enabled, search for "LSA Provider" autorun category.  
Category "Service" | Checkbox | Unchecked | If enabled, search for "Service" autorun category.  
Category "Bits" | Checkbox | Unchecked | If enabled, search for "Bits" autorun category.  
Category "Known dll" | Checkbox | Unchecked | If enabled, search for "Known dll" autorun category.  
Category "Print Provider" | Checkbox | Unchecked | If enabled, search for "Print Provider" autorun category.  
Category "Image Hijack" | Checkbox | Unchecked | If enabled, search for "Image Hijack" autorun category.  
Category "Startup Folder" | Checkbox | Unchecked | If enabled, search for "Startup Folder" autorun category.  
Category "Internet Explorer" | Checkbox | Unchecked | If enabled, search for "Internet Explorer" autorun category.  
Category "Codec" | Checkbox | Unchecked | If enabled, search for "Codec" autorun category.  
Category "Logon" | Checkbox | Unchecked | If enabled, search for "Logon" autorun category.  
Category "Search Order Hijack" | Checkbox | Unchecked | If enabled, search for "Search Order Hijack" autorun category.  
Category "Winsock Provider" | Checkbox | Unchecked | If enabled, search for "Winsock Provider" autorun category .  
Category "Boot Execute' | Checkbox | Unchecked | If enabled, search for "Boot Execute" autorun category.  
Category "Phantom dll" | Checkbox | Unchecked | If enabled, search for "Phantom dll" autorun category.  
Category "Com Hijack" | Checkbox | Unchecked | If enabled, search for "Com Hijack" autorun category.  
Category "Explorer" | Checkbox | Unchecked | If enabled, search for "Explorer" autorun category.  
Category "Scheduled Task" | Checkbox | Unchecked | If enabled, search for "Scheduled Task" autorun category.  
Include All Metadata | Checkbox | Checked | If enabled, provides all available data.  
Include Malware Classification Metadata | Checkbox | Unchecked | If enabled, provides information about MalwareScore.  
Include Authenticode Metadata | Checkbox | Unchecked | If enabled, provides Signer Information.  
Include MD5 Hash | Checkbox | Unchecked | If enabled, provides MD5 hash in the response.  
Include SHA-1 Hash | Checkbox | Unchecked | If enabled, provides SHA-1 hash in the response.  
Include SHA-256 Hash | Checkbox | Unchecked | If enabled, provides SHA-256 hash in the response.  
  
#### Use cases

This action can be used to gather information about autoruns on the endpoint. This data can assist analysts to perform triage and remediation processes.

#### Run on

This action runs on the following entities:

  * Host
  * IP Address



#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
      "data": {
          "count": 1,
          "per_page": 50,
          "previous": null,
          "tasks": [
              {
                  "user_id": "5ed3c5d7-f450-489d-8b5f-9430b18da4c1",
                  "data": {
                      "category_option": {
                          "category_network_provider": true,
                          "category_office": false,
                          "category_driver": false,
                          "category_app_init": false,
                          "category_winlogon": false,
                          "category_print_monitor": false,
                          "category_ease_of_access": false,
                          "category_wmi": false,
                          "category_lsa_provider": false,
                          "category_service": false,
                          "category_bits": false,
                          "category_known_dll": false,
                          "category_print_provider": false,
                          "category_image_hijack": false,
                          "category_startup_folder": false,
                          "category_internet_explorer": false,
                          "category_codec": false,
                          "category_logon": false,
                          "category_all": false,
                          "category_search_order_hijack": false,
                          "category_winsock_provider": false,
                          "category_boot_execute": false,
                          "category_phantom_dll": false,
                          "category_com_hijack": false,
                          "category_explorer": false,
                          "category_scheduled_task": false
                      },
                      "metadata_option": {
                          "metadata_all": true,
                          "metadata_malware_classification": false,
                          "metadata_sha1": false,
                          "metadata_sha256": false,
                          "metadata_authenticode": false,
                          "metadata_md5": false
                      }
                  },
                  "account_id": "c374bb8a-9a98-4823-b280-68e74c170a0e",
                  "metadata": {
                      "sensor_id": "8eef6873-6db7-58ab-a1ca-68dc19b54117",
                      "investigation_id": "0b043f77-531f-4109-93b1-e01019ad0980",
                      "task_id": "e667b0c3-39de-4862-9baf-d6697db79721",
                      "echo": "",
                      "endpoint_id": "b23c8a14-69e0-4966-b78a-c9fba4fdd934",
                      "destination_plugin": "autoruns",
                      "key": "collectAutoRunsRequest",
                      "semantic_version": "3.52.\\d+",
                      "collection_id": "2393f424-bf57-40af-81e6-91b95acf5409"
                  }
              }
          ],
          "next": null
      },
      "metadata": {
          "timestamp": "2020-01-08T13:15:37.238341"
      }
    }
    

### Isolate Host

Isolate Endgame endpoint. This action supports only Windows and macOS systems.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Create Insight | Checkbox | Unchecked | If enabled, creates an Insight after successful execution of this action.  
  
#### Use cases

This action is used to get information about host isolation config. This config allows isolated hosts to connect to the IP subnets listed there. Analysts may use this action to add required IP subnets to the host isolation config.

#### Run on

This action runs on the following entities:

  * Host
  * IP Address



#### Action results

##### Entity enrichment

N/A

##### Insights

If the endpoint was isolated using Endgame agent, then create an insight to indicate this.

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
      "data": {
          "valid": true,
          "bulk_task_id": "a6ccc2f7-39a7-42e7-b646-41b281316b1d",
          "error_messages": []
      },
      "metadata": {
          "timestamp": "2020-01-08T15:09:22.474963"
      }
    }
    

### Unisolate Host

Unisolate an Endgame endpoint. This action supports only Windows and macOS systems.

#### Parameters

Parameter Display Name | Type | Default Value | Description  
---|---|---|---  
Create Insight | Checkbox | Unchecked | If enabled, creates an Insight after successful execution of this action.  
  
#### Run on

This action runs on the following entities:

  * Host
  * IP Address



#### Action Results

##### Insights

If the endpoint was unisolated using Endgame agent, then create an insight to indicate this.

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
      "data": {
          "domain": "InstallerInitiated",
          "updated_at": "2020-01-08T08:16:26.063394+00:00",
          "id": "b23c8a14-69e0-4966-b78a-c9fba4fdd934",
          "display_operating_system": "Windows 10 (v1511)",
          "hostname": "example",
          "mac_address": "01:23:45:ab:cd:ef",
          "upgrade_status": "",
          "base_image": false,
          "isolation_updated_at": "2020-01-08T15:09:24.665367+00:00",
          "status": "monitored",
          "ad_distinguished_name": "CN=EXAMPLE,CN=Computers,DC=example,DC=com",
          "ad_hostname": "example.com",
          "tags": [],
          "isolation_request_status": null,
          "alert_count": 0,
          "groups": [
              {
                  "is_dynamic": false,
                  "count": 2,
                  "id": "d9de26c9-ee63-4d38-9997-7418bd13c45e",
                  "name": "Demo: APT28"
              }
          ],
          "sensors": [
              {
                  "status": "monitored",
                  "sensor_version": "3.52.12",
                  "policy_status": "successful",
                  "policy_name": "Lab (Detect-Only with Streaming)",
                  "sensor_type": "hunt",
                  "id": "8eef6873-6db7-58ab-a1ca-68dc19b54117",
                  "policy_id": "07b7a44f-25f3-4e5c-977b-2915de8160c5"
              }
          ],
          "ip_address": "192.0.2.3",
          "is_isolated": false,
          "operating_system": "Windows 10.0",
          "name": "example",
          "status_changed_at": "2020-01-08T12:30:48.704802+00:00",
          "core_os": "windows",
          "created_at": "2019-11-01T06:31:32.519640+00:00",
          "error": null,
          "machine_id": "5dc677fd-6b47-7df9-f7f4-d45434c8d0f8"
      },
      "metadata": {
          "timestamp": "2020-01-08T15:16:34.303701"
      }
    }
    

### Download file

Download a file from a specific Endgame endpoint.

#### Parameters

Parameter Display Name | Type | Default Value | Description  
---|---|---|---  
Full File Path | String | N/A | If enabled, creates an Insight after successful execution of this action.  
Full Download Folder Path | String | N/A | Enter the path to the folder, where you want to store this file.  
Expected SHA-256 Hash | String | N/A | Enter the expected SHA-256 hash.  
  
#### Use cases

You can use this action to access the files from endpoints. Files should sometimes be processed manually, and this activity helps users to access the required files.

#### Run on

This action runs on the following entities:

  * Host
  * IP Address



#### Action results

##### Insights

If the endpoint was unisolated using the Endgame agent, then create an insight to indicate this.

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result

If status is `success`, the JSON result is as follows:
    
    
    {
      "data": {
          "status": "success",
          "doc_type": "collection",
          "endpoint": {
              "domain": "InstallerInitiated",
              "updated_at": "2019-11-01T05:41:10.150817+00:00",
              "id": "a3cdc174-3af0-400a-85c3-bbb1435a6b61",
              "display_operating_system": "Ubuntu 18.04.1",
              "hostname": "example",
              "mac_address": "01:23:45:ab:cd:ef",
              "base_image": false,
              "isolation_updated_at": null,
              "status": "monitored",
              "ad_distinguished_name": "",
              "ad_hostname": "",
              "tags": [
                  {
                      "id": "fc2dfcc8-9329-4f33-86a2-877bfb27575e",
                      "name": "CORE ENV"
                  }
              ],
              "isolation_request_status": null,
              "upgrade_status": "",
              "groups": [
                  {
                      "is_dynamic": false,
                      "count": 1,
                      "id": "e453d4f6-95c9-4dc5-bc41-2f4cae423e19",
                      "name": "Demo: Bad Admin"
                  }
              ],
              "sensors": [
                  {
                      "status": "A",
                      "sensor_version": "3.52.12",
                      "sensor_type": "hunt",
                      "id": "c7347a4b-3e71-5514-980f-90bdbab758cf"
                  }
              ],
              "ip_address": "192.0.2.1",
              "is_isolated": false,
              "operating_system": "Linux 4.15.0-29-generic",
              "name": "example",
              "status_changed_at": "2020-01-07T08:16:46.895105+00:00",
              "core_os": "linux",
              "created_at": "2019-03-19T04:25:06.953312+00:00",
              "error": null,
              "machine_id": "b389c979-2fb1-6a8c-63bc-5547b3c26d1d"
          },
          "task_id": "0854ae75-47ca-438a-8731-615defac44ac",
          "family": "response",
          "data": {
              "results": [
                  {
                      "size": 1731,
                      "endpoint": {
                          "status": "monitored",
                          "ad_distinguished_name": "",
                          "ad_hostname": "",
                          "operating_system": "Linux 4.15.0-29-generic",
                          "name": "example",
                          "display_operating_system": "Ubuntu 18.04.1",
                          "hostname": "example",
                          "updated_at": "2020-01-07T08:16:44Z",
                          "mac_address": "01:23:45:ab:cd:ef",
                          "ip_address": "192.0.2.1",
                          "id": "a3cdc174-3af0-400a-85c3-bbb1435a6b61"
                      },
                      "user_id": "5ed3c5d7-f450-489d-8b5f-9430b18da4c1",
                      "account_id": "c374bb8a-9a98-4823-b280-68e74c170a0e",
                      "investigation_id": null,
                      "filepath": "/home/a-arobinson/Downloads/bad_admin.sh",
                      "bulk_task_id": null,
                      "created_by": "a-arobinson",
                      "file_uuid": "4c45cc36-b6ca-412a-ae0b-ed214a9c7187",
                      "correlation_id": "13dfca7b-9e75-4115-be93-e6684dbfc7c8",
                      "user": {
                          "username": "admin",
                          "first_name": "Example",
                          "last_name": "User",
                          "id": "5ed3c5d7-f450-489d-8b5f-9430b18da4c1"
                      },
                      "chunk_size": 26214400,
                      "existing_path": "/home/a-arobinson/Downloads/bad_admin.sh",
                      "sha256": "8066b309db13bae560c15c35f42247a0f778786f0056d326ff3e6dffd1eac4f8",
                      "origination_task_id": "0854ae75-47ca-438a-8731-615defac44ac",
                      "md5": "6441b8f58feddb5a5f6fcd81c117ecb8"
                  }
              ]
          },
          "created_at": "2020-01-07T11:28:02.826397Z",
          "os_type": "linux",
          "machine_id": "b389c979-2fb1-6a8c-63bc-5547b3c26d1d",
          "type": "downloadFileResponse",
          "id": "d6fb3bf3-afea-44e0-8472-389f4e7e0002"
      },
      "metadata": {
          "count": 1,
          "previous_url": null,
          "timestamp": "2020-01-07T11:41:56.750788",
          "next": null,
          "per_page": 50,
          "next_url": null,
          "previous": null
      }
    }
    

If the status is `failure`, the JSON result is as follows:
    
    
    {
        "data": {
            "status": "failure",
            "doc_type": "collection",
            "endpoint": {
                "domain": "InstallerInitiated",
                "updated_at": "2019-11-01T05:42:09.150756+00:00",
                "id": "12c3530d-657f-4ccd-835e-6df9affeed3d",
                "display_operating_system": "Ubuntu 18.04.3",
                "hostname": "example",
                "mac_address": "01:23:45:ab:cd:ef",
                "base_image": false,
                "isolation_updated_at": null,
                "status": "monitored",
                "ad_distinguished_name": "",
                "ad_hostname": "",
                "tags": [],
                "isolation_request_status": null,
                "upgrade_status": "",
                "groups": [
                    {
                        "is_dynamic": false,
                        "count": 4,
                        "id": "c1af3cd6-2638-4144-842d-adc9cfb67fb9",
                        "name": "SOC"
                    }
                ],
                "sensors": [
                    {
                        "status": "A",
                        "sensor_version": "3.52.12",
                        "sensor_type": "hunt",
                        "id": "dc2e35cc-0c87-5a60-8fc8-de23ef747d02"
                    }
                ],
                "ip_address": "192.0.2.1",
                "is_isolated": false,
                "operating_system": "Linux 4.15.0-72-generic",
                "name": "example",
                "status_changed_at": "2020-01-19T11:05:16.765186+00:00",
                "core_os": "linux",
                "created_at": "2019-09-20T21:34:51.966863+00:00",
                "error": null,
                "machine_id": "5ae8ddd9-9339-ae4b-ccf7-5ed68f38b3a9"
            },
            "task_id": "85148460-c868-4fe5-a3e6-0d90784fadd1",
            "family": "response",
            "data": {
                "results": [
                    {
                        "endpoint": {
                            "status": "monitored",
                            "ad_distinguished_name": "",
                            "ad_hostname": "",
                            "operating_system": "Linux 4.15.0-72-generic",
                            "name": "example",
                            "display_operating_system": "Ubuntu 18.04.3",
                            "hostname": "example",
                            "updated_at": "2020-01-16T14:04:22Z",
                            "mac_address": "01:23:45:ab:cd:ef",
                            "ip_address": "192.0.2.1",
                            "id": "12c3530d-657f-4ccd-835e-6df9affeed3d"
                        },
                        "user_id": "5ed3c5d7-f450-489d-8b5f-9430b18da4c1",
                        "account_id": "c374bb8a-9a98-4823-b280-68e74c170a0e",
                        "investigation_id": null,
                        "expected_sha256": "123",
                        "bulk_task_id": null,
                        "correlation_id": "a7dc04c8-932c-4056-9477-8095b1fa15d8",
                        "user": {
                            "username": "admin",
                            "first_name": "Example",
                            "last_name": "User",
                            "id": "5ed3c5d7-f450-489d-8b5f-9430b18da4c1"
                        },
                        "chunk_size": 26214400,
                        "existing_path": "/home/example/Downloads/bad_admin.sh",
                        "origination_task_id": "85148460-c868-4fe5-a3e6-0d90784fadd1"
                    }
                ]
            },
            "created_at": "2020-01-19T12:19:57Z",
            "os_type": "linux",
            "machine_id": "5ae8ddd9-9339-ae4b-ccf7-5ed68f38b3a9",
            "type": "downloadFileResponse",
            "id": "8eb6b538-d480-4210-92fb-df08a3a4dfb9"
        },
        "metadata": {
            "count": 1,
            "previous_url": null,
            "timestamp": "2020-01-19T12:23:23.623961",
            "next": null,
            "per_page": 50,
            "next_url": null,
            "previous": null
        }
    }
    

### Delete file

Delete a file from an Endgame endpoint.

#### Parameters

Parameter Display Name | Type | Default Value | Description  
---|---|---|---  
File Path | String | N/A | Enter the path to the file.  
  
#### Use cases

This action is used to delete files from the endpoint. For example, it can be used when malware was found and an analyst wants to remove it.

#### Run on

This action runs on the following entities:

  * Host
  * IP Address



#### Action results

##### Insights

If the endpoint was unisolated using the Endgame agent, then create an insight to indicate this.

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result

(status = success)
    
    
    {
        "data": [
            {
                "status": "success",
                "doc_type": "collection",
                "endpoint": {
                    "domain": "InstallerInitiated",
                    "updated_at": "2019-11-01T05:41:10.150817+00:00",
                    "id": "a3cdc174-3af0-400a-85c3-bbb1435a6b61",
                    "display_operating_system": "Ubuntu 18.04.1",
                    "hostname": "08203s-lubu1804",
                    "mac_address": "01:23:45:ab:cd:ef",
                    "upgrade_status": "",
                    "base_image": false,
                    "isolation_updated_at": null,
                    "status": "monitored",
                    "ad_distinguished_name": "",
                    "ad_hostname": "",
                    "tags": [
                        {
                            "id": "fc2dfcc8-9329-4f33-86a2-877bfb27575e",
                            "name": "CORE ENV"
                        }
                    ],
                    "isolation_request_status": null,
                    "groups": [
                        {
                            "is_dynamic": false,
                            "count": 1,
                            "id": "e453d4f6-95c9-4dc5-bc41-2f4cae423e19",
                            "name": "Demo: Bad Admin"
                        }
                    ],
                    "sensors": [
                        {
                            "status": "monitored",
                            "sensor_version": "3.52.12",
                            "policy_status": "successful",
                            "policy_name": "Lab (Detect-Only with Streaming)",
                            "sensor_type": "hunt",
                            "id": "c7347a4b-3e71-5514-980f-90bdbab758cf",
                            "policy_id": "07b7a44f-25f3-4e5c-977b-2915de8160c5"
                        }
                    ],
                    "ip_address": "192.0.2.1",
                    "is_isolated": false,
                    "operating_system": "Linux 4.15.0-29-generic",
                    "name": "08203s-lubu1804",
                    "status_changed_at": "2020-01-20T07:25:02.633331+00:00",
                    "core_os": "linux",
                    "created_at": "2019-03-19T04:25:06.953312+00:00",
                    "error": null,
                    "machine_id": "b389c979-2fb1-6a8c-63bc-5547b3c26d1d"
                },
                "task_id": "bfb82b8d-71a0-4e5f-9cfe-bd573ea32b25",
                "family": "response",
                "created_at": "2020-01-20T07:31:37Z",
                "local_msg": "Success",
                "system_msg": null,
                "system_code": null,
                "local_code": 0,
                "os_type": "linux",
                "machine_id": "b389c979-2fb1-6a8c-63bc-5547b3c26d1d",
                "type": "deleteFileResponse",
                "id": "eb50fe9c-1059-42d4-9f5f-52e5af4ae64d"
            }
        ],
        "metadata": {
            "count": 1,
            "previous_url": null,
            "timestamp": "2020-01-20T07:32:04.425044",
            "next": null,
            "per_page": 50,
            "next_url": null,
            "previous": null
        }
    }
    

(status = failure) local_msg and system_msg will be used.
    
    
    {
      "data": [
          {
              "status": "failure",
              "doc_type": "collection",
              "endpoint": {
                  "domain": "InstallerInitiated",
                  "updated_at": "2019-11-01T05:41:10.150817+00:00",
                  "id": "a3cdc174-3af0-400a-85c3-bbb1435a6b61",
                  "display_operating_system": "Ubuntu 18.04.1",
                  "hostname": "08203s-lubu1804",
                  "mac_address": "01:23:45:ab:cd:ef",
                  "upgrade_status": "",
                  "base_image": false,
                  "isolation_updated_at": null,
                  "status": "monitored",
                  "ad_distinguished_name": "",
                  "ad_hostname": "",
                  "tags": [
                      {
                          "id": "fc2dfcc8-9329-4f33-86a2-877bfb27575e",
                          "name": "CORE ENV"
                      }
                  ],
                  "isolation_request_status": null,
                  "groups": [
                      {
                          "is_dynamic": false,
                          "count": 1,
                          "id": "e453d4f6-95c9-4dc5-bc41-2f4cae423e19",
                          "name": "Demo: Bad Admin"
                      }
                  ],
                  "sensors": [
                      {
                          "status": "monitored",
                          "sensor_version": "3.52.12",
                          "policy_status": "successful",
                          "policy_name": "Lab (Detect-Only with Streaming)",
                          "sensor_type": "hunt",
                          "id": "c7347a4b-3e71-5514-980f-90bdbab758cf",
                          "policy_id": "07b7a44f-25f3-4e5c-977b-2915de8160c5"
                      }
                  ],
                  "ip_address": "192.0.2.1",
                  "is_isolated": false,
                  "operating_system": "Linux 4.15.0-29-generic",
                  "name": "08203s-lubu1804",
                  "status_changed_at": "2020-01-07T08:16:46.895105+00:00",
                  "core_os": "linux",
                  "created_at": "2019-03-19T04:25:06.953312+00:00",
                  "error": null,
                  "machine_id": "b389c979-2fb1-6a8c-63bc-5547b3c26d1d"
              },
              "task_id": "5da277fe-503d-468a-822b-8801d9671cde",
              "family": "response",
              "created_at": "2020-01-07T13:10:50Z",
              "local_msg": "Not found",
              "system_msg": null,
              "system_code": null,
              "local_code": -7,
              "os_type": "linux",
              "machine_id": "b389c979-2fb1-6a8c-63bc-5547b3c26d1d",
              "type": "deleteFileResponse",
              "id": "6f3e6148-6801-4cb8-8a5d-25f75ea93555"
          }
      ],
      "metadata": {
          "count": 1,
          "previous_url": null,
          "timestamp": "2020-01-07T13:16:18.834163",
          "next": null,
          "per_page": 5,
          "next_url": null,
          "previous": null
      }
    }
    

### Drivers Survey (Windows only)

Get the information on drivers from a specific Endgame endpoint.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Max Items to Return | String | 50 | Specify how many items to return.  
  
#### Run on

This action runs on the following entities:

  * Hostname
  * IP Address



#### Action results

##### Entity enrichment

Enrichment Field Name | Logic-When to apply  
---|---  
driver_basename | Returns if it exists in JSON result  
driver_filename | Returns if it exists in JSON result  
date_modified | Returns if it exists in JSON result  
driver_file_version | Returns if it exists in JSON result  
driver_load_address | Returns if it exists in JSON result  
collection_id | Returns if it exists in JSON result  
hashes | Returns if it exists in JSON result  
machine_id | Returns if it exists in JSON result  
driver_product_version | Returns if it exists in JSON result  
driver_description | Returns if it exists in JSON result  
  
##### Script result

Script Result Name | **Value options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [{
       "EntityResult":
          [{ "driver_basename": "test.exe",
             "driver_filename": "C:\\\\Windows\\\\system32\\\\test.exe",
             "date_modified": 1446189483.0185645,
             "driver_file_version": "10.0.10586.0 (th2_release.151029-1700)",
             "driver_load_address": "12345678",
             "collection_id": "a9925cf1-6d4c-4bea-b13d-12345678",
             "hashes": {
                         "sha256": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
                         "md5": "098f6bcd4621d373cade4e832627b4f6",
                         "sha1": "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3"
                        },
            "machine_id": "5dc677fd-6b47-7df9-f7f4-12345678",
            "driver_product_version": "10.0.10586.0",
            "driver_description": "Test"
          }],
       "Entity": "PC-01"
     }]
    

### Firewall Survey (Windows only)

Get information about the firewall rules on a specific Endgame endpoint.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Max Items to Return | String | 50 | Specify how many items to return.  
  
#### Run on

This action runs on the following entities:

  * Hostname
  * IP Address



#### Action results

##### Entity enrichment

Enrichment Field Name | Logic-When to apply  
---|---  
direction | Returns if it exists in JSON result  
machine_id | Returns if it exists in JSON result  
description | Returns if it exists in JSON result  
remote_addresses | Returns if it exists in JSON result  
protocol_number | Returns if it exists in JSON result  
enabled | Returns if it exists in JSON result  
edge_traversal | Returns if it exists in JSON result  
profiles | Returns if it exists in JSON result  
interface_types | Returns if it exists in JSON result  
rule_name | Returns if it exists in JSON result  
icmp_and_type_codes | Returns if it exists in JSON result  
local_addresses | Returns if it exists in JSON result  
application_name | Returns if it exists in JSON result  
collection_id | Returns if it exists in JSON result  
remote_ports | Returns if it exists in JSON result  
action | Returns if it exists in JSON result  
local_ports | Returns if it exists in JSON result  
  
##### Script result

Script Result Name | **Value options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [{
       "EntityResult":
          [{
             "direction": "in",
             "machine_id": "870499c3-d6bf-8edd-972d-12345678",
             "description": "Inbound rule for Google Chrome to allow mDNS traffic.",
             "remote_addresses": "*",
             "protocol_number": 17,
             "enabled": true,
             "edge_traversal": false,
             "profiles":
                 ["domain", "public", "private"],
             "interface_types": "All",
             "rule_name": "Google Chrome (mDNS-In)",
             "icmp_and_type_codes": "",
             "local_addresses": "*",
             "application_name": "C:\\\\Program Files (x86)\\\\Google\\\\Chrome\\\\Application\\\\chrome.exe",
             "collection_id": "0925eea5-c61f-464a-ba61-12345678",
             "remote_ports": "*",
             "action": "allow",
             "local_ports": "1234"
          }],
       "Entity": "PC-01"
    }]
    

### Get Endpoints

List all endpoints.

#### Parameters

N/A

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script Result Name | **Value options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [{
       "domain": "",
       "updated_at": "2019-05-30T01:40:21.126499+00:00",
       "id": "db33d864-7d58-4d85-9d2d-1a98a101995d",
       "display_operating_system": "Windows 7 (SP1)",
       "hostname": "ip-AC170169",
       "mac_address": "01:23:45:ab:cd:ef",
       "isolation_updated_at": "",
       "status": "monitored",
       "ad_distinguished_name": "",
       "ad_hostname": "",
       "tags": [],
       "isolation_request_status": "",
       "alert_count": 72,
       "investigation_count": 0,
       "groups": [],
       "sensors":
          [{
             "status": "monitored",
             "sensor_version": "3.51.10",
             "policy_status": "successful",
             "policy_name": "POC-Lab",
             "sensor_type": "hunt",
             "id": "ec17f7bb-1d63-536a-b694-ca066cc2572e",
             "policy_id": "d31f0192-b8e2-49ae-ae54-041376183b7f"
          }],
       "ip_address": "192.0.2.1",
       "is_isolated": "false",
       "operating_system": "Windows 6.1 Service Pack 1",
       "name": "ip-AC170169",
       "status_changed_at": "2019-05-30T01:40:18.200770+00:00",
       "core_os": "windows",
       "created_at": "2019-05-30T01:36:43.761600+00:00",
       "error":
         [{
            "msg": "Installer failure - Execution failed for (http://192.0.2.1:5985/wsman)\\n",
           "deployment_id": "90C2BAA6-B38B-4037-9A9E-7C8628E8D7D6",
           "code": 1001, "ts": 1559180421.125456
         }],
       "machine_id": "4f1adabb-17c4-e39e-caa7-7900562d0b51"
    }]
    

### Hunt File

Searches for running files.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Endpoints Core OS | String | windows | Select an operating system (for example, Windows, Linux, or Mac) to filter the Endpoints list. Note: You can only create a single investigation for endpoints that run on the same operating system.  
MD5 Hashes | String | N/A | ADVANCED CONFIGURATION for this hunt. Enter MD5 Hashes, separated by comma.   
SHA1 Hashes | String | N/A | ADVANCED CONFIGURATION for this hunt. Enter SHA-1 Hashes, separated by comma.   
SHA256 Hashes | String | N/A | ADVANCED CONFIGURATION for this hunt. Enter SHA256 Hashes, separated by comma.   
Directory | String | N/A | The starting directory path Example C:\windows\system32  
Find File | String | N/A | Enter the filename(s) to search. Enter a regular expression to narrow search results.  
  
#### Run on

This action runs on the following entities:

  * Hostname
  * IP Address



#### Action results

##### Entity enrichment

Enrichment Field Name | Logic-When to apply  
---|---  
meta_data | Returns if it exists in JSON result  
file_path | Returns if it exists in JSON result  
  
##### Script result

Script Result Name | **Value options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [{
          "meta_data":
              {  "hashes":
                    {  "sha256": "4705ba6793dc93c1bbe2a9e790e9e22778d217531b1750471206fd5c52bbd2b5",
                       "md5": "6383522c180badc4e1d5c30a5c4f4913",
                       "sha1": "62a30e96459b694f7b22d730c460a65cd2ebaaca"
                     },
                 "file_name_timestamps":
                    {  "accessed": 1468675289.0711532,
                       "entry_modified": 0,
                       "modified": 1468675289.0711532,
                       "created": 1468675404.0330572
                     },
                 "file_attributes": 38,
                 "file_size": 174
               },
          "file_path": "C:\\\\Program Files\\\\desktop.ini"
        },
      {
         "meta_data":
              {  "hashes":
                    {  "sha256": "44fe5eebd80e46f903d68c07bcf06d187a3698bf3953bc58bb578465e2e0fe6c",
                       "md5": "6bd5fb46283aa48e638bef47510c47da",
                       "sha1": "c38d46ec6c9bc8baece4a459b617f44d10af973c"
                     },
                 "file_name_timestamps":
                    {
                       "accessed": 1468675289.0024028,
                       "entry_modified": 0,
                       "modified": 1468675289.0024028,
                       "created": 1468675404.0111823
                     },
                "file_attributes": 38,
                "file_size": 645
               },
        "file_path": "C:\\\\Program Files\\\\Common Files\\\\microsoft shared\\\\Stationery\\\\Desktop.ini"
    }]
    

### Hunt IP

Searches for network connections.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Endpoints Core OS | String | windows | Select an operating system (for example, Windows, Linux, or Mac) to filter the Endpoints list. Note: You can only create a single investigation for endpoints that run on the same operating system.  
Remote IP Address | String | N/A | remote IP address - separated by comma  
Local IP Address | String | N/A | separated by comma  
State | String | N/A | Enter state to return. Example: ANY  
Protocol | String | N/A | Example: ANY, UDP, TCP  
Network Port | String | N/A | N/A  
Network Remote | String | N/A | Network Remote or Local.  
  
#### Run on

This action runs on the following entities:

  * Hostname
  * IP Address



#### Action results

##### Entity enrichment

Enrichment Field Name | Logic-When to apply  
---|---  
parent_name | Returns if it exists in JSON result  
domain | Returns if it exists in JSON result  
exe | Returns if it exists in JSON result  
name | Returns if it exists in JSON result  
has_unbacked_execute_memory | Returns if it exists in JSON result  
pid | Returns if it exists in JSON result  
up_time | Returns if it exists in JSON result  
is_sensor | Returns if it exists in JSON result  
cmdline | Returns if it exists in JSON result  
parent_exe | Returns if it exists in JSON result  
unbacked_execute_byte_count | Returns if it exists in JSON result  
create_time | Returns if it exists in JSON result  
user | Returns if it exists in JSON result  
sid | Returns if it exists in JSON result  
threads | Returns if it exists in JSON result  
ppid | Returns if it exists in JSON result  
unbacked_execute_region_count | Returns if it exists in JSON result  
  
##### Script result

Script Result Name | **Value options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [{
       "parent_name": "System Idle Process",
       "domain": "NT AUTHORITY",
       "exe": "",
       "name": "System",
       "has_unbacked_execute_memory": false,
       "pid": 4,
       "up_time": 2384701,
       "is_sensor": false,
       "cmdline": "",
       "parent_exe": "",
       "unbacked_execute_byte_count": 0,
       "create_time": 1559179903,
       "user": "SYSTEM",
       "sid": "S-1-5-18",
       "threads":
         [{
            "thread_id": 8
          }, {
           "thread_id": 12,
           "up_time": 13206038203,
           "create_time": -11644473599
         }, {
           "thread_id": 16,
           "up_time": 13206038203,
           "create_time": -11644473599
          }],
       "ppid": 0,
       "unbacked_execute_region_count": 0
    }]​
    

### Hunt Process

Searches for running processes.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Endpoints Core OS | String | windows | Select an operating system (i.e., Windows, Linux, or Mac) to filter the Endpoints list. Note: You can only create a single investigation for endpoints that run on the same operating system.  
MD5 Hashes | String | N/A | ADVANCED CONFIGURATION for this hunt. Enter MD5 Hashes, separated by comma.  
SHA1 Hashes | String | N/A | ADVANCED CONFIGURATION for this hunt. Enter SHA-1 Hashes, separated by comma.  
SHA256 Hashes | String | N/A | ADVANCED CONFIGURATION for this hunt. Enter SHA256 Hashes, separated by comma.  
Process Name | String | N/A | ADVANCED CONFIGURATION for this hunt. Enter Process Name ex. iss.exe*  
  
#### Run on

This action runs on the following entities:

  * Hostname
  * IP Address



#### Action results

##### Entity enrichment

Enrichment Field Name | Logic-When to apply  
---|---  
parent_name | Returns if it exists in JSON result  
domain | Returns if it exists in JSON result  
exe | Returns if it exists in JSON result  
name | Returns if it exists in JSON result  
has_unbacked_execute_memory | Returns if it exists in JSON result  
pid | Returns if it exists in JSON result  
up_time | Returns if it exists in JSON result  
is_sensor | Returns if it exists in JSON result  
cmdline | Returns if it exists in JSON result  
parent_exe | Returns if it exists in JSON result  
unbacked_execute_byte_count | Returns if it exists in JSON result  
create_time | Returns if it exists in JSON result  
user | Returns if it exists in JSON result  
sid | Returns if it exists in JSON result  
threads | Returns if it exists in JSON result  
ppid | Returns if it exists in JSON result  
unbacked_execute_region_count | Returns if it exists in JSON result  
  
##### Script result

Script Result Name | **Value options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [{
       "parent_name": "System Idle Process",
       "domain": "NT AUTHORITY",
       "exe": "",
       "name": "System",
       "has_unbacked_execute_memory": false,
       "pid": 4,
       "up_time": 2384701,
       "is_sensor": false,
       "cmdline": "",
       "parent_exe": "",
       "unbacked_execute_byte_count": 0,
       "create_time": 1559179903,
       "user": "SYSTEM",
       "sid": "S-1-5-18",
       "threads":
          [{
             "thread_id": 8
           },{
             "thread_id": 12,
             "up_time": 13206038203,
             "create_time": -11644473599
           },{
            "thread_id": 16,
            "up_time": 13206038203,
            "create_time": -11644473599
          }],
       "ppid": 0,
       "unbacked_execute_region_count": 0
    }]
    

### Hunt Registry

Searches for a registry key or value name.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Hive | String | ALL | One of the following: HKEY_CLASSES_ROOT, HKEY_CURRENT_CONFIG, HKEY_USERS, HKEY_LOCAL_MACHINE, ALL.  
Keys | String | N/A | Registry Key or Value Name.  
Min Size | String | N/A | Min byte size.  
Max Size | String | N/A | Max byte size.  
Endpoints Core OS | String | windows | Select an operating system (i.e., Windows, Linux, or Mac) to filter the Endpoints list. Note: You can only create a single investigation for endpoints that run on the same operating system.  
  
#### Run on

This action runs on the following entities:

  * Hostname
  * IP Address



#### Action results

##### Entity enrichment

Enrichment Field Name | Logic-When to apply  
---|---  
parent_name | Returns if it exists in JSON result  
domain | Returns if it exists in JSON result  
exe | Returns if it exists in JSON result  
name | Returns if it exists in JSON result  
up_time | Returns if it exists in JSON result  
is_sensor | Returns if it exists in JSON result  
cmdline | Returns if it exists in JSON result  
parent_exe | Returns if it exists in JSON result  
unbacked_execute_byte_count | Returns if it exists in JSON result  
create_time | Returns if it exists in JSON result  
user | Returns if it exists in JSON result  
sid | Returns if it exists in JSON result  
threads | Returns if it exists in JSON result  
ppid | Returns if it exists in JSON result  
unbacked_execute_region_count | Returns if it exists in JSON result  
  
##### Script result

Script Result Name | **Value options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [{
       "parent_name": "System Idle Process",
       "domain": "NT AUTHORITY",
       "exe": "",
       "name": "System",
       "has_unbacked_execute_memory": false,
       "pid": 4,
       "up_time": 2384701,
       "is_sensor": false,
       "cmdline": "",
       "parent_exe": "",
       "unbacked_execute_byte_count": 0,
       "create_time": 1559179903,
       "user": "SYSTEM",
       "sid": "S-1-5-18",
       "threads":
          [{
              "thread_id": 8
            },{
              "thread_id": 12,
              "up_time": 13206038203,
              "create_time": -11644473599
            }, {
              "thread_id": 16,
              "up_time": 13206038203,
              "create_time": -11644473599
             }],
       "ppid": 0,
       "unbacked_execute_region_count": 0
    }]
    

### Hunt User

Searches the network for logged in users.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Endpoints Core OS | String | windows | Select an operating system (i.e., Windows, Linux, or Mac) to filter the Endpoints list. Note: You can only create a single investigation for endpoints that run on the same operating system.  
Find Username | String | N/A | ADVANCED CONFIGURATION for this hunt. Enter username(s), separate multiple entries with a semicolon.  
Domain Name | String | N/A | ADVANCED CONFIGURATION for this hunt. Enter Domain Name.  
  
#### Run on

This action runs on the following entities:

  * Hostname
  * IP Address



#### Action results

##### Entity enrichment

Enrichment Field Name | Logic-When to apply  
---|---  
parent_name | Returns if it exists in JSON result  
domain | Returns if it exists in JSON result  
exe | Returns if it exists in JSON result  
name | Returns if it exists in JSON result  
has_unbacked_execute_memory | Returns if it exists in JSON result  
pid | Returns if it exists in JSON result  
up_time | Returns if it exists in JSON result  
is_sensor | Returns if it exists in JSON result  
cmdline | Returns if it exists in JSON result  
parent_exe | Returns if it exists in JSON result  
unbacked_execute_byte_count | Returns if it exists in JSON result  
create_time | Returns if it exists in JSON result  
user | Returns if it exists in JSON result  
sid | Returns if it exists in JSON result  
threads | Returns if it exists in JSON result  
ppid | Returns if it exists in JSON result  
unbacked_execute_region_count | Returns if it exists in JSON result  
  
##### Script result

Script Result Name | **Value options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [{
       "parent_name": "System Idle Process",
       "domain": "NT AUTHORITY",
       "exe": "",
       "name": "System",
       "has_unbacked_execute_memory": false,
       "pid": 4,
       "up_time": 2384701,
       "is_sensor": false,
       "Cmdline":"",
       "parent_exe": "",
       "unbacked_execute_byte_count": 0,
       "create_time": 1559179903,
       "user": "SYSTEM",
       "sid": "S-1-5-18",
       "threads":
         [{
            "thread_id": 8
          }, {
           "thread_id": 12,
           "up_time": 13206038203,
           "create_time": -11644473599
         }, {
           "thread_id": 16,
           "up_time": 13206038203,
           "create_time": -11644473599
        }],
      "ppid": 0,
      "unbacked_execute_region_count": 0
    }]
    

### Kill Process

Kill a process in a specific Endgame endpoint.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Process Name | String | N/A | Enter the process name  
PID | String | N/A | Enter ID of the process.  
  
#### Run on

This action runs on the following entities:

  * Hostname
  * IP Address



#### Action results

##### Script result

Script Result Name | **Value options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### Network Survey

Get information about connections, DNS cache, NetBIOS, ARP, and Route tables from a specific Endgame endpoint.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Max Items to Return | String | 50 | Specify how many autoruns to return.  
Include Route Entries Information | Checkbox | Checked | Specify to get information about the Route Entries.  
Include Net Bios Information | Checkbox | Checked | Specify to get information about Net Bios.  
Include DNS Cache Information | Checkbox | Checked | Specify to get information about the DNS Cache.  
Include ARP Table Information | Checkbox | Checked | Specify to get information about the ARP table.  
  
#### Run on

This action runs on the following entities:

  * Hostname
  * IP Address



#### Action results

##### Entity enrichment

Enrichment Field Name | Logic-When to apply  
---|---  
connections | Returns if it exists in JSON result  
netbios_info | Returns if it exists in JSON result  
arp_table | Returns if it exists in JSON result  
route_table | Returns if it exists in JSON result  
dns_cache | Returns if it exists in JSON result  
  
##### Script result

Script Result Name | **Value options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [{
      "EntityResult":
       {
        "connections":
          [{
           "connection_type": "SOCK_STREAM",
           "collection_id": "50e74bd2-1cd4-412c-a7fc-24cf1456e883",
           "exe": "C:\\\\Windows\\\\System32\\\\test.exe",
           "connection_status": "LISTEN",
           "name": "test.exe",
           "family": "ipv4",
           "local_port": 111,
           "remote_port": 0,
           "pid": 700,
           "remote_address": "0.0.0.0",
           "create_time": 1583314664,
           "connection_timestamp": 1583314664.0117714,
           "local_address": "0.0.0.0",
           "protocol": "tcp",
           "hashes":
              {
                "sha256": "5d00bbeb147e0c838a622fc42c543b2913d57eaca4e69d9a37ed61e98c819347", "md5": "8497852ed44aff902d502015792d315d",
                "sha1": "800a4c2e524fc392c45748eae1691fa01d24ea4c"
               },
           "machine_id": "5dc677fd-6b47-7df9-f7f4-d45434c8d0f8"
         }],
       "netbios_info":
         [{
           "comment": "",
           "name": "PC-01",
           "version_major": 10,
           "netbios_neighbor_type": 8392747,
           "platform": "WINDOWS NT",
           "version_minor": 0
         }],
       "arp_table":
         [{
           "connection_type": "SOCK_STREAM",
           "collection_id": "50e74bd2-1cd4-412c-a7fc-24cf1456e883",
           "exe": "C:\\\\Windows\\\\System32\\\\test.exe",
           "connection_status": "LISTEN",
           "name": "test.exe",
           "family": "ipv4",
           "local_port": 111,
           "remote_port": 0,
           "pid": 700,
           "remote_address": "0.0.0.0",
           "create_time": 1583314664,
           "connection_timestamp": 1583314664.0117714,
           "local_address": "0.0.0.0",
           "protocol": "tcp",
           "hashes": {"sha256": "5d00bbeb147e0c838a622fc42c543b2913d57eaca4e69d9a37ed61e98c819347", "md5": "8497852ed44aff902d502015792d315d",
                     "sha1": "800a4c2e524fc392c45748eae1691fa01d24ea4c"},
           "machine_id": "5dc677fd-6b47-7df9-f7f4-d45434c8d0f8"
         }],
       "route_table":
         [{
           "machine_id": "5dc677fd-6b47-7df9-f7f4-d45434c8d0f8",
           "family": "ipv4",
           "destination": "0.0.0.0",
           "netmask": "0.0.0.0",
           "collection_id": "50e74bd2-1cd4-412c-a7fc-24cf1456e883",
           "interface_name": "Ethernet0",
           "gateway": "1.1.1.1"
         }],
       "dns_cache":
         [{
           "name": "test.ms",
           "dns_record_type": "A",
           "ttl": 0,
           "collection_id": "50e74bd2-1cd4-412c-a7fc-24cf1456e883",
           "machine_id": "5dc677fd-6b47-7df9-f7f4-d45434c8d0f8",
           "query_error": 9701
          }]
        },
      "Entity": "PC-01"
    }]
    

### Ping

Test connectivity to the Endgame server.

#### Parameters

N/A

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script Result Name | **Value options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### Process Survey

Get information about running processes on a specific Endgame endpoint.

#### Parameters

Parameter | Type | Default Vaule | Description  
---|---|---|---  
Max Items to Return | String | 50 | Specify how many items to return.  
Detect Fileless Attacks (Windows Only) | Checkbox | Unchecked | Specify to detect fileless attacks. Windows Only.  
Detect Malware With MalwareScore (Windows Only) | Checkbox | Unchecked | Specify to detect malware processes with MalwareScore. Windows Only.  
Collect Process Threads | Checkbox | Unchecked | Specify to include information about the amount of process threads in the response.  
Return Only Suspicious Processes | Checkbox | Checked | Specify to return only suspicious processes from the endpoint. By the Endgame definition: Suspicious processes are unbacked executable processes.  
  
#### Run on

This action runs on the following entities:

  * Hostname
  * IP Address



#### Action results

##### Entity enrichment

Enrichment Field Name | Logic-When to apply  
---|---  
domain | Returns if it exists in JSON result  
name_suspicious | Returns if it exists in JSON result  
pid | Returns if it exists in JSON result  
name_uncommon_path | Returns if it exists in JSON result  
repeat_offender | Returns if it exists in JSON result  
cmdline | Returns if it exists in JSON result  
create_time | Returns if it exists in JSON result  
parent_name | Returns if it exists in JSON result  
has_unbacked_execute_memory | Returns if it exists in JSON result  
sid | Returns if it exists in JSON result  
ppid | Returns if it exists in JSON result  
up_time | Returns if it exists in JSON result  
unbacked_execute_region_count | Returns if it exists in JSON result  
is_sensor | Returns if it exists in JSON result  
threads | Returns if it exists in JSON result  
user | Returns if it exists in JSON result  
collection_id | Returns if it exists in JSON result  
parent_exe | Returns if it exists in JSON result  
exe | Returns if it exists in JSON result  
name | Returns if it exists in JSON result  
unbacked_execute_byte_count | Returns if it exists in JSON result  
machine_id | Returns if it exists in JSON result  
unbacked_execute_region_count | Returns if it exists in JSON result  
tty_device_minor_number | Returns if it exists in JSON result  
uid | Returns if it exists in JSON result  
name_suspicious | Returns if it exists in JSON result  
phys_memory_bytes | Returns if it exists in JSON result  
pid | Returns if it exists in JSON result  
env_variables | Returns if it exists in JSON result  
repeat_offender | Returns if it exists in JSON result  
cmdline | Returns if it exists in JSON result  
create_time | Returns if it exists in JSON result  
tty_device_major_number | Returns if it exists in JSON result  
parent_name | Returns if it exists in JSON result  
group | Returns if it exists in JSON result  
cpu_percent | Returns if it exists in JSON result  
has_unbacked_execute_memory | Returns if it exists in JSON result  
gid | Returns if it exists in JSON result  
sha256 | Returns if it exists in JSON result  
cwd | Returns if it exists in JSON result  
exe | Returns if it exists in JSON result  
up_time | Returns if it exists in JSON result  
short_name | Returns if it exists in JSON result  
tty_device_name | Returns if it exists in JSON result  
is_sensor | Returns if it exists in JSON result  
sha1 | Returns if it exists in JSON result  
threads | Returns if it exists in JSON result  
name_uncommon_path | Returns if it exists in JSON result  
collection_id | Returns if it exists in JSON result  
md5 | Returns if it exists in JSON result  
argv_list | Returns if it exists in JSON result  
num_threads | Returns if it exists in JSON result  
user | Returns if it exists in JSON result  
virt_memory_bytes | Returns if it exists in JSON result  
name | Returns if it exists in JSON result  
session_id | Returns if it exists in JSON result  
memory_percent | Returns if it exists in JSON result  
machine_id | Returns if it exists in JSON result  
unbacked_execute_byte_count | Returns if it exists in JSON result  
  
##### Script result

Script Result Name | **Value options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [{
      "EntityResult":
       [{
          "domain": "NT AUTHORITY",
          "name_suspicious": false,
          "pid": 4,
          "name_uncommon_path": false,
          "repeat_offender": false,
          "cmdline": "",
          "create_time": 1583314654,
          "parent_name": "System Idle Process",
          "has_unbacked_execute_memory": false,
          "sid": "S-1-5-18",
          "ppid": 0,
         "up_time": 342643,
         "unbacked_execute_region_count": 0,
         "is_sensor": false,
         "threads":
          [{  "thread_id": 12,
              "up_time": 13228130896,
              "create_time": -11644473599
           },
           {
              "thread_id": 16,
              "up_time": 13228130896,
              "create_time": -11644473599
           }],
         "user": "SYSTEM",
         "collection_id": "ac1fb296-db5a-4426-b32e-292e4a50188d",
         "parent_exe": "",
         "exe": "",
         "name": "System",
         "unbacked_execute_byte_count": 0,
         "machine_id": "5dc677fd-6b47-7df9-f7f4-d45434c8d0f8"
        }],
      "Entity": "PC-01"
     },
    {
      "EntityResult":
       [{
         "unbacked_execute_region_count": 0,
         "tty_device_minor_number": 0,
         "uid": 0,
         "name_suspicious": false,
         "phys_memory_bytes": 8900608,
         "pid": 1,
         "env_variables":
           [  "HOME=/",
              "init=/sbin/init",
              "NETWORK_SKIP_ENSLAVED=",
              "recovery=",
              "TERM=linux",
              "drop_caps=",
              "BOOT_IMAGE=/vmlinuz-4.15.0-88-generic",
              "PATH=/sbin:/usr/sbin:/bin:/usr/bin",
              "PWD=/", "rootmnt=/root"  ],
        "repeat_offender": false,
        "cmdline": "/sbin/init maybe-ubiquity",
        "create_time": 1583632302,
        "tty_device_major_number": 0,
        "parent_name": "",
        "group": "root",
        "cpu_percent": 0,
        "has_unbacked_execute_memory": false,
        "gid": 0,
        "sha256": "3a14ff4b18505543eda4dccb054aa5860478a95ed0cac76da392f3472da3ad67",
        "cwd": "/",
        "exe": "/lib/systemd/systemd",
        "up_time": 24942,
        "short_name": "systemd",
        "tty_device_name": "",
        "is_sensor": false,
        "sha1": "e016f80b87101a74b52d15ce2726560a6e128b60",
        "threads": [{"thread_id": 1}],
        "name_uncommon_path": false,
        "collection_id": "bcb6b33a-0ffb-4e72-818a-1731024dfd79",
        "md5": "ca563cf817f03ed7d01a6462818a5791",
        "argv_list": ["/sbin/init", "maybe-ubiquity"],
        "num_threads": 1,
        "ppid": 0,
        "virt_memory_bytes": 79818752,
        "name": "systemd",
        "session_id": 1,
        "memory_percent": 0.21517109870910645,
        "parent_exe": "",
        "unbacked_execute_byte_count": 0,
        "machine_id": "5ae8ddd9-9339-ae4b-ccf7-5ed68f38b3a9",
        "user": "root"
      }],
     "Entity": "PC-202"
    }]
    

### Removable Media Survey (Windows only)

DGet information about removable media from a specific Endgame endpoint.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Max Items to Return | String | 50 | Specify how many items to return.  
  
#### Run on

This action runs on the following entities:

  * Hostname
  * IP Address



#### Action results

##### Entity enrichment

Enrichment Field Name | Logic-When to apply  
---|---  
name | Returns if it exists in JSON result  
is_storage_device | Returns if it exists in JSON result  
vendor_id | Returns if it exists in JSON result  
collection_id | Returns if it exists in JSON result  
last_connect_time | Returns if it exists in JSON result  
serial_number | Returns if it exists in JSON result  
machine_id | Returns if it exists in JSON result  
is_connected | Returns if it exists in JSON result  
product_id | Returns if it exists in JSON result  
  
##### Script result

Script Result Name | **Value options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [{
       "EntityResult":
        [{  "name": "USB Composite Device",
            "is_storage_device": false,
            "vendor_id": "0E0F",
            "collection_id": "fbe61b16-e6b2-4595-8409-abf4ce15fa85",
            "last_connect_time": 1552596043.0610971,
            "serial_number": "6&35D1F50B&0&1",
            "machine_id": "a4c05d5a-7ebc-c3ab-1beb-f1fe517768d8",
            "is_connected": false,
            "product_id": "0003"
         }],
       "Entity": "PC-01"
    }]
    

### Software Survey (Windows only)

Get information about an installed software on a specific Endgame endpoint.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Max Items to Return | String | 50 | Specify how many items to return.  
  
#### Run on

This action runs on the following entities:

  * Hostname
  * IP Address



#### Action results

##### Entity enrichment

Enrichment Field Name | Logic-When to apply  
---|---  
publisher | Returns if it exists in JSON result  
machine_id | Returns if it exists in JSON result  
package | Returns if it exists in JSON result  
install_date | Returns if it exists in JSON result  
version | Returns if it exists in JSON result  
collection_id | Returns if it exists in JSON result  
installed_for | Returns if it exists in JSON result  
  
##### Script result

Script Result Name | **Value options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [{
     "EntityResult":
       [{
          "publisher": "John Doe",
          "machine_id": "5dc677fd-6b47-7df9-f7f4-d45434c8d0f8",
          "package": "Test",
          "install_date": "20191008",
          "version": "18.06",
          "collection_id": "fc079e17-8a2e-40d9-94c9-b974e5534e58",
          "installed_for": "allUsers"
       }],
     "Entity": "PC-01"
    }]
    

### System Survey

Get system information on a single endgame endpoint, such as memory use, dns, and OS.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Max Items to Return | String | 50 | Specify how many items to return.  
Include Security Product Information (Windows only) | Checkbox | Checked | Specify to get information about the security products installed on the endpoint (Windows only).  
Include Patch Information (Windows only) | Checkbox | Checked | Specify to get information about patches (Windows only).  
Include Disk Information | Checkbox | Checked | Specify to get information about Disks.  
Include Network Interface Information | Checkbox | Checked | Specify to get information about network interfaces.  
  
#### Run on

This action runs on the following entities:

  * Hostname
  * IP Address



#### Action results

##### Entity enrichment

Enrichment Field Name | Logic-When to apply  
---|---  
patches_info | Returns if it exists in JSON result  
Disks_info | Returns if it exists in JSON result  
network_interfaces | Returns if it exists in JSON result  
Os_info | Returns if it exists in JSON result  
installed_security_products | Returns if it exists in JSON result  
  
##### Script result

Script Result Name | **Value options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [{
      "EntityResult":
       {
         "patches_info":
          [{
            "collection_id": "f7d a62bb-318d-40c1-a490-85979c0c9ede",
            "installed_on": "2/3/2018",
            "hotfix_id": "KB4049065",
            "machine_id": "870499c3-d6bf-8edd-972d-f2f6621dd971"
          }],
         "Disks_info":
          [{
            "disk_id": "\\\\Device\\\\HarddiskVolume2",
            "fstype": "NTFS",
            "disk_total": 15579738112,
            "disk_free": 1219571712,
            "collection_id": "a27ebace-32ec-4257-ab4f-7da49f02a9d4",
            "device": "\\\\Device\\\\HarddiskVolume2",
            "path": "C:\\\\",
            "machine_id": "5dc677fd-6b47-7df9-f7f4-d45434c8d0f8"
          }],
         "network_interfaces":
           [{
            "machine_id": "5dc677fd-6b47-7df9-f7f4-d45434c8d0f8",
            "mac_address": "01:23:45:ab:cd:ef",
            "ipv4_addresses": ["1.1.1.1"],
            "ipv6_addresses": ["1111::1111:1111:1111:1111"],
            "collection_id": "a27ebace-32ec-4257-ab4f-7da49f02a9d4",
            "smp_interface": true,
            "interface_name": "Ethernet0"
           }],
        "Os_info":
          [{
            "memory":
              {  "ram_free": 1240039424,
                 "page_percent_used": 36.89334358507761,
                 "page_total": 2818101248,
                 "ram_percent_used": 42.24349594504104,
                 "ram_total": 2147012608,
                 "ram_used": 906973184,
                 "page_used": 1039691776,
                 "page_free": 1778409472
              },
            "doc_type": "collection",
            "domain": "PC-01.test.com",
            "endpoint":
              {  "status": "unmonitored",
                 "ad_distinguished_name":
                 "CN=PC_01,OU=TESTOU,OU=Organization,DC=test,DC=com",
                 "ad_hostname": "test.com",
                 "operating_system": "Windows 10.0 ",
                 "name": "PC-01",
                 "display_operating_system": "Windows 10 (v1511)",
                 "hostname": "PC-01",
                 "updated_at": "2020-03-08T08:27:22.919880+00:00",
                 "mac_address": "01:23:45:ab:cd:ef",
                 "machine_id": "5dc677fd-6b47-7df9-f7f4-d45434c8d0f8",
                 "ip_address": "1.1.1.1",
                 "id": "b23c8a14-69e0-4966-b78a-c9fba4fdd934"
              },
           "investigation_id": "85cff906-8b39-4a37-aa05-84950c9b2a02",
           "hostname": "PC-01",
           "bulk_task_id": null,
           "original_machine_id": "5dc677fd-6b47-7df9-f7f4-d45434c8d0f8",
           "os_version":
             {
                "os_minor": 0,
                "os_is_server": false,
                "os_major": 10,
                "os_build_number": 10586,
                "os_service_pack": ""
              },
          "correlation_id": "7e17de5a-abcb-4de0-a510-7ca79bfdc345",
          "architecture": "x64",
          "sensor_info":
             {
                "malware_feature_version": "3.0.0",
                "sensor_build_time": "1581375786",
                "sensor_commit_sha": "80af56b6b295de785e502d82f39deac34973b2dd",
                "sensor_build_number": 48,
                "sensor_version": "3.53.9"
              },
          "time":
            {
               "tz_observes_dst": true,
               "tz_currently_in_dst": false,
               "tz_name": "Pacific Standard Time",
               "tz_offset_minutes": 480
            },
         "os_type": "windows",
         "ad_info":
           {
               "distinguished_name": "CN=PC-01,OU=TESTOU,OU=Organization,DC=test,DC=com",
               "domain_hostname": "test.com"
            },
         "origination_task_id": "d3d67012-cfb1-47d0-8ec9-bf7ffb68a019"
        }],
     "installed_security_products":
       [{
         "security_product_type": "AntiVirus",
         "collection_id": "a27ebace-32ec-4257-ab4f-7da49f02a9d4",
         "machine_id": "5dc677fd-6b47-7df9-f7f4-d45434c8d0f8",
         "enabled": false, "name": "Windows Defender"
       }]
      },
     "Entity": "PC-01"
    }]
    

### User Sessions Survey

Get information about an active user sessions on a specific Endgame endpoint.

#### Parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Max Items to Return | String | 50 | Specify how many items to return.  
  
#### Run on

  * Hostname
  * IP Address



#### Action results

##### Entity enrichment

Enrichment Field Name | Logic-When to apply  
---|---  
username | Returns if it exists in JSON result  
shell | Returns if it exists in JSON result  
uid | Returns if it exists in JSON result  
started | Returns if it exists in JSON result  
hostname | Returns if it exists in JSON result  
host_ip | Returns if it exists in JSON result  
session_id | Returns if it exists in JSON result  
session_count | Returns if it exists in JSON result  
terminal | Returns if it exists in JSON result  
ended | Returns if it exists in JSON result  
gid | Returns if it exists in JSON result  
collection_id | Returns if it exists in JSON result  
machine_id | Returns if it exists in JSON result  
started | Returns if it exists in JSON result  
password_last_set | Returns if it exists in JSON result  
logon_type | Returns if it exists in JSON result  
sid | Returns if it exists in JSON result  
  
##### Script result

Script Result Name | **Value options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [{
       "EntityResult":
         [{
            "username": "endgame",
            "shell": "/opt/endgame/bin/console",
            "uid": 1000,
            "started": 1582554802.55514,
            "hostname": "",
            "host_ip": "",
            "session_id": 887,
            "session_count": 1,
            "terminal": "tty1",
            "ended": 0,
            "gid": 1000,
            "collection_id": "1aebade8-9f7b-4237-8c43-2aed8729511e",
            "machine_id": "827255f4-53a2-1823-cac0-7c0f7730ca26"
         }],
       "Entity": "PC-01"
     }, {
        "EntityResult":
          [{
            "username": "example",
            "domain": "3B",
            "started": 1580205134.001,
            "session_count": 1,
            "ended": 0,
            "password_last_set": 0,
            "logon_type": "interactive",
            "sid": "",
            "collection_id": "88b876b1-5063-40a8-b40e-440df5eb8952",
            "machine_id": "5dc677fd-6b47-7df9-f7f4-d45434c8d0f8"
          }],
      "Entity": "PC-02"
    }
    

## Connectors

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

### Endgame Connector

Use the following parameters to configure the connector:

**Parameter** | **Type** | **Default Value** | **Description**  
---|---|---|---  
DeviceProductField | String | device_product | The field name used to determine the device product.  
EventClassId | String | event_name | The field name used to determine the event name (sub-type)  
PythonProcessTimeout | String | 30 | The timeout limit (in seconds) for the python process running current script   
API Root | String | N/A | N/A  
Username | String | N/A | N/A  
Password | Password | N/A | N/A  
Verify SSL | Checkbox | Unchecked | N/A  
Max Days Backwards | String | N/A | N/A  
Environment Field Name | String | N/A | If defined, the connector extracts the environment from the specified event field. You can manipulate the field data using the regular expression pattern field to extract a specific string.  
Alerts Count Limit | String | N/A | N/A  
Proxy Server Address | String | N/A | The address of the proxy server to use.  
Proxy Username | String | N/A | The proxy username to authenticate with.  
Proxy Password | Password | N/A | The proxy password to authenticate with.  
  
#### Connector rules

  * The connector supports proxy.

  * The connector supports the dynamic list.




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
