---
url: https://docs.cloud.google.com/chronicle/docs/install/forwarder-management-api/
title: Forwarder Management API reference \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:09.378098+00:00
---

# Forwarder Management API reference  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/install/forwarder-management-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Forwarder Management API reference

**Caution:** The forwarder is [deprecated](https://docs.cloud.google.com/chronicle/docs/deprecations). The forwarder component is being phased out of the Google SecOps platform and will reach end-of-life (EOL) in January 2027. **Apr 1, 2026** : New Google SecOps customers cannot use the forwarder component. **Jan 1, 2027** : The forwarder is officially EOL. No further patches, including security patches, will be released. **Apr 1, 2027** : Data is no longer allowed to be ingested from the forwarder component. **Google recommends using Bindplane for Google SecOps as the primary solution for log collection. For more information, see[Use Bindplane with Google SecOps](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent)**.

You can use the Google Security Operations Forwarder Management API Methods to do the following programmatically:

  * Create and manage forwarders.
  * Create and manage collectors.
  * Get the file contents for a Google SecOps forwarder's configuration.(`.conf`) and authentication (`_auth.conf`) files.

**Note:** Pre-existing forwarders can't be managed with this API and must be re-created using the API to take advantage of the Forwarder Management API features.

Forwarders are composed of one or more collectors. Each collector's configuration specifies its **ingestion mechanism** (for example, File, Kafka, PCAP, Splunk, or Syslog) and **log type**.

Assuming hardware requirements are met, you can use many collectors on the same forwarder to ingest data from a variety of mechanisms and log types. For example, you can install a forwarder with two syslog collectors listening for PAN_FIREWALL and CISCO_ASA_FIREWALL data on separate ports, respectively.

The API lets you create forwarders and their collectors in your Google SecOps instance. Once a forwarder is created, you can use the Generate Forwarder Files endpoint to get the file contents (as JSON payload) for a forwarder's configuration (`.conf`) and authentication (`_auth.conf`) files. These contents can then be written to their respective `.conf` files for deployment with the Google SecOps Forwarder service on a Windows or Linux system.

For Python samples that use the Forwarder Management API, see the [GitHub repository](https://github.com/chronicle/api-samples-python/tree/master/forwarders).

## Create a forwarder and its collector(s)

A forwarder must be created before any of its collectors can be created.

To create a forwarder and its collector(s):

  1. Create a forwarder.
  2. Create a collector for the forwarder.
  3. (Optional) Repeat Step 2 to add more collectors.



## Get API authentication credentials

Your Google Security Operations representative will provide you with a [Google Developer Service Account](https://developers.google.com/identity/protocols/OAuth2#serviceaccount) Credential to enable the API client to communicate with the API.

You also must provide the Auth Scope when initializing your API client. OAuth 2.0 uses a scope to limit an application's access to an account. When an application requests a scope, the access token issued to the application is limited to the scope granted.

Use the following scope to initialize your Backstory API client:

`https://www.googleapis.com/auth/chronicle-backstory`

###  Python example 

The following Python example demonstrates how to use the OAuth2 credentials and HTTP client using `google.oauth2` and `googleapiclient`.
    
    
    # Imports required for the sample - Google Auth and API Client Library Imports.
    # Get these packages from https://pypi.org/project/google-api-python-client/ or run $ pip
    # install google-api-python-client from your terminal
    from google.auth.transport import requests
    from google.oauth2 import service_account
    
    SCOPES = ['https://www.googleapis.com/auth/chronicle-backstory']
    
    # The apikeys-demo.json file contains the customer's OAuth 2 credentials.
    # SERVICE_ACCOUNT_FILE is the full path to the apikeys-demo.json file
    # ToDo: Replace this with the full path to your OAuth2 credentials
    SERVICE_ACCOUNT_FILE = '/customer-keys/apikeys-demo.json'
    
    # Create a credential using the Google Developer Service Account Credential and Backstory API
    # Scope.
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    
    # Build a requests Session Object to make authorized OAuth requests.
    http_session = requests.AuthorizedSession(credentials)
    
    # Your endpoint GET|POST|PATCH|etc. code will vary below
    
    # Reference List example (for US region)
    url = 'https://backstory.googleapis.com/v2/lists/COLDRIVER_SHA256'
    
    # You might need another regional endpoint for your API call; see
    # https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints
    
    # requests GET example
    response = http_session.request("GET", url)
    
    # POST example uses json
    body = {
      "foo": "bar"
    }
    response = http_session.request("POST", url, json=body)
    
    # PATCH example uses params and json
    params = {
      "foo": "bar"
    }
    response = http_session.request("PATCH", url, params=params, json=body)
    
    # For more complete examples, see:
    # https://github.com/chronicle/api-samples-python/
    

## Backstory API query limits

The Backstory API enforces limits on the volume of requests that can be made by any one customer against the Google SecOps platform. If you reach or exceed the query limit, the Backstory API server returns HTTP 429 (RESOURCE_EXHAUSTED) to the caller. When developing applications for the Backstory API, Google recommends that you enforce rate limits within your system to avoid resource exhaustion. These limits apply to all of the Backstory APIs, including the Search, Forwarder Management, and Tooling APIs.

See the detailed list of the [Backstory API quotas](https://docs.cloud.google.com/chronicle/docs/reference/backstory-api-quotas).

The following limit for the Forwarder Management is being enforced and is measured in queries per second (QPS):

**Backstory API** | **API Endpoint** | **Limit**  
---|---|---  
Forwarder Management  | Create Forwarder  | 1 QPS   
| Get Forwarder  | 1 QPS   
| List Forwarders  | 1 QPS   
| Update Forwarder  | 1 QPS   
| Delete Forwarder  | 1 QPS   
Collector Management  | Create Collector  | 1 QPS   
| Get Collector  | 1 QPS   
| List Collectors  | 1 QPS   
| Update Collector  | 1 QPS   
| Delete Collector  | 1 QPS   
  
## Forwarder API Methods reference

This section describes the endpoints for creating and managing forwarders. For endpoints for creating and managing collectors, see the Collector API reference.

### Create Forwarder

Creates a new forwarder in the Google SecOps instance. The new forwarder will include any _forwarder_ configuration values provided in the request body. Configuration values for _collectors_ must be specified using Create Collector after using Create Forwarder.

For certain settings, configuration values that are missing or zero-valued in the request body are set to default values. For details about forwarder fields and values, see Forwarder configuration fields.

#### Request

`POST https://backstory.googleapis.com/v2/forwarders`

##### Request body
    
    
    {
      "display_name": string,
      "config": {
        object (ForwarderConfig)
      }
    }
    

##### Body parameters

**Field** | **Type** | **Required** | **Description**  
---|---|---|---  
display_name | _string_ | Required | The name of the forwarder. This name is displayed in the Google SecOps interface.  
config | _object_ | Optional | The configuration settings for this forwarder. See Forwarder configuration fields.  
  
##### Request example

This example shows the required key:value pairs in a Create Forwarder request. If a field isn't specified in the request and has a default value, the default value is applied during forwarder creation. For details about default values, see Forwarder configuration fields.
    
    
    POST https://backstory.googleapis.com/v2/forwarders
    {
      "display_name": "chronicle_forwarder"
    }
    

#### Response

If the request is successful, the response returns an HTTP status code of 200 (OK).

The response shows the configuration values applied during creation of the forwarder. Default configuration values are applied for certain settings during resource creation if those fields are missing or zero-valued in the request body. For details, see Forwarder configuration fields.

##### Response fields

In addition to the fields specified in the request and the fields for which default values are applied, the response includes the following generated and output-only fields.

**Field** | **Type** | **Description**  
---|---|---  
name | _string_ | The resource ID of the forwarder. The format is "forwarders/forwarderID". For example:  
  
forwarders/12ab3cd4-56ef-7ghi-j89k-1l23m4nopq56  
state | _enum_ | Specifies the current state of the forwarder. Valid values are:

  * **ACTIVE** : The forwarder is allowed to upload data.
  * **SUSPENDED** : The forwarder is not allowed to upload data.

The default value is ACTIVE.  
  
##### Response example

This is an example of the response returned for the request example above.
    
    
    {
      "name": "forwarders/12ab3cd4-56ef-7abc-d89e-1f23a4bcde56",
      "displayName": "chronicle_forwarder",
      "config": {
        "uploadCompression": "false",
        "serverSettings": {
          "gracefulTimeout": 15,
          "drainTimeout": 10,
          "httpSettings": {
            "port": "8080",
            "host": "0.0.0.0",
            "readTimeout": "3",
            "readHeaderTimeout": "3",
            "writeTimeout": "3",
            "idleTimeout": "3"
            "routeSettings": {
              "availableStatusCode": "204",
              "readyStatusCode": "204",
              "unreadyStatusCode": "503"
            },
          },
        },
      },
      "state": "ACTIVE"
    }
    

### Get Forwarder

Returns a forwarder.

#### Request

`GET https://backstory.googleapis.com/v2/forwarders/{forwarderID}`

**Note:** The forwarderID in the request URL is the value of the `name` field returned in a List Forwarders response.

##### Request body

Don't include a request body.

##### Request example
    
    
    GET https://backstory.googleapis.com/v2/forwarders/12ab3cd4-56ef-7abc-d89e-1f23a4bcde56
    

##### Response example
    
    
    {
      "name": "forwarders/12ab3cd4-56ef-7abc-d89e-1f23a4bcde56",
      "displayName": "chronicle_forwarder",
      "config": {
        "uploadCompression": "false",
        "serverSettings": {
          "gracefulTimeout": 15,
          "drainTimeout": 10,
          "httpSettings": {
            "port": "8080",
            "host": "0.0.0.0",
            "readTimeout": "3",
            "readHeaderTimeout": "3",
            "writeTimeout": "3",
            "idleTimeout": "3"
            "routeSettings": {
              "availableStatusCode": "204",
              "readyStatusCode": "204",
              "unreadyStatusCode": "503"
            },
          },
        },
      },
      "state": "ACTIVE"
    }
    

### List Forwarders

Lists all of the forwarders for a Google SecOps instance.

#### Request

`GET https://backstory.googleapis.com/v2/forwarders`

##### Request example

`GET https://backstory.googleapis.com/v2/forwarders`

#### Response

Returns a list of forwarders.

##### Response example
    
    
    {
      "forwarders": [
        {
          "name": "forwarders/12ab3cd4-56ef-7abc-d89e-1f23a4bcde56",
          "displayName": "chronicle_forwarder_1",
          "config": {
            "uploadCompression": "false",
            "serverSettings": {
              "gracefulTimeout": 15,
              ...
             },
          },
          "state": "ACTIVE"
        },
        {
          "name": "forwarders/12ab3cd4-56ef-7abc-d89e-1f23a4bcde57",
          "displayName": "chronicle_forwarder_2",
          "config": {
            "uploadCompression": "false",
            "serverSettings": {
              "gracefulTimeout": 15,
           ...
           },
          },
          "state": "ACTIVE"
        }
      ]
    }
    

### Update Forwarder

You can update a forwarder by using the `updateMask` URL query parameter to specify the fields to update.

For example, to update the display name, you would use the `updateMask` query parameter as follows in the patch request:
    
    
    ?updateMask=displayName
    

The request body should only contain the fields that you wish to update (in their exact locations).

#### Request
    
    
    PATCH https://backstory.googleapis.com/v2/forwarders/{forwarderID}?updateMask=<field_1,field_2>
    

##### Request body
    
    
    {
      "display_name": string,
      "config": {
        object (ForwarderConfig)
      },
    }
    

##### Body parameters

**Field** | **Type** | **Required** | **Description**  
---|---|---|---  
display_name | _string_ | Required | The name of the forwarder. This name is displayed in the Google SecOps interface.  
config | _object_ | Optional | The configuration settings for this forwarder. See Forwarder configuration fields.  
  
##### Request example

This is an example of an Update Forwarder request where the request specifies new values for `displayName` and adds a Metadata label.

**Note:** The entire list is replaced during an update operation. Therefore, to update metadata.labels with a new label, specify all existing labels and the new label.
    
    
    PATCH https://backstory.googleapis.com/v2/forwarders/12ab3cd4-56ef-7abc-d89e-1f23a4bcde56?updateMask=displayName,config.metadata.labels
    {
      "display_name": "UpdatedForwarder",
      "config": {
        "metadata": {
          "labels": [
            {
              "key": "office",
              "value": "corporate",
            }
          ]
        }
      }
    }
    

##### Response example

This is an example of the response returned for the request example above.
    
    
    {
      "name": "forwarders/{forwarderUUID}",
      "displayName": "UpdatedForwarder",
      "config": {
        "uploadCompression": "false",
        "metadata": {
          "labels": [
            {
              "key": "office",
              "value": "corporate"
            }
          ]
        }
      },
      "state": "ACTIVE"
    }
    

### Delete Forwarder

Deletes a forwarder.

#### Request
    
    
    DELETE https://backstory.googleapis.com/v2/forwarders/{forwarderID}
    

**Note:** The forwarderID is returned in the value for the `name` field in a List Forwarders response.

##### Request body

Don't include a request body.

##### Request example
    
    
    DELETE https://backstory.googleapis.com/v2/forwarders/12ab3cd4-56ef-7abc-d89e-1f23a4bcde56
    

##### Response example

If the operation is successful, Delete Forwarder returns an empty response with an HTTP status code 200 (OK).
    
    
    {}
    

### Generate Forwarder Files

Generates and returns the contents of the forwarder's configuration (`.conf`) and authentication (`_auth.conf`) files.

#### Request
    
    
    GET https://backstory.googleapis.com/v2/forwarders/{forwarderID}:generateForwarderFiles
    

**Note:** The forwarderID is returned in the value for the `name` field in a List Forwarders response.

##### Request body

Don't include a request body.

##### Request example
    
    
    GET https://backstory.googleapis.com/v2/forwarders/12ab3cd4-56ef-7abc-d89e-1f23a4bcde56:generateForwarderFiles
    

##### Response example

If the operation is successful, it returns an HTTP status code 200 (OK). It also returns the contents of a forwarder configuration file, including the configuration data for the forwarder's collectors, as well as the contents of the authentication (`_auth.conf`) file that is used by the forwarder to authenticate with the Google SecOps instance.

### Forwarder configuration fields

The following table lists the forwarder configuration settings that you can specify using Create Forwarder and Update Forwarder. If you don't specify a value for a setting when you use Create Forwarder, the setting's default value (shown below) is applied.

**Note:** The metadata and regex settings in a forwarder configuration are global settings that apply to the forwarder and the forwarder's collectors. You can override these settings for a specific collector by using Create Collector or Update Collector.

The following fields can be provided in the **`config`** object of the request body.

**Field** | **Type** | **Required** | **Description**  
---|---|---|---  
upload_compression | _bool_ | Optional | If `true`, batches of data are compressed before upload.  
  
The default is `false`.  
metadata.asset_namespace | _string_ | Optional | The namespace for identifying logs from this forwarder.  
  
**Note:** This is a global setting that applies to the forwarder and the forwarder's collectors, unless it is overridden at the collector level. For more information, see [Configure namespaces](https://docs.cloud.google.com/chronicle/docs/install/forwarder-linux#configure_namespaces).  
metadata.labels | _list_ | Optional | A list of arbitrary key:value pairs that can be specified in the forwarder configuration.  
  
**Note:** This is a global setting that applies to the forwarder and the forwarder's collectors, unless it is overridden at the collector level.  
metadata.labels.key | _string_ | Optional | The key for a field in the metadata labels list.  
metadata.labels.value | _string_ | Optional | The value for a field in the metadata labels list.  
regex_filters.description | _string_ | Optional | Describes what is being filtered and why.  
regex_filters.regexp | _string_ | Optional | The regular expression used to match against each incoming line.  
regex_filters.behavior | _enum_ | Optional | Specifies the state of the server functionality. Valid values are:

  * **ALLOW** : This state allows the filtered line to be uploaded.
  * **BLOCK** : This state prevents the filtered line from being uploaded.

  
server_settings | _object_ | Optional | Settings that configure the forwarder's built-in HTTP server, which can be used to [configure load balancing and high availability options](https://docs.cloud.google.com/chronicle/docs/install/forwarder-linux#configure_load_balancing_and_high_availability_options) for syslog collection on Linux.  
server_settings.state | _enum_ | Optional | Specifies the state of the server functionality. Valid values are:

  * **ACTIVE** : In this state, server settings are applied as specified.
  * **SUSPENDED** In this state, server settings are not applied.

  
server_settings.graceful_timeout | _integer_ | Optional | The number of seconds after which the forwarder returns a bad readiness/health check and still accepts new connections. This is also the time to wait between receiving a signal to stop and actually beginning the shutdown of the server itself. This allows the load balancer time to remove the forwarder from the pool.  
  
The default value is `15`.  
server_settings.drain_timeout | _integer_ | Optional | The number of seconds after which the forwarder waits for active connections to successfully close on their own before being closed by the server.  
  
The default value is `10`.  
server_settings.http_settings.port | _integer_ | Optional | The port number that the HTTP server listens on for health checks from the load balancer. Must be between 1024-65535.  
  
The default is `8080`.  
server_settings.http_settings.host | _string_ | Optional | The IP address, or hostname that can be resolved to IP addresses, that the server should listen to.   
  
The default value is `0.0.0.0` (the local system).  
server_settings.http_settings.read_timeout | _integer_ | Optional | The maximum number of seconds allowed to read entire requests, which includes the header and the body.  
  
The default value is `3`.  
server_settings.http_settings.read_header_timeout | _integer_ | Optional | The maximum number of seconds allowed to read request headers.  
  
The default value is `3`.  
server_settings.http_settings.write_timeout | _integer_ | Optional | The maximum number of seconds allowed to send a response.  
  
The default value is `3`.  
server_settings.http_settings.idle_timeout | _integer_ | Optional | The maximum number of seconds to wait for the next request when idle connections are enabled.  
  
The default is `3`.  
server_settings.http_settings.route_settings.available_status_code | _integer_ | Optional | The status code returned when a liveness check is received and the forwarder is available.  
  
The default is `204`.  
server_settings.http_settings.route_settings.ready_status_code | _integer_ | Optional | The status code returned when the forwarder is ready to accept traffic.  
  
The default is `204`.  
server_settings.http_settings.route_settings.unready_status_code | _integer_ | Optional | The status code returned when the forwarder is not ready to accept traffic.  
  
The default is `503`.  
  
## Collector API Methods reference

This section describes the endpoints for working with collectors.

When creating and updating collectors, note that each collector configuration can specify ingestion settings for one, but not more than one, of the following:

  * Log file data
  * Kafka topics
  * Packet data (pcap)
  * Splunk data
  * Syslog data

**Note:** You must create a forwarder using Create Forwarder before you can create one of its collectors using Create Collector.

For endpoints for working with forwarders, see the Forwarder API reference.

**Important:** Although the authentication fields (username and password) for Splunk and Kafka data collection are optional, data collection cannot succeed without these values.

### Create Collector

Creates a new collector in the Google SecOps account. Configuration values for _collectors_ must be specified using Create Collector after using Create Forwarder.

For certain settings, configuration values that are missing or zero-valued in the request body are set to default values. For details about collector configuration fields and values, see Collector configuration fields.

**Note:** The metadata and regex settings in a forwarder configuration are global settings that apply to the forwarder and the forwarder's collectors. These settings can be overridden on a per-collector basis.

#### Request
    
    
    POST https://backstory.googleapis.com/v2/forwarders/{forwarderID}/collectors
    

##### Request body
    
    
    {
      "display_name": string,
      "config": {
        object (CollectorConfig)
      }
      "state": enum
    }
    

##### Body parameters

**Field** | **Type** | **Required** | **Description**  
---|---|---|---  
display_name | _string_ | Required | The name of the collector. This name is displayed in the Google SecOps interface.  
config | _object_ | Required | The configuration settings for this collector. See Collector configuration fields.  
state | _enum_ | Optional | Specifies the current state of the collector. Valid values are:

  * **ACTIVE** : The collector is allowed to accept data.
  * **SUSPENDED** : The collector is not allowed to accept data.

  
  
##### Request example

This example shows the required key:value pairs in a Create Collector request. For any fields that aren't provided, default values are applied during collector creation.

In this example, the collector type is `file`, so the collector configuration includes `file_settings` to indicate the collector type and its settings. If the collector type is `syslog`, then the collector configuration includes `syslog_settings`. For more information, see Collector configuration fields.
    
    
    POST https://backstory.googleapis.com/v2/forwarders/12ab3cd4-56ef-7abc-d89e-1f23a4bcde56/collectors
    {
      "display_name": "abc_collector",
      "config" {
        "log_type": "CS_EDR"
        "file_settings": {
          "file_path": "/opt/chronicle/edr/output/sample.txt",
        }
      }
    }
    

#### Response

If the request is successful, the response returns an HTTP status code of 200 (OK).

The response shows the configuration values applied during creation of the collector. Default configuration values are applied for certain settings during resource creation if those fields are missing or zero-valued in the request body. For details, see Collector configuration fields.

##### Response fields

In addition to the fields specified in the request and the fields for which default values are applied, the response includes the following fields:

**Field** | **Type** | **Description**  
---|---|---  
name | _string_ | The resource ID of the collector. The format is "forwarders/{forwarderID}/collectors/{collectorID}". For example:  
  
`forwarders/12ab3cd4-56ef-7abc-d89e-1f23a4bcde56/collectors/98ab7cd6-54ef-3abc-d21e-1f23a4bcde56`  
  
##### Response example

This is an example of the response returned for the request example above.
    
    
    {
      "name": "forwarders/12ab3cd4-56ef-7ghi-j89k-1l23m4nopq56/collectors/
         98ab7cd6-54ef-3abc-d21e-1f23a4bcde56",
      "displayName": "abc_collector",
      "config": {
        "logType": "tomcat",
        "maxSecondsPerBatch": "10",
        "maxBytesPerBatch": "1048576"
      }
    }
    

### Get Collector

Returns a collector.

#### Request
    
    
    GET https://backstory.googleapis.com/v2/forwarders/{forwarderID}/collectors/{collectorID}
    

**Note:** The collectorID in the request URL is the value of the `name` field returned in a List Forwarders response.

##### Request body

Don't include a request body.

##### Request example
    
    
    GET
    https://backstory.googleapis.com/v2/forwarders/12ab3cd4-56ef-7abc-d89e-1f23a4bcde56/collectors/98ab7cd6-54ef-3abc-d21e-1f23a4bcde56
    

##### Response example
    
    
    {
      "name": "?",
      "displayName": "abc_collector",
      "config": {
        "logType": "tomcat",
        "maxSecondsPerBatch": "10",
        "maxBytesPerBatch": "1048576"
      }
    }
    

### List Collectors

Lists the existing collectors for the specified forwarder.

#### Request
    
    
    GET https://backstory.googleapis.com/v2/forwarders/{forwarderID}/collectors
    

##### Request example
    
    
    GET https://backstory.googleapis.com/v2/forwarders/12ab3cd4-56ef-7abc-d89e-1f23a4bcde56/collectors
    

#### Response

Returns multiple collectors.

##### Response example
    
    
    {
      "collectors": [
        {
          "name": "?",
          "displayName": "abc_collector_1",
          "config": {
            "logType": "tomcat",
            "maxSecondsPerBatch": "10",
            "maxBytesPerBatch": "1048576"
          }
        },
        {
          "name": "?",
          "displayName": "abc_collector_2",
          "config": {
            "logType": "tomcat",
            "maxSecondsPerBatch": "10",
            "maxBytesPerBatch": "1048576"
          }
        }
      ]
    }
    

### Update Collector

When updating a collector with the API, you can choose to overwrite the entire collector configuration or to overwrite only specific fields of the collector configuration. It is usually best to overwrite specific fields, so you avoid accidentally overwriting all of your data. To overwrite specific fields, supply a FieldMask to your update request.

To supply a FieldMask to update the display name for a collector, supply the updateMask URL query parameter in the patch request. For example:
    
    
    ?updateMask=displayName
    

The request body should only contain the fields that you wish to update (in their exact locations).

#### Request
    
    
    PATCH https://backstory.googleapis.com/v2/forwarders/{forwarderID}/collectors/{collectorID}?updateMask=<field_1,field_2>
    

##### Request body
    
    
    {
      "display_name": string,
      "config": {
        object (CollectorConfig)
      },
    }
    

##### Body parameters

**Field** | **Type** | **Required** | **Description**  
---|---|---|---  
displayName | _string_ | Required | The name of the collector. This name is displayed in the Google SecOps interface.  
config | _object_ | Optional | The configuration settings for this forwarder. See Collector configuration fields.  
  
##### Request example

This is an example of an Update Collector request where the request specifies new values for displayName, logType, assetNamespace, and protocol.

**Note:** As a list, all labels in `metadata.labels` are replaced during an update operation. Therefore, to update `metadata.labels` with a new label, specify all existing labels and the new label.
    
    
    PATCH https://backstory.googleapis.com/v2/forwarders/12ab3cd4-56ef-7abc-d89e-1f23a4bcde56/collectors/98ab7cd6-54ef-3abc-d21e-1f23a4bcde56?updateMask=displayName,config.logType,config.metadata.assetNamespace,config.syslogSettings.protocol
    {
      "display_name": "UpdatedCollector"
      "config": {
        "metadata": {
          "asset_namespace": "COLLECTOR",
          },
          "log_type": "CISCO_ASA_FIREWALL",
          "syslog_settings": {
            "protocol": "TCP",
          }
        }
      }
    

##### Response example

This is an example of the response returned for the request example above.
    
    
    {
      "name": "forwarders/12ab3cd4-56ef-7abc-d89e-1f23a4bcde56/collectors/98ab7cd6-54ef-3abc-d21e-1f23a4bcde56",
      "displayName": "UpdatedCollector",
      "config": {
        "logType": "CISCO_ASA_FIREWALL",
        "metadata": {
          "assetNamespace": "COLLECTOR"
        },
        "maxSecondsPerBatch": 10,
        "maxBytesPerBatch": "1048576",
        "syslogSettings": {
          "protocol": "TCP",
          "address": "0.0.0.0",
          "port": 10514,
        }
      },
      "state": "ACTIVE"
    }
    

### Delete Collector

Deletes a collector.

#### Request
    
    
    DELETE https://backstory.googleapis.com/v2/forwarders/{forwarderID}/collectors/{collectorID}
    

**Note:** The forwarderID and collectorID in the request URL are the values of the `name` field returned in a List Forwarders and List Forwarders response.

##### Request body

Don't include a request body.

##### Request example
    
    
    DELETE https://backstory.googleapis.com/v2/forwarders/12ab3cd4-56ef-7abc-d89e-1f23a4bcde56/collectors/98ab7cd6-54ef-3abc-d21e-1f23a4bcde56
    

##### Response example

If the operation is successful, Delete Collector returns an empty response with an HTTP status code 200 (OK).
    
    
    {}
    

### Collector configuration fields

The following fields can be provided in the **`config`** object of the request body.

**Field** | **Type** | **Required** | **Description**  
---|---|---|---  
log_type | _string_ | Required | A supported log type (one that can be ingested by Google SecOps). For a list of supported log types for which Google SecOps has a parser, see the the Ingestion Label column on the [Supported default parsers](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/supported-default-parsers) page. To get a complete list of supported log types, use the [`logtypes` endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#logtypes).   
metadata.asset_namespace | _object_ | Optional | The namespace for identifying logs from this collector.  
  
**Note:** This is a global setting that applies to the forwarder and the forwarder's collectors, unless it is overridden at the collector level. For more information, see [Configure namespaces](https://docs.cloud.google.com/chronicle/docs/install/forwarder-linux#configure_namespaces).   
metadata.labels | _list_ | Optional | A list of arbitrary key:value pairs that can be specified in the collector configuration.  
  
**Note:** This is a global setting that applies to the forwarder and the forwarder's collectors, unless it is overridden at the collector level.  
metadata.labels.key | _string_ | Optional | The key for a field in the metadata labels list.  
metadata.labels.value | _string_ | Optional | The value for a field in the metadata labels list.  
regex_filters.description | _string_ | Optional | Describes what is being filtered and why.  
regex_filters.regexp | _string_ | Optional | The regular expression used to match against each incoming line.  
regex_filters.behavior | _enum_ | Optional | Specifies the state of the server functionality. Valid values are:

  * **ALLOW** : This state allows the filtered line to be uploaded.
  * **BLOCK** : This state prevents the filtered line from being uploaded.

  
disk_buffer.state | _enum_ | Optional | Specifies the disk buffering state for the collector. Valid values are:

  * **ACTIVE** : Buffering is enabled.
  * **SUSPENDED** : Buffering is disabled.

  
disk_buffer.directory_path | _string_ | Optional | The directory path for files written.  
disk_buffer.max_file_buffer_bytes | _integer_ | Optional | The maximum buffered file size.  
max_seconds_per_batch | _integer_ | Optional | The number of seconds between batches.  
  
The default is `10`.  
max_bytes_per_batch | _integer_ | Optional | The number of bytes queued before forwarder batch upload.  
  
The default is `1048576`.  
<collector_type>_settings.<fields> |  | Required | Specifies a collector type and its settings. Every collector must specify one collector type and its fields. For example, to use the `file` collector type, the `file_settings.file_path` field must be added to the configuration and given a value. For example:  
  
`"file_settings": {  
"file_path": "/opt/chronicle/edr/output/sample.txt",  
}`  
  
The collector types and their fields are listed in the subsequent rows of this table. The available collector types are:  


  * `file`
  * `kafka`
  * `pcap`
  * `splunk`
  * `syslog`

  
file_settings.file_path | _string_ | Optional | The path of the file to monitor.  
kafka_settings.authentication.username | _string_ | Optional | The username of an identity used for authentication.  
kafka_settings.authentication.password | _string_ | Optional | The password of the account identified by the username.  
kafka_settings.topic | _string_ | Optional | The Kafka topic from which to ingest data. For details, see [Collect data from Kafka topics](https://docs.cloud.google.com/chronicle/docs/install/forwarder-linux#collect_data_from_kafka_topic).  
kafka_settings.group_id | _string_ | Optional | A group ID.  
kafka_settings.timeout | _integer_ | Optional | The maximum number of seconds a dial will wait for a connect to complete.  
  
The default is `60`.  
kafka_settings.brokers | _string_ | Optional | A repeated string listing Kafka brokers. For example:  
  
"broker-1:9092", "broker-2:9093"  
  
**Note:** All values are replaced during an update operation. Therefore, to update a list of brokers to add a new broker, specify all existing brokers and the new broker.  
kafka_settings.tls_settings.certificate | _string_ | Optional | The path and certificate filename. For example:  
  
`/path/to/cert.pem`  
kafka_settings.tls_settings.certificate_key | _string_ | Optional | The path and certificate key filename. For example:  
  
`/path/to/cert.key`  
kafka_settings.tls_settings.minimum_tls_version | _string_ | Optional | The minimum TLS version.  
kafka_settings.tls_settings.insecure_skip_verify | _bool_ | Optional | If `true`, enables SSL certification verification.  
  
The default is `false`.  
pcap_settings.network_interface | _string_ | Optional | The interface to listen to for PCAP data.  
pcap_settings.bpf | _string_ | Optional | The Berkeley Packet Filter (BPF) for pcap.  
splunk_settings.authentication.username | _string_ | Optional | The username of an identity used for authentication.  
splunk_settings.authentication.password | _string_ | Optional | The password of the account identified by the username.  
splunk_settings.host | _string_ | Optional | The host or IP address for the Splunk REST API.  
splunk_settings.port | _integer_ | Optional | The port for the Splunk REST API.  
splunk_settings.minimum_window_size | _integer_ | Optional | The minimum time range in seconds for a given Splunk search. For details, see [Collect Splunk data](https://docs.cloud.google.com/chronicle/docs/install/forwarder-linux#collect_splunk_data).  
  
The default is `10`.  
splunk_settings.maximum_window_size | _integer_ | Optional | The maximum time range in seconds for a given Splunk search. For details, see [Collect Splunk data](https://docs.cloud.google.com/chronicle/docs/install/forwarder-linux#collect_splunk_data).  
  
The default is `30`.  
splunk_settings.query_string | _string_ | Optional | The query used to filter records within Splunk.  
  
For example: `search index=* sourcetype=dns`  
splunk_settings.query_mode | _string_ | Optional | The query mode for Splunk.  
  
For example: `realtime`  
splunk_settings.cert_ignored | _bool_ | Optional | If `true`, the certificate is ignored.  
syslog_settings.protocol | _enum_ | Optional | Specifies the protocol the collector will use to listen for syslog data. Valid values are:

  * `TCP`
  * `UDP`

  
syslog_settings.address | _string_ | Optional | The target IP address or hostname where the collector resides and listens for syslog data.  
syslog_settings.port | _integer_ | Optional | The target port where the collector resides and listens for syslog data.  
syslog_settings.buffer_size | _integer_ | Optional | The size in bytes of the TCP socket's buffer.  
  
The default for TCP is `65536`.  
The default for UDP is `8192`.  
syslog_settings.connecton_timeout | _integer_ | Optional | The number of seconds of inactivity after which the TCP connection is dropped.  
  
The default is `60`.  
syslog_settings.tls_settings.certificate | _string_ | Optional | The path and certificate filename. For example:  
  
`/path/to/cert.pem`  
syslog_settings.tls_settings.certificate_key | _string_ | Optional | The path and certificate key filename. For example:  
  
`/path/to/cert.key`  
syslog_settings.tls_settings.minimum_tls_version | _string_ | Optional | The minimum TLS version.  
syslog_settings.tls_settings.insecure_skip_verify | _bool_ | Optional | If `true`, enables SSL certification verification.  
  
The default is `false`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
