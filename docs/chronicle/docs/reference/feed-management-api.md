---
url: https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api/
title: Ingest data with API connectors \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:26:19.373941+00:00
---

# Ingest data with API connectors  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Ingest data with API connectors

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Caution:** The Backstory API is [deprecated](https://docs.cloud.google.com/chronicle/docs/deprecations) and will be discontinued on July 20, 2027. To manage feeds and accounts in Google SecOps, use the [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/rest) instead. For details on how to migrate, see [Migrate from legacy SIEM API to Chronicle API](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-api-to-chronicle-api).

This document explains how to use the Feed Management API to programmatically create, run, and manage data feeds that send logs to your Google Security Operations instance. For details about how to use the Google SecOps console to create and manage feeds, see [Work with the feeds UI](https://docs.cloud.google.com/chronicle/docs/administration/feed-management).

## Prerequisites

Each data feed has its own set of prerequisites that must be completed prior to setting up the feed in Google Security Operations. You can find the prerequisites as follows:

  * Prerequisites for each source type are listed in Configuration by source type. 

  * Prerequisites for each log type ingested using the `API` feed source type are listed in Configuration by log type. 

  * Prerequisites for all log types ingested using any source type are listed in the Google SecOps UI. Go to **Settings > Feeds > Add New**, select a **Source Type** and **Log Type** , and review the required fields. For details, see [Add a feed](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#add-new-feed). 




For example, if you set up a data feed from a Google Cloud Storage. bucket, you might need to complete the following tasks:

  1. Use the feed management `fetchFeedServiceAccount` method to get a Google SecOps service account that Google SecOps uses to ingest data.
  2. Grant access to the Google SecOps service account to the relevant Cloud Storage objects. For more information, see [Grant access to the Google SecOps service account](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#grant-sa-access).



## Set up IP allowlisting

When Google SecOps pulls data from S3, SQS, Azure, and third-party APIs, the Google infrastructure connects outbound to the customer's bucket or the third-party API.

For ingress allowlisting on your storage buckets or firewalls, you must configure allowlisting according to the feed type, as described in the following list:

  * **V2 feeds (S3_V2, SQS_V2, Azure_Blobstore_V2)** : These feeds exclusively use Google Cloud Storage Transfer Service (STS) to pull data from customer storage. They require allowlisting the STS IP ranges: [ipranges.json](https://www.gstatic.com/storage-transfer-service/ipranges.json).
  * **Third-party APIs** : Require [goog.json](https://www.gstatic.com/ipranges/goog.json).
  * **Legacy feeds (S3, Azure_Blobstore)** : Require dedicated IP ranges. For more information, contact [Google SecOps support](https://docs.cloud.google.com/chronicle/docs/getting-support).
  * **Azure Event Hub** : Requires region-specific IP ranges. For more information, see [Configure network security (optional) in _Create an Azure Event Hub feed_](https://docs.cloud.google.com/chronicle/docs/administration/create-azure-feed#network-security).

**Note:** Google SecOps can't guarantee that all feeds will exclusively originate from IP addresses according to a specified region.

Because Google Services IP ranges change dynamically, Google recommends that you configure your firewall to periodically fetch and parse the feeds as follows:

  * **V2 feeds (S3_V2, SQS_V2, Azure_Blobstore_V2)** : Data transfer is executed exclusively by Storage Transfer Service workers. You only need to periodically fetch and parse [ipranges.json](https://www.gstatic.com/storage-transfer-service/ipranges.json).
  * **Legacy feeds (S3, SQS, Azure_Blobstore, Azure Event Hub) and third-party APIs** : These connections originate from the Google infrastructure. You only need to periodically fetch and parse [goog.json](https://www.gstatic.com/ipranges/goog.json) and [cloud.json](https://www.gstatic.com/ipranges/cloud.json).



## Credential validation for third-party API feeds

For all third-party API connectors, Google SecOps automatically validates the provided credentials, for example, API keys, secrets, or OAuth tokens, during the feed creation process.

  * **Blocking validation:** If the credentials fail validation, the system returns an error and blocks the creation of the feed. You must provide valid, active credentials to successfully create the feed.
  * **Error messages:** If validation fails, the API response includes a descriptive error message and code. For more information, see [Troubleshoot failed feeds](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#troubleshooting).



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
    
    # Create a credential using the Google Developer Service Account Credential and Backstory API Scope. 
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    
    # Build a requests Session Object to make authorized OAuth requests.
    http_session = requests.AuthorizedSession(credentials)
    
    # Your endpoint GET|POST|PATCH|etc. code will vary below
    
    # Reference List example (for US region)
    url = 'https://backstory.googleapis.com/v2/lists/COLDRIVER_SHA256'
    
    # You might need another regional endpoint for your API call; see
    # https://cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints
    
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

The Backstory API enforces limits on the volume of requests that can be made by any one customer against the Google SecOps platform. If you reach or exceed the query limit, the Backstory API server returns an `HTTP 429 (RESOURCE\_EXHAUSTED)` response. To avoid this, we recommend that you implement rate limiting in your applications. These limits apply to all of the Backstory APIs, including the feed management API.

The feed management API enforces the following limits, which are measured in queries per second (QPS):

**Backstory API** | **API Method** | **Limit**  
---|---|---  
Feed management  | Create Feed  | 1 QPS   
| Get Feed  | 1 QPS   
| List Feeds  | 1 QPS   
| Update Feed  | 1 QPS   
| Delete Feed  | 1 QPS   
  
## Control the rate of ingestion

When the data ingestion rate for a tenant reaches a certain threshold, Google Security Operations restricts the rate of ingestion for new data feeds to prevent a source with a high ingestion rate from affecting the ingestion rate of another data source. In this case, there is a delay but no data is lost. The ingestion volume and tenant's usage history determine the threshold.

You can request a rate limit increase by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).

## API ingestion and latency

Google SecOps uses a dynamic polling mechanism to ingest data from third-party APIs. This system ensures that all available records are captured, even when there is provider-side latency. You monitor data ingestion more accurately when you account for the interaction between query windows and provider latency.

Third-party API feeds operate in a _forward-moving state_ , which means that feeds cannot retroactively pull historical data to ingest delayed or missed logs.

### Dynamic query windows

For API-based feeds, such as Office 365, the ingestion process uses a dynamic query window to poll the provider's management API. This window is defined by the following parameters:

  * `startTime`: The beginning of the period for which Google SecOps requests data.
  * `endTime`: The end of the period for which Google SecOps requests data.



Google SecOps automatically manages these parameters to support continuous data coverage and to minimize gaps in ingestion.

### Provider-specific latency

The effectiveness of the query window depends on when a third-party provider makes audit records available. This delay is known as _provider latency_.

For example, Microsoft Office 365 audit records are typically available **60 to 90 minutes** after an event occurs. Due to this latency, Google SecOps maintains a lookback window to capture these delayed records (backfillability). If you search for recent events, account for this delay between the event occurrence and its availability in Google SecOps.

## Prevent deduplication

Google SecOps includes built-in mechanisms to prevent the ingestion of duplicate logs within a single third-party API feed.

## Deduplication is at the batch level

Google SecOps performs deduplication at the batch level, _not_ at log level. This means that if the same log is sent in different transfers, Google SecOps will ingest them all.

### Content tracking mechanism

For API-based feeds, Google SecOps tracks successfully processed data to avoid re-fetching the same records.

For example, in Office 365 feeds, the ingestion process receives a list of `contentId` values from the Microsoft Management API. These `contentId` values represent immutable blobs of data. Google SecOps maintains a record of these IDs and only requests content that has not been previously ingested, ensuring that the same data is not processed twice within the same feed.

## Best practices for avoiding redundant data

While Google SecOps prevents duplicates within a single feed, it doesn't automatically detect if the same data is being sent through multiple, independent ingestion paths.

### Verify ingestion paths

To avoid duplicate Unified Data Model (UDM) events, make sure you audit your ingestion surface area to make sure each log source (Tenant ID/Subscription) maps to exactly one ingestion method.

Redundancy often occurs when multiple ingestion paths are enabled for the same source, such as:

  * Ingesting Office 365 data via a third-party API feed
  * Simultaneously ingesting the same Office 365 data via a Google SecOps forwarder or a SIEM-to-SIEM integration



Before you configure a new feed, audit your existing ingestion configurations to make sure each log source has only one active path into Google SecOps.

## Limitations

When ingesting text-based logs (JSON, CSV, or Syslog), ensure your data adheres to these specific ingestion limits:

  * **Maximum Line Size** : A single log line cannot exceed **4MB**. If a single line exceeds this limit, the feed fails with the error `MaxLogLineSize4MBExceeded`.
  * **Supported Delimiters** : Both Newline (\n) and Carriage Return + Newline (\r\n) are supported.



See the detailed list of the [Backstory API query limits](https://docs.cloud.google.com/chronicle/docs/reference/backstory-api-quotas).

**Note:** For log types with high data density, verify that your log source is not grouping multiple events into a single line that exceeds the 4 MB limit. If you encounter size errors, you may need to adjust the source logging configuration to ensure individual entries are properly delimited.

### Ingestion Latency for Microsoft Feeds

For all log types ingested via the Microsoft fetcher (including Azure AD and Microsoft Graph Security API), a mandatory 5-minute ingestion lag is applied. 

This lag is an architectural requirement of the fetcher to account for late data availability within the Microsoft Graph API. Since the polling mechanism retrieves point-in-time snapshots of data, status changes occurring within this 5-minute window may not be captured as intermediate events. This inherent latency is a known behavior of the fetcher and may result in event count discrepancies when compared to other ingestion methods or platforms.

## Python example using OAuth2 credentials and HTTP client

The following Python example demonstrates how to use the OAuth2 credentials and the HTTP client using `google.oauth2` and `googleapiclient`.
    
    
    # Imports required for the sample - Google Auth and API Client Library Imports.
    # Get these packages from https://pypi.org/project/google-api-python-client/ or
    # run $ pip install google-api-python-client from your terminal
    
    from google.auth.transport import requests
    from google.oauth2 import service_account
    
    SCOPES = ['https://www.googleapis.com/auth/chronicle-backstory']
    
    # The apikeys-demo.json file contains the customer's OAuth 2 credentials.
    # SERVICE_ACCOUNT_FILE is the full path to the apikeys-demo.json file
    # ToDo: Replace this with the full path to your OAuth2 credentials
    
    SERVICE_ACCOUNT_FILE = '/customer-keys/apikeys-demo.json'
    
    # Create a credential using Google Developer Service Account Credential and
    Backstory API Scope.
    
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    
    # Build an HTTP session to make authorized OAuth requests.
    
    http_session = requests.AuthorizedSession(credentials)
    
    # <your code continues here>
    

## Regional endpoints

Google Security Operations provides regional endpoints for each API.

  * [São Paulo](https://cloud.google.com/about/locations#americas)—`https://southamerica-east1-backstory.googleapis.com`
  * [Canada](https://cloud.google.com/about/locations#americas)—`https://northamerica-northeast2-backstory.googleapis.com`
  * [Dammam](https://cloud.google.com/about/locations#middle-east)—`https://me-central2-backstory.googleapis.com`
  * [Doha](https://cloud.google.com/about/locations#middle-east)—`https://me-central1-backstory.googleapis.com`
  * [Europe Multi-Region](https://cloud.google.com/about/locations#multi-region)—`https://europe-backstory.googleapis.com`
  * [Frankfurt](https://cloud.google.com/about/locations#europe)—`https://europe-west3-backstory.googleapis.com`
  * [Jakarta](https://cloud.google.com/about/locations#asia-pacific)—`https://asia-southeast2-backstory.googleapis.com`
  * [Johannesburg](https://cloud.google.com/about/locations#africa-south1)—`https://africa-south1-backstory.googleapis.com`
  * [London](https://cloud.google.com/about/locations#europe)—`https://europe-west2-backstory.googleapis.com`
  * [Mumbai](https://cloud.google.com/about/locations#asia-pacific)—`https://asia-south1-backstory.googleapis.com`
  * [Paris](https://cloud.google.com/about/locations#europe)—`https://europe-west9-backstory.googleapis.com`
  * [Warsaw](https://cloud.google.com/about/locations#europe)—`https://europe-central2-backstory.googleapis.com`
  * [Singapore](https://cloud.google.com/about/locations#asia-pacific)—`https://asia-southeast1-backstory.googleapis.com`
  * [Sydney](https://cloud.google.com/about/locations#asia-pacific)—`https://australia-southeast1-backstory.googleapis.com`
  * [Tel Aviv](https://cloud.google.com/about/locations#middle-east)—`https://me-west1-backstory.googleapis.com`
  * [Tokyo](https://cloud.google.com/about/locations#asia-pacific)—`https://asia-northeast1-backstory.googleapis.com`
  * [Turin](https://cloud.google.com/about/locations#europe)—`https://europe-west12-backstory.googleapis.com`
  * [United States Multi-Region](https://cloud.google.com/about/locations#multi-region)—`https://backstory.googleapis.com`
  * [Zurich](https://cloud.google.com/about/locations#europe)—`https://europe-west6-backstory.googleapis.com`



## Feed Schema API reference

The Feed Schema API returns information that is useful for constructing valid feed management API requests. For example, you can get the data structure representing the entire feed schema. This structure defines the specific fields to specify for each valid combination of feed source type and log type. Alternatively, you can get a list of all log types compatible with a particular feed source type.

Specifically, the feed schema contains:

  * Information about each valid feed source type: 
    * A human-readable name
    * A human-readable description
    * Whether feeds with a given feed source type can be modified using the API, or are read-only
  * Information about each log type: 
    * A human-readable name
    * Whether feeds with a given log type can be modified using the API, or are read-only
  * Which log types are compatible with which feed source types
  * Information about the specific fields to specify for each valid combination of log type and feed source type: 
    * A human-readable field name and description
    * Compatibility with other fields
    * Semantic type (e.g. URI, "secret", etc)
    * Whether the field is required
    * What a valid value for the field looks like



The schema can be accessed using a few different methods.

### GetFeedSchema

This method returns a structure representing the entire feed schema. The schema is comprised of a list of "feed source type schemas" each of which describe the supported feed source types. Each feed source types' schema contains a list of "log type schemas" that correspond to the set of log types that are compatible with the feed source type and describe the log type. Each log type schema contains a list of "details field schemas" that describe those fields you would set when issuing a create feed request, for example, or expect to see as a result of a ListFeed or GetFeed response. The field schemas specified are unique to the particular combination of log type and feed source type.

**Note:** GetFeedSchema uses the GET method. The request body must be empty.

Request
    
    
    GET https://backstory.googleapis.com/v1/feedSchema
    

Response
    
    
    {
      "feedSourceTypeSchemas": [{
          "name": "feedSourceTypeSchemas/AMAZON_S3",
          "displayName": "Amazon S3",
          "description": "Amazon S3, a service offered by Amazon Web Services that provides object storage through a web service interface",
          "feedSourceType": "AMAZON_S3",
          "logTypeSchemas": [{
              "name": "feedSourceTypeSchemas/AMAZON_S3/logTypeSchemas/AWS_CLOUDTRAIL",
              "displayName": "AWS Cloudtrail",
              "logType": "AWS_CLOUDTRAIL",
              "detailsFieldSchemas": [{
                  "fieldPath": "details.amazon_s3_settings.authentication.accessKeyId",
                  "displayName": "Access key ID",
                  "description": "An account access key that is a 20-character alphanumeric string, for example AKIAIOSFODNN7EXAMPLE",
                  "type": "STRING",
                  "exampleInput": "AKIAIOSFODNN7EXAMPLE",
                },
                ...
                {
                  "fieldPath": "details.amazon_s3_settings.s3Uri",
                  "displayName": "S3 URI",
                  "description": "The S3 bucket source URI",
                  "type": "STRING_URI",
                  "isRequired": true,
                  "exampleInput": "s3://cs-prod-cannon-00afe0c847a8/data/",
                }],
            },
            ...
            {
              "name": "feedSourceTypeSchemas/AMAZON_S3/logTypeSchemas/ABNORMAL_SECURITY",
              "displayName": "Abnormal Security",
              "logType": "ABNORMAL_SECURITY",
              ...
            }],
        },
        ...
        {
          "name": "feedSourceTypeSchemas/AMAZON_SQS",
          "displayName": "Amazon SQS",
          "description": "Amazon Simple Queue Service, a service offered by Amazon Web Services that provides fully managed message queuing service to transfer messages asynchronously",
          "feedSourceType": "AMAZON_SQS",
          ...
        }],
    }
    

**Note:** The `field_path` field can be used to refer to a particular field in a request body, but it is not in JSON format. It is a period-delimited path of snake_case fields, whereas the fields as they appear in a JSON-formatted request body are all camelCase.

### ListFeedSourceTypeSchemas

This method returns information about all feed source types.

**Note:** ListFeedSourceTypeSchemas uses the GET method. The request body should be empty.

##### Request
    
    
    GET https://backstory.googleapis.com/v1/feedSourceTypeSchemas
    

###### Sample Response
    
    
    {
      "feedSourceTypeSchemas": [{
          "name": "feedSourceTypeSchemas/AMAZON_S3",
          "displayName": "Amazon S3",
          "description": "Amazon S3, a service offered by Amazon Web Services that provides object storage through a web service interface",
          "feedSourceType": "AMAZON_S3",
        },
        ...
        {
          "name": "feedSourceTypeSchemas/AMAZON_SQS",
          "displayName": "Amazon SQS",
          "description": "Amazon Simple Queue Service, a service offered by Amazon Web Services that provides fully managed message queuing service to transfer messages asynchronously",
          "feedSourceType": "AMAZON_SQS",
        }],
    }
    

### ListLogTypeSchemas

This method returns information about all log types compatible with a particular feed source type.

**Note:** ListLogTypeSchemas uses the GET method. The request body should be empty.

##### Request
    
    
    GET https://backstory.googleapis.com/v1/feedSourceTypeSchemas/{feed source type}/logTypeSchemas
    

###### Sample Request
    
    
    https://backstory.googleapis.com/v1/feedSourceTypeSchemas/AMAZON_S3/logTypeSchemas
    

###### Sample Response
    
    
    {
      "logTypeSchemas": [{
          "name": "feedSourceTypeSchemas/AMAZON_S3/logTypeSchemas/AWS_CLOUDTRAIL",
          "displayName": "AWS Cloudtrail",
          "logType": "AWS_CLOUDTRAIL",
        },
        ...
        {
          "name": "feedSourceTypeSchemas/AMAZON_S3/logTypeSchemas/ABNORMAL_SECURITY",
          "displayName": "Abnormal Security",
          "logType": "ABNORMAL_SECURITY",
          ...
        }],
    }
    

### GetLogTypeSchema

This method returns detailed information about all the fields necessary to configure a feed for a particular source type and log type.

**Note:** GetLogTypeSchema uses the GET method. The request body must be empty.

##### Request
    
    
    GET https://backstory.googleapis.com/v1/feedSourceTypeSchemas/{feed source type}/logTypeSchemas/{log type}
    

###### Sample Request
    
    
    https://backstory.googleapis.com/v1/feedSourceTypeSchemas/AMAZON_S3/logTypeSchemas/AWS_CLOUDTRAIL
    

###### Sample Response
    
    
    {
      "name": "feedSourceTypeSchemas/AMAZON_S3/logTypeSchemas/AWS_CLOUDTRAIL",
      "displayName": "AWS Cloudtrail",
      "logType": "AWS_CLOUDTRAIL",
      "detailsFieldSchemas": [{
          "fieldPath": "details.amazon_s3_settings.authentication.accessKeyId",
          "displayName": "Access key ID",
          "description": "An account access key that is a 20-character alphanumeric string, for example AKIAIOSFODNN7EXAMPLE",
          "type": "STRING",
          "exampleInput": "AKIAIOSFODNN7EXAMPLE",
        },
        ...
        {
          "fieldPath": "details.amazon_s3_settings.s3Uri",
          "displayName": "S3 URI",
          "description": "The S3 bucket source URI",
          "type": "STRING_URI",
          "isRequired": true,
          "exampleInput": "s3://cs-prod-cannon-01abc2d345e6/data/",
        }],
    }
    

**Note:** The `field_path` field can be used to refer to a particular field in a request body, but it is not in JSON format. It is a period-delimited path of snake_case fields, whereas the fields as they appear in a JSON-formatted request body are all camelCase.

## Feed management API reference

This section describes the endpoints for creating, enabling, and managing feeds.

When creating or editing a feed, you need to specify the `feedSourceType` and `logType` in the request body. For details about these fields, see Configuration by source type and Configuration by log type.

### Create feed

Creates a third party data feed in your Google SecOps instance. For third-party API connectors, the system validates credentials during the API call. If validation fails, the system does not create the feed and returns an API error.

**Note:** Create feed uses the POST method.

#### Request
    
    
    POST https://backstory.googleapis.com/v1/feeds
    

##### Request body

**Note:** The following is an example of a request body that changes based on the feed source type and log type of the feed. Refer to Configuration by source type and Configuration by log type for how to build the request message for any supported feed.

This example shows how to collect authentication logs from Duo Security.
    
    
    {
      "display_name": "some feed name",
      "details": {
        "feedSourceType": "API",
        "logType": "DUO_AUTH",
        "duoAuthSettings": {
          "authentication": {
            "user": "ABCUSERNAMEDEF",
            "secret": "aBcS3cReTdEf"
          },
          "hostname": "api-abc123.duosecurity.com"
        },
        "namespace": "my-asset-namespace",
        "labels": [{
          "key": "my-ingestion-label-key",
          "value": "my-ingestion-label-value"
        }]
      }
    }
    
    

##### Sample request
    
    
    https://backstory.googleapis.com/v1/feeds
    {
      "display_name": "some feed name",
      "details": {
        "feedSourceType": "API",
        "logType": "DUO_AUTH",
        "duoAuthSettings": {
          "authentication": {
            "user": "ABCUSERNAMEDEF",
            "secret": "aBcS3cReTdEf"
          },
          "hostname": "api-abc123.duosecurity.com"
        }
      }
    }
    

##### Sample successful response
    
    
    {
     "name": "feeds/12a34567-bc8d-1111-e9f0-gh1ijk234567",
     "display_name": "some feed name",
     "details": {
       "logType": "DUO_AUTH",
       "feedSourceType": "API",
       "duoAuthSettings": {
         "hostname": "api-abc123.duosecurity.com"
       }
     },
     "feedState": "ACTIVE"
    }
    

If the response is unsuccessful, it returns an HTTP status code other than 200 (OK). Be sure to check the body of the response for details of the failure.

#### Asset namespace

To assign an [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces) to all events that are ingested from a particular feed, set the `"namespace"` field within `details`. The `namespace` field is a string.

#### Ingestion label

Ingestion labels are part of [Unified Data Model metadata](https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list#metadata). They are repeated key and value pairs. To assign ingestion labels to all events that are ingested from a particular feed, set the `labels` field within `details`. The `labels` field is an array of JSON objects with `key` and `value` fields.

### Delete Feed

Deletes a feed that was configured using the Google SecOps feed management API.

**Note:** Delete Feed uses the `DELETE` method.

#### Request
    
    
    DELETE  https://backstory.googleapis.com/v1/feeds/{feedID}
    

##### Sample request
    
    
    DELETE https://backstory.googleapis.com/v1/feeds/12a34567-bc8d-1111-e9f0-gh1ijk234567
    

##### Sample response

If the operation is successful, Delete Feed returns an empty response with an HTTP status code 200 (OK).
    
    
    {}
    

### Enable Feed

Enables an `INACTIVE` feed, which allows it to be executed.

**Note:** Enable Feed uses the POST method.

##### Request
    
    
    POST https://backstory.googleapis.com/v1/feeds/{feedID}:enable
    

###### Sample request
    
    
    POST https://backstory.googleapis.com/v1/feeds/12a34567-bc8d-1111-e9f0-gh1ijk234567:enable
    

###### Sample response
    
    
    {
     "name": "feeds/12a34567-bc8d-1111-e9f0-gh1ijk234567",
     "display_name": "some feed name",
     "details": {
       "logType": "DUO_AUTH",
       "feedSourceType": "API",
       "duoAuthSettings": {
         "hostname": "api-abc123.duosecurity.com"
       }
     },
     "feedState": "ACTIVE"
    }
    

### Disable Feed

Disables a feed. A disabled feed has a status of `INACTIVE`. Disabled feeds will no longer fetch data.

**Note:** Disable Feed uses the POST method.

##### Request
    
    
    POST https://backstory.googleapis.com/v1/feeds/{feedID}:disable
    

###### Sample request
    
    
    POST https://backstory.googleapis.com/v1/feeds/12a34567-bc8d-1111-e9f0-gh1ijk234567:disable
    

###### Sample response
    
    
    {
     "name": "feeds/12a34567-bc8d-1111-e9f0-gh1ijk234567",
     "display_name": "some feed name",
     "details": {
       "logType": "DUO_AUTH",
       "feedSourceType": "API",
       "duoAuthSettings": {
         "hostname": "api-abc123.duosecurity.com"
       }
     },
     "feedState": "INACTIVE"
    }
    

### Get Feed

Gets the details of the feed that was configured.

**Note:** Fields used to authenticate with a third-party are not returned in the response.

#### Request
    
    
    GET https://backstory.googleapis.com/v1/feeds/{feedID}
    

##### Sample request
    
    
    https://backstory.googleapis.com/v1/feeds/12a34567-bc8d-1111-e9f0-gh1ijk234567
    

##### Sample response
    
    
    {
     "name": "feeds/12a34567-bc8d-1111-e9f0-gh1ijk234567",
     "display_name": "some feed name",
     "details": {
       "logType": "DUO_AUTH",
       "feedSourceType": "API",
       "duoAuthSettings": {
         "hostname": "api-abc123.duosecurity.com"
       }
     },
     "feedState": "FAILED",
    "last_feed_initiation_time": "2024-01-15T01:30:15.01Z",
    "failure_details": {
      "error_code": "INVALID_ARGUMENT"
      "http_error_code": 400,
      "error_cause": "A connection to the source was established, but the feed failed because of invalid arguments",
      "error_action":"Check the feed configuration. Learn more about setting up the feeds.\nIf the problem continues, contact Chronicle Support"
     }
    }
    

### List Feeds

Retrieves all the feeds configured for a given Google SecOps instance.

**Note:** Fields used to authenticate with a third-party are not returned in the response.**Note:** List Feeds uses the GET method.

##### Request
    
    
    GET https://backstory.googleapis.com/v1/feeds
    

###### Sample request
    
    
    https://backstory.googleapis.com/v1/feeds
    

###### Sample response
    
    
    {
     "feeds": [
       {
         "name": "feeds/12a34567-bc8d-1111-e9f0-gh1ijk234567",
         "details": {
           "logType": "AZURE_AD_CONTEXT",
           "feedSourceType": "API",
           "azureAdContextSettings": {}
         },
         "feedState": "FAILED",
      "last_feed_initiation_time": "2024-01-15T01:30:15.01Z",
      "failure_details": {
        "error_code": "INVALID_ARGUMENT"
        "http_error_code": 400,
        "error_cause": "A connection to the source was established, but the feed failed because of invalid arguments",
        "error_action":"Check the feed configuration. Learn more about setting up the feeds.\nIf the problem continues, contact Chronicle Support"
       }
       },
       {
         "name": "feeds/12a34567-bc8d-1111-e9f0-gh1ijk234567",
         "display_name": "some feed name",
         "details": {
           "logType": "PAN_PRISMA_CLOUD",
           "feedSourceType": "API",
           "panPrismaCloudSettings": {
             "hostname": "api2.prismacloud.io"
           }
         },
         "feedState": "ACTIVE",
      "last_feed_initiation_time": "2024-01-15T01:30:15.01Z",
       }
     ]
    }
    

#### Read-only feeds

There may be feeds returned from a List Feeds request that have the field `readOnly` set to `true`. Read-only feeds cannot be created, updated, or deleted.

Feeds are read-only for a few reasons. For example:

  * Some feed source types are not fully supported by feed management at the moment, or were created before the release of feed management.
  * Some specialized log types are not available to every Google SecOps user. If a feed exists with one of these types, it is considered read-only.



### Update Feed

Updates the given feed with new details.

**Note:** Update Feed uses the PATCH method.

##### Request
    
    
    PATCH https://backstory.googleapis.com/v1/feeds/{feedID}
    

###### Request body

**Note:** The following is an example of a request body that changes based on the feed source type and log type of the feed. Refer to Configuration by source type and Configuration by log type for how to build the request message for any supported feed.

The following examples shows how to update a Duo Auth feed.

###### Sample request
    
    
    {
      "display_name": "my feed",
      "details": {
        "feedSourceType": "API",
        "logType": "DUO_AUTH",
        "duoAuthSettings": {
          "authentication": {
            "user": "ABCUSERNAMEDEF",
            "secret": "aBcS3cReTdEf"
          },
          "hostname": "api-abc123.duosecurity.com"
        }
      }
    }
    

###### Sample response
    
    
    {
     "display_name": "my feed",
     "name": "feeds/12a34567-bc8d-1111-e9f0-gh1ijk234567",
     "details": {
       "logType": "DUO_AUTH",
       "feedSourceType": "API",
       "duoAuthSettings": {
         "hostname": "api-abc123.duosecurity.com"
       }
     },
     "feedState": "ACTIVE"
    }
    

**Note:** The display_name should be unique. It should only be included if the user intends to update the display_name. Otherwise, don't include display_name in the request.

##### Sample Request that does not update displayName
    
    
    {
     "name": "feeds/12a34567-bc8d-1111-e9f0-gh1ijk234567",
     "details": {
       "logType": "DUO_AUTH",
       "feedSourceType": "API",
       "duoAuthSettings": {
         "hostname": "api-abc123.duosecurity.com"
       }
     },
     "feedState": "ACTIVE"
    }
    

### Fetch service account

Gets a unique service account that Google Security Operations uses to ingest data. Use this method only if you're setting up a Cloud Storage feed. You can also obtain this service account using the Google SecOps console. See [Google Cloud Storage feed setup example](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#storage-example).

##### Request
    
    
    GET https://backstory.googleapis.com/v1/fetchFeedServiceAccount
    

###### Sample request
    
    
    GET https://backstory.googleapis.com/v1/fetchFeedServiceAccount
    

###### Sample response
    
    
    "serviceAccount": "xxxxxxxx-0-account@partnercontent.gserviceyesaccount.com"
    

## Response message fields

This section describes the following fields that are returned in response messages:

  * `feedState`
  * `failureMsg`



### Feed state

The `feedState` field can be found in the response message of most operations. `feedState` gives some insight into the current state of a feed.

`feedState` | Description  
---|---  
`"ACTIVE"` | Feed successfully created and fetching data.  
`"INACTIVE"` | Feed has been disabled.  
`"IN_PROGRESS"` | Feed is attempting to fetch data. A feed will only have this status if it has not previously failed.  
`"COMPLETED"` | Feed has recently fetched data successfully.  
`"FAILED"` | Feed has failed and has not successfully fetched data since it failed. Mis-configuration is the typical cause of feed failure. Please see the `failureMsg` field for more information.  
  
### Failure message

The `failureMsg` field can be found in the response message of most operations, but only for those feeds whose `feedState` is `FAILED`. It provides information regarding the error code, cause of the error, and how to troubleshoot the error. For information about error messages, see [Troubleshooting](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#troubleshooting). Refer to the following documentation for your particular feed type to understand how to correctly configure the feed.

## Generate secret key and API key to authenticate the feed

You need to generate the secret key and API key to authenticate the feed when you set up a feed that has webhook or Amazon Data Firehose as the source type. You can reuse your existing API key to authenticate to Google Security Operations. You must generate a secret key for every new feed and can't reuse the secret key.

**Note:** The secret key is restricted to `chronicle.googleapis.com`. To further restrict the key, allow the `ImportPushLogs` method. For more information, see [Restricting API keys](https://docs.cloud.google.com/api-keys/docs/add-restrictions-api-keys#add-api-restrictions).

  1. To generate a secret key for a webhook or Amazon Data Firehose feed, run the following `curl` command that uses the `generateSecret` Backstory API.
         
         curl --location --request POST -H "Authorization: Bearer $(gcloud auth print-access-token)" 'https://REGIONAL_ENDPOINT/v1alpha/projects/PROJECT_NUMBER/locations/REGION_ID/instances/CUSTOMER_ID/feeds/FEED_ID:generateSecret'
         

Replace the following:

     * `REGIONAL_ENDPOINT`: the Google Security Operations regional endpoint, such as `us-chronicle.googleapis.com`. For information about supported regional endpoints, see Google Security Operations regional endpoints section of this document.
     * `PROJECT_NUMBER`: an automatically generated unique identifier for your project. For information about project name, project ID, and project number, which are used to identify a project, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin).
     * `REGION_ID`: the code that Google assigns based on the region. The following are the supported region IDs: `Asia-Southeast1`, `Australia-Southeast1`, `Europe`, `EU`, `Europe-West2`, `Europe-West3`, `Europe-West6`, `Govcloud-US`, `Me-West1`, and `US`.
     * `CUSTOMER_ID`: the Google Security Operations customer ID.
     * `FEED_ID`: the Google Security Operations feed ID.

A secret key is returned. Copy and store the secret key because you cannot view this secret again. You can use the `generateSecret` API again to generate a new secret key, but regeneration of the secret key makes the previous secret key obsolete.

  2. To generate the API key, do the following:

     1. Go to the Google Cloud console [Credentials](https://console.cloud.google.com/apis/credentials) page.
     2. Click **Create credentials** , and then select **API key**.
     3. Restrict the API key access to the Backstory API.



## Configuration by source type

This section provides information about configuring feed source types. A feed source type defines where data is located and how it's accessed. Valid values for `feedSourceType` are as follows:

**`feedSourceType`** | **Description** | `API` | Ingest data from a third-party API.  
---|---  
`HTTPS_PUSH_GOOGLE_CLOUD_PUBSUB` | Ingest data using a Pub/Sub push subscription.  
`GOOGLE_CLOUD_STORAGE (Deprecated)` | Ingest data from a Cloud Storage bucket.  
`GOOGLE_CLOUD_STORAGE_V2` | Ingest data from a Cloud Storage bucket.  
`GOOGLE_CLOUD_STORAGE_EVENT_DRIVEN` | Ingest data from a Cloud Storage bucket, using a Pub/Sub subscription, where each entry references files stored in a Cloud Storage bucket.  
`HTTPS_PUSH_AMAZON_KINESIS_FIREHOSE` | Ingest data from Amazon Data Firehose.  
`AMAZON_S3 (Deprecated)` | Ingest data from an Amazon S3 bucket.  
`AMAZON_S3_V2` | Ingest data from an Amazon S3 bucket.  
`AMAZON_SQS` | Ingest data from an Amazon SQS queue, where each entry references files stored in Amazon S3.  
`AMAZON_SQS_V2` | Ingest data from an Amazon SQS queue, where each entry references files stored in Amazon S3.  
`AZURE_BLOBSTORE (Deprecated)` | Ingest data from Azure Blob Storage containers.  
`AZURE_BLOBSTORE_V2` | Ingest data from Azure Blob Storage containers.  
`AZURE_EVENT_HUB` | Ingest data directly from a Microsoft Azure Event hub.  
`HTTP` | Ingest data from files accessible by an HTTP(S) request. Note: This **shouldn't** be used to interact with third-party APIs. Use the `API` feed source type for third-party APIs supported by Google Security Operations.  
`HTTPS_PUSH_WEBHOOK` | Ingest data using an HTTPS webhook.  
  
**Note:** Bucket-based feeds such as Cloud Storage, Amazon S3, and Azure Blobstore don't ingest logs in real-time. The log latency depends on the pull frequency of the corresponding feed.

## API

Use the `API` feed source type to ingest data from a third-party API.

**Note:** You must enable allowlisting and add the IP ranges from [goog.json](https://www.gstatic.com/ipranges/goog.json) and [cloud.json](https://www.gstatic.com/ipranges/cloud.json) for all log types that ingest data from third-party APIs. For more information, see Set up IP allowlisting.

The configuration settings for the `API` feed source type depend on the log type that you specify. For details, see Configuration by log type.

## Google Cloud Pub/Sub

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
Pub/Sub  | Based on your implementation, it might take approximately a minute for a new feed to populate because Google Security Operations takes some time to process the data. | `HTTPS_PUSH_GOOGLE_CLOUD_PUBSUB`  
  
### Prerequisites

  * Ensure that a [Google Cloud project for Google Security Operations is configured](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project) and the Backstory API is enabled for the project.
  * [Link a Google Security Operations instance to Google Cloud services](https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud).



### Set up push ingestion using Pub/Sub

Data can be sent to Google Security Operations using Pub/Sub. You must first create a feed with the appropriate log type before configuring Pub/Sub to send data.

**Note:** If you need to push logs from an additional Google Cloud project that isn't bound to your Google Security Operations tenant, such as from a user-managed service account, you must set up a log sink. For more information about log sinks, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#overview).

To set up HTTPS push ingestion using Pub/Sub, do the following:

  1. Create a Pub/Sub feed using the following [`create`](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.feeds/create) API request:
         
         {
             "displayName": "FEED_NAME",
             "details": {
               "feedSourceType": "HTTPS_PUSH_GOOGLE_CLOUD_PUBSUB",
               "logType": "projects/PROJECT_ID/locations/REGION_ID/instances/CUSTOMER_ID/logTypes/LOG_TYPE"
             }
           }
         

Replace the following:

     * `FEED_NAME`: specify a name for the feed.
     * `PROJECT_ID`: the project ID of the project that is bound to Google Security Operations.
     * `REGION_ID`: the region configured for your Google Security Operations instance. This was set when the tenant was provisioned. The following are the supported region IDs: `Asia-Southeast1`, `Australia-Southeast1`, `Europe`, `EU`, `Europe-West2`, `Europe-West3`, `Europe-West6`, `Govcloud-US`, `Me-West1`, and `US`.
     * `CUSTOMER_ID`: the Google Security Operations customer ID.
     * `LOG_TYPE`: the type of data the feed ingests. Google Security Operations supports specific log types for the Pub/Sub feed.

If the data to be ingested contains a delimiter that separate log lines, such as `\\n`, include the following in the `details` field of the feed request body:
    
    "httpsPushGoogleCLoudPubsubSettings": {
        "splitDelimiter": "LOG_DELIMITER"
      }
    

Replace `LOG_DELIMITER` with the delimiter that separates the log lines, such as `\\n`.

  2. After you create a feed in Pub/Sub, create a push subscription, specify the HTTPS endpoint, and enable authentication. For more information about how to create a push subscription, see [Create push subscriptions](https://docs.cloud.google.com/pubsub/docs/create-push-subscription).

     * Specify the endpoint URL. The endpoint URL must have the following format: `https://REGIONAL_ENDPOINT/v1alpha/projects/PROJECT_ID/ locations/REGION_ID/instances/CUSTOMER_ID/feeds/FEED_ID:importPushLogs`

       * `REGIONAL_ENDPOINT`: the Google Security Operations regional endpoint, such as `us-chronicle.googleapis.com`. For information about supported regional endpoints, see Google Security Operations regional endpoints section of this document.
       * `PROJECT_ID`: the project ID of the project that is bound to Google Security Operations.
       * `REGION_ID`: the region configured for your Google Security Operations instance. This was set when the tenant was provisioned. The following are the supported region IDs: `Asia-Southeast1`, `Australia-Southeast1`, `Europe`, `EU`, `Europe-West2`, `Europe-West3`, `Europe-West6`, `Govcloud-US`, `Me-West1`, and `US`.
       * `CUSTOMER_ID`: the Google Security Operations customer ID.
       * `FEED_ID`: the Google Security Operations feed ID.
     * Select **Enable authentication** and select a service account.




## GOOGLE_CLOUD_STORAGE

**Caution:** The `GOOGLE_CLOUD_STORAGE` (v1) connector is deprecated and will be discontinued on **March 15, 2027**. After this date, v1 feeds will stop returning data. You must migrate to the GOOGLE_CLOUD_STORAGE_V2 connector, which uses the Google Cloud Storage Transfer Service (STS), to ensure continued data ingestion. For more information, see [Feature deprecations](https://docs.cloud.google.com/chronicle/docs/deprecations).Data source | Ingest schedule | `details.feedSourceType` | `details.logType`  
---|---|---|---  
Google Cloud Storage Bucket | Every 15 minutes. This cannot be altered.  | `GOOGLE_CLOUD_STORAGE` | See the Feed Schema API reference to get compatible log types.  
  
### Prerequisites

Before you set up a Cloud Storage feed, you must get a Google Security Operations service account and provide access to the account so that Google Security Operations can ingest data.

  1. Obtain a Google Security Operations service account using one of the following methods:

     * Programmatically, using the `fetchFeedServiceAccount` method.
     * Using the [Google SecOps console](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#storage-example).
  2. Grant access to the Google Security Operations service account to the relevant Cloud Storage objects. For more information, see [Grant access to the Google Security Operations service account](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#grant-sa-access).

  3. If VPC Service Controls is enabled, configure an ingress rule to provide access to the Cloud Storage bucket. For details, see [Configure VPC Service Controls](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#configure-vpcsc).




### Recommendations

  * If your Cloud Storage bucket contains many small files, data transfer may take longer. To speed up the feed transfer process, we recommend combining smaller files into a single, larger file.

  * [Set a data retention policy](https://docs.cloud.google.com/storage/docs/using-bucket-lock#set-policy) on your Cloud Storage buckets to ensure that transferred files are deleted and not listed in future transfer feeds. Alternatively, you can use the Google SecOps feed management page to set the option to [delete the source files](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#delete_source_files) from the storage buckets after they have been transferred.

  * Because Google SecOps pulls files from Cloud Storage on a frequent basis, we recommend to specify the most cost-effective [storage class for your containers](https://docs.cloud.google.com/storage/docs/storage-classes#classes).




### Type-specific request fields

**Field** | **Required** | **Description**  
---|---|---  
`details.gcsSettings.bucketUri` | Yes | The Cloud Storage bucket's URI. Use the same format to specify a resource as is used by the [`gcloud storage`](https://docs.cloud.google.com/sdk/gcloud/reference/storage) command group.  
`details.gcsSettings.sourceType` | Yes | The type of object specified by `bucketUri`. Valid values are: 

  * `FILES`: The URI points to a single file ingested with each execution of the feed.
  * `FOLDERS`: The URI points to a directory. All files within the directory are ingested each time the feed is executed.
  * `FOLDERS_RECURSIVE`: The URI points to a directory. All files and subdirectories within the directory, including those within any nested directories, will be ingested.

  
`details.gcsSettings.sourceDeletionOption` | Yes | Whether to delete source files after they have been transferred to Google Security Operations. This reduces storage costs. Valid values are: 

  * `SOURCE_DELETION_NEVER`: Never delete files from the source.
  * `SOURCE_DELETION_ON_SUCCESS`: Delete files and empty directories from the source after successful ingestion.
  * `SOURCE_DELETION_ON_SUCCESS_FILES_ONLY`: Delete source files after successful ingestion.

  
  
#### Sample create feed request
    
    
    {
     "details": {
       "feedSourceType": "GOOGLE_CLOUD_STORAGE",
       "logType": "LOGTYPE_YOU_WANT_TO_BRING",
       "gcsSettings": {
         "bucketUri": "gs://bucket/folder/",
         "sourceType": "FOLDERS_RECURSIVE",
         "sourceDeletionOption": "SOURCE_DELETION_NEVER"
       }
     }
    }
    

## GOOGLE_CLOUD_STORAGE_V2

Data source | Ingest schedule | `details.feedSourceType` | `details.logType`  
---|---|---|---  
Google Cloud Storage Bucket | Every 15 minutes. This cannot be altered.  | `GOOGLE_CLOUD_STORAGE_V2` | See the Feed Schema API reference to get compatible log types.  
  
### Prerequisites

Before you set up a Cloud Storage feed, you must get a Google Security Operations service account and provide access to the account so that Google Security Operations can ingest data.

  1. Obtain a Google Security Operations service account using one of the following methods:

     * Programmatically, using the `fetchFeedServiceAccount` method.
     * Using the [Google SecOps console](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#storage-example).
  2. Grant access to the Google Security Operations service account to the relevant Cloud Storage objects. For more information, see [Grant access to the Google Security Operations service account](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#grant-sa-access).

  3. If VPC Service Controls is enabled, configure an ingress rule to provide access to the Cloud Storage bucket. For details, see [Configure VPC Service Controls](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#configure-vpcsc).




### Recommendations

  * If your Cloud Storage bucket contains many small files, data transfer may take longer. To speed up the feed transfer process, we recommend combining smaller files into a single, larger file.

  * [Set a data retention policy](https://docs.cloud.google.com/storage/docs/using-bucket-lock#set-policy) on your Cloud Storage buckets to ensure that transferred files are deleted and not listed in future transfer feeds. Alternatively, you can use the Google SecOps feed management page to set the option to [delete the source files](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#delete_source_files) from the storage buckets after they have been transferred.

  * Because Google SecOps pulls files from Cloud Storage on a frequent basis, we recommend to specify the most cost-effective [storage class for your containers](https://docs.cloud.google.com/storage/docs/storage-classes#classes).




### Type-specific request fields

**Field** | **Required** | **Description**  
---|---|---  
`details.gcsV2Settings.bucketUri` | Yes | The Cloud Storage bucket's URI. Use the same format to specify a resource as is used by the [`gcloud storage`](https://docs.cloud.google.com/sdk/gcloud/reference/storage) command group.  
`details.gcsV2Settings.sourceDeletionOption` | Yes | Option to delete source files from the source bucket after transfer to Google SecOps, reducing storage costs. Valid values are:  


  * `NEVER`: Never delete files from the source.
  * `ON_SUCCESS`: Delete files and empty directories from the source after successful ingestion.

  
`details.gcsV2Settings.maxLookbackDays` | Yes | Maximum file age (days since file last modified) of files to include. The maximum limit and the default value is 180 days.  
  
#### Sample create feed request
    
    
    {
     "details": {
       "feedSourceType": "GOOGLE_CLOUD_STORAGE_V2",
       "logType": "LOGTYPE_YOU_WANT_TO_BRING",
       "gcsV2Settings": {
         "bucketUri": "gs://bucket/folder/",
         "sourceDeletionOption": "ON_SUCCESS",
         "maxLookbackDays": 30
       }
     }
    }
    

## GOOGLE_CLOUD_STORAGE_EVENT_DRIVEN

Data source | `details.feedSourceType` | `details.logType`  
---|---|---  
Google Cloud Storage Bucket | `GOOGLE_CLOUD_STORAGE_EVENT_DRIVEN` | See the Feed Schema API reference to get compatible log types.  
  
### Prerequisites

Before you set up a Cloud Storage feed, you must get a Google Security Operations service account and provide access to the account so that Google Security Operations can ingest data.

  1. Obtain a Google Security Operations service account using one of the following methods:

     * Programmatically, using the `fetchFeedServiceAccount` method.
     * Using the [Google SecOps console](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#storage-example).
  2. Grant access to the Google Security Operations service account to the relevant Cloud Storage objects. For more information, see [Grant access to the Google Security Operations service account](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#grant-sa-access).

  3. If VPC Service Controls is enabled, configure an ingress rule to provide access to the Cloud Storage bucket. For details, see [Configure VPC Service Controls](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#configure-vpcsc).

  4. Grant the `Pub/Sub Subscriber` role to the Google SecOps service account.




### Recommendations

  * If your Cloud Storage bucket contains many small files, data transfer may take longer. To speed up the feed transfer process, we recommend combining smaller files into a single, larger file.

  * [Set a data retention policy](https://docs.cloud.google.com/storage/docs/using-bucket-lock#set-policy) on your Cloud Storage buckets to ensure that transferred files are deleted and not listed in future transfer feeds. Alternatively, you can use the Google SecOps feed management page to set the option to [delete the source files](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#delete_source_files) from the storage buckets after they have been transferred.

  * Because Google SecOps pulls files from Cloud Storage on a frequent basis, we recommend to specify the most cost-effective [storage class for your containers](https://docs.cloud.google.com/storage/docs/storage-classes#classes).


**Note:** Using GOOGLE_CLOUD_STORAGE_EVENT_DRIVEN enables direct Cloud Storage ingestion with a pull frequency of 15 seconds.

### Set up a Pub/Sub subscription for Cloud Storage

Set up a Pub/Sub subscription for Cloud Storage, as described in [Configure Pub/Sub](https://docs.cloud.google.com/storage-transfer/docs/event-driven-google#configure_pub_sub).

### Type-specific request fields

**Field** | **Required** | **Description**  
---|---|---  
`details.google_cloud_storage_event_driven_settings.bucketUri` | Yes | The Cloud Storage bucket's URI. Use the same format to specify a resource as is used by the [`gcloud storage`](https://docs.cloud.google.com/sdk/gcloud/reference/storage) command group.  
`details.google_cloud_storage_event_driven_settings.pubsub_subscription` | Yes | This is the subscription name on the Pub/Sub topic that you created for your transfer job.  
`details.google_cloud_storage_event_driven_settings.sourceDeletionOption` | Yes | Option to delete source files from the source bucket after transfer to Google SecOps, reducing storage costs. Valid values are:  


  * `NEVER`: Never delete files from the source.
  * `ON_SUCCESS`: Delete files and empty directories from the source after successful ingestion.

  
`details.google_cloud_storage_event_driven_settings.maxLookbackDays` | Yes | Maximum file age (days since file last modified) of files to include. The maximum limit and the default value is 180 days.  
  
#### Sample create feed request
    
    
    {
     "details {
        feed_source_type: GOOGLE_CLOUD_STORAGE_EVENT_DRIVEN
        log_type: "LOGTYPE_YOU_WANT_TO_BRING"
        google_cloud_storage_event_driven_settings {
          bucket_uri: "gs://path/to/bucket/"
          pubsub_subscription: "projects/your-project/subscriptions/your-subscription"
          sourceDeletionOption": "ON_SUCCESS"
          max_lookback_days: 30
        }
      }
    }
    

## Amazon Data Firehose

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
Amazon Data Firehose  | Based on your implementation, it might take approximately a minute for a new feed to populate because Google Security Operations takes some time to process the data. | `HTTPS_PUSH_AMAZON_KINESIS_FIREHOSE`  
  
### Prerequisites

  * Ensure that a [Google Cloud project for Google Security Operations is configured](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project) and the Backstory API is enabled for the project.
  * [Link a Google Security Operations instance to Google Cloud services](https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud).



### Set up push ingestion using Amazon Data Firehose

Data can be sent to Google Security Operations using Amazon Data Firehose. You must first create a feed with the appropriate log type before configuring Amazon Data Firehose to send data.

To set up HTTPS push ingestion using Amazon Data Firehose, do the following:

  1. Create an Amazon Data Firehose feed using the following [`create`](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.feeds/create) API request:
         
         {
             "displayName": "FEED_NAME",
             "details": {
               "feedSourceType": "HTTPS_PUSH_AMAZON_KINESIS_FIREHOSE",
               "logType": "projects/PROJECT_NUMBER/locations/REGION_ID/instances/CUSTOMER_ID/logTypes/LOG_TYPE"
             }
           }
         

Replace the following:

     * `FEED_NAME`: specify a name for the feed.
     * `PROJECT_NUMBER`: an automatically generated unique identifier for your project. For information about project name, project ID, and project number, which are used to identify a project, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin).
     * `REGION_ID`: the region configured for your Google Security Operations instance. This was set when the tenant was provisioned. The following are the supported region IDs: `Asia-Southeast1`, `Australia-Southeast1`, `Europe`, `EU`, `Europe-West2`, `Europe-West3`, `Europe-West6`, `Govcloud-US`, `Me-West1`, and `US`.
     * `CUSTOMER_ID`: the Google Security Operations customer ID.
     * `LOG_TYPE`: the type of data the feed ingests. Google Security Operations supports specific log types for the Amazon Data Firehose feed.

If the data to be ingested contains a delimiter that separate log lines, such as `\\n`, include the following in the `details` field of the feed request body:
    
    "httpsPushAmazonKinesisFirehoseSettings": {
        "splitDelimiter": "LOG_DELIMITER"
      }
    

Replace `LOG_DELIMITER` with the delimiter that separates the log lines, such as `\\n`.

  2. After you create a feed, generate a secret key for the feed and generate an API key to authenticate to Google Security Operations.

  3. In Amazon Data Firehose, specify the HTTPS endpoint and access key.

     * Specify the endpoint URL. Here is a sample Amazon Data Firehose endpoint: `https://REGIONAL_ENDPOINT/v1alpha/projects/PROJECT_NUMBER/ locations/REGION_ID/instances/CUSTOMER_ID/feeds/FEED_ID%3AimportPushLogs?key=API_KEY`

**Note:** Amazon Data firehose doesn't support ":" (colon) in the endpoint URL. You must use "%3A" instead of ":" in the URL.

The endpoint includes the following values:

       * `REGIONAL_ENDPOINT`: the Google Security Operations regional endpoint, such as `us-chronicle.googleapis.com`. For information about supported regional endpoints, see Google Security Operations regional endpoints section of this document.
       * `PROJECT_NUMBER`: an automatically generated unique identifier for your project. For information about project name, project ID, and project number, which are used to identify a project, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin).
       * `REGION_ID`: the region configured for your Google Security Operations instance. This was set when the tenant was provisioned. The following are the supported region IDs: `Asia-Southeast1`, `Australia-Southeast1`, `Europe`, `EU`, `Europe-West2`, `Europe-West3`, `Europe-West6`, `Govcloud-US`, `Me-West1`, and `US`.
       * `CUSTOMER_ID`: the Google Security Operations customer ID.
       * `FEED_ID`: the Google Security Operations feed ID.
       * `API_KEY`: the API key value.
     * In the **Access key** field, specify the secret key that you obtained using the `generateSecret` API.




## AMAZON_S3

**Caution:** The `AMAZON_S3` (v1) connector is deprecated and will be discontinued on **March 15, 2027**. After this date, v1 feeds will stop returning data. You must migrate to the AMAZON_S3_V2 connector, which uses the Google Cloud Storage Transfer Service (STS), to ensure continued data ingestion. For more information, see [Feature deprecations](https://docs.cloud.google.com/chronicle/docs/deprecations).Data source | Ingest schedule | `details.feedSourceType` | `details.logType`  
---|---|---|---  
Amazon S3 Bucket | Every 15 minutes. This cannot be altered.  | `AMAZON_S3` | See the Feed Schema API reference to get compatible log types.   
  
### Prerequisites

  1. [Create an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
  2. [Create a security key](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html) for programmatic access.



To learn more about how to configure a feed to ingest data from an Amazon S3 bucket, see [Ingest AWS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/ingest-aws-logs-into-chronicle).

### Recommendations

  * If your S3 bucket contains many small files, data transfer may take longer. To speed up the feed transfer process, we recommend combining smaller files into a single, larger file.

  * Set a data retention policy on your S3 buckets to ensure transferred files are deleted and not included in future transfer feeds. Alternatively, you can use the Google SecOps feed management page to [delete the source files](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#delete_source_files) from the storage buckets after they've been transferred.

  * Using Amazon SQS as the source type is preferred over Amazon S3. When Amazon SQS is used, Google SecOps reads the Amazon S3 notifications sent to the Amazon SQS service and retrieves the corresponding files from the Amazon S3 bucket. This approach provides a push-based version of an Amazon S3 feed, helping to reduce ingestion latency.




### Type-specific request fields

**Field** | **Required** | **Description**  
---|---|---  
`details.amazonS3Settings.s3Uri` | Yes | The S3 URI to ingest.  
`details.amazonS3Settings.sourceType` | Yes | The type of file specified by the URI. Valid values are:  


  * `FILES`: The URI points to a single file ingested with each execution of the feed.
  * `FOLDERS`: The URI points to a directory. All files within the directory are ingested with each execution of the feed.
  * `FOLDERS_RECURSIVE`: The URI points to a directory. All files and subdirectories within the directory, including those within any nested directories, will be ingested.

  
`details.amazonS3Settings.sourceDeletionOption` | Yes | Whether to delete source files after they've been transferred to Google SecOps. Valid values are:  


  * `SOURCE_DELETION_NEVER`: Never delete files from the source.
  * `SOURCE_DELETION_ON_SUCCESS`: Delete files and empty directories from the source after successful ingestion.
  * `SOURCE_DELETION_ON_SUCCESS_FILES_ONLY`: Delete source files after successful ingestion.

  
`details.amazonS3Settings.authentication.region` | Yes | The region where the S3 bucket resides. For a list of regions, see Amazon S3 regions.  
`details.amazonS3Settings.authentication.accessKeyId` | Yes | The 20-character ID for your Amazon IAM account.  
`details.amazonS3Settings.authentication.secretAccessKey` | Yes | The 40-character access key for your Amazon IAM account.  
  
#### Sample create feed request
    
    
    {
     "details": {
       "feedSourceType": "AMAZON_S3",
       "logType": "LOGTYPE_YOU_WANT_TO_BRING",
       "amazonS3Settings": {
         "s3Uri": "s3://uri/to/folder/",
         "sourceType": "FILES",
         "sourceDeletionOption": "SOURCE_DELETION_NEVER",
         "authentication": {
           "region": "US_EAST_1",
           "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
           "secretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
         }
       }
     }
    }
    

#### Amazon S3 regions

AWS Region | AWS Region code | `authentication.region`  
---|---|---  
Africa (Cape Town) | af-south-1 | `AF_SOUTH_1`  
Asia Pacific (Hong Kong) | ap-east-1 | `AP_EAST_1`  
Asia Pacific (Hyderabad) | ap-south-2 | `AP_SOUTH_2`  
Asia Pacific (Jakarta) | ap-southeast-3 | `AP_SOUTHEAST_3`  
Asia Pacific (Melbourne) | ap-southeast-4 | `AP_SOUTHEAST_4`  
Asia Pacific (Mumbai) | ap-south-1 | `AP_SOUTH_1`  
Asia Pacific (Osaka) | ap-northeast-3 | `AP_NORTHEAST_3`  
Asia Pacific (Seoul) | ap-northeast-2 | `AP_NORTHEAST_2`  
Asia Pacific (Singapore) | ap-southeast-1 | `AP_SOUTHEAST_1`  
Asia Pacific (Sydney) | ap-southeast-2 | `AP_SOUTHEAST_2`  
Asia Pacific (Tokyo) | ap-northeast-1 | `AP_NORTHEAST_1`  
AWS GovCloud (US-East) | us-gov-east-1 | `US_GOV_EAST_1`  
AWS GovCloud (US-West) | us-gov-west-1 | `US_GOV_CLOUD`  
Canada (Central) | ca-central-1 | `CA_CENTRAL_1`  
Canada West (Calgary) | ca-west-1 | `CA_WEST_1`  
China (Beijing) | cn-north-1 | `CN_NORTH_1`  
China (Ningxia) | cn-northwest-1 | `CN_NORTHWEST_1`  
Europe (Frankfurt) | eu-central-1 | `EU_CENTRAL_1`  
Europe (Ireland) | eu-west-1 | `EU_WEST_1`  
Europe (London) | eu-west-2 | `EU_WEST_2`  
Europe (Milan) | eu-south-1 | `EU_SOUTH_1`  
Europe (Paris) | eu-west-3 | `EU_WEST_3`  
Europe (Spain) | eu-south-2 | `EU_SOUTH_2`  
Europe (Stockholm) | eu-north-1 | `EU_NORTH_1`  
Europe (Zurich) | eu-central-2 | `EU_CENTRAL_2`  
Israel (Tel Aviv) | il-central-1 | `IL_CENTRAL_1`  
Middle East (Bahrain) | me-south-1 | `ME_SOUTH_1`  
Middle East (UAE) | me-central-1 | `ME_CENTRAL_1`  
South America (São Paulo) | sa-east-1 | `SA_EAST_1`  
US East (N. Virginia) | us-east-1 | `US_EAST_1`  
US East (Ohio) | us-east-2 | `US_EAST_2`  
US West (N. California) | us-west-1 | `US_WEST_1`  
US West (Oregon) | us-west-2 | `US_WEST_2`  
**Note:** The Auto-detect option works also for the regions not listed in the platform.

## AMAZON_S3_V2

Data source | Ingest schedule | `details.feedSourceType` | `details.logType`  
---|---|---|---  
Amazon S3 Bucket | Every 15 minutes. This cannot be altered.  | `AMAZON_S3_V2` | See the Feed Schema API reference to get compatible log types.   
  
### Prerequisites

  1. [Create an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
  2. [Create an access key for authentication, or create an AWS IAM role for Federated authentication](https://docs.cloud.google.com/storage-transfer/docs/source-amazon-s3) to access both the SQS queue and the S3 bucket.
  3. AWS STS endpoint configuration for opt-in regions: If you are using AWS IAM Role for federated authentication and your S3 bucket is in an AWS "opt-in" region (such as `eu-central-2`, `il-central-1`, `ap-southeast-3`, etc.), you must ensure that your AWS account is configured to allow session tokens from the global STS endpoint (`sts.amazonaws.com`) to be valid in all AWS regions. By default, tokens issued by the global STS endpoint are not valid in opt-in regions.

To enable this, sign in to your AWS account and navigate to the IAM console. In the Account Settings, change the **Security Token Service (STS) Global Endpoint** session token configuration to be **Valid in all AWS regions**. Without this setting, the feed may fail with a `PERMISSION_DENIED` error due to an invalid security token. For more details, see the [AWS documentation on managing STS session tokens in opt-in regions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html#sts-regions-manage-tokens).




To learn more about how to configure a feed to ingest data from an Amazon S3 bucket, see [Ingest AWS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/ingest-aws-logs-into-chronicle).

### Recommendations

  * If your S3 bucket contains many small files, data transfer may take longer. To speed up the feed transfer process, we recommend combining smaller files into a single, larger file.

  * Set a data retention policy on your S3 buckets to ensure transferred files are deleted and not included in future transfer feeds. Alternatively, you can use the Google SecOps feed management page to [delete the source files](https://docs.cloud.google.com/chronicle/docs/administration/feed-management#delete_source_files) from the storage buckets after they've been transferred.

  * Using Amazon SQS as the source type is preferred over Amazon S3. When Amazon SQS is used, Google SecOps reads the Amazon S3 notifications sent to the Amazon SQS service and retrieves the corresponding files from the Amazon S3 bucket. This approach provides a push-based version of an Amazon S3 feed, helping to reduce ingestion latency.




### Enable access to your Amazon S3 storage

This feed source uses the Storage Transfer Service (STS) to transfer data from Amazon S3 to Google SecOps. Before using this feed source, you must add the IP ranges used by STS workers to your list of allowed IP addresses. For details, see Set up IP allowlisting and [IP ranges](https://www.gstatic.com/storage-transfer-service/ipranges.json).

You can also include and exclude prefixes to control which files are transferred. For more information, see [Filter by prefix](https://docs.cloud.google.com/storage-transfer/docs/filtering-objects-from-transfers).

### Type-specific request fields

**Field** | **Required** | **Description**  
---|---|---  
`details.amazonS3V2Settings.s3Uri` | Yes | S3 URI. The S3 bucket source URI from where the messages are read. Example: `s3://cs-prod-cannon-00afe0c847a8/data/`  
`details.amazonS3V2Settings.sourceDeletionOption` | Yes | Option to delete source files from the S3 bucket after transfer to Google SecOps. Valid values are:  


  * `NEVER`: Never delete files from the source.
  * `ON_SUCCESS`: Delete files and empty directories from the source after successful ingestion.

  
`details.amazonS3V2Settings.maxLookbackDays` | Yes | Maximum file age (days since file last modified) of files to include. The maximum limit and the default value is 180 days.  
`details.amazonS3V2Settings.authentication.accessKeySecretAuth.accessKeyId` | Conditional. Required if using access key authenication. | The 20-character ID for your Amazon IAM account.  
`details.amazonS3V2Settings.authentication.accessKeySecretAuth.secretAccessKey` | Conditional. Required if using access key authenication. | The 40-character access key for your Amazon IAM account.  
`details.amazonS3V2Settings.authentication.aws_iam_role_arn` | Conditional. Required if using AWS IAM authenication. | ARN of the AWS IAM role configured to access S3 bucket.  
  
#### Sample create feed request - Using access credentials authentication
    
    
    {
     "details": {
       "feedSourceType": "AMAZON_S3_V2",
       "logType": "LOGTYPE_YOU_WANT_TO_BRING",
       "amazonS3V2Settings": {
         "s3Uri": "s3://uri/to/folder/",
         "sourceDeletionOption": "ON_SUCCESS",
         "maxLookbackDays": 30,
         "authentication": {
           "accessKeySecretAuth": {
                "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
                "secretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
            }
         }
       }
     }
    }
    

#### Sample create feed request - Using AWS IAM authentication
    
    
    {
     "details": {
       "feedSourceType": "AMAZON_S3_V2",
       "logType": "LOGTYPE_YOU_WANT_TO_BRING",
       "amazonS3V2Settings": {
         "s3Uri": "s3://uri/to/folder/",
         "sourceDeletionOption": "ON_SUCCESS",
         "maxLookbackDays": 30,
         "authentication": {
           "aws_iam_role_arn": "arn:aws:iam::1234567689:role/test-user"
       }
     }
    }
    

## AMAZON_SQS (Deprecated)

Data source | `details.feedSourceType` | `details.logType`  
---|---|---  
Amazon S3 Bucket that sends notifications to an Amazon Simple Queue Service (SQS) | `AMAZON_SQS` | See the Feed Schema API reference to get compatible log types.   
**Note:** This connector is deprecated and will be discontinued on March 15, 2027. We recommend using **Amazon SQS v2** for improved reliability, scalability, and performance.

You can ingest data from an Amazon SQS service whose entries point to files stored in an Amazon S3 bucket.

The interval at which Google SecOps checks your SQS queue for new messages is determined by the system, and is not user-configurable.

The Amazon SQS (v1) connector uses a frequent long-polling strategy, often polling your SQS queue multiple times per second.

### Recommendations

  * Using Amazon SQS as the source type is preferred over Amazon S3. When Amazon SQS is used, Google SecOps reads the Amazon S3 notifications sent to the Amazon SQS service and retrieves the corresponding files from the Amazon S3 bucket. This approach provides a push-based version of an Amazon S3 feed, that helps to reduce ingestion latency.
  * If your S3 bucket contains many small files, data transfer may take longer. To speed up the feed transfer process, we recommend combining smaller files into a single, larger file.



### Prerequisites

  1. Create the S3 bucket and the SQS queue in the same region.

  2. [Create an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html#creating-bucket).

  3. [Create an SQS queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html).

The queue _must_ be a _Standard_ queue, not a First-In-First-Out (FIFO) queue.

  4. [Set up notifications on your S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ways-to-add-notification-config-to-bucket.html) to write to your SQS queue.

Be sure to attach an access policy.

  5. [Create an access key](https://aws.amazon.com/blogs/security/how-to-find-update-access-keys-password-mfa-aws-management-console/) to access both the SQS queue and the S3 bucket.

  6. Get the following required permissions:

When applying a policy, include the `sqs:DeleteMessage` permission. If this permission is not attached to the SQS queue, Google SecOps is unable to delete messages. As a result, messages accumulate on the AWS side, causing delays as Google SecOps repeatedly attempts to transfer the same files.




To learn more about how to configure a feed to ingest data from an Amazon SQS queue, whose entries point to files stored in an Amazon S3 bucket, see [Ingest AWS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/ingest-aws-logs-into-chronicle).

### Amazon SQS regions

AWS Region | AWS Region code | `authentication.region`  
---|---|---  
Africa (Cape Town) | af-south-1 | `AF_SOUTH_1`  
Asia Pacific (Hong Kong) | ap-east-1 | `AP_EAST_1`  
Asia Pacific (Hyderabad) | ap-south-2 | `AP_SOUTH_2`  
Asia Pacific (Jakarta) | ap-southeast-3 | `AP_SOUTHEAST_3`  
Asia Pacific (Melbourne) | ap-southeast-4 | `AP_SOUTHEAST_4`  
Asia Pacific (Mumbai) | ap-south-1 | `AP_SOUTH_1`  
Asia Pacific (Osaka) | ap-northeast-3 | `AP_NORTHEAST_3`  
Asia Pacific (Seoul) | ap-northeast-2 | `AP_NORTHEAST_2`  
Asia Pacific (Singapore) | ap-southeast-1 | `AP_SOUTHEAST_1`  
Asia Pacific (Sydney) | ap-southeast-2 | `AP_SOUTHEAST_2`  
Asia Pacific (Tokyo) | ap-northeast-1 | `AP_NORTHEAST_1`  
AWS GovCloud (US-East) | us-gov-east-1 | `US_GOV_EAST_1`  
AWS GovCloud (US-West) | us-gov-west-1 | `US_GOV_CLOUD`  
Canada (Central) | ca-central-1 | `CA_CENTRAL_1`  
Canada West (Calgary) | ca-west-1 | `CA_WEST_1`  
China (Beijing) | cn-north-1 | `CN_NORTH_1`  
China (Ningxia) | cn-northwest-1 | `CN_NORTHWEST_1`  
Europe (Frankfurt) | eu-central-1 | `EU_CENTRAL_1`  
Europe (Ireland) | eu-west-1 | `EU_WEST_1`  
Europe (London) | eu-west-2 | `EU_WEST_2`  
Europe (Milan) | eu-south-1 | `EU_SOUTH_1`  
Europe (Paris) | eu-west-3 | `EU_WEST_3`  
Europe (Spain) | eu-south-2 | `EU_SOUTH_2`  
Europe (Stockholm) | eu-north-1 | `EU_NORTH_1`  
Europe (Zurich) | eu-central-2 | `EU_CENTRAL_2`  
Israel (Tel Aviv) | il-central-1 | `IL_CENTRAL_1`  
Middle East (Bahrain) | me-south-1 | `ME_SOUTH_1`  
Middle East (UAE) | me-central-1 | `ME_CENTRAL_1`  
South America (São Paulo) | sa-east-1 | `SA_EAST_1`  
US East (N. Virginia) | us-east-1 | `US_EAST_1`  
US East (Ohio) | us-east-2 | `US_EAST_2`  
US West (N. California) | us-west-1 | `US_WEST_1`  
US West (Oregon) | us-west-2 | `US_WEST_2`  
**Note:** The auto-detect region option in the platform doesn't work for Amazon SQS.

### Type-specific request fields

**Field** | **Required** | **Description**  
---|---|---  
`details.amazonSqsSettings.queue` | Yes | The SQS queue name.  
`details.amazonSqsSettings.region` | Yes | The region where the SQS queue and S3 bucket reside. For a list of regions, see Amazon SQS regions.  
`details.amazonSqsSettings.accountNumber` | Yes | The account number for the SQS queue and S3 bucket.  
`details.amazonSqsSettings.sourceDeletionOption` | Yes | Option to delete source files from the S3 bucket after transfer to Google SecOps. Valid values are:  


  * `SOURCE_DELETION_NEVER`: Never delete files from the source.
  * `SOURCE_DELETION_ON_SUCCESS`: Delete files and empty directories from the source after successful ingestion.
  * `SOURCE_DELETION_ON_SUCCESS_FILES_ONLY`: Delete source files after successful ingestion.

  
`details.amazonSqsSettings.authentication.sqsAccessKeySecretAuth.accessKeyId` | Yes | The 20-character ID for your Amazon IAM account.  
`details.amazonSqsSettings.authentication.sqsAccessKeySecretAuth.secretAccessKey` | Yes | The 40-character access key for your Amazon IAM account.  
`details.amazonSqsSettings.authentication.additionalS3AccessKeySecretAuth.accessKeyId` | No | The additional 20-character ID for your Amazon IAM account. _Only specify if using a different access key for the S3 bucket._  
`details.amazonSqsSettings.authentication.additionalS3AccessKeySecretAuth.secretAccessKey` | No | The additional 40-character access key for your Amazon IAM account. _Only specify if using a different access key for the S3 bucket._  
  
#### Sample create feed request
    
    
    {
     "details": {
       "feedSourceType": "AMAZON_SQS",
       "logType": "LOGTYPE_YOU_WANT_TO_BRING",
       "amazonSqsSettings": {
         "queue": "cs-prod-canon-queue-01234abc56de789f",
         "region": "US_EAST_1",
         "accountNumber": "123456789012",
         "sourceDeletionOption": "SOURCE_DELETION_NEVER",
         "authentication": {
           "sqsAccessKeySecretAuth": {
             "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
             "secretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
           }
         }
       }
     }
    }
    

### Troubleshooting

Google Security Operations may disable an SQS feed (V1) automatically if the feed fails continuously.

To fix the problem and re-enable the feed, do the following:

  1. Verify that the credentials are correct.
  2. Ensure that the feed configuration matches the details described in this section, and make corrections if necessary.
  3. Re-enable the feed using either of these methods: 
     * From the **Feeds** page: Go to **Settings** > **Feeds** page, click more_vert **menu** on the feed row, and clear **Disable Feed**.
     * Using the **Feed management API** : For details, see Enable feed.



## AMAZON_SQS_V2

Data source | `details.feedSourceType` | `details.logType`  
---|---|---  
Amazon S3 Bucket that sends notifications to an Amazon Simple Queue Service (SQS) | `AMAZON_SQS_V2` | See the Feed Schema API reference to get compatible log types.   
  
You can ingest data from an Amazon SQS service whose entries point to files stored in an Amazon S3 bucket.

The interval at which Google SecOps checks your SQS queue for new messages is determined by the system, and is not user-configurable. 

The Amazon SQS v2 connector checks for new messages in your SQS queue in near real-time, and it's optimized to reduce the number of empty receive requests.

### Recommendations

  * Using Amazon SQS as the source type is preferred over Amazon S3. When Amazon SQS is used, Google SecOps reads the Amazon S3 notifications sent to the Amazon SQS service and retrieves the corresponding files from the Amazon S3 bucket. This approach provides a push-based version of an Amazon S3 feed, helping to reduce ingestion latency.
  * If your S3 bucket contains many small files, data transfer may take longer. To speed up the feed transfer process, we recommend combining smaller files into a single, larger file.
  * The feed processes the messages only from the S3 bucket configured for the feed.
  * Both your S3 bucket and the SQS Queue should be accessible with the same set of credentials.



### Prerequisites

**Caution:** Ensure that your feed configuration inputs contain the correct URI, and the correct authentication access key or AWS IAM role for federated authentication, to ensure that our system is able to access both your SQS queue and the linked S3 bucket. In situations where our system is able to access your SQS queue, but unable to access your S3 bucket due to incorrect configuration settings, our system still acknowledges the SQS notification, but is unable to ingest data from your S3 bucket. This can result in data gaps.

  1. Create the S3 bucket and the SQS queue in the same region.

  2. [Create an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html#creating-bucket).

  3. [Create an SQS queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html).

The queue _must_ be a _Standard_ queue, not a First-In-First-Out (FIFO) queue.

  4. [Set up notifications on your S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ways-to-add-notification-config-to-bucket.html) to write to your SQS queue.

  5. If you are using Amazon Simple Notification Service (SNS) with an S3 > SNS > SQS setup, you must [select **Enable raw message delivery** on the Amazon SNS console](https://docs.aws.amazon.com/sns/latest/dg/sns-large-payload-raw-message-delivery.html).

  6. [Create an access key for authentication, or create an AWS IAM role for Federated authentication](https://docs.cloud.google.com/storage-transfer/docs/source-amazon-s3) to access both the SQS queue and the S3 bucket.

  7. Required IAM Permissions: Ensure the credentials used by the feed have at least the following permissions:

     * `sqs:ReceiveMessage`
     * `sqs:DeleteMessage`

**Note:** If the `sqs:DeleteMessage` permission is not attached to the SQS queue, Google SecOps is unable to delete messages. As a result, messages accumulate on the AWS side, causing delays as Google SecOps repeatedly attempts to transfer the same files.
     * `s3:GetObject` on the target S3 bucket and objects.

     * `s3:ListBucket` on the target S3 bucket can be helpful for some configurations.

  8. AWS STS endpoint configuration for opt-in regions: If you are using AWS IAM Role for federated authentication and your SQS queue and S3 bucket are in an AWS "opt-in" region (such as `eu-central-2`, `il-central-1`, `ap-southeast-3`, etc.), you must ensure that your AWS account is configured to allow session tokens from the global STS endpoint (`sts.amazonaws.com`) to be valid in all AWS regions. By default, tokens issued by the global STS endpoint are not valid in opt-in regions.

To enable this, sign in to your AWS account and navigate to the IAM console. In the Account Settings, change the **Security Token Service (STS) Global Endpoint** session token configuration to be **Valid in all AWS regions**. Without this setting, the feed may fail with a `PERMISSION_DENIED` error due to an invalid security token. For more details, see the [AWS documentation on managing STS session tokens in opt-in regions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html#sts-regions-manage-tokens).




### Message acknowledgement behavior and error handling

It is critical to understand how Google SecOps handles Amazon SQS messages in the `AMAZON_SQS_V2` feed to prevent unintended data loss:

  1. **Acknowledgement on terminal failure:** Google SecOps attempts to retrieve the Amazon S3 object referenced in each Amazon SQS message. If these attempts consistently fail due to what is considered a **terminal error** (after internal retries), Google SecOps still **acknowledges** (deletes) the message from the Amazon SQS queue. This design prevents unprocessable "poison pill" messages from clogging the queue and incurring excessive AWS costs from perpetual retries.

  2. **Examples of terminal failures:**

     * **Permission denied:** The most common cause is the IAM role or user associated with the feed lacking the necessary `s3:GetObject` permissions on the specific Amazon S3 bucket or objects.
     * **Object not found:** The Amazon S3 object key specified in the Amazon SQS message does not exist in the bucket.
     * **Invalid SQS message format:** The Amazon SQS message structure does not match the expected formats. See Supported SQS message formats.
  3. **Risk of data loss:** If a message is acknowledged due to such terminal failures, the data from the related Amazon S3 object is **not** ingested into Google SecOps. This is why correct configuration and monitoring are essential.




#### Recommendations to prevent data loss and ensure feed health

  * **Verify permissions:** Before and after you configure the feed, meticulously check that the IAM role or user credentials provided have the correct `s3:GetObject` permissions for all required Amazon S3 paths.
  * **Enable AWS CloudTrail:** Ensure that AWS CloudTrail is logging all relevant management and data events for Amazon SQS and Amazon S3. This lets you audit API calls made by the Google SecOps feed credentials, showing access attempts, successes, and failures (for example, `AccessDenied`).
  * **Use Amazon S3 server access logs:** Enable server access logging for your Amazon S3 bucket to get detailed records of all requests made to your bucket.
  * **Monitor feed status in Google SecOps:** Regularly check the feed status in the **Feed Management** page in the Google SecOps UI. Terminal errors like permission issues are designed to be surfaced here in near real-time.
  * **Programmatic feed monitoring:** Use the List Feeds or Get Feed API method to programmatically poll the status of your feeds. Check the `feedState` and any content in `failure_details`.
  * **Amazon CloudWatch alarms:** Set up Amazon CloudWatch alarms on your Amazon SQS queue metrics (for example, `ApproximateAgeOfOldestMessage`) and potentially on AWS CloudTrail logs using metric filters to get notified of anomalies or errors.

**Note:** Integration for more direct feed status notifications using Google Cloud Logging is under development. At this time, polling the Feed Management API is the recommended method for automated checks.

To learn more about how to configure a feed to ingest data from an Amazon SQS queue, whose entries point to files stored in an Amazon S3 bucket, see [Ingest AWS logs](https://docs.cloud.google.com/chronicle/docs/ingestion/ingest-aws-logs-into-chronicle).

### Enable access to your Amazon S3 storage

This feed source uses the Storage Transfer Service (STS) to transfer data from Amazon S3 to Google SecOps. Before using this feed source, you must add the IP ranges used by STS workers to your list of allowed IP addresses, to enable STS and Google SecOps to access your Amazon S3 storage service. For details, see Set up IP allowlisting and [IP ranges](https://www.gstatic.com/storage-transfer-service/ipranges.json).

You can also include and exclude prefixes to control which files are transferred. For more information, see [Filter by prefix](https://docs.cloud.google.com/storage-transfer/docs/filtering-objects-from-transfers).

### Amazon SQS regions

AWS Region | AWS Region code | `authentication.region`  
---|---|---  
Africa (Cape Town) | af-south-1 | `AF_SOUTH_1`  
Asia Pacific (Hong Kong) | ap-east-1 | `AP_EAST_1`  
Asia Pacific (Hyderabad) | ap-south-2 | `AP_SOUTH_2`  
Asia Pacific (Jakarta) | ap-southeast-3 | `AP_SOUTHEAST_3`  
Asia Pacific (Melbourne) | ap-southeast-4 | `AP_SOUTHEAST_4`  
Asia Pacific (Mumbai) | ap-south-1 | `AP_SOUTH_1`  
Asia Pacific (Osaka) | ap-northeast-3 | `AP_NORTHEAST_3`  
Asia Pacific (Seoul) | ap-northeast-2 | `AP_NORTHEAST_2`  
Asia Pacific (Singapore) | ap-southeast-1 | `AP_SOUTHEAST_1`  
Asia Pacific (Sydney) | ap-southeast-2 | `AP_SOUTHEAST_2`  
Asia Pacific (Tokyo) | ap-northeast-1 | `AP_NORTHEAST_1`  
AWS GovCloud (US-East) | us-gov-east-1 | `US_GOV_EAST_1`  
AWS GovCloud (US-West) | us-gov-west-1 | `US_GOV_CLOUD`  
Canada (Central) | ca-central-1 | `CA_CENTRAL_1`  
Canada West (Calgary) | ca-west-1 | `CA_WEST_1`  
China (Beijing) | cn-north-1 | `CN_NORTH_1`  
China (Ningxia) | cn-northwest-1 | `CN_NORTHWEST_1`  
Europe (Frankfurt) | eu-central-1 | `EU_CENTRAL_1`  
Europe (Ireland) | eu-west-1 | `EU_WEST_1`  
Europe (London) | eu-west-2 | `EU_WEST_2`  
Europe (Milan) | eu-south-1 | `EU_SOUTH_1`  
Europe (Paris) | eu-west-3 | `EU_WEST_3`  
Europe (Spain) | eu-south-2 | `EU_SOUTH_2`  
Europe (Stockholm) | eu-north-1 | `EU_NORTH_1`  
Europe (Zurich) | eu-central-2 | `EU_CENTRAL_2`  
Israel (Tel Aviv) | il-central-1 | `IL_CENTRAL_1`  
Middle East (Bahrain) | me-south-1 | `ME_SOUTH_1`  
Middle East (UAE) | me-central-1 | `ME_CENTRAL_1`  
South America (São Paulo) | sa-east-1 | `SA_EAST_1`  
US East (N. Virginia) | us-east-1 | `US_EAST_1`  
US East (Ohio) | us-east-2 | `US_EAST_2`  
US West (N. California) | us-west-1 | `US_WEST_1`  
US West (Oregon) | us-west-2 | `US_WEST_2`  
**Note:** The auto-detect region option in the platform doesn't work for Amazon SQS.

### Type-specific request fields

**Field** | **Required** | **Description**  
---|---|---  
`details.amazon_sqs_v2_settings.queue` | Yes | Queue ARN. The Amazon Resource Name (ARN) of the SQS queue to read from. Format: `arn:aws:sqs:region:account_id:queue_name`. For `region`, specify the region where the SQS queue and S3 bucket reside. For a list of regions, see Amazon SQS regions. For `account_id`, provide the account number associated with both the SQS queue and S3 bucket.  
`details.amazon_sqs_v2_settings.s3Uri` | Yes | S3 URI. The S3 bucket source URI from where the messages are read. You can use `s3://bucket_name/` for this field. The feed will access the files from the subdirectory path. Example: `s3://cs-prod-cannon-00afe0c847a8/data/`. Don't use URL-encoded characters in literal S3 object keys, because AWS decodes them to comply with its specifications.  
`details.amazon_sqs_v2_settings.sourceDeletionOption` | Yes | Option to delete source files from the S3 bucket after transfer to Google SecOps. Valid values are:  


  * `NEVER`: Never delete files from the source.
  * `ON_SUCCESS`: Delete files and empty directories from the source after successful ingestion.

  
`details.amazon_sqs_v2_settings.maxLookbackDays` | Yes | Maximum file age (days since file last modified) of files to include. The maximum limit and the default value is 180 days.  
`details.amazon_sqs_v2_settings.authentication.sqs_v2_accessKeySecretAuth.accessKeyId` | Conditional. Required if using access key authenication. | The 20-character ID for your Amazon IAM account and the S3 bucket. (Both SQS Queue and S3 bucket need to have the same credentials.)  
`details.amazon_sqs_v2_settings.authentication.sqs_v2_accessKeySecretAuth.secretAccessKey` | Conditional. Required if using access key authenication. | The 40-character access key for your Amazon IAM account and the S3 bucket. (Both SQS Queue and S3 bucket need to have the same credentials.)  
`details.amazon_sqs_v2_settings.authentication.aws_iam_role_arn` | Conditional. Required if using AWS IAM authenication. | ARN of the AWS IAM role configured to access S3 bucket and SQS queue.  
  
#### Sample create feed request - Using access credentials authentication
    
    
    {
     "details": {
       "feedSourceType": "AMAZON_SQS_V2",
       "logType": "LOGTYPE_YOU_WANT_TO_BRING",
       "amazon_sqs_v2_settings": {
         "queue": "arn:aws:sqs:US_EAST_1:123456789012:queue_name",
         "s3Uri": "s3://cs-prod-cannon-00afe0c847a8/data/",
         "maxLookbackDays": 30,
         "sourceDeletionOption": "ON_SUCCESS",
         "authentication": {
           "accessKeySecretAuth": {
                "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
                "secretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
            }
         }
       }
     }
    }
    

#### Sample create feed request - Using AWS IAM role authentication
    
    
    {
     "details": {
       "feedSourceType": "AMAZON_SQS_V2",
       "logType": "LOGTYPE_YOU_WANT_TO_BRING",
       "amazon_sqs_v2_settings": {
         "queue": "arn:aws:sqs:US_EAST_1:123456789012:queue_name",
         "s3Uri": "s3://cs-prod-cannon-00afe0c847a8/data/",
         "maxLookbackDays": 30,
         "sourceDeletionOption": "ON_SUCCESS",
         "authentication": {
           "aws_iam_role_arn": "arn:aws:iam::1234567689012:role/test-user"
         }
       }
     }
    }
    

### Supported SQS message formats

When Google SecOps retrieves a message from your Amazon SQS queue, it parses the JSON content in the message body to extract the S3 bucket name and object keys. The system supports the following JSON structures:

#### Standard S3 event notifications

This is the native format that Amazon S3 uses to send event notifications. The message body must contain a top-level `Records` array. Each element in this array must include an `s3` object containing the bucket name and object key.

##### Example structure
    
    
    {
      "Records": [
        {
          "eventVersion": "2.1",
          "eventSource": "aws:s3",
          "awsRegion": "us-east-1",
          "eventTime": "2025-05-09T12:00:00.000Z",
          "eventName": "ObjectCreated:Put",
          "s3": {
            "bucket": {
              "name": "example-log-bucket",
              "arn": "arn:aws:s3:::example-log-bucket"
            },
            "object": {
              "key": "AWSLogs/123456789012/CloudTrail/us-east-1/2025/05/09/logfile.json.gz",
              "size": 5242881
            }
          }
        }
      ]
    }
    

#### CrowdStrike event notifications

Google SecOps supports notifications generated by CrowdStrike services, such as Falcon Data Replicator (FDR).

##### Example structure
    
    
    {
      "cid": "123456789abcdef123456789abcdef12",
      "timestamp": 1753958678203,
      "fileCount": 1,
      "totalSize": 127695,
      "bucket": "crowdstrike-fdr-example-bucket",
      "pathPrefix": "data/partition/2025-05-09/",
      "files": [
        {
          "path": "data/partition/2025-05-09/part-00001.gz",
          "size": 127695
        }
      ]
    }
    

#### SNS wrapped notifications

If you route notifications through Amazon SNS, the message might be wrapped in an SNS notification envelope. The standard format is supported.

##### Example structure
    
    
    {
      "Type": "Notification",
      "MessageId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
      "TopicArn": "arn:aws:sns:us-east-1:123456789012:S3-Notification-Topic",
      "Subject": "Amazon S3 Notification",
      "Message": "{\"Records\":[{\"s3\":{\"bucket\":{\"name\":\"example-log-bucket\"},\"object\":{\"key\":\"logs/new_log_event.json\"}}}]}",
      "Timestamp": "2025-05-09T12:00:00.000Z"
    }
    

## AZURE_BLOBSTORE

**Important:** Google SecOps doesn't support ingestion from Azure sovereign clouds, including Azure China (operated by 21Vianet) and Azure Government. Only commercial Azure endpoints (for example, `*.servicebus.windows.net` for Event Hub or `*.blob.core.windows.net` for Blob Storage) are supported.**Caution:** The `AZURE_BLOBSTORE` (v1) connector is deprecated and will be discontinued on **March 15, 2027**. After this date, v1 feeds will stop returning data. You must migrate to the AZURE_BLOBSTORE_V2 connector, which uses the Google Cloud Storage Transfer Service (STS), to ensure continued data ingestion. For more information, see [Deprecations](https://docs.cloud.google.com/chronicle/docs/deprecations).Data source | Ingest schedule | `details.feedSourceType` | `details.logType`  
---|---|---|---  
Microsoft Azure Blob Storage Container | Every 15 minutes. This cannot be altered.  | `AZURE_BLOBSTORE` | See the Feed Schema API reference to get compatible log types.  
  
### Prerequisites

To access an Azure Blob Storage container, you need one of the following:

  * A [shared key](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage?tabs=azure-portal#view-account-access-keys) authorized to access an Azure Blob Storage container.
  * A [Shared Access Signature](https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview) with authority to read an Azure Blob Storage container.



To learn more about how to configure a feed to ingest data from Azure Blob Storage, see [Ingest Azure activity logs](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-azure-activity-logs).

### Recommendations

  * If your Azure Blob Storage container contains many small files, data transfer may take longer. To speed up the feed transfer process, we recommend combining smaller files into a single, larger file.

  * Set a data retention policy on your Azure Blob Storage containers to ensure that transferred files are deleted, so they are not listed in future transfer feeds.




### Enable access to your Azure storage

To ingest data successfully from Azure Blob Storage into Google SecOps, you must configure your Azure firewall to allow incoming connections from Google's ingestion infrastructure.

#### Allowlist the full Google IP address range (recommended)

Because Google's infrastructure routes traffic dynamically and scales over time, the most reliable method is to allowlist the full set of Google IP address ranges. This helps prevent disruptions to your feeds when backend routing changes occur or when new capacity is added. You can retrieve the list of Google IP addresses from [goog.json](https://www.gstatic.com/ipranges/goog.json). To automate your firewall configuration by polling this list with a script, see [Configure Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#ip-addr-defaults).

#### Allowlist a specific IP address subset (alternative)

If your organization's security policies require a more restrictive firewall configuration, you can allowlist the specific subset of IP addresses used by this ingestion service.

**Caution:** Google might add new IP ranges to this infrastructure to support capacity and routing needs. If you choose to use this restrictive subset, you must proactively monitor your feeds and update your firewall rules to prevent ingestion failures.

IPv4 ranges:

  * `192.179.0.0/20`
  * `172.217.80.0/20`
  * `108.177.64.0/20`
  * `142.250.88.0/22`
  * `192.178.20.0/22`
  * `136.124.152.0/21`
  * `34.104.4.0/23`
  * `34.104.24.0/23`
  * `34.116.44.0/22`



IPv6 ranges:

  * `2001:4860:4801:8000::/52`



### Type-specific request fields

**Field** | **Required** | **Description**  
---|---|---  
`details.azureBlobStoreSettings.azureUri` | Yes | The URI pointing to an Azure Blob Storage blob or container.  
`details.azureBlobStoreSettings.sourceType` | Yes | The type of object specified by the URI. Valid values are:  


  * `FILES`: The URI points to a single blob ingested with each execution of the feed.
  * `FOLDERS_RECURSIVE`: The URI points to an Amazon Blob Storage container.

  
`details.azureBlobStoreSettings.sourceDeletionOption` | Yes | Source file deletion is not supported in Azure. This field's value must be set to `SOURCE_DELETION_NEVER`.  
`details.azureBlobStoreSettings.authentication.sharedKey` | No | A shared key, a 512-bit random string in base64 encoding, authorized to access Azure Blob Storage. Required if not specifying an SAS Token.  
`details.azureBlobStoreSettings.authentication.sasToken` | No | A Shared Access Signature authorized to access the Azure Blob Storage container.  
  
#### Azure URI source types

When specifying an Azure URI, you must also indicate the type of object is specified by the URI.

`details.sourceType` | Source type  
---|---  
`FILES` | The URI points to a single blob ingested with each execution of the feed.  
`FOLDERS` | The URI points to a directory. All files within the directory are ingested each time the feed is executed.  
`FOLDERS_RECURSIVE` | The URI points to an Amazon Blob Storage container.  
  
#### Sample create feed request
    
    
    {
     "details": {
       "feedSourceType": "AZURE_BLOBSTORE",
       "logType": "LOGTYPE_YOU_WANT_TO_BRING",
       "azureBlobStoreSettings": {
         "azureUri": "https://myaccount.blob.core.windows.net/logging",
         "sourceType": "FOLDERS_RECURSIVE",
         "sourceDeletionOption": "SOURCE_DELETION_NEVER",
         "authentication": {
           "sharedKey": "Ab12CyDEFG3HI45JklMnopQrs00TU6xVw7xYZ8AbcdeFgHioJkL0MnoPqRsTUvWxYZaBCdEFg9hijKlm0N12pqR=="
         }
       }
     }
    }
    

## AZURE_BLOBSTORE_V2

**Important:** Google SecOps doesn't support ingestion from Azure sovereign clouds, including Azure China (operated by 21Vianet) and Azure Government. Only commercial Azure endpoints (for example, `*.servicebus.windows.net` for Event Hub or `*.blob.core.windows.net` for Blob Storage) are supported.Data source | Ingest schedule | `details.feedSourceType` | `details.logType`  
---|---|---|---  
Microsoft Azure Blob Storage Container | Every 15 minutes. This cannot be altered.  | `AZURE_BLOBSTORE_V2` | See the Feed Schema API reference to get compatible log types.  
  
### Prerequisites

To access an Azure Blob Storage container, you need one of the following:

  * An [access key](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage?tabs=azure-portal#view-account-access-keys) authorized to access an Azure Blob Storage container.
  * A [Shared Access Signature](https://docs.microsoft.com/en-us/azure/storage/common/storage-sas-overview) with authority to read an Azure Blob Storage container.
  * Authenticate using [Federated identity](https://docs.cloud.google.com/storage-transfer/docs/source-microsoft-azure#option_3_authenticate_using_federated_identity).



To learn more about how to configure a feed to ingest data from Azure Blob Storage, see [Ingest Azure activity logs](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-azure-activity-logs).

### Recommendations

  * If your Azure Blob Storage container contains many small files, data transfer may take longer. To speed up the feed transfer process, we recommend combining smaller files into a single, larger file.

  * Set a data retention policy on your Azure Blob Storage containers to ensure that transferred files are deleted, so they are not listed in future transfer feeds.




### Enable access to your Azure storage

This feed source uses the Storage Transfer Service (STS) to transfer data from Azure storage to Google SecOps. Before using this feed source, you must add the IP ranges used by STS workers to your list of allowed IP addresses, to enable STS and Google SecOps to access your Azure storage service. For details, see Set up IP allowlisting and [IP ranges](https://www.gstatic.com/storage-transfer-service/ipranges.json).

You can also include and exclude prefixes to control which files are transferred. For more information, see [Filter by prefix](https://docs.cloud.google.com/storage-transfer/docs/filtering-objects-from-transfers).

### Type-specific request fields

**Field** | **Required** | **Description**  
---|---|---  
`details.azureBlobStoreV2Settings.azureUri` | Yes | The URI pointing to an Azure Blob Storage blob or container.  
`details.azureBlobStoreV2Settings.sourceDeletionOption` | Yes | Option to delete source files from the source bucket after transfer to Google SecOps. Valid values are:  


  * `NEVER`: Never delete files from the source.
  * `ON_SUCCESS`: Delete files and empty directories from the source after successful ingestion.

  
`details.azureBlobStoreV2Settings.maxLookbackDays` | Yes | Maximum file age (days since file last modified) of files to include. The maximum limit and the default value is 180 days.  
`details.azureBlobStoreV2Settings.authentication.accessKey` | Conditional. Required if using an access key for authentication. | An access key, a 512-bit random string in base64 encoding, authorized to access Azure Blob Storage.  
`details.azureBlobStoreV2Settings.authentication.sasToken` | Conditional. Required if using a SAS Token for authentication. | A Shared Access Signature authorized to access the Azure Blob Storage container.  
`details.azureBlobStoreV2Settings.authentication.azure_v2_workload_identity_federation.client_id` | Conditional. Required if using Workload Identity Federation for authentication. | Application (client) ID of the registered Azure applications.  
`details.azureBlobStoreV2Settings.authentication.azure_v2_workload_identity_federation.tenant_id` | Conditional. Required if using Workload Identity Federation for authentication. | Directory (tenant) ID of the registered Azure applications.  
  
#### Sample feed creation using access key
    
    
    {
     "details": {
       "feedSourceType": "AZURE_BLOBSTORE_V2",
       "logType": "LOGTYPE_YOU_WANT_TO_BRING",
       "azureBlobStoreV2Settings": {
         "azureUri": "https://myaccount.blob.core.windows.net/logging",
         "sourceDeletionOption": "ON_SUCCESS",
         "maxLookbackDays": 30,
         "authentication": {
           "accessKey": "Ab12CyDEFG3HI45JklMnopQrs00TU6xVw7xYZ8AbcdeFgHioJkL0MnoPqRsTUvWxYZaBCdEFg9hijKlm0N12pqR=="
         }
       }
     }
    }
    

#### Sample create feed request - using Federated identity authentication
    
    
    {
     "details": {
       "feedSourceType": "AZURE_BLOBSTORE_V2",
       "logType": "LOGTYPE_YOU_WANT_TO_BRING",
       "azureBlobStoreV2Settings": {
         "azureUri": "https://myaccount.blob.core.windows.net/logging",
         "sourceDeletionOption": "ON_SUCCESS",
         "maxLookbackDays": 30,
         "authentication": {
           "accessKey": "Uv38ByGCZU8WP18PmmIdcpVmx00QA3xNe7sEB9HixkNtaLqaaB0NhtHpHgAWeTnLZpTSxCKs0gigByk5SH9pmQ==",
           "sas_token": "sv=2015-04-05&sr=c&spr=https&st=2017-09-22T00%3A10%3A00Z&se=2017-09-22T02%3A00%3A00Z&sp=rcw&sig=QcVwljccgWcNMbe9roAJbD8J5oEkYoq%2F0cUPlgrNwO1%3D"
           "azure_v2_workload_identity_federation": {
               "clientID": "1234abcd-1234-abcd-1234-abcd1234abcd",
               "tenantID": "0fc27awf-fe30-41be-97d3-abe1d7681418"
           }
         }
       }
     }
    }
    

## AZURE_EVENT_HUB

**Important:** Google SecOps doesn't support ingestion from Azure sovereign clouds, including Azure China (operated by 21Vianet) and Azure Government. Only commercial Azure endpoints (for example, `*.servicebus.windows.net` for Event Hub or `*.blob.core.windows.net` for Blob Storage) are supported.**Data source** | **Ingest schedule** | **details.feedSourceType**  
---|---|---  
Data streamed to an Azure Event Hub | It can take up to one minute for data from Azure Event Hub to appear in Google SecOps after ingestion begins. | `AZURE_EVENT_HUB`  
  
### Prerequisites

  * Make sure that a [Google Cloud project is set up for Google SecOps](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project) and that the Google SecOps API is enabled for the project.
  * [Ensure that your Google SecOps instance is linked to your Google Cloud services project](https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud).



### Sample create feed request
    
    
    {
        "displayName": "FEED_NAME",
        "details": {
            "feedSourceType": "AZURE_EVENT_HUB",
            "logType": "projects/PROJECT_NUMBER/locations/REGION_ID/instances/CUSTOMER_ID/logTypes/LOG_TYPE",
            "azureEventHubSettings": {
                "name": "NAME",
                "consumerGroup": "CONSUMER_GROUP",
                "eventHubConnectionString": "CONNECTION_STRING"
            }
        }
    }
    

## HTTP

Data source | Ingest schedule | `details.feedSourceType` | `details.logType`  
---|---|---|---  
Files available over the open internet using an HTTP request. | Every 15 minutes. This cannot be altered.  | `HTTP` | See the Feed Schema API reference to get compatible log types.   
  
WARNING: Don't use the HTTP type to gather data from an API. Refer to the following supported API feed types.

### Type-specific request fields

**Field** | **Required** | **Description**  
---|---|---  
`details.httpSettings.uri` | Yes | The URI pointing to a file or collection of files.  
`details.httpSettings.sourceType` | Yes | The type of file specified by the URI. Valid values are: 

  * `FILES`: The URI points to a single file ingested with each execution of the feed.
  * `FOLDERS`: The URI points to a directory. All files within the directory are ingested with each execution of the feed.
  * `FOLDERS_RECURSIVE`: The URI points to a directory. All files and directories within the indicated directory are ingested, including all files and directories within those directories.

  
`details.httpSettings.sourceDeletionOption` | Yes | Whether to delete source files after they have been transferred to Google SecOps. Valid values are: 

  * `SOURCE_DELETION_NEVER`: Never delete files from the source.
  * `SOURCE_DELETION_ON_SUCCESS`: Delete files and empty directories from the source after successful ingestion.
  * `SOURCE_DELETION_ON_SUCCESS_FILES_ONLY`: Delete source files after successful ingestion.

  
  
#### Sample create feed request
    
    
    {
     "details": {
       "feedSourceType": "HTTP",
       "logType": "LOGTYPE_YOU_WANT_TO_BRING",
       "httpSettings": {
         "uri": "https://url.com/myfile",
         "sourceType": "FILES",
         "sourceDeletionOption": "SOURCE_DELETION_NEVER"
       }
     }
    }
    

## Webhook

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
Data that is streamed to an HTTPS webhook.  | Based on your implementation, it might take approximately a minute for a new feed to populate because Google Security Operations takes some time to process the data. | `HTTPS_PUSH_WEBHOOK`  
  
### Prerequisites

  * Ensure that a [Google Cloud project for Google Security Operations is configured](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project) and the Backstory API is enabled for the project.
  * [Link a Google Security Operations instance to Google Cloud services](https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud).



### Set up push ingestion using an HTTPS webhook

Data can be sent to Google Security Operations using an HTTPS webhook. You must first create a feed with the appropriate log type before configuring an HTTPS webhook to send data.

To set up HTTPS push ingestion using an HTTPS webhook, do the following:

  1. Create an HTTPS webhook feed using the following [`create`](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.feeds/create) API request:
         
         {
             "displayName": "FEED_NAME",
             "details": {
               "feedSourceType": "HTTPS_PUSH_WEBHOOK",
               "logType": "projects/PROJECT_NUMBER/locations/REGION_ID/instances/CUSTOMER_ID/logTypes/LOG_TYPE"
             }
           }
         

Replace the following:

     * `FEED_NAME`: specify a name for the feed.
     * `PROJECT_NUMBER`: an automatically generated unique identifier for your project. For information about project name, project ID, and project number, which are used to identify a project, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin).
     * `REGION_ID`: the code that Google assigns based on the region. The following are the supported region IDs: `Asia-Southeast1`, `Australia-Southeast1`, `Europe`, `EU`, `Europe-West2`, `Europe-West3`, `Europe-West6`, `Govcloud-US`, `Me-West1`, and `US`.
     * `CUSTOMER_ID`: the Google Security Operations customer ID.
     * `LOG_TYPE`: the type of data the feed ingests. Google Security Operations supports specific log types for the HTTPS webhook feed.

If the data to be ingested contains a delimiter that separate log lines, such as `\\n`, include the following in the `details` field of the feed request body:
    
    "httpsPushWebhookSettings": {
        "splitDelimiter": "LOG_DELIMITER"
      }
    

Replace `LOG_DELIMITER` with the delimiter that separates the log lines, such as `\\n`.

  2. After you create a feed, generate a secret key for the feed and generate an API key to authenticate to Google Security Operations.

  3. In your client application, specify the HTTPS endpoint. Here is a sample HTTPS webhook endpoint:
         
         https://REGIONAL_ENDPOINT/v1alpha/projects/PROJECT_NUMBER/locations/REGION_ID/instances/CUSTOMER_ID/feeds/FEED_ID:importPushLogs
         

The endpoint includes the following values:

     * `REGIONAL_ENDPOINT`: the Google Security Operations regional endpoint, such as `us-chronicle.googleapis.com`. For information about supported regional endpoints, see Google Security Operations regional endpoints section of this document.
     * `PROJECT_NUMBER`: an automatically generated unique identifier for your project. For information about project name, project ID, and project number, which are used to identify a project, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin).
     * `REGION_ID`: the code that Google assigns based on the region. The following are the supported region IDs: `Asia-Southeast1`, `Australia-Southeast1`, `Europe`, `EU`, `Europe-West2`, `Europe-West3`, `Europe-West6`, `Govcloud-US`, `Me-West1`, and `US`.
     * `CUSTOMER_ID`: the Google Security Operations customer ID.
     * `FEED_ID`: the Google Security Operations feed ID.
  4. Enable authentication by specifying the API key and secret key as part of the custom header in the following format: `X-goog-api-key = KEY_VALUE` `X-Webhook-Access-Key = SECRET_VALUE`

Replace the following:

     * `SECRET_VALUE`: the secret key value that you generated using the `GenerateSecret` API. You can also pass the secret as a query parameter in the endpoint URL `(?secret=SECRET_VALUE)`. We recommend that you specify the secret as a header instead of specifying it in the URL.
     * `KEY_VALUE`: the API key value. You can also pass the API key as a query parameter in the endpoint URL `(?key=KEY_VALUE)`. We recommend that you specify the API key as a header instead of specifying it in the URL.



#### Google Security Operations regional endpoints

When you construct the HTTPS endpoint URL to push feeds, use the following regional endpoints that Google Security Operations supports:

  * `chronicle.us.rep.googleapis.com`
  * `chronicle.eu.rep.googleapis.com`
  * `chronicle.asia-northeast1.rep.googleapis.com`
  * `chronicle.asia-south1.rep.googleapis.com`
  * `chronicle.asia-southeast1.rep.googleapis.com`
  * `chronicle.australia-southeast1.rep.googleapis.com`
  * `chronicle.europe-west2.rep.googleapis.com`
  * `chronicle.europe-west3.rep.googleapis.com`
  * `chronicle.europe-west6.rep.googleapis.com`
  * `chronicle.europe-west9.rep.googleapis.com`
  * `chronicle.europe-west12.rep.googleapis.com`
  * `chronicle.me-central1.rep.googleapis.com`
  * `chronicle.me-central2.rep.googleapis.com`
  * `chronicle.me-west1.rep.googleapis.com`
  * `chronicle.northamerica-northeast2.rep.googleapis.com`
  * `chronicle.southamerica-east1.rep.googleapis.com`



## Configuration by log type

The following table lists the log types that Google Security Operations supports for the `API` feed source type (that is, ingesting data from third-party APIs).

**Note:**

  * Microsoft APIs can experience data latency and polling window limitations, which may result in data gaps or delayed events. This means the data might not be immediately available from Microsoft's side for Google SecOps to collect.
  * For all log types ingested using the Microsoft fetcher, a mandatory 5-minute ingestion lag is applied within the fetcher to account for this typical source-side data availability delay. This lag is a known behavior to accommodate potential delays from the Microsoft Graph API.
  * To maintain data consistency and achieve near real-time ingestion, Google recommends using Azure Event Hub to stream logs to Google SecOps rather than a polling-based API feed.
    * Switching ingestion methods does not impact existing rules or detections provided that the log format and schema remain identical across both methods. If the schema differs, rules and detections may require updates to align with the new data structure.
    * When transitioning, ensure you carefully coordinate the activation of the new feed and the decommissioning of the old one to minimize potential data gaps or duplication. For more information, see AZURE_EVENT_HUB.



If a log type has Google Security Operations parser support, the ingested data is stored in Google Security Operations UDM format as well as raw log data.

Click a **Data Source** name for detailed reference information, prerequisites, and API examples for the log type.

**Note:** Enable allowlisting and add the IP ranges from [goog.json](https://www.gstatic.com/ipranges/goog.json) and [cloud.json](https://www.gstatic.com/ipranges/cloud.json) for all log types that ingest data from third-party APIs. HTTPS push feeds don't require IP allowlisting, because they are push-based. Google SecOps can't guarantee that all feeds will exclusively originate from IP addresses according to a specified region.

To learn about prerequisites for other log types and feed source types, see Prerequisites.

**Data Source** | **Log Type** | **Google Security Operations Parser Support** | Anomali ThreatStream | `ANOMALI_IOC` | Yes  
---|---|---  
CrowdStrike Detection Monitoring | `CS_DETECTS` | Yes  
Duo Authentication Logs | `DUO_AUTH` | Yes  
Duo Users | `DUO_USER_CONTEXT` | Yes  
Fidelis Cloud Passage Events | `CLOUD_PASSAGE` | Yes  
Fox-IT | `FOX_IT_STIX` | No  
Google Cloud Identity Devices | `GCP_CLOUDIDENTITY_DEVICES` | Yes  
Google Cloud Identity Device Users | `GCP_CLOUDIDENTITY_DEVICEUSERS` | Yes  
Google Workspace Activity | `WORKSPACE_ACTIVITY` | Yes  
Google Workspace Alerts | `WORKSPACE_ALERTS` | Yes  
Google Workspace Chrome | `WORKSPACE_CHROMEOS` | Yes  
Google Workspace Groups | `WORKSPACE_GROUPS` | Yes  
Google Workspace Mobile | `WORKSPACE_MOBILE` | Yes  
Google Workspace Privileges | `WORKSPACE_PRIVILEGES` | Yes  
Google Workspace Users | `WORKSPACE_USERS` | Yes  
Imperva | `IMPERVA_WAF` | Yes  
Microsoft Azure AD Directory Audit | AZURE_AD_AUDIT | Yes  
Microsoft Azure AD Context | `AZURE_AD_CONTEXT` | Yes  
Microsoft Azure AD Sign-Ins | `AZURE_AD` | Yes  
Microsoft Azure MDM Intune Audit Events | `AZURE_MDM_INTUNE` | Yes  
Microsoft Graph Security API | `MICROSOFT_GRAPH_ALERT` | Yes  
Microsoft 365 Management Activity | `OFFICE_365` | Yes  
Mimecast Secure Email Gateway | `MIMECAST_MAIL` | Yes  
Netskope Alerts | `NETSKOPE_ALERT` | Yes  
Netskope Alerts V2 | `NETSKOPE_ALERT_V2` | Yes  
Okta System Log | `OKTA` | Yes  
Okta Users | `OKTA_USER_CONTEXT` | Yes  
Palo Alto Networks Autofocus | `PAN_IOC` | Yes  
Palo Alto Networks Cortex XDR | `CORTEX_XDR` | Yes  
Palo Alto Networks Prisma Cloud Audit Logs | `PAN_PRISMA_CLOUD` | Yes  
Proofpoint on Demand | `PROOFPOINT_ON_DEMAND` | Yes  
Proofpoint TAP | `PROOFPOINT_MAIL` | Yes  
Qualys VM | `QUALYS_VM` | Yes  
Qualys Scan | `QUALYS_SCAN` | No  
Rapid7 InsightVM | `RAPID7_INSIGHT` | Yes  
Recorded Future | `RECORDED_FUTURE_IOC` | Yes  
RH-ISAC | `RH_ISAC_IOC` | Yes  
Salesforce | `SALESFORCE` | Yes  
SentinelOne Alert | `SENTINELONE_ALERT` | Yes  
ServiceNow CMDB | `SERVICENOW_CMDB` | Yes  
Thinkst Canary | `THINKST_CANARY` | Yes  
ThreatConnect | `THREATCONNECT_IOC` | Yes  
Trellix HX alerts | `TRELLIX_HX_ALERTS` | Yes  
Trellix HX audit | `TRELLIX_HX_AUDIT` | Yes  
Trellix HX hosts | `TRELLIX_HX_HOSTS` | Yes  
Workday | `WORKDAY` | Yes  
Workday Audit Logs | `WORKDAY_AUDIT` | No  
AWS EC2 Hosts | `AWS_EC2_HOSTS` | Yes  
AWS EC2 Instances | `AWS_EC2_INSTANCES` | Yes  
AWS EC2 VPCs | `AWS_EC2_VPCS` | Yes  
AWS Identity and Access Management | `AWS_IAM` | Yes  
  
### Anomali ThreatStream

This section provides API reference details for the `ANOMALI_IOC` log type. For details about the data source, see the [Anomali ThreatStream](https://www.anomali.com/products/threatstream) documentation.

Data source | Ingest schedule | `details.feedSourceType` | `details.logType`  
---|---|---|---  
api.threatstream.com/api/v2/intelligence | Every minute | `API` | `ANOMALI_IOC`  
  
#### Prerequisites

  * Get the values for all required request fields.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.anomaliSettings.authentication.user` | Yes | Username  
`details.anomaliSettings.authentication.secret` | Yes | API key  
  
#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example shows a `curl` request:
    
    
    curl --location 'https://api.threatstream.com/api/v2/intelligence?modified_ts__lt=2025-04-21T15%3A30%3A00&modified_ts__gt=2025-01-21T15%3A30%3A00&status=active&order_by=update_id&limit=1' --header 'Authorization: apikey :'
    

Replace the following placeholders:

  * USERNAME: username of your account
  * PASSWORD: password of your account



#### Sample create feed request
    
    
    {
     "details": {
       "feedSourceType": "API",
       "logType": "ANOMALI_IOC",
       "anomaliSettings": {
         "authentication": {
           "user": "USERNAME",
           "secret": "APIKEY"
         },
       }
     }
    }
    

### AWS EC2 Hosts

This section provides API reference details for the `AWS_EC2_HOSTS` log type.

Data source | Ingest schedule | `details.feedSourceType`  
---|---|---  
ec2.amazonaws.com | Every 6 hours | `API`  
  
#### Prerequisites

  * Get the values for all required request fields.
  * Get the following required permissions: 
    * The user whose credentials are used to authenticate must have the [`AmazonEC2ReadOnlyAccess` permission](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEC2ReadOnlyAccess.html). 



#### Type-specific request fields

The following table lists the field values required when creating a feed to collect data for the `AWS_EC2_HOSTS` log type.

Field | Required | Description | `details.awsEc2HostsSettings.authentication.user` | Yes | The 20-character ID for your Amazon IAM account.  
---|---|---  
`details.awsEc2HostsSettings.authentication.secret` | Yes | The 40-character access key for your Amazon IAM account.  
  
#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following is an example request to retrieve host description using curl:
    
    
    curl --location 'https://ec2.us-east-1.amazonaws.com?Action=DescribeHosts&Version=2016-11-15&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=XXXXXXXXXXXXXXXXXXXX%2F20250625%2Fus-east-1%2Fec2%2Faws4_request&X-Amz-Date=20250625T120840Z&X-Amz-Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&X-Amz-SignedHeaders=host'
    

#### Sample create feed request
    
    
    {
      "details": {
          "awsEc2HostsSettings": {
              "authentication": {
                  "user": "AccessKeyID",
                  "secret": "SecretAccessKey"
              }
          },
          "feedSourceType": "API",
          "logType": "AWS_EC2_HOSTS"
      }
    }
    

### AWS EC2 Instances

This section provides API reference details for the `AWS_EC2_INSTANCES` log type.

Data source | Ingest schedule | `details.feedSourceType`  
---|---|---  
ec2.amazonaws.com | Every 6 hours | `API`  
  
#### Prerequisites

  * Get the values for all required request fields.
  * Get the following required permissions: 
    * The user whose credentials are used to authenticate must have the [`AmazonEC2ReadOnlyAccess` permission](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEC2ReadOnlyAccess.html). 

**Note:** All AWS regions require permissions.

#### Type-specific request fields

The following table lists the field values required when creating a feed to collect data for the `AWS_EC2_INSTANCES` log type.

Field | Required | Description | `details.awsEc2InstancesSettings.authentication.user` | Yes | The 20-character ID for your Amazon IAM account.  
---|---|---  
`details.awsEc2InstancesSettings.authentication.secret` | Yes | The 40-character access key for your Amazon IAM account.  
  
#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example shows a `curl` request to retrieve an instance description:
    
    
    curl --location 'https://ec2.us-east-1.amazonaws.com?Action=DescribeInstances&Version=2016-11-15&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=XXXXXXXXXXXXXXXXXXXX%2F20250625%2Fus-east-1%2Fec2%2Faws4_request&X-Amz-Date=20250625T120840Z&X-Amz-Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&X-Amz-SignedHeaders=host'
    

#### Sample create feed request
    
    
    {
      "details": {
          "awsEc2InstancesSettings": {
              "authentication": {
                  "user": "AccessKeyID",
                  "secret": "SecretAccessKey"
              }
          },
          "feedSourceType": "API",
          "logType": "AWS_EC2_INSTANCES"
      }
    }
    

### AWS EC2 VPCs

This section provides API reference details for the `AWS_EC2_VPCS` log type.

Data source | Ingest schedule | `details.feedSourceType`  
---|---|---  
ec2.amazonaws.com | Every 6 hours | `API`  
  
#### Prerequisites

  * Get the values for all required request fields.
  * Get the following required permissions: 
    * The user whose credentials are used to authenticate must have the [`AmazonEC2ReadOnlyAccess` permission](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEC2ReadOnlyAccess.html). 



#### Type-specific request fields

The following table lists the field values required when creating a feed to collect data for the `AWS_EC2_VPCS` log type.

Field | Required | Description | `details.awsEc2VpcsSettings.authentication.user` | Yes | The 20-character ID for your Amazon IAM account.  
---|---|---  
`details.awsEc2VpcsSettings.authentication.secret` | Yes | The 40-character access key for your Amazon IAM account.  
  
#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example shows a `curl` request to retrieve a VPC description:
    
    
    curl --location 'https://ec2.us-east-1.amazonaws.com?Action=DescribeVpcs&Version=2016-11-15&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=XXXXXXXXXXXXXXXXXXXX%2F20250625%2Fus-east-1%2Fec2%2Faws4_request&X-Amz-Date=20250625T120840Z&X-Amz-Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&X-Amz-SignedHeaders=host'
    

#### Sample create feed request
    
    
    {
      "details": {
          "awsEc2VpcsSettings": {
              "authentication": {
                  "user": "AccessKeyID",
                  "secret": "SecretAccessKey"
              }
          },
          "feedSourceType": "API",
          "logType": "AWS_EC2_VPCS"
      }
    }
    

### AWS Identity and Access Management

This section provides API reference details for the `AWS_IAM` log type.

Data source | Ingest schedule | `details.feedSourceType`  
---|---|---  
iam.amazonaws.com | Every 24 hours | `API`  
  
#### Prerequisites

  * Get the values for all required request fields.
  * Get the following required permissions: 
    * The user whose credentials are used to authenticate must have the [`IAMReadOnlyAccess` permission](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/IAMReadOnlyAccess.html).



#### Type-specific request fields

The following table lists the field values required when creating a feed to collect data for the `AWS_IAM` log type.

Field | Required | Description | `details.awsIamSettings.authentication.user` | Yes | The 20-character ID for your Amazon IAM account.  
---|---|---  
`details.awsIamSettings.authentication.secret` | Yes | The 40-character access key for your Amazon IAM account.  
`details.awsIamSettings.apiType` | Yes | API which needs to be called (Users/Roles/Groups).  
  
#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example shows a `curl` request to retrieve users:
    
    
    curl --location 'https://iam.amazonaws.com/?Action=ListRoles&MaxItems=1000&Version=2010-05-08&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=XXXXXXXXXXXXXXXXXXXX%2F20250612%2Fus-east-1%2Fiam%2Faws4_request&X-Amz-Date=20250612T105043Z&X-Amz-Signature=0000000000000000000000000000000000000000000000000000000000000000&X-Amz-SignedHeaders=host'
    

The following example shows a `curl` request to retrieve roles:
    
    
    curl --location 'https://iam.amazonaws.com/?Action=ListRoles&MaxItems=1000&Version=2010-05-08&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=XXXXXXXXXXXXXXXXXXXX%2F20250612%2Fus-east-1%2Fiam%2Faws4_request&X-Amz-Date=20250612T105043Z&X-Amz-Signature=0000000000000000000000000000000000000000000000000000000000000000&X-Amz-SignedHeaders=host'
    

The following example shows a `curl` request to retrieve groups:
    
    
    curl --location 'https://iam.amazonaws.com/?Action=ListGroups&MaxItems=1000&Version=2010-05-08&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=XXXXXXXXXXXXXXXXXXXX%2F20250612%2Fus-east-1%2Fiam%2Faws4_request&X-Amz-Date=20250612T105956Z&X-Amz-Signature=0000000000000000000000000000000000000000000000000000000000000000&X-Amz-SignedHeaders=host'
    

#### Sample create feed request
    
    
    {
      "details": {
          "awsIamSettings": {
              "authentication": {
                  "user": "AccessKeyID",
                  "secret": "SecretAccessKey"
              },
              "apiType": "USERS"
          },
          "feedSourceType": "API",
          "logType": "AWS_IAM"
      }
    }
    

### CrowdStrike Alerts API

This section provides API reference details for the `CS_ALERTS` log type. For details about the data source, see the [CrowdStrike Alerts Monitoring](https://www.crowdstrike.com/) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`** | **`details.logType`**  
---|---|---|---  
  
  * api.crowdstrike.com/alerts/queries/alerts/v2
  * api.crowdstrike.com/alerts/entities/alerts/v2

| Every minute | `API` | `CS_ALERTS`  
**Note:** When first setting up a `CS_ALERTS` feed, you might notice an initial ingestion lag. This is typically due to the volume of historical data being backfilled from the CrowdStrike API. The time taken depends on the amount of past data. This is a source-side volume effect.

#### Prerequisites

  * Get the values for all required request fields.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.crowdstrikeAlertsSettings.authentication.clientId` | Yes | Application ID  
`details.crowdstrikeAlertsSettings.authentication.clientSecret` | Yes | Client Secret  
`details.crowdstrikeAlertsSettings.authentication.tokenEndpoint` | Yes | Authentication URL  
`details.crowdstrikeAlertsSettings.hostname` | Yes | API Endpoint URL  
  
#### Sample create feed request
    
    
    {
      "details": {
        "feedSourceType": "API",
        "logType": "CS_ALERTS",
        "crowdstrikeAlertsSettings": {
          "authentication": {
              "clientId": "CLIENT ID",
              "clientSecret": "CLIENT SECRET",
              "tokenEndpoint": "https://api.us-2.crowdstrike.com/oauth2/token"
          },
          "hostname": "api.crowdstrike.com"
        }
      }
    }
    

#### Enable Crowdstrike feed

This section describes the steps to enable a CrowdStrike feed.

##### Create a CrowdStrike API client

  1. In the CrowdStrike Falcon console, navigate to **Support and resources** > **API clients and keys** to create an API client.

  2. Create a new **API Client** and assign the API scope to **Read Detections and Alerts**.

  3. Record the values for **Base URL** , **Client ID** , and **Client Secret**. You'll need these values to set up your feed in Google SecOps.




##### Set up the Google SecOps feed

  1. In Google SecOps, go to the **Settings** menu.

  2. Click **Feeds** , and then **Add New**.

  3. Select **Third party API** as the source type and select **CrowdStrike Alerts API** as the log type.

  4. Enter the following values:

     * **OAuth token endpoint** : Endpoint to retrieve the OAuth token
     * **OAuth client ID** : An OAuth 2.0 client ID
     * **OAuth client secret** : Secret associated with the client ID
     * **Base URL** : The fully qualified domain name for the CrowdStrike API, having the form `api.(xx-xx.)crowdstrike.com`
**Note:** Your token endpoint may not include "us-2" in your URL. This depends on your CrowdStrike region. Use the correct base URL from the CrowdStrike console.
     * **Ingestion Type**
       * **Bring all alerts** : Ingests both new and existing alerts that have been updated.
       * **Bring only new alerts** : Ingests new alerts only.
  5. Click **Submit**.




After setup, the feed begins to retrieve alerts from the CrowdStrike instance in chronological order. Alerts older than 6 months are skipped. After the initial backfill completes (which can take time depending on volume), the feed polls for new alerts every 5 minutes.

### CrowdStrike Detection Monitoring

**Caution:** CrowdStrike is decommissioning its `Detects API` on September 30, 2025. To prevent service disruption, see [Migrate from CrowdStrike Detects API to Alerts API](https://docs.cloud.google.com/chronicle/docs/detection/migrate-detects-api-to-alerts-api).

This section provides API reference details for the `CS_DETECTS` log type. For details about the data source, see the [CrowdStrike Detection Monitoring](https://www.crowdstrike.com/) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`** | **`details.logType`**  
---|---|---|---  
  
  * api.crowdstrike.com/oauth/token
  * api.crowdstrike.com/alerts/queries/alerts/v2
  * api.crowdstrike.com/alerts/entities/alerts/v2

| Every minute | `API` | `CS_DETECTS`  
  
#### Prerequisites

  * Get the values for all required request fields.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.crowdstrikeDetectsSettings.authentication.clientId` | Yes | Application ID  
`details.crowdstrikeDetectsSettings.authentication.clientSecret` | Yes | Client Secret  
`details.crowdstrikeDetectsSettings.authentication.tokenEndpoint` | Yes | Authentication URL  
`details.crowdstrikeDetectsSettings.hostname` | Yes | API Endpoint URL  
  
#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example shows a `curl` request to retrieve alert IDs:
    
    
    curl --location 'https://api.us-2.crowdstrike.com/alerts/queries/alerts/v2?offset=0&limit=3&sort=updated_timestamp%7Casc&filter=product%3A%27epp%27%2bupdated_timestamp%3A%3E%272025-04-07T04%3A17%3A04.954919044Z%27' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer token'
    

The following example shows a `curl` request to retrieve alert entities:
    
    
    curl --location 'https://api.crowdstrike.com/alerts/entities/alerts/v2' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer token' \
    --data '{
        ""composite_ids"":[""27fe4e476ca3490b8476b2b6650e5a74:ind:2a1c5ef609ac479ba77f8ca5879c82fc:417272807417669-10304-33535504"",
    ""27fe4e476ca3490b8476b2b6650e5a74:ind:2a1c5ef609ac479ba77f8ca5879c82fc:417273145118955-10305-33606672""]
    }'
    

#### Sample create feed request
    
    
    {
      "details": {
        "feedSourceType": "API",
        "logType": "CS_DETECTS",
        "crowdstrikeDetectsSettings": {
          "authentication": {
              "clientId": "CLIENT ID",
              "clientSecret": "CLIENT SECRET",
              "tokenEndpoint": "oauth2/token"
          "hostname": "api.crowdstrike.com"
        }
      }
    }
    

#### Enable Crowdstrike Feed

This section describes the steps to enable a CrowdStrike feed.

##### Create a CrowdStrike API client

  1. In the CrowdStrike Falcon console, navigate to **Support and resources** > **API clients and keys** to create an API client.

  2. Create a new **API Client** and assign the API scope to **Read Detections and Alerts**.

  3. Record the values for **Base URL** , **Client ID** , and **Client Secret**. You'll need these values to set up your feed in Google SecOps.




##### Set up the Google Security Operations feed

  1. In Google SecOps, go to the **Settings** menu.

  2. Click **Feeds** , and then **Add New**.

  3. Select **Third party API** as the source type and select **Crowdstrike Detection Monitoring** as the log type.

  4. Enter the values collected from CrowdStrike (`clientId`, `clientSecret`, `tokenEndpoint`, and `hostname`), and then click **Submit**.

**Note:** Your token endpoint may not include "us-2" in your URL. This depends on your CrowdStrike region. Use the correct base URL from the CrowdStrike console.
  5. Enter the **Ingestion Type**

     * **Bring Only New Detections** : Ingests only new detections.
     * **Bring All Detections (Default)** : Ingests both new and existing detections that have been updated. After setup, the feed begins to retrieve alerts from the CrowdStrike instance in chronological order. Alerts older than 6 months are skipped. After the initial backfill completes (which can take time depending on volume), the feed polls for new alerts every 5 minutes.



### Duo Authentication Logs

This section provides API reference details for the `DUO_AUTH` log type. For details about the data source, see the [Duo Authentication Logs](https://duo.com/docs/adminapi#authentication-logs) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
`API_HOSTNAME/admin/v2/logs/authentication` Replace `API_HOSTNAME` with the fully qualified domain name of the API instance. | Every 30 minutes | `API`  
  
#### Prerequisites

  * Get the values for all authentication fields.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.duoAuthSettings.authentication.user` | Yes | The username to authenticate to Duo.  
`details.duoAuthSettings.authentication.secret` | Yes | The secret to authenticate to Duo.  
`details.duoAuthSettings.hostname` | Yes | The fully qualified domain name for your instance of the API, such as `api-myinstance.duosecurity.com`.  
  
#### Test the endpoint

The Duo Admin API provides programmatic access to the administrative functionality of Duo Security's two-factor authentication platform.

To query your Duo account's authentication logs, you need to send a request to the `/admin/v2/logs/authentication` endpoint.

For details on how to use the API, see the [Authentication Logs](https://duo.com/docs/adminapi#authentication-logs) section in the Duo documentation.

#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "DUO_AUTH",
         "duoAuthSettings": {
           "authentication": {
             "user": "USERNAME",
             "secret": "SECRET"
           },
           "hostname": "api-mytenant.duosecurity.com"
         }
       }
    }
    

### Duo Users

This section provides API reference details for the `DUO_USER_CONTEXT` log type. For details about the data source, see the [Duo Users](https://duo.com/docs/adminapi#users) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
`API_HOSTNAME/admin/v1/users` Replace `API_HOSTNAME` with the fully qualified domain name of the API instance. | Every 24 hours | `API`  
  
#### Prerequisites

  * Get the values for all authentication fields.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.duoUserContextSettings.authentication.user` | Yes | The username to authenticate to Duo.  
`details.duoUserContextSettings.authentication.secret` | Yes | The secret to authenticate to Duo.  
`details.duoUserContextSettings.hostname` | Yes | The fully qualified domain name for your instance of the API, such as `api-myinstance.duosecurity.com`.  
  
#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example shows a `curl` request to retrieve authentication logs:
    
    
    curl --location 'https://api-ceabb574.duosecurity.com/admin/v2/logs/authentication?maxtime=1745942682000&mintime=1745856282000&limit=1000&sort=ts%3Adesc' \
    --header 'Date: Tue, 29 Apr 2025 16:06:47 -0000' \
    --header 'Authorization: Basic TOKEN''
    

Replace the following:

  * TOKEN: OAuth access token



The following example shows a `curl` request to retrieve user context:
    
    
    "curl --location 'https://api-22627695.duosecurity.com/admin/v1/users?limit=1000&offset=0' \
    --header 'Date: Tue, 29 Apr 2025 14:19:07 -0000' \
    --header 'Authorization: Basic TOKEN'' \
    --data ''"
    

Replace the following:

  * TOKEN: OAuth access token



#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "DUO_USER_CONTEXT",
         "duoUserContextSettings": {
           "authentication": {
             "user": "USERNAME",
             "secret": "SECRET"
           },
           "hostname": "api-mytenant.duosecurity.com"
         }
       }
    }
    

### Fidelis Cloud Passage Events

This section provides API reference details for the `CLOUD_PASSAGE` log type. For details about the data source, see the [Cloud Passage Events](https://fidelissecurity.com/) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
`api.cloudpassage.com/events?event_types` | Every minute | `API`  
  
#### Prerequisites

  * Get the values for all authentication fields.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.cloudPassageSettings.authentication.user` | Yes | The username that is used for authentication.  
`details.cloudPassageSettings.authentication.secret` | Yes | The secret that is for authentication.  
`details.cloudPassageSettings.eventTypes` | No | The type of events to include in the response. If you don't specify any event types, then the following event types are fetched: `fim_target_integrity_changed`, `lids_rule_failed`, and `sca_rule_failed`.  
  
#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "CLOUD_PASSAGE",
         "cloudPassageSettings": {
           "authentication": {
             "user": "api_key_id",
             "secret": "api_key_secret",
           }
           "eventTypes": [
             "fim_target_integrity_changed",
             "lids_rule_failed",
             "sca_rule_failed"
           ],
         }
       }
    }
    

### Fox-IT

This section provides API reference details for the `FOX_IT_STIX` log type. For details about the data source, see the [Fox-IT](https://fox-it.com/en/services/threat-intelligence/) documentation.

Data source | Ingest schedule | `details.feedSourceType`  
---|---|---  
stix.fox-it.com/services/poll | Every 24 hours | `API`  
  
#### Prerequisites

  * Get the values for all authentication and SSL fields.
  * Get the following required permissions: 
    * None



#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "FOX_IT_STIX",
         "foxItStixSettings": {
           "authentication": {
             "user": "USERNAME",
             "secret": "SECRET"
           },
           "ssl": {
             "sslCertificate": "<cert>",
             "encodedPrivateKey": "key"
           }
           "pollServiceURI": "https://stix.fox-it.com/services/poll",
           "collection": "mycollection"
         }
       }
    }
    

### Google Cloud Identity Devices

This section provides API reference details for the `GCP_CLOUDIDENTITY_DEVICES` log type. For details about the data source, see the [Google Cloud Identity Devices](https://docs.cloud.google.com/identity) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
`cloudidentity.googleapis.com/v1/devices` | Every 24 hours | `API`  
  
#### Prerequisites

  * Get the values for all authentication fields.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.googleCloudIdentityDevicesSettings.authentication.tokenEndpoint` | Yes | The endpoint to retrieve the OAuth JSON web token.  
`details.googleCloudIdentityDevicesSettings.authentication.claims.issuer` | Yes | The JWT claims issuer, which is usually a client ID.  
`details.googleCloudIdentityDevicesSettings.authentication.claims.subject` | Yes | The JWT claims subject, which is usually an email ID.  
`details.googleCloudIdentityDevicesSettings.authentication.claims.audience` | Yes | The JWT claims audience.  
`details.googleCloudIdentityDevicesSettings.authentication.rsCredentials.privateKey` | Yes | An RSA private key in PEM format.  
`details.googleCloudIdentityDevicesSettings.apiVersion` | No | The API version to use to fetch device information. The value must be either `v1`, `v1beta1`, or `vx`. If no version is specified, `v1` version is used.  
  
#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example uses `curl` to retrieve a host description:
    
    
    curl --location 'https://cloudidentity.googleapis.com/v1/devices?pageSize=100' \
    --header 'Authorization: ••••••'
    

#### Sample create feed request
    
    
    {
     "details": {
       "feedSourceType": "API",
       "logType": "GCP_CLOUDIDENTITY_DEVICES",
       "googleCloudIdentityDevicesSettings": {
         "authentication": {
           "tokenEndPoint": "jwt_token_uri",
           "claims": {
             "issuer": "jwt_client_email",
             "subject": "user_email",
             "audience": "jwt_token_uri"
           },
           "rsCredentials": {
             "private_key": "privatekey"
           }
         },
         "apiVersion": "v1",
       }
     }
    }
    

### Google Cloud Identity Device Users

This section provides API reference details for the `GCP_CLOUDIDENTITY_DEVICEUSERS` log type. For details about the data source, see the [Google Cloud Identity Device Users](https://docs.cloud.google.com/identity) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
`cloudidentity.googleapis.com/v1/devices/-/deviceUsers` | Every 24 hours | `API`  
  
#### Prerequisites

  * Get the values for all authentication fields.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.googleCloudIdentityDeviceUsersSettings.authentication.tokenEndpoint` | Yes | The endpoint to retrieve the OAuth JSON web token.  
`details.googleCloudIdentityDeviceUsersSettings.authentication.claims.issuer` | Yes | The JWT claims issuer, which is usually a client ID.  
`details.googleCloudIdentityDeviceUsersSettings.authentication.claims.subject` | Yes | The JWT claims subject, which is usually an email ID.  
`details.googleCloudIdentityDeviceUsersSettings.authentication.claims.audience` | Yes | The JWT claims audience.  
`details.googleCloudIdentityDeviceUsersSettings.authentication.rsCredentials.privateKey` | Yes | An RSA private key in PEM format.  
`details.googleCloudIdentityDeviceUsersSettings.apiVersion` | No | The API version to use to fetch device information. The value must be either `v1`, `v1beta1`, or `vx`. If no version is specified, `v1` version is used.  
  
#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example uses `curl` to retrieve a host description:
    
    
    curl --location 'https://cloudidentity.googleapis.com/v1/devices/-/deviceUsers?pageSize=25' \
    --header 'Authorization: Bearer token'
    

#### Sample create feed request
    
    
    {
     "details": {
       "feedSourceType": "API",
       "logType": "GCP_CLOUDIDENTITY_DEVICEUSERS",
       "googleCloudIdentityDeviceUsersSettings": {
         "authentication": {
           "tokenEndPoint": "jwt_token_uri",
           "claims": {
             "issuer": "jwt_client_email",
             "subject": "user_email",
             "audience": "jwt_token_uri"
           },
           "rsCredentials": {
             "private_key": "privatekey"
           }
         },
       }
     }
    }
    

### Google Workspace Activities

This section provides API reference details for the `WORKSPACE_ACTIVITY` log type. For details about the data source, see the [Google Workspace Activities](https://developers.google.com/admin-sdk/reports/reference/rest/v1/activities/list) documentation.

Data source | Ingest schedule | `details.feedSourceType` | `details.logType`  
---|---|---|---  
admin.googleapis.com | Native ingestion: real time. Feed based ingestion: 5-hour minimum for `login` and `user_accounts` events to prevent data loss. | `API` | `WORKSPACE_ACTIVITY`  
**Note:** You cannot use the [Feed Management](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-workspace-logs#configure_a_feed_in_to_ingest_logs) capabilities to ingest `gmail` application logs into your Google Security Operations instance. `gmail` logs are accessible through WORKSPACE_ACTIVITY logs, which require you to first [link your Google Workspace log fields to your Google Security Operations instance](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/workspace-to-chronicle).

#### Prerequisites

For Google Security Operations to ingest Google Workspace activities, you must do the following:

  1. Enable the [Admin SDK API](https://developers.google.com/admin-sdk) on your Google Cloud project.
  2. [Create a Service Account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) to handle authentication when accessing the administrator API.
  3. [Generate a JSON key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys) for the Service Account.
  4. [Create a domain-wide delegation](https://developers.google.com/admin-sdk/directory/v1/guides/delegation) for the Service Account with the following OAuth scope: 
     * [https://www.googleapis.com/auth/admin.reports.audit.readonly](https://developers.google.com/identity/protocols/oauth2/scopes#admin-reports)
  5. Create a Google Workspace user and [assign it an administrator role](https://support.google.com/a/answer/9807615) that includes the Reports administrator privilege, or [create a custom role](https://support.google.com/a/answer/2406043) with that privilege.
  6. [Locate your Google Workspace customer ID](https://support.google.com/a/answer/10070793).



To learn more about how to configure a feed to ingest Google Workspace logs, see [Collect Google Workspace logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-workspace-logs).

#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.workspaceActivitySettings.authentication.tokenEndpoint` | Yes | The value of the `token_uri` field in the JSON key for the service account created to access the administrator API.  
`details.workspaceActivitySettings.authentication.claims.issuer` | Yes | The value of the `client_email` field in the JSON key for the service account created to access the administrator API.  
`details.workspaceActivitySettings.authentication.claims.subject` | Yes | The email address of the Google Workspace administrator user with Reports privilege.  
`details.workspaceActivitySettings.authentication.claims.audience` | Yes | The value of the `token_uri` field in the JSON key for the service account created to access the administrator API.  
`details.workspaceActivitySettings.authentication.rsCredentials.privateKey` | Yes | The value of the `private_key` field in the JSON key for the service account created to access the administrator API. Note that literal newline characters (`\n`) should be replaced with carriage returns. Also note that the field name is `rsCredentials`, and not `rsaCredentials`.  
`details.workspaceActivitySettings.workspaceCustomerId` | Yes | The Google Workspace customer ID. The customer ID must have a leading 'C' character. The customer ID may appear differently depending on where in the Google administrator console it is found. If the customer ID you have does not have a leading 'C', then prepend what you have with a 'C'.  
`details.workspaceActivitySettings.applications` | Yes | The Google Workspace applications to gather activities for. See the following table for valid values.  
  
#### Google Workspace applications

Activities are associated with one or more applications. The applications that Google Security Operations supports includes the following.

`details.workspaceActivitySettings.applications` | Description  
---|---  
`access_transparency` | [Access Transparency log events](https://support.google.com/a/answer/9230979)  
`admin` | [Admin log events](https://support.google.com/a/answer/4579579)  
`calendar` | [Calendar log events](https://support.google.com/a/answer/6110475)  
`chat` | [Chat log events](https://support.google.com/a/answer/9142478)  
`drive` | [Drive log events](https://support.google.com/a/answer/4579696)  
`gcp` | Google Cloud activity events  
`gplus` | [Currents log events](https://support.google.com/a/answer/7421557)  
`groups` | [Groups log events](https://support.google.com/a/answer/6270454)  
`groups_enterprise` | [Groups Enterprise log events](https://support.google.com/a/answer/9667889)  
`jamboard` | [Jamboard log events](https://support.google.com/a/answer/9350573)  
`login` | [User log events](https://support.google.com/a/answer/4580120)  
`meet` | [Meet log events](https://support.google.com/a/answer/9186729)  
`mobile` | [Device log events](https://support.google.com/a/answer/6350074)  
`rules` | [Rule log events (beta)](https://support.google.com/a/answer/11203624)  
`saml` | [SAML log events](https://support.google.com/a/answer/7007375)  
`token` | [OAuth log events](https://support.google.com/a/answer/6124308)  
`user_accounts` | [User log events](https://support.google.com/a/answer/4580120)  
`context_aware_access` | [Context-Aware Access log events](https://support.google.com/a/answer/9394107)  
`chrome` | [Chrome log events](https://support.google.com/a/answer/9393909)  
`data_studio` | [Data Studio log events](https://support.google.com/a/answer/9690662)  
`keep` | [Keep log events](https://support.google.com/a/answer/10657662)  
  
#### Test the API endpoint

Before you create the feed, use curl to test the API endpoint.

The following is a generic example request using curl to fetch from different endpoints:
    
    
    curl --location 'https://admin.googleapis.com/endpoint?customerId=C04f3xv95&maxResults=1000&startTime=2025-03-15T10%3A00%3A00.000000000Z&endTime=2025-03-15T11%3A30%3A00.000000000Z' \
    --header 'Authorization: Bearer  XXXX'
    

#### Sample create feed request
    
    
    {
     "details": {
       "feedSourceType": "API",
       "logType": "WORKSPACE_ACTIVITY",
       "workspaceActivitySettings": {
         "authentication": {
           "tokenEndpoint": "https://oauth2.googleapis.com/token",
           "claims": {
             "issuer": "service-account@project.iam.gserviceaccount.com",
             "subject": "user@domain.com",
             "audience": "https://oauth2.googleapis.com/token"
           },
           "rsCredentials": {
             "privateKey": "-----BEGIN PRIVATE KEY-----
    ABCDeFGHIJKLMnopqrsT0u1VWXY...z/abCdefgHIJK+lMN2o345P=
             -----END PRIVATE KEY-----"
           },
         },
         "workspaceCustomerId": "C1e2x3ample",
         "applications": [
           "admin",
           "groups",
           "mobile"
         ],
       }
     }
    }
    

### Google Workspace Alerts

This section provides API reference details for the `WORKSPACE_ALERTS` log type. For details about the data source, see the [Google Workspace Alerts](https://developers.google.com/admin-sdk/alertcenter/reference/rest/v1beta1/alerts/list) documentation.

Data source | Ingest schedule | `details.feedSourceType` | `details.logType`  
---|---|---|---  
alertcenter.googleapis.com | Every hour | `API` | `WORKSPACE_ALERTS`  
  
#### Prerequisites

For Google Security Operations to ingest Google Workspace alerts, complete the following steps:

  1. Enable the [Alert Center API](https://developers.google.com/admin-sdk/alertcenter/guides/prerequisites) on your Google Cloud project.
  2. [Create a Service Account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) used to authenticate against the Alert Center API.
  3. [Generate a JSON key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys) for the Service Account.
  4. [Create a domain-wide delegation](https://developers.google.com/admin-sdk/directory/v1/guides/delegation) for the Service Account with the following OAuth scope: 
     * [https://www.googleapis.com/auth/apps.alerts](https://developers.google.com/identity/protocols/oauth2/scopes#alertcenter)
  5. Create a Google Workspace user and [assign it an administrator role](https://support.google.com/a/answer/9807615) with Alert Center view access, or [create a custom role](https://support.google.com/a/answer/2406043) with that privilege.
  6. [Locate your Google Workspace customer ID](https://support.google.com/a/answer/10070793).



To learn more about how to configure a feed to ingest Google Workspace logs, see [Collect Google Workspace logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-workspace-logs).

#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.workspaceAlertsSettings.authentication.tokenEndpoint` | Yes | The value of the `token_uri` field in the JSON key for the service account created to access the administrator API.  
`details.workspaceAlertsSettings.authentication.claims.issuer` | Yes | The value of the `client_email` field in the JSON key for the service account created to access the administrator API.  
`details.workspaceAlertsSettings.authentication.claims.subject` | Yes | The email address of the Google Workspace administrator user with Alert Center view access.  
`details.workspaceAlertsSettings.authentication.claims.audience` | Yes | The value of the `token_uri` field in the JSON key for the service account created to access the administrator API.  
`details.workspaceAlertsSettings.authentication.rsCredentials.privateKey` | Yes | The value of the `private_key` field in the JSON key for the service account created to access the Alert Center API. Note that literal newline characters (`\n`) should be replaced with carriage returns. Also note that the field name is `rsCredentials`, and not `rsaCredentials`.  
`details.workspaceAlertsSettings.workspaceCustomerId` | Yes | The Google Workspace customer ID. Note that the customer ID must _not_ have a leading 'C' character. The customer ID may appear differently depending on where in the Google administrator console it's found. If the customer ID you have has a leading 'C', then remove it before including in your request.  
  
#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example shows a `curl` request to retrieve alerts:
    
    
    curl --location 'https://alertcenter.googleapis.com/v1beta1/alerts?filter=createTime%20%3E%222025-05-06T01%3A00%3A00.000000Z%22&orderBy=createTime%20desc&customerId=04f3xv95' \
    --header 'Authorization: Bearer ya29.a0AW4XtxhL0Y4JUJj4p-bL1JDbSTprBuoXbtT3mToTpucNLr-4e1t1FGUGiVzcUU4IwCmM9EUBtDL6wTC7AFjBmtk2KciHzev8GWVSxLzsVKh1U15q_2Ziub48eKz850_5vTw6mUzi4Z64oR__oTwof1QAedQClQcHJyvr6heXOZLe8fnzCx6g8jwyaV4jII-s9YD7IR4jlHXauL6An-i2IwaCgYKAQUSARYSFQHGX2MiM-yCOt16l8VM6vlegKtYFA0221'
    

#### Sample create feed request
    
    
    {
     "details": {
       "feedSourceType": "API",
       "logType": "WORKSPACE_ALERTS",
       "workspaceAlertsSettings": {
         "authentication": {
           "tokenEndpoint": "https://oauth2.googleapis.com/token",
           "claims": {
             "issuer": "service-account@project.iam.gserviceaccount.com",
             "subject": "user@domain.com",
             "audience": "https://oauth2.googleapis.com/token"
           },
           "rsCredentials": {
             "privateKey": "-----BEGIN PRIVATE KEY-----
    ABCDeFGHIJKLMnopqrsT0u1VWXY...z/abCdefgHIJK+lMN2o345P=
             -----END PRIVATE KEY-----"
           },
         },
         "workspaceCustomerId": "1e2x3ample",
       }
     }
    }
    

### Google Workspace ChromeOS Devices

This section provides API reference details for the `WORKSPACE_CHROMEOS` log type. For details about the data source, see the [Google Workspace ChromeOS Devices](https://developers.google.com/admin-sdk/directory/v1/guides/manage-chrome-devices) documentation.

Data source | Ingest schedule | `details.feedSourceType` | `details.logType`  
---|---|---|---  
admin.googleapis.com | Every 24 hours | `API` | `WORKSPACE_CHROMEOS`  
  
#### Prerequisites

For Google Security Operations to ingest Google Workspace ChromeOS devices, complete the following steps:

  1. Enable the [Admin SDK API](https://developers.google.com/admin-sdk) on your Google Cloud project.
  2. [Create a Service Account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) used to authenticate against the administrator API.
  3. [Generate a JSON key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys) for the Service Account.
  4. [Create a domain-wide delegation](https://developers.google.com/admin-sdk/directory/v1/guides/delegation) for the Service Account with the following OAuth scope: 
     * [https://www.googleapis.com/auth/admin.directory.device.chromeos.readonly](https://developers.google.com/identity/protocols/oauth2/scopes#admin-directory)
  5. Create a Google Workspace user and [assign it an administrator role](https://support.google.com/a/answer/9807615) with Chrome Management Settings access, or [create a custom role](https://support.google.com/a/answer/2406043) with that privilege.
  6. [Locate your Google Workspace customer ID](https://support.google.com/a/answer/10070793).



To learn more about how to configure a feed to ingest Google Workspace logs, see [Collect Google Workspace logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-workspace-logs).

#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.workspaceChromeOsSettings.authentication.tokenEndpoint` | Yes | The value of the `token_uri` field in the JSON key for the service account created to access the administrator API.  
`details.workspaceChromeOsSettings.authentication.claims.issuer` | Yes | The value of the `client_email` field in the JSON key for the service account created to access the administrator API.  
`details.workspaceChromeOsSettings.authentication.claims.subject` | Yes | The email address of the Google Workspace administrator user with Chrome Management Settings access.  
`details.workspaceChromeOsSettings.authentication.claims.audience` | Yes | The value of the `token_uri` field in the JSON key for the service account created to access the administrator API.  
`details.workspaceChromeOsSettings.authentication.rsCredentials.privateKey` | Yes | The value of the `private_key` field in the JSON key for the service account created to access the administrator API. Replace the literal newline characters (`\n`) with carriage returns. The field name is `rsCredentials`, and not `rsaCredentials`.  
`details.workspaceChromeOsSettings.workspaceCustomerId` | Yes | The Google Workspace customer ID. Note that the customer ID must have a leading 'C' character. The customer ID may appear differently depending on where in the Google administrator console it's found. If the customer ID you have does not have a leading 'C', then prepend what you have with a 'C'.  
  
#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example shows a `curl` request to retrieve alerts:
    
    
    curl --location 'https://admin.googleapis.com/admin/directory/v1/customer/C02whl9a1/devices/chromeos?pageToken=CloaVAo0qgExCi8wLDI0NjY2ODY0ODgsOTMyODk0NzMsInYxOjAwNzY0OTQ0NzkxMDIyNjcxMTQyIiIcY2RtX2RldmljZS5kZHNfc29ydF9rZXkgZGVzY0gBUAAaAhIA&maxResults=1000' \
    --header 'Authorization: Bearer ya29.a0AW4Xtxju-YA65Lkc4Yl4W2-v7YTXeuadv7Rw_5mPIKbPgnW5gcKqRB8w-osdVZG3jtlPT51UkGig6r017GDdqPblTufwTc16laa2oq-R3wmnWmZNGs_17pPreh8zX-EoG3_uLPY4AychzYXrXtISvyjpyyGyq2u6nUmQ5tH6wN5wbM1Bq15KNrV8gSZwzLNrkIMYriknX-WGZ7vrTVzrUQaCgYKAQISARUSFQHGX2MiqmbcGjl0-BxmN-EmpG43qQ0221'
    

#### Sample create feed request
    
    
    {
     "details": {
       "feedSourceType": "API",
       "logType": "WORKSPACE_CHROMEOS",
       "workspaceChromeOsSettings": {
         "authentication": {
           "tokenEndpoint": "https://oauth2.googleapis.com/token",
           "claims": {
             "issuer": "service-account@project.iam.gserviceaccount.com",
             "subject": "user@domain.com",
             "audience": "https://oauth2.googleapis.com/token"
           },
           "rsCredentials": {
             "privateKey": "-----BEGIN PRIVATE KEY-----
    ABCDeFGHIJKLMnopqrsT0u1VWXY...z/abCdefgHIJK+lMN2o345P=
             -----END PRIVATE KEY-----"
           },
         },
         "workspaceCustomerId": "C1e2x3ample",
       }
     }
    }
    

### Google Workspace Groups

This section provides API reference details for the `WORKSPACE_GROUPS` log type. For details about the data source, see the [Google Workspace Groups](https://developers.google.com/admin-sdk/directory/reference/rest/v1/groups/list) documentation.

Data source | Ingest schedule | `details.feedSourceType` | `details.logType`  
---|---|---|---  
admin.googleapis.com | Every 24 hours | `API` | `WORKSPACE_GROUPS`  
  
#### Prerequisites

For Google Security Operations to ingest Google Workspace Groups, complete the following steps:

  1. Enable the [Admin SDK API](https://developers.google.com/admin-sdk) on your Google Cloud project.
  2. [Create a Service Account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) used to authenticate against the administrator API.
  3. [Generate a JSON key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys) for the Service Account.
  4. [Create a domain-wide delegation](https://developers.google.com/admin-sdk/directory/v1/guides/delegation) for the Service Account with the following OAuth scope: 
     * [https://www.googleapis.com/auth/admin.directory.group.readonly](https://developers.google.com/identity/protocols/oauth2/scopes#admin-directory)
  5. Create a Google Workspace user and [assign it an administrator role](https://support.google.com/a/answer/9807615) with administrator API Group read privileges, or [create a custom role](https://support.google.com/a/answer/2406043) with that privilege.
  6. [Locate your Google Workspace customer ID](https://support.google.com/a/answer/10070793).



To learn more about how to configure a feed to ingest Google Workspace logs, see [Collect Google Workspace logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-workspace-logs).

#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.workspaceGroupsSettings.authentication.tokenEndpoint` | Yes | The value of the `token_uri` field in the JSON key for the service account created to access the administrator API.  
`details.workspaceGroupsSettings.authentication.claims.issuer` | Yes | The value of the `client_email` field in the JSON key for the service account created to access the administrator API.  
`details.workspaceGroupsSettings.authentication.claims.subject` | Yes | The email address of the Google Workspace administrator user with the administrator API Group read privilege.  
`details.workspaceGroupsSettings.authentication.claims.audience` | Yes | The value of the `token_uri` field in the JSON key for the service account created to access the administrator API.  
`details.workspaceGroupsSettings.authentication.rsCredentials.privateKey` | Yes | The value of the `private_key` field in the JSON key for the service account created to access the administrator API. Note that literal newline characters (`\n`) should be replaced with carriage returns. Note that the field name is `rsCredentials`, and not `rsaCredentials`.  
`details.workspaceGroupsSettings.workspaceCustomerId` | Yes | The Google Workspace customer ID. Note that the customer ID must have a leading 'C' character. The customer ID may appear differently depending on where in the Google administrator console it is found. If the customer ID you have does not have a leading 'C' then prepend what you have with a 'C'.  
  
#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example shows a `curl` request to retrieve groups:
    
    
    curl --location 'https://admin.googleapis.com/admin/directory/v1/groups?maxResults=10&customer=C04f3xv95' \
    --header 'Authorization: Bearer token'
    

#### Sample create feed request
    
    
    {
     "details": {
       "feedSourceType": "API",
       "logType": "WORKSPACE_GROUPS",
       "workspaceGroupsSettings": {
         "authentication": {
           "tokenEndpoint": "https://oauth2.googleapis.com/token",
           "claims": {
             "issuer": "service-account@project.iam.gserviceaccount.com",
             "subject": "user@domain.com",
             "audience": "https://oauth2.googleapis.com/token"
           },
           "rsCredentials": {
             "privateKey": "-----BEGIN PRIVATE KEY-----
    ABCDeFGHIJKLMnopqrsT0u1VWXY...z/abCdefgHIJK+lMN2o345P=
             -----END PRIVATE KEY-----"
           },
         },
         "workspaceCustomerId": "C1e2x3ample",
       }
     }
    }
    

### Google Workspace Mobile Devices

This section provides API reference details for the `WORKSPACE_MOBILE` log type. For details about the data source, see the [Google Workspace Mobile Devices](https://developers.google.com/admin-sdk/directory/v1/guides/manage-mobile-devices) documentation.

Data source | Ingest schedule | `details.feedSourceType` | `details.logType`  
---|---|---|---  
admin.googleapis.com | Every 24 hours | `API` | `WORKSPACE_MOBILE`  
  
#### Prerequisites

For Google Security Operations to ingest Google Workspace Mobile devices, complete the following steps:

  1. Enable the [Admin SDK API](https://developers.google.com/admin-sdk) on your Google Cloud project.
  2. [Create a Service Account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) used to authenticate against the administrator API.
  3. [Generate a JSON key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys) for the Service Account.
  4. [Create a domain-wide delegation](https://developers.google.com/admin-sdk/directory/v1/guides/delegation) for the Service Account with the following OAuth scope: 
     * [https://www.googleapis.com/auth/admin.directory.device.mobile.readonly](https://developers.google.com/identity/protocols/oauth2/scopes#admin-directory)
  5. Create a Google Workspace user and [assign it an administrator role](https://support.google.com/a/answer/9807615) with Mobile Device Management Settings access, or [create a custom role](https://support.google.com/a/answer/2406043) with that privilege.
  6. [Locate your Google Workspace customer ID](https://support.google.com/a/answer/10070793).



To learn more about how to configure a feed to ingest Google Workspace logs, see [Collect Google Workspace logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-workspace-logs).

#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.workspaceMobileSettings.authentication.tokenEndpoint` | Yes | The value of the `token_uri` field in the JSON key for the service account created to access the administrator API.  
`details.workspaceMobileSettings.authentication.claims.issuer` | Yes | The value of the `client_email` field in the JSON key for the service account created to access the administrator API.  
`details.workspaceMobileSettings.authentication.claims.subject` | Yes | The email address of the Google Workspace administrator user with the Mobile Device Management Settings access.  
`details.workspaceMobileSettings.authentication.claims.audience` | Yes | The value of the `token_uri` field in the JSON key for the service account created to access the administrator API.  
`details.workspaceMobileSettings.authentication.rsCredentials.privateKey` | Yes | The value of the `private_key` field in the JSON key for the service account created to access the administrator API. Note that literal newline characters (`\n`) should be replaced with carriage returns. Note that the field name is `rsCredentials`, and not `rsaCredentials`.  
`details.workspaceMobileSettings.workspaceCustomerId` | Yes | The Google Workspace customer ID. Note that the customer ID must have a leading 'C' character. The customer ID may appear differently depending on where in the Google administrator console it is found. If the customer ID you have does not have a leading 'C' then prepend what you have with a 'C'.  
  
#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example shows a `curl` request to retrieve mobile devices:
    
    
    curl --location 'https://admin.googleapis.com/admin/directory/v1/users' \
    --header 'Authorization: Bearer ya29.a0AW4XtxgNLeN4E506tSSlKbejjo2Vcjv3w6lVYr6y1jqn6MGolG101Xd2-UojXPR-_pK5wBx2Kqi--XDJXeH0AA-2x6bVBOw1WaZzPCK4aHl6qP-sgUEpYfbt6b27celqR68VDw-ylbMwb-  xz ZX ZX ZX zx-LSdnIQrb2gaCgYKAbYSARESFQHGX2Mi0n47o6S7eLTpsmLmwQPHdQ0221'
    

#### Sample create feed request
    
    
    {
     "details": {
       "feedSourceType": "API",
       "logType": "WORKSPACE_MOBILE",
       "workspaceMobileSettings": {
         "authentication": {
           "tokenEndpoint": "https://oauth2.googleapis.com/token",
           "claims": {
             "issuer": "service-account@project.iam.gserviceaccount.com",
             "subject": "user@domain.com",
             "audience": "https://oauth2.googleapis.com/token"
           },
           "rsCredentials": {
             "privateKey": "-----BEGIN PRIVATE KEY-----
    ABCDeFGHIJKLMnopqrsT0u1VWXY...z/abCdefgHIJK+lMN2o345P=
             -----END PRIVATE KEY-----"
           },
         },
         "workspaceCustomerId": "C1e2x3ample",
       }
     }
    }
    

### Google Workspace Privileges

This section provides API reference details for the `WORKSPACE_PRIVILEGES` log type. For details about the data source, see the [Google Workspace Privileges](https://developers.google.com/admin-sdk/directory/reference/rest/v1/privileges/list) documentation.

Data source | Ingest schedule | `details.feedSourceType` | `details.logType`  
---|---|---|---  
admin.googleapis.com | Every 24 hours | `API` | `WORKSPACE_PRIVILEGES`  
  
#### Prerequisites

For Google Security Operations to ingest Google Workspace privileges, complete the following steps:

  1. Enable the [Admin SDK API](https://developers.google.com/admin-sdk) on your Google Cloud project.
  2. [Create a Service Account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) used to authenticate against the administrator API.
  3. [Generate a JSON key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys) for the Service Account.
  4. [Create a domain-wide delegation](https://developers.google.com/admin-sdk/directory/v1/guides/delegation) for the Service Account with the following OAuth scope: 
     * [https://www.googleapis.com/auth/admin.directory.rolemanagement.readonly](https://developers.google.com/identity/protocols/oauth2/scopes#admin-directory)
  5. Create a Google Workspace user and [assign it a super administrator role](https://support.google.com/a/answer/9807615).
  6. [Locate your Google Workspace customer ID](https://support.google.com/a/answer/10070793).



To learn more about how to configure a feed to ingest Google Workspace logs, see [Collect Google Workspace logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-workspace-logs).

#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.workspacePrivilegesSettings.authentication.tokenEndpoint` | Yes | The value of the `token_uri` field in the JSON key for the service account created to access the administrator API.  
`details.workspacePrivilegesSettings.authentication.claims.issuer` | Yes | The value of the `client_email` field in the JSON key for the service account created to access the administrator API.  
`details.workspacePrivilegesSettings.authentication.claims.subject` | Yes | The email address of the Google Workspace super administrator user.  
`details.workspacePrivilegesSettings.authentication.claims.audience` | Yes | The value of the `token_uri` field in the JSON key for the service account created to access the administrator API.  
`details.workspacePrivilegesSettings.authentication.rsCredentials.privateKey` | Yes | The value of the `private_key` field in the JSON key for the service account created to access the administrator API. Note that literal newline characters (`\n`) should be replaced with carriage returns. Note that the field name is `rsCredentials`, and not `rsaCredentials`.  
`details.workspacePrivilegesSettings.workspaceCustomerId` | Yes | The Google Workspace customer ID. Note that the customer ID must have a leading 'C' character. The customer ID may appear differently depending on where in the Google administrator console it's found. If the customer ID you have does not have a leading 'C' then prepend what you have with a 'C'.  
  
#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example shows a `curl` request to retrieve role assignments:
    
    
    curl --location 'https://admin.googleapis.com/admin/directory/v1/customer/[CID]/roleassignments?maxResults=10' \
    --header 'Authorization: Bearer Access Token'
    

The following example shows a `curl` request to retrieve access privileges:
    
    
    curl --location --globoff 'https://admin.googleapis.com/admin/directory/v1/customer/[CID]/roles/ALL/privileges' \
    --header 'Authorization: Bearer Access Token'
    

The following is an example request to retrieve role information using curl:
    
    
    curl --location 'https://admin.googleapis.com/admin/directory/v1/customer/[CID]/roles?maxResults=10' \
    --header 'Authorization: Bearer Access Token'
    

The following example shows a `curl` request to retrieve access tokens:
    
    
    curl --location 'https://oauth2.googleapis.com/token' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer' \
    --data-urlencode 'assertion=signature'
    

#### Sample create feed request
    
    
    {
     "details": {
       "feedSourceType": "API",
       "logType": "WORKSPACE_PRIVILEGES",
       "workspacePrivilegesSettings": {
         "authentication": {
           "tokenEndpoint": "https://oauth2.googleapis.com/token",
           "claims": {
             "issuer": "service-account@project.iam.gserviceaccount.com",
             "subject": "user@domain.com",
             "audience": "https://oauth2.googleapis.com/token"
           },
           "rsCredentials": {
             "privateKey": "-----BEGIN PRIVATE KEY-----
    ABCDeFGHIJKLMnopqrsT0u1VWXY...z/abCdefgHIJK+lMN2o345P=
             -----END PRIVATE KEY-----"
           },
         },
         "workspaceCustomerId": "C1e2x3ample",
       }
     }
    }
    

### Google Workspace Users

This section provides API reference details for the `WORKSPACE_USERS` log type. For details about the data source, see the [Google Workspace Users](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list) documentation.

Data source | Ingest schedule | `details.feedSourceType` | `details.logType`  
---|---|---|---  
admin.googleapis.com | Every 24 hours | `API` | `WORKSPACE_USERS`  
  
#### Prerequisites

For Google Security Operations to ingest Google Workspace Users, complete the following steps:

  1. Enable the [Admin SDK API](https://developers.google.com/admin-sdk) on your Google Cloud project.
  2. [Create a Service Account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) used to authenticate against the administrator API.
  3. [Generate a JSON key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys) for the Service Account.
  4. [Create a domain-wide delegation](https://developers.google.com/admin-sdk/directory/v1/guides/delegation) for the Service Account with the following OAuth scope: 
     * [https://www.googleapis.com/auth/admin.directory.user.readonly](https://developers.google.com/identity/protocols/oauth2/scopes#admin-directory)
  5. Create a Google Workspace user and [assign it an administrator role](https://support.google.com/a/answer/9807615) that includes administrator API User read privileges, or [create a custom role](https://support.google.com/a/answer/2406043) that includes that privilege.
  6. [Locate your Google Workspace customer ID](https://support.google.com/a/answer/10070793).
  7. Create a feed in Google SecOps as follows:

     1. Click the **Google Workspace** pack.
     2. Locate the **Workspace Users** log type.
     3. Specify values for the following fields:

        * **Source Type** : Third Party API
        * **OAuth JWT endpoint** : contains the OAuth JSON Web Token. Specify the `token_uri` value from the service account JSON key.
        * **JWT claims issuer** : client ID. Specify the `client_email` value from the service account JSON key. For example, `InsertServiceAccount@project.iam.gserviceaccount.com`
        * **JWT claims subject** : email address of the user that you created in the Google Workspace Admin console.
        * **JWT claims audience** : `token_uri` value from the service account JSON key.
        * **RSA private key** : key in PEM format. The PEM key is available in the service account key file. When you enter the private key, include the `BEGIN PRIVATE KEY` header and the `END PRIVATE KEY` footer in the field.
        * **Customer ID** : for all log types, except the Alerts log type, the customer ID field requires a leading 'C' character. If the customer ID field does not contain a leading 'C' character, then prepend what the value with a 'C' character.
        * **Projection Type** : choose Basic - Don't include any custom fields for the user, or Full - Include all fields associated with this user.

**Advanced options**

        * **Feed Name** : A prepopulated value that identifies the feed.
        * **Asset Namespace** : Namespace associated with the feed.
        * **Ingestion Labels** : Labels applied to all events from this feed.



To learn more about how to configure a feed to ingest Google Workspace logs, see [Collect Google Workspace logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-workspace-logs).

#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.workspaceUserSettings.authentication.tokenEndpoint` | Yes | The value of the `token_uri` field in the JSON key for the service account created to access the administrator API.  
`details.workspaceUserSettings.authentication.claims.issuer` | Yes | The value of the `client_email` field in the JSON key for the service account created to access the administrator API.  
`details.workspaceUserSettings.authentication.claims.subject` | Yes | The email address of the Google Workspace administrator user with the administrator API User read privilege.  
`details.workspaceUserSettings.authentication.claims.audience` | Yes | The value of the `token_uri` field in the JSON key for the service account created to access the administrator API.  
`details.workspaceUserSettings.authentication.rsCredentials.privateKey` | Yes | The value of the `private_key` field in the JSON key for the service account created to access the administrator API. Note that literal newline characters (`\n`) should be replaced with carriage returns. Note that the field name is `rsCredentials`, and not `rsaCredentials`.  
`details.workspaceUserSettings.workspaceCustomerId` | Yes | The Google Workspace customer ID. Note that the customer ID must have a leading 'C' character. The customer ID may appear differently depending on where in the Google administrator console it is found. If the customer ID you have does not have a leading 'C' then prepend what you have with a 'C'.  
  
#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example shows a `curl` request to retrieve users:
    
    
    curl --location 'https://admin.googleapis.com/admin/directory/v1/users?customer=C04f3xv95&maxResults=500&pageToken=Q0FFU3RnSUJrUHpWQVA5NEZZdkIrSDRDMXJkL2VWaVBzN3BETEhiazd6eGhkUVM4RkZqQmRFV0E0dzZYNWNJQWRxNnVsRjhTM09CQVY1UGZ4bGNIeDdZWTFvd0ZLY0xKRkptV3JJSXlQQTFodWI3VGoxT2UyU0tkSjZjZFI0YlVqemV0L1JRbzR6VkJsWkFFR2ROMER1SHBLRlhSMDgyZStIdjRvcDZsUENHdzZ1d3RUYlBVYmJwMW1oOW1pK2Rtd1JUaXgrRjJxZEZqVU1yMUxrTFB0c0dqVXBXdnpVdVc1UzdMRm1sYms2bWhmdE8wdFBqY1hzc2E2Y1psTWxscDdERStmMzFuWFc0emZhK1REVWlhVTNVQzhOTFBWR1hmbitYNlhKOEovRXQ0Yk9BNTNUOURLZllSSTV2bCtYNXBQbHF2RU1ydnV1VnNIdHlHK1R4TW9uNnhUM3Q4TlNkUDQ5TGl3WXlRTE1XaFJUc3ZUOW5Bei9KRjlFSnR2YlBwVURCMENzbkZxbFFRUm9WQ1dEMHZpTFFHYlErN1BJL2t2Z3Bw' \
    --header 'Authorization: Bearer ya29.a0AW4XtxijofuSQh0vIGModmk2CkVaNAqMHJmOL9x1hXVxOfjrildQIVhp_TAIkzm9zd5re2EVhMiRFO5VCgCuoowwvNxL3MAZ4uAMc9QJuxS2ju2ku2qKCxINWqeLWIhRcTnBF8SfLTWWVa1BoppLxidJF4TPMRJ9heTzNvp0s-ppXEgDempQncY9QzXNt7DJekrKL4Tnp07X--K8qNz3BwaCgYKAYsSARYSFQHGX2MiBAfxmnBJqb0cZFBppmor1g0221'
    

#### Sample create feed request
    
    
    {
     "details": {
       "feedSourceType": "API",
       "logType": "WORKSPACE_USERS",
       "workspaceUserSettings": {
         "authentication": {
           "tokenEndpoint": "https://oauth2.googleapis.com/token",
           "claims": {
             "issuer": "service-account@project.iam.gserviceaccount.com",
             "subject": "user@domain.com",
             "audience": "https://oauth2.googleapis.com/token"
           },
           "rsCredentials": {
             "privateKey": "-----BEGIN PRIVATE KEY-----
    ABCDeFGHIJKLMnopqrsT0u1VWXY...z/abCdefgHIJK+lMN2o345P=
             -----END PRIVATE KEY-----"
           },
         },
         "workspaceCustomerId": "C1e2x3ample",
       }
     }
    }
    

### Imperva

This section provides API reference details for the `IMPERVA_WAF` log type. For details about the data source, see the [Imperva documentation](https://docs-cybersec.thalesgroup.com/bundle/api-docs/page/audit-trail-api-definition.htm?operationId=operations-Audit_Trail-getAuditEventsV2).

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
`api.imperva.com/audit-trail/v2/events` | Every 24 hours | `API`  
  
#### Prerequisites

  * Get the values for all authentication fields.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.impervaWafSettings.authentication.headerKeyValues` | Yes | The HTTP header used to authenticate `api.imperva.com` in key-value format.  
  
#### Optional fields

`initialStartTime`

#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example shows a `curl` request to retrieve audit data:
    
    
    curl --location 'https://api.imperva.com/audit-trail/v2/events?start=1750747297110&limit=1&offset=0' \
    --header 'x-API-Key: $xxxxxxxxxxxxxxxx-2cf15bdc33c0' \
    --header 'x-API-Id: 12344'
    

#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "IMPERVA_WAF",
         "impervaWafSettings": {
           "authentication": {
             "headerKeyValues": [{
                "key": "key"
                "value": "value"
             }],
           }
         }
       }
    }
    

### Microsoft Azure Active Directory Audit

This section provides API reference details for the `AZURE_AD_AUDIT` log type. For details about the data source, see [Azure Active Directory Audit](https://docs.microsoft.com/en-us/graph/api/directoryaudit-list).

Data source | Ingest schedule | `details.feedSourceType` | `details.logType`  
---|---|---|---  
graph.microsoft.com | Every minute | `API` | `AZURE_AD_AUDIT`  
**Note:** The Azure Active Directory Audit feed supports beta Microsoft Graph API endpoints, but does not support filters.

#### Prerequisites

  * Get an Azure AD Premium P1 or P2 license. For more information, see [License requirements](https://learn.microsoft.com/en-us/graph/api/resources/azure-ad-auditlog-overview?view=graph-rest-1.0#license-requirements).
  * Get the values for all required request fields. Note that the token endpoint for OAuth 2.0 is: https://login.microsoftonline.com/{tenantId}/oauth2/token
  * Get the following required permissions: 
    * The user whose credentials are used to authenticate against the Microsoft Graph API to access [directory audits](https://docs.microsoft.com/en-us/graph/api/directoryaudit-list) must have the [permissions](https://docs.microsoft.com/en-us/graph/permissions-reference) `AuditLog.Read.All` and `Directory.Read.All`.



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.azureAdAuditSettings.authentication.clientId` | Yes | Application ID (a UUID)  
`details.azureAdAuditSettings.authentication.clientSecret` | Yes | Client Secret  
`details.azureAdAuditSettings.tenantId` | Yes | Tenant ID (a UUID)  
`details.azureAdAuditSettings.hostname` | No | API Full Path, default value : `"graph.microsoft.com/v1.0/auditLogs/directoryAudits"`  
  
#### Test the API endpoint by using curl

Before you create the feed, use `curl` to test the API endpoint.

  1. Request an OAuth token to authenticate your request to the API resource. 
         
         curl 'https://login.microsoftonline.com/TENANT_ID/oauth2/token' \
             --data-urlencode 'grant_type=client_credentials' \
             --data-urlencode 'client_id=CLIENT_ID' \
             --data-urlencode 'client_secret=CLIENT_SECRET' \
             --data-urlencode 'resource=https://graph.microsoft.com'
         

Replace the following:

     * CLIENT_ID: Application ID
     * CLIENT_SECRET: Client secret
     * TENANT_ID: Tenant ID

The result of the curl request is a JSON response that contains the OAuth access token.

  2. Send a request to the Microsoft Graph API endpoint using the OAuth token. 
         
         curl 'https://graph.microsoft.com/v1.0/auditLogs/signIns' \
             --header 'Accept: application/json' \
             --header 'Authorization: Bearer ACCESS_TOKEN'
         

Replace ACCESS_TOKEN with the value of the OAuth access token that you obtained from the previous step.




#### Sample create feed request
    
    
    {
     "details": {
       "feedSourceType": "API",
       "logType": "AZURE_AD_AUDIT",
       "azureAdAuditSettings": {
         "authentication": {
           "clientId": "0ab12c34-d5ef-678g-9012-hi34j56k78l9",
           "clientSecret": "clientSecret",
         }
         "tenantId": "0ab123c4-de56-78fg-90h1-ijk2l3456789",
         "hostname": "graph.microsoft.com/v1.0/auditLogs/directoryAudits",
       }
     }
    }
    

### Microsoft Azure Active Directory Organizational Context

This section provides API reference details for the `AZURE_AD_CONTEXT` log type. For details about the data source, see the Microsoft Graph API [List users endpoint](https://learn.microsoft.com/en-us/graph/api/user-list?view=graph-rest-1.0&tabs=http), which this feed uses to retrieve device and group data.

Data source | Ingest schedule | `details.feedSourceType` | `details.logType`  
---|---|---|---  
graph.microsoft.com | Every 24 hours | `API` | `AZURE_AD_CONTEXT`  
  
#### Prerequisites

  * Get the values for all required request fields. The token endpoint for OAuth 2.0 is `https://login.microsoftonline.com/{tenantId}/oauth2/token`
  * Get the following required permissions: 
    * The user whose credentials are used to authenticate against Microsoft Graph API to access organizational context must have [permissions](https://docs.microsoft.com/en-us/graph/permissions-reference) `Directory.Read.All`.



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.azureAdContextSettings.authentication.clientId` | Yes | Application ID (a UUID)  
`details.azureAdContextSettings.authentication.clientSecret` | Yes | Client secret  
`details.azureAdContextSettings.tenantId` | Yes | Tenant ID (a UUID)  
`details.azureAdContextSettings.retrieveDevices` | No | Whether to retrieve device information  
`details.azureAdContextSettings.retrieveGroups` | No | Whether to retrieve user group information  
`details.azureAdContextSettings.hostname` | No | API Full Path, default value : `graph.microsoft.com/beta`  
  
#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example shows a `curl` request to retrieve details for all users:
    
    
    curl --location 'https://graph.microsoft.com/v1.0/users?%24top=999&%24select=*&%24expand=manager' \
    --header 'Authorization: Bearer XXX'
    

The following example shows a `curl` request to retrieve the group information for a given user ID:
    
    
    curl --location 'https://graph.microsoft.com/v1.0/users/2949fc05-94b3-4277-8d07-b42b3798e209/transitiveMemberOf?%24select=*' \
    --header 'Authorization: Bearer XXX'
    

The following example shows a `curl` request to retrieve device information for a given user ID:
    
    
    curl --location 'https://graph.microsoft.com/v1.0/users/d6b9dd46-e585-41c6-91ae-841690b07d64/ownedDevices' \
    --header 'Authorization: Bearer XXX'
    

#### Sample create feed request
    
    
    {
     "details": {
       "feedSourceType": "API",
       "logType": "AZURE_AD_CONTEXT",
       "azureAdContextSettings": {
         "authentication": {
           "clientId": "0ab12c34-d5ef-678g-9012-hi34j56k78l9",
           "clientSecret": "clientSecret",
         }
         "tenantId": "0ab123c4-de56-78fg-90h1-ijk2l3456789",
         "retrieveDevices": false,
         "retrieveGroups": false,
         "hostname": "graph.microsoft.com/beta",
       }
     }
    }
    

### Microsoft Azure Active Directory Sign-ins

This section provides API reference details for the `AZURE_AD` log type. For details about the data source, see the [Azure Active Directory Sign-ins](https://docs.microsoft.com/en-us/graph/api/signin-list) documentation.

Data source | Ingest schedule | `details.feedSourceType` | `details.logType`  
---|---|---|---  
graph.microsoft.com | Every minute | `API` | `AZURE_AD`  
**Note:** For `AZURE_AD` logs, Google SecOps maintains a lookback window of 30 minutes to capture delayed records (backfillability).

#### Prerequisites

  * Get an Azure AD Premium P1 or P2 license. For more information, see [License requirements](https://learn.microsoft.com/en-us/graph/api/resources/azure-ad-auditlog-overview?view=graph-rest-1.0#license-requirements).
  * Get the values for all required request fields. The token endpoint for OAuth 2.0 is `https://login.microsoftonline.com/{tenantId}/oauth2/token`
  * Get the following required permissions: 
    * The user whose credentials are used to authenticate against Microsoft Graph API to access [sign-ins](https://docs.microsoft.com/en-us/graph/api/signin-list) must have [permissions](https://docs.microsoft.com/en-us/graph/permissions-reference) `AuditLog.Read.All` and `Directory.Read.All`.



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.azureAdSettings.authentication.clientId` | Yes | Application ID (a UUID)  
`details.azureAdSettings.authentication.clientSecret` | Yes | Client Secret  
`details.azureAdSettings.tenantId` | Yes | Tenant ID (a UUID)  
`details.azureAdSettings.hostname` | No | API Full Path, default value : `graph.microsoft.com/v1.0/auditLogs/signIns`  
  
#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example shows a `curl` request to retrieve audits:
    
    
    curl --location 'https://graph.microsoft.com/v1.0/auditLogs/signIns' \
    --header 'Authorization: Bearer token'
    

#### Sample create feed request
    
    
    {
     "details": {
       "feedSourceType": "API",
       "logType": "AZURE_AD",
       "azureAdSettings": {
         "authentication": {
           "clientId": "0ab12c34-d5ef-678g-9012-hi34j56k78l9",
           "clientSecret": "clientSecret",
         }
         "tenantId": "0ab123c4-de56-78fg-90h1-ijk2l3456789",
         "hostname": "graph.microsoft.com/v1.0/auditLogs/signIns",
       }
     }
    }
    

### Microsoft Azure Microsoft Device Management Intune Audit Events

This section provides API reference details for the `AZURE_MDM_INTUNE` log type. For details about the data source, see the [Azure Microsoft Device Management Intune Audit Events](https://docs.microsoft.com/en-us/graph/api/intune-auditing-auditevent-list) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
The Microsoft Graph REST API endpoint URL. The default value is `graph.microsoft.com/beta/deviceManagement/auditEvents` | Every minute | `API`  
  
#### Prerequisites

  * Get an [active Intune license](https://www.microsoft.com/en-us/security/business/endpoint-management/microsoft-intune).
  * Get the values for all authentication fields. The token endpoint for OAuth 2.0 is `https://login.microsoftonline.com/{tenantId}/oauth2/token`
  * Get the following required permission: 
    * The provisioned OAuth client must have [permission](https://docs.microsoft.com/en-us/graph/permissions-reference) `DeviceManagementApps.Read.All` or `DeviceManagementApps.ReadWrite.All`.



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.azureMdmIntuneSettings.authentication.clientId` | Yes | The application ID.  
`details.azureMdmIntuneSettings.authentication.clientSecret` | Yes | The client secret.  
`details.azureMdmIntuneSettings.tenantId` | Yes | The tenant ID, which is a UUID.  
`details.azureMdmIntuneSettings.hostname` | No | The Microsoft Graph REST API endpoint URL. The following is the default value: `graph.microsoft.com/beta/deviceManagement/auditEvents`.  
  
#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example shows a `curl` request to retrieve audit:
    
    
    curl --location 'https://graph.microsoft.com/beta/deviceManagement/auditEvents' \
    --header 'Authorization: Bearer token'
    

#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "AZURE_MDM_INTUNE",
         "azureMdmIntuneSettings": {
           "authentication": {
             "clientId": "0ab12c34-d5ef-678g-9012-hi34j56k78l9",
             "clientSecret": "clientSecret",
           }
           "tenantId": "0ab123c4-de56-78fg-90h1-ijk2l3456789",
           "hostname": "graph.microsoft.com/beta/deviceManagement/auditEvents",
         }
       }
    }
    

### Microsoft Graph Security API Alerts

**Caution:** **Microsoft Graph Security Legacy Alerts Deprecation**

According to [Microsoft documentation](https://learn.microsoft.com/en-us/graph/api/resources/alert?view=graph-rest-1.0), the Legacy Alerts option will be fully deprecated on **April 10, 2026**. After this date, configuring this integration to use the "Legacy Alerts" option will stop returning data. Users utilizing Legacy Alerts must migrate to the **Alerts v2 API** option to ensure continued data ingestion.

This section provides API reference details for the `MICROSOFT_GRAPH_ALERT` log type. For details about the data source, see Microsoft Graph Security [Legacy List alerts](https://learn.microsoft.com/en-us/graph/api/alert-list) and [List alerts_v2](https://learn.microsoft.com/en-us/graph/api/security-list-alerts_v2?view=graph-rest-1.0&tabs=http).

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
  
  * `graph.microsoft.com/v1.0/security/alerts`
  * `graph.microsoft.com/v1.0/security/alerts_v2`

| Every minute | `API`  
  
#### Prerequisites

  * Get the values for authentication fields. The token endpoint for OAuth 2.0 is `https://login.microsoftonline.com/{tenantId}/oauth2/token`
  * Get the following required permissions; the API supports two data sources: 
    * `graph.microsoft.com/v1.0/security/alerts` requires `SecurityEvents.Read.All` permissions
    * `graph.microsoft.com/beta/security/alerts_v2` or `graph.microsoft.com/v1.0/security/alerts_v2` requires `SecurityAlert.Read.All` permissions
    * The user whose credentials are used must have [permissions](https://docs.microsoft.com/en-us/graph/permissions-reference) `SecurityEvents.Read.All`.



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.microsoftGraphAlertSettings.authentication.clientId` | Yes | Application ID (a UUID)  
`details.microsoftGraphAlertSettings.authentication.clientSecret` | Yes | Client secret  
`details.microsoftGraphAlertSettings.tenantId` | Yes | Tenant ID (a UUID)  
`details.microsoftGraphAlertSettings.authEndpoint` | Yes | The Microsoft Active Directory authentication endpoint. The default value is `login.microsoftonline.com`.  
`details.microsoftGraphAlertSettings.hostname` | No | The API full path. The default value is `graph.microsoft.com/v1.0/security/alerts`  
  
#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

  1. Request an OAuth token to authenticate your request to the API resource: 
         
         curl --location 'https://login.microsoftonline.com/c990bb7a-51f4-439b-bd36-9c07fb1041c0/oauth2/token'   
         
         --header 'Content-Type: application/x-www-form-urlencoded'   
         
         --header 'Cookie: fpc=AslaSjK3O0xMiJ4per_H_amVeD2hAQAAAM05498OAAAA; stsservicecookie=estsfd; x-ms-gateway-slice=estsfd'   
         
         --data-urlencode 'client_id=id'   
         
         --data-urlencode 'client_secret=secret'   
         
         --data-urlencode 'grant_type=client_credentials'   
         
         --data-urlencode 'resource=https://graph.microsoft.com/'
         




Replace the following placeholders:

  * ID: Your Application (client) ID
  * secret: Your client secret


  1. Use the OAuth token to send a request to the Microsoft Graph Security API: 
         
         curl --location 'https://graph.microsoft.com/v1.0/security/alerts'   
         
         --header 'Authorization: Bearer '
         




Replace the following placeholder:

  * ACCESS_TOKEN: OAuth access token



#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "MICROSOFT_GRAPH_ALERT",
         "microsoftGraphAlertSettings": {
           "authentication": {
             "clientId": "0ab12c34-d5ef-678g-9012-hi34j56k78l9",
             "clientSecret": "clientSecret",
           }
           "tenantId": "0ab123c4-de56-78fg-90h1-ijk2l3456789",
           "hostname": "graph.microsoft.com/v1.0/security/alerts",
           "authEndpoint": "login.microsoftonline.com",
         }
       }
    }
    

### Microsoft Office 365 Management Activity

This section provides API reference details for the `OFFICE_365` log type. For details about the data source, see the [Microsoft Office 365 Management Activity](https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-reference) documentation.

**Note:** The Source API returns duplicate events for OFFICE_365 log types. This is the intended behavior to prevent the loss of any audit events.**Data source** | **Ingest schedule** | **`details.feedSourceType`** | **`details.logType`**  
---|---|---|---  
  
  * manage.office.com
  * manage-gcc.office.com

| Every minute | `API` | `OFFICE_365`  
**Note:** For `OFFICE_365` logs, Google SecOps maintains a lookback window of 1 hour to capture delayed records (backfillability).

#### Prerequisites

  * Get the values for all required request fields. The token endpoint for OAuth 2.0 is `https://login.microsoftonline.com/{tenantId}/oauth2/token`

  * Get the following required permissions:

    * The user whose credentials are used to authenticate against the API must have [permissions](https://docs.microsoft.com/en-us/office/office-365-management-api/get-started-with-office-365-management-apis#specify-the-permissions-your-app-requires-to-access-the-office-365-management-apis) `ActivityFeed.Read`. If ingesting DLP data then the permission `ActivityFeed.ReadDlp` must be specified.

**Note:** If you are a GCC High Microsoft 365 customer, see [Microsoft 365 US Government GCC high endpoints](https://learn.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-u-s-government-gcc-high-endpoints?view=o365-worldwide) for the GCC high-specific endpoints.

To learn more about how to configure a feed to ingest Microsoft Office 365 logs, see [Collect Microsoft 365 logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-microsoft365).

#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.office365Settings.authentication.clientId` | Yes | Application ID (a UUID)  
`details.office365Settings.authentication.clientSecret` | Yes | Client secret  
`details.office365Settings.tenantId` | Yes | Tenant ID (a UUID)  
`details.office365Settings.contentType` | Yes | The type of logs to fetch. See below to see the valid values for `contentType`.  
`details.office365Settings.hostname` | No | API Full Path, default value: `manage.office.com/api/v1.0`  
  
#### Office 365 content type

This section provides API reference details for the `OFFICE_365` log type. For details about the data source, see the [Office 365 Management Activity API reference](https://docs.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-reference) documentation.

`details.office365Settings.contentType` | Description  
---|---  
`AUDIT_AZURE_ACTIVE_DIRECTORY` | Azure active directory audit logs.  
`AUDIT_EXCHANGE` | Azure exchange audit logs.  
`AUDIT_SHARE_POINT` | Azure share point audit logs.  
`AUDIT_GENERAL` | All other workloads not included in other Audit content types.  
`DLP_ALL` | DLP events only for all workloads.  
  
#### Test the API endpoint by using curl

Before you create the feed, use `curl` to test the API endpoint.

  1. Request an OAuth token to authenticate your request to the API resource. 
         
         curl 'https://login.microsoftonline.com/TENANT_ID/oauth2/token' \
             --data-urlencode 'grant_type=client_credentials' \
             --data-urlencode 'client_id=CLIENT_ID' \
             --data-urlencode 'client_secret=CLIENT_SECRET' \
             --data-urlencode 'resource=https://manage.office.com'
         

Replace the following:

     * CLIENT_ID: Application ID
     * CLIENT_SECRET: Client secret
     * TENANT_ID: Tenant ID

The result of the curl request is a JSON response that contains the OAuth access token.

  2. Send a request to the Office 365 Management Activity API using the OAuth token. 
         
         curl 'https://manage.office.com/api/v1.0/TENANT_ID/activity/feed/subscriptions/content?contentType=Audit.AzureActiveDirectory' \
             --header 'Authorization: Bearer ACCESS_TOKEN'
         

Replace ACCESS_TOKEN with the value of the OAuth access token that you obtained from the previous step.




#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "OFFICE_365",
         "office365Settings": {
           "authentication": {
             "clientId": "0ab12c34-d5ef-678g-9012-hi34j56k78l9",
             "clientSecret", "clientSecret",
           },
           "tenantId": "0ab123c4-de56-78fg-90h1-ijk2l3456789"",
           "contentType": "AUDIT_AZURE_ACTIVE_DIRECTORY",
           "hostname": "manage.office.com/api/v1.0",
         }
       }
    }
    

### Mimecast V1

This section provides API reference details for the `MIMECAST_MAIL` log type. For details about the data source, see the [Mimecast](https://www.mimecast.com/products/email-security/secure-email-gateway/) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
The fully qualified domain name of your Mimecast API endpoint, such as `us-api.mimecast.com`.  | Every minute | `API`  
  
#### Prerequisites

  * Get the values for all authentication fields.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.mimecastMailSettings.authentication.headerKeyValues` | Yes | The configuration in the key-value format that is used to construct the authentication header.  
`details.mimecastMailSettings.hostname` | Yes | The fully qualified domain name of your Mimecast API endpoint, such as `us-api.mimecast.com`.  
  
#### Test the endpoint

The API endpoint used to download Mimecast MTA logs is `/api/audit/get-siem-logs`. To use this endpoint, send a POST request to `/api/audit/get-siem-logs`.

For details on how to use the API, see the sample code in the [Mimecast documentation](https://integrations.mimecast.com/documentation/endpoint-reference/logs-and-statistics/get-siem-logs/#sample-code).

#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "MIMECAST_MAIL",
         "mimecastMailSettings": {
           "authentication": {
             "headerKeyValues": [
               {
                 "key": "access_key",
                 "value": "ACCESS_KEY"
               },
               {
                 "key": "app_id",
                 "value": "APP_ID"
               },
               {
                 "key": "app_key",
                 "value": "APP_KEY"
               },
               {
                 "key": "secret_key",
                 "value": "SECRET_KEY"
               }
             ]
           },
           "hostname": "xx-api.mimecast.com"
         }
       }
    }
    

### Mimecast V2

This section provides API reference details for the `MIMECAST_MAIL_V2` log type. For details about the data source, see the [Mimecast](https://www.mimecast.com/products/email-security/secure-email-gateway/) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
The Mimecast API endpoint for SIEM event data is `api.services.mimecast.com/siem/v1/batch/events/cg`.  | Every minute | `API`  
  
#### Prerequisites

  * Get the values for all authentication fields.



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.mimecastMailV2Settings.authCredentials.clientId` | Yes | Authentication required to get valid access token.  
`details.mimecastMailV2Settings.authCredentials.clientSecret` | Yes | Authentication required to get valid access token.  
  
#### Test the endpoint

The API endpoint used to download Mimecast MTA logs is `/siem/v1/batch/events/cg`. To use this endpoint, send a POST request to `/siem/v1/batch/events/cg`.

For details on how to use the API, see the sample code in the [Mimecast documentation](https://developer.services.mimecast.com/docs/threatssecurityeventsanddataforcg/1/routes/siem/v1/batch/events/cg/get) and the [API Migration from V1 to V2 guide](https://developer.services.mimecast.com/api-1-0-to-2-0-migration-guide).

#### Test the API endpoint

  * Curl call to get the OAuth 2.0 token:


    
    
    curl --location 'https://api.services.mimecast.com/oauth/token'
    --header 'Content-Type: application/x-www-form-urlencoded'
    --data-urlencode 'client_id=xxx'
    --data-urlencode 'client_secret=xxxx'
    --data-urlencode 'grant_type=client_credentials'
    

  * Curl call to get the batch Mimecast endpoint:


    
    
    curl 'https://api.services.mimecast.com/siem/v1/batch/events/cg?type=av' \
      --header 'Accept: application/json' \
      --header 'Authorization: Bearer xxxx'
    

For the `type` query parameter, you can specify _only_ one of the following permissible values: `av`, `delivery`, `internal email protect`, `impersonation protect`, `journal`, `process`, `receipt`, `attachment protect`, `spam`, or `url protect`.

#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "MIMECAST_MAIL_V2",
         "mimecastMailV2Settings": {
           "authentication": {
             "client_id": "CLIENT_ID",
             "client_secret": "CLIENT_SECRET"
           }
         }
       }
    }
    

### Netskope Alerts V1

**Caution:** The Netskope v1 API feed has been deprecated by Netskope. If you are using the Netskope REST API v1 with Google SecOps, you must switch to the Netskope REST API v2.

This section provides API reference details for the `NETSKOPE_ALERT` log type. For details about the data source, see the [Netskope Alerts](https://docs.netskope.com/en/http-header-profile.html) documentation. Netskope REST API v1 data is supported.

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
`API_HOSTNAME/api/v1/alerts` Replace `API_HOSTNAME` with the fully qualified domain name of your Netskope REST API endpoint, such as `myinstance.goskope.com`. | Every 10 minutes | `API`  
  
#### Prerequisites

  * Get the values for all authentication fields. Use auth tokens for the Netskope REST API v1.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.netskopeAlertSettings.authentication.headerKeyValues` | Yes | The HTTP header used to authenticate Netskope in key-value format.  
`details.netskopeAlertSettings.hostname` | Yes | The fully qualified domain name of your Netskope REST API endpoint.  
`details.netskopeAlertSettings.feedname` | Yes | The REST endpoint to connect to. This can be `alerts` or `events`.  
`details.netskopeAlertSettings.contentType` | Yes | The value of the `type` query parameter that determines which type of event or alert is acquired.  
  
#### Optional fields

`initialStartTime`

#### Test the API endpoint

Before you create the feed, you can test the Netskope alerts API endpoint by sending a POST request to `https://TENANT_URL/api/v1/alerts`. This endpoint returns alerts generated by Netskope.

The following is an example request using curl:
    
    
    curl -X POST 'https://TENANT_URL/api/v1/alerts?' \
        -H 'Content-Type: application/json' \
        -d 'timeperiod=86400' \
        -d 'type=Security%20Assessment' \
        -d 'limit=1' \
        -d 'stimeperiod=2592000' \
        -d 'query=%28compliance_standards.standard%20eq%20%27CSA-CCM-3.0.1%27%29' \
        -d 'token=ACCESS_TOKEN'
    

Replace the following:

  * TENANT_URL: URL of your tenant
  * ACCESS_TOKEN: OAuth access token



To learn more about the different query parameters that can be used as a part of the request, see the [Get Alerts Data](https://docs.netskope.com/en/netskope-help/admin-console/rest-api/netskope-platform-rest-apis/get-alerts-data/) page in the Netskope documentation.

#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "NETSKOPE_ALERT",
         "netskopeAlertSettings": {
           "authentication": {
             "headerKeyValues": [{
              "key": "token",
              "value": secret
             }]
           },
           "hostname": hostname,
           "feedname": feedname,
           "contentType": contenttype
         }
       },
       "display_name": displayname
    }
    

### Netskope Alerts V2

This section provides API reference details for the `NETSKOPE_ALERT_V2` log type. For details about the data source, see the [Netskope Alerts V2](https://docs.netskope.com/en/rest-api-v2-overview-312207/) documentation. Netskope REST API v2 data is supported.

**Data source** |  **Content Type** |  **Content Category**  
---|---|---  
`API_HOSTNAME`/api/v2/events/dataexport/alerts/uba |  uba |  alerts  
`API_HOSTNAME`/api/v2/events/dataexport/alerts/securityassessment |  securityassessment |  alerts  
`API_HOSTNAME`/api/v2/events/dataexport/alerts/quarantine |  quarantine |  alerts  
`API_HOSTNAME`/api/v2/events/dataexport/alerts/remediation |  remediation |  alerts  
`API_HOSTNAME`/api/v2/events/dataexport/alerts/policy |  policy |  alerts  
`API_HOSTNAME`/api/v2/events/dataexport/alerts/malware |  malware |  alerts  
`API_HOSTNAME`/api/v2/events/dataexport/alerts/malsite |  malsite |  alerts  
`API_HOSTNAME`/api/v2/events/dataexport/alerts/compromisedcredential |  compromisedcredential |  alerts  
`API_HOSTNAME`/api/v2/events/dataexport/alerts/ctep |  ctep |  alerts  
`API_HOSTNAME`/api/v2/events/dataexport/alerts/dlp |  dlp |  alerts  
`API_HOSTNAME`/api/v2/events/dataexport/alerts/watchlist |  watchlist |  alerts  
`API_HOSTNAME`/api/v2/events/dataexport/events/application |  application |  events  
`API_HOSTNAME`/api/v2/events/dataexport/events/audit |  audit |  events  
`API_HOSTNAME`/api/v2/events/dataexport/events/connection |  connection |  events  
`API_HOSTNAME`/api/v2/events/dataexport/events/incident |  incident |  events  
`API_HOSTNAME`/api/v2/events/dataexport/events/infrastructure |  infrastructure |  events  
`API_HOSTNAME`/api/v2/events/dataexport/events/network |  network |  events  
`API_HOSTNAME`/api/v2/events/dataexport/events/page |  page |  events  
  
  * **Ingest schedule** = Every 10 mins
  * **`details.feedSourceType`** = API



Replace `API_HOSTNAME` with the fully qualified domain name of your Netskope REST API v2 endpoint, such as `myinstance.goskope.com`.

#### Prerequisites

  * Get the values for all authentication fields. Use auth tokens for the Netskope REST API v2.
  * Create a Netskope access token following the steps on the [REST API v2 Overview](https://docs.netskope.com/en/rest-api-v2-overview/#rest-api-v2-overview-1) page. **Note** , when creating the Netskope token make sure to select all the relevant **endpoint privileges**.



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.netskopeAlertV2Settings.authentication.headerKeyValues` | Yes | The HTTP header used to authenticate Netskope in key-value format.  
`details.netskopeAlertV2Settings.hostname` | Yes | The fully qualified domain name of your Netskope REST API endpoint.  
`details.netskopeAlertV2Settings.contentCategory` | Yes | The REST endpoint to connect to. This can be `alerts` or `events`.  
`details.netskopeAlertV2Settings.contentTypes` | Yes | The type of event or alert. Allowed values for alerts are uba, securityassessment, quarantine, remediation, policy, malware, malsite, compromisedcredential, ctep, dlp and watchlist. Allowed values for events are application, audit, connection, incident, infrastructure, network and page.  
  
#### Test the API endpoint

Before you create the feed, you can test the Netskope alerts V2 API endpoint by sending a GET request to `https://TENANT_URL`. This endpoint returns alerts generated by Netskope.

The following is an example request using curl:
    
    
    curl -X 'GET' \
        'https://TENANT_URL' \
        -H 'accept: application/json' \
        -H 'Netskope-Api-Token: ACCESS_TOKEN'
    

Replace the following:

  * TENANT_URL: URL of one of the Data sources listed in the Data source table.
  * ACCESS_TOKEN: OAuth access token (See Prerequisites for details of creating the token.)



To learn more about the different query parameters that can be used as a part of the request, see the [Get Alerts Data](https://docs.netskope.com/en/rest-api-v2-overview-312207/#swagger-api-documentation) page in the Netskope documentation.

#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "NETSKOPE_ALERT_V2",
         "netskopeAlertV2Settings": {
           "authentication": {
             "headerKeyValues": [{
              "key": "Netskope-Api-Token",
              "value": "token_value"
             }]
           },
           "contentTypes": [
              "uba",
              "securityassessment"
           ],
           "hostname": "myinstance.goskope.com",
           "contentCategory": "alerts"
         }
       }
    }
    

### Okta System Log

This section provides API reference details for the `OKTA` log type. For details about the data source, see the [Okta System Log](https://developer.okta.com/docs/reference/api/system-log/) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
`API_HOSTNAME/api/v1/logs` Replace `API_HOSTNAME` with the fully qualified domain name of your Okta instance, such as `example.okta.com`. | Every minute | `API`  
**Note:** Potential ingestion delays can occur with Okta logs. These delays can stem from processing times or API availability issues within the Okta service itself, affecting when the logs are available for Google SecOps to collect.**Note:** To maintain stable ingestion and remain within Okta's rate limits, Google SecOps limits batch requests to a maximum of 30 consecutive requests per cycle.

#### Prerequisites

  * Get the values for all authentication fields.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.oktaUserContextSettings.authentication.headerKeyValues` | Yes | The HTTP header used to authenticate Okta in key-value format.  
`details.oktaUserContextSettings.hostname` | Yes | The fully qualified domain name of your Okta instance.  
  
#### Test the API endpoint

Before you create the feed, you can test the Okta System Log API endpoint by sending a GET request to `OKTA_URL/api/v1/logs`. This endpoint returns system log events that can be ingested into a SIEM platform.

The following is an example request to obtain system log events from a particular point of time in the past:
    
    
    curl -v -X GET \
        -H "Accept: application/json" \
        -H "Content-Type: application/json" \
        -H "Authorization: SSWS API_TOKEN" \
        "https://OKTA_URL/api/v1/logs?since=DATETIME"
    

Replace the following:

  * API_TOKEN: OAuth access token
  * OKTA_URL: fully qualified domain name of your Okta instance, such as `example.okta.com`
  * DATETIME: timestamp in UTC format according to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601), separating date and time with a `T`. For example: `2024-01-31T00:00:00Z`. The API will fetch the logs recorded after the specified timestamp.



#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "OKTA",
         "oktaSettings": {
           "authentication": {
             "headerKeyValues": [{
                "key": "Authorization",
                "value": "APITOKEN"
              }]
           },
           "hostname": "hostname"
         }
       }
    }
    

### Okta Users

This section provides API reference details for the `OKTA_USER_CONTEXT` log type. For details about the data source, see the [Okta Users](https://developer.okta.com/docs/reference/api/users/) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
`API_HOSTNAME/api/v1/users` Replace `API_HOSTNAME` with the fully qualified domain name of your Okta instance, such as `example.okta.com`. | Every 24 hours | `API`  
**Note:** To comply with Okta's rate limits, Google SecOps applies the following limits. Google SecOps applies a maximum of 10 consecutive requests in a single batch for initial requests to list users. Google SecOps applies a maximum of 420 requests per minute for follow-up fetches to obtain manager details (which keeps it at 70% of Okta's limit of 600 requests per minute).

#### Prerequisites

  * Get the values for `hostname` and all authentication fields.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.oktaUserContextSettings.authentication.headerKeyValues` | Yes | The HTTP header used to authenticate Okta in key-value format.  
`details.oktaUserContextSettings.hostname` | Yes | The fully qualified domain name of your Okta instance.  
`details.oktaUserContextSettings.managerIdReferenceField` | No | This ID is required when you use a non Okta ID to reference managers.  
  
#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example shows a `curl` request to retrieve system log events:
    
    
    "curl --location 'https://xyz.okta.com/api/v1/users?limit=200' \
    --header 'Accept: application/json' \
    --header 'Authorization: SSWS TOKEN' \
    --header 'Cookie: JSESSIONID=XXXX'"
    

Replace the following placeholder:

  * TOKEN: OAuth access token



#### Sample create feed request

`managerIdReferenceField` is required when you use a non-Okta ID to reference managers. It should be a JSON field path pointing to the field that contains the manager ID in the result of a call to the "users" Okta API.
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "OKTA_USER_CONTEXT",
         "oktaSettings": {
           "authentication": {
             "headerKeyValues": [{
                "key": "Authorization",
                "value": "APITOKEN"
              }]
           },
           "hostname": "hostname",
           "managerIdReferenceField": "fooId"
         }
       }
    }
    

### Palo Alto Networks AutoFocus

This section provides API reference details for the `PAN_IOC` log type. For details about the data source, see the [Palo Alto Networks AutoFocus](https://docs.paloaltonetworks.com/content/dam/techdocs/en_US/pdf/autofocus/autofocus-api/autofocus-api.pdf) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
`autofocus.paloaltonetworks.com/api/v1.0/IOCFeed/FEED_ID/FEED_NAME` Replace `FEED_ID` and `FEED_NAME` with the Google Security Operations feed ID and feed name respectively. | Every five minutes | `API`  
  
#### Prerequisites

  * Get the values for `feedId`, `feed`, and all authentication fields.
  * Get the following required permissions: 
    * None



#### Test the endpoint

To get the results for a custom threat indicator feed, you need to send a request to the custom feed resource of the AutoFocus API. The custom feed endpoint is as follows: `/IOCFeed/OUTPUT_FEED_ID/OUTPUT_FEED_NAME`.

The following is an example request to retrieve threat intelligence:
    
    
    curl -X GET \
    -H "apiKey:API_KEY" \
    https://autofocus.paloaltonetworks.com/api/v1.0/IOCFeed/OUTPUT_FEED_ID/OUTPUT_FEED_NAME?limit=MAX_ENTRIES
    

Replace the following:

  * API_KEY: API key tied to your license

  * OUTPUT_FEED_ID: custom threat feed ID number

  * OUTPUT_FEED_NAME: name of the custom feed

  * MAX_ENTRIES: maximum number of indicator entries displayed in the output




For details on how to use the Palo Alto AutoFoucs API, see the [Get Custom Threat Indicator Feed](https://docs.paloaltonetworks.com/autofocus/autofocus-api/perform-direct-searches/get-custom-threat-indicator-feed) documentation.

#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "PAN_IOC",
         "panIocSettings": {
           "authentication": {
             "headerKeyValues": [{
                "key": "key"
                "value": "value"
             }],
           }
           "feedId": "ID",
           "feed": "feed"
         }
       }
    }
    

### Palo Alto Networks Cortex XDR

This section provides API reference details for the `CORTEX_XDR` log type. For details about the data source, see the [Palo Alto Networks Cortex XDR](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR/Cortex-XDR-API-Reference/APIs-Overview) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
`API_HOSTNAME/0ab123c4incidents/get_incidents` Replace `API_HOSTNAME` with the fully qualified domain name of your instance, such as `api-abcd.xdr.ab.paloaltonetworks.com`. | Every five minutes | `API`  
  
#### Prerequisites

  * Get the values for all authentication fields.
  * Make sure the API key is an advanced key, not a standard key.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.cortexXdrSettings.authentication.headerKeyValues` | Yes | The HTTP header used to authenticate Cortex XDR API in key-value format.  
`details.cortexXdrSettings.hostname` | Yes | The fully qualified domain name of your Cortex XDR instance.  
`details.cortexXdrSettings.endpoint` | No | The API endpoint to connect to retrieve logs, which include `incidents` or `alerts`.  
  
#### Optional fields

`initialStartTime`

#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example shows a `curl` request to retrieve a list of incidents:
    
    
    curl --location 'https://api-abcd.xdr.us.paloaltonetworks.com/public_api/v1/incidents/get_incidents' \
    --header 'x-xdr-auth-id: 308' \
    --header 'Authorization: TOKEN'' \
    --header 'x-xdr-timestamp: 1748436026000' \
    --header 'x-xdr-nonce: NONCE' \
    --header 'Content-Type: application/json' \
    --header 'Cookie: XSRF-TOKEN=COOKIE' \
    --data '{"request_data":{
        "filters":[{"field":"creation_time","operator":"gte","value":1716246103951},{"field":"creation_time","operator":"lte","value":1717378040247}],
        "sort":{"field":"creation_time","keyword":"asc"},"search_from":0,"search_to":100}}'
    

The following example shows a `curl` request to retrieve a list of alerts:
    
    
    curl --location 'https://api-abcd.xdr.us.paloaltonetworks.com/public_api/v1/alerts/get_alerts' \
    --header 'x-xdr-auth-id: 308' \
    --header 'Authorization: TOKEN'' \
    --header 'x-xdr-timestamp: 1748607162000' \
    --header 'x-xdr-nonce: NONCE' \
    --header 'Content-Type: application/json' \
    --header 'Cookie: XSRF-TOKEN=COOKIE' \
    --data '{"request_data":{
        "filters":[{"field":"server_creation_time","operator":"gte","value":1729937259000},{"field":"server_creation_time","operator":"lte","value":1739937259000}],
        "sort":{"field":"creation_time","keyword":"asc"},"search_from":100,"search_to":200}}'
    

#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "CORTEX_XDR",
         "cortexXdrSettings": {
           "authentication": {
             "headerKeyValues": [{
                "key": "Authorization"
                "value": "api_key"
             },
             {
                "key": "x-xdr-auth-id"
                "value": "api_key_id"
             }
             ],
           },
           "hostname": "api-abcd.xdr.ab.paloaltonetworks.com",
           "endpoint": "incidents"
         }
       }
    }
    

### Palo Alto Networks Prisma Cloud Audit Logs

This section provides API reference details for the `PAN_PRISMA_CLOUD` log type. For details about the data source, see the [Palo Alto Networks Prisma Cloud Audit Logs](https://prisma.pan.dev/api/cloud/cspm/audit-logs/) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
`api.prismacloud.io/audit/redlock` | Every five minutes | `API`  
  
#### Prerequisites

  * Get the values for all authentication fields.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.panPrismaCloudSettings.authentication.user` | Yes | The Prisma Cloud username.  
`details.panPrismaCloudSettings.authentication.password` | Yes | The Prisma Cloud password.  
`details.panPrismaCloudSettings.hostname` | Yes | The Palo Alto Prisma Cloud API hostname.  
  
#### Test the endpoints by using curl

Before you create the feed, you can test the API endpoints by using curl. Send a GET request to `https://api.prismacloud.io/audit/redlock`

The following example returns audit logs for events that took place on the Prisma Cloud platform:
    
    
    curl -L 'https://api.prismacloud.io/audit/redlock' \
    -H 'Accept: application/json; charset=UTF-8' \
    -H 'x-redlock-auth: API_KEY_VALUE'
    

Replace the following:

  * API_KEY_VALUE: The Prisma Cloud authentication value is a JSON Web Token (JWT).



#### Optional fields

`timeType`, `timeAmount`, `timeUnit`

For details about the data source, see the [Palo Alto Networks Prisma Cloud Audit Logs](https://prisma.pan.dev/api/cloud/cspm/audit-logs/) documentation.

#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "PAN_PRISMA_CLOUD",
         "panPrismaCloudSettings": {
           "authentication": {
             "user": "user",
             "password": "password"
           },
           "hostname": "api2.prismacloud.io"
         }
       }
    }
    

### Proofpoint on Demand

This section provides API reference details for the `PROOFPOINT_ON_DEMAND` log type. For details about the data source, see the [Proofpoint on Demand](https://www.proofpoint.com/us) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
The default data endpoint is used.  | Every hour | `API`  
  
#### Prerequisites

  * Get the values for all authentication fields. 
    * Make sure that the token is not used in any other instance or connection, whether inside or outside Google SecOps, as Proofpoint limits tokens to one active session.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.proofpointOnDemandSettings.authentication.headerKeyValues` | Yes | The HTTP header used to authenticate `logstream.proofpoint.com` in the key-value format.  
`details.proofpointOnDemandSettings.clusterId` | Yes | The cluster ID, which is a user group string.  
  
#### Other fields

`proofpointOnDemandSourceDetails`

#### Optional fields

`initialStartTime`

#### Test the endpoint

Before you create a real-time email processing log feed, you can test connectivity between your system and the Proofpoint on Demand (PoD) Log API.

The following is an example request to receive uncompressed data:
    
    
    curl -i --no-buffer \
    -H "Connection: Upgrade" \
    -H "Upgrade: websocket" \
    -H "Host: logstream.proofpoint.com:443" \
    -H "Authorization: Bearer ACCESS_TOKEN " \
    -H "Sec-WebSocket-Key: KEY" \
    -H "Sec-WebSocket-Version: 13" \
    "https://logstream.proofpoint.com:443/v1/stream?cid=CLUSTER_ID&type=message&sinceTime=DATE_TIME"
    

Replace the following:

  * ACCESS_TOKEN: a token provided by Proofpoint for a customer cluster to authenticate with the service.

  * KEY: a base64-encoded key used in the WebSocket opening handshake.

  * CLUSTER_ID: the cluster ID assigned by Proofpoint.

  * DATE_TIME: start time to begin streaming log data, in ISO 8601 format, which includes timezone information. For example: `2018-08-31T00:00:00-0800`. The API fetches the logs recorded after the specified timestamp.




#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "PROOFPOINT_ON_DEMAND",
         "proofpointOnDemandSettings": {
           "authentication": {
             "user": "user",
             "secret": "secret"
           },
           "clusterId": "ID"
         }
       }
    }
    

### Proofpoint TAP

This section provides API reference details for the `PROOFPOINT_MAIL` log type. For details about the data source, see the [Proofpoint SIEM API](https://help.proofpoint.com/Threat_Insight_Dashboard/API_Documentation/SIEM_API#.2Fv2.2Fsiem.2Fall) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
The default data endpoint is used.  | Every 10 minutes | `API`  
  
#### Limitations

When analyzing `PROOFPOINT_MAIL` logs, you might observe events with historical timestamps despite real-time ingestion. This behavior is inherent to the Proofpoint API, not the Google SecOps ingestion pipeline. Even when Google SecOps queries for the most recent activity, the Proofpoint API can return events that occurred several days prior. Discrepancies between the `event_timestamp` and the `ingestion_time` are expected for the `PROOFPOINT_MAIL` log type due to how Proofpoint buffers and releases event data. For further details, see the [Proofpoint event timestamp documentation](https://help.proofpoint.com/Threat_Insight_Dashboard/API_Documentation/SIEM_API#.2Fv2.2Fsiem.2Fall:%7E:text=In%20other%20words,%20a%20request%20using%20the%20sinceSeconds=3600%C2%A0parameter%20will%20retrieve%20all%20events%20which%20have%20been%20created%20in%20the%20last%20hour.%20It%20is%20possible%20that%20the%20events%20returned%20from%20that%20interval%20reference%20messages%20or%20clicks%20which%20were%20first%20observed%20more%20than%20one%20hour%20ago%E2%80%94perhaps%20even%20several%20days%20ago).

#### Prerequisites

  * Get the values for all authentication fields.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.proofpointMailSettings.authentication.user` | Yes | The user account required for authentication.  
`details.proofpointMailSettings.authentication.secret` | Yes | The secret required for authentication.  
  
#### Test the endpoint

Before you create the feed, you can test the Proofpoint TAP SIEM API endpoint by sending a GET request to `/v2/siem/all`.

To fetch events for all clicks and messages relating to known threats within the specified time period, use a GET request as follows:
    
    
    curl \
    "https://tap-api-v2.proofpoint.com/v2/siem/all?format=syslog&sinceSeconds=SECONDS" \
    --user "PRINCIPAL:SECRET" \
    -s
    

Replace the following:

  * SECONDS: an integer representing a time window in seconds from the current API server time. For example, `3600`.

  * PRINCIPAL: Proofpoint service principal to authenticate to the SIEM API.

  * SECRET: Proofpoint API secret to authenticate to the SIEM API.




To learn more about the different query parameters that can be used as a part of the request, see the [Proopoint TAP SIEM API documentation](https://help.proofpoint.com/Threat_Insight_Dashboard/API_Documentation/SIEM_API).

#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "PROOFPOINT_MAIL",
         "proofpointMailSettings": {
           "authentication": {
             "user": "user",
             "secret": "secret"
           }
         }
       }
    }
    

### Qualys VM

This section provides API reference details for the `QUALYS_VM` log type. For details about the data source, see the [Qualys VM documentation (PDF)](https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf).

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
The domain and full path of the resource, such as `qualysapi.qualys.com/api/2.0/fo/asset/host/?action=list`.  | Every minute | `API`  
**Note:** The Qualys VM feed fetches new data every minute. If there is no new data available, the feed will pause for approximately 4 hours before it attempts to fetch new data again.

#### Prerequisites

  * Get the values for all authentication fields.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.qualysVmSettings.authentication.user` | Yes | The user account required for authentication.  
`details.qualysVmSettings.authentication.secret` | Yes | The secret required for authentication.  
`details.qualysVmSettings.hostname` | Yes | The domain and full path of the resource, such as `qualysapi.qualys.com/api/2.0/fo/asset/host/?action=list`.  
  
#### Test the endpoints by using curl

Before you create the feed, use `curl` to test the API endpoint.

  * To test the endpoint for the Qualys VM Host List API, use the following `curl` command: 
        
        curl -H "X-Requested-With: Curl Sample" -u "USERNAME:PASSWORD" \
        "https://qualysapi.qg3.apps.qualys.com/api/2.0/fo/asset/host/?action=list"
        

  * To test the endpoint for the Qualys VM Host List Detection API, use the following `curl` command: 
        
        curl -H "X-Requested-With: Curl Sample" -u "USERNAME:PASSWORD" \
        "https://qualysapi.qg3.apps.qualys.com/api/2.0/fo/asset/host/vm/detection/?action=list"
        




Replace the following:

  * USERNAME: username of your Qualys account
  * PASSWORD: password of your Qualys account



#### Sample create feed request for Qualys VM Host List API
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "QUALYS_VM",
         "qualysVmSettings": {
           "authentication": {c
             "user": "USERNAME",
             "secret": "PASSWORD"
           },
           "hostname": "qualysapi.qualys.com/api/2.0/fo/asset/host/?action=list"
         }
       }
    }
    

#### Sample create feed request for Qualys VM Host List Detection API
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "QUALYS_VM",
         "qualysVmSettings": {
           "authentication": {
             "user": "USERNAME",
             "secret": "PASSWORD"
           },
           "hostname": "qualysapi.qualys.com/api/2.0/fo/asset/host/vm/detection/?action=list"
         }
       }
    }
    

### Qualys Scan

This section provides API reference details for the `QUALYS_SCAN` log type. For details about the data source, see the [Qualys VM documentation (PDF)](https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf).

Data source  | Ingest schedule | `details.feedSourceType` | `details.logType`  
---|---|---|---  
qualysapi.qualys.com  | Every Day | `API` | `QUALYS_SCAN`  
  
#### Prerequisites

  * Get the values for all authentication fields.
  * Get the following required permissions: 
    * Ensure API access is enabled for the user.



#### Scan APIs

The Qualys Scan APIs that Google Security Operations supports include the following.

`details.qualysScanSettings.api_type` | Description  
---|---  
`SCAN_SUMMARY_OUTPUT` | Scan Summaries API to identify which hosts were scanned or not scanned and why.  
`SCAN_COMPLIANCE_OUTPUT` | Scan Compliance API to list out the compliance scans in your Qualys account.  
`SCAN_COMPLIANCE_CONTROL_OUTPUT` | Compliance Control API to view a list of compliance controls which are visible to the user.  
  
#### Test the endpoints by using curl

Before you create the feed, you can test the API endpoints by using curl.

  * To test the endpoint for the API type `SCAN_SUMMARY_OUTPUT`, use the following `curl` command: 
        
        curl -H "X-Requested-With: Curl Sample" -u "USERNAME:PASSWORD" \
        "https://qualysapi.qg3.apps.qualys.com/api/2.0/fo/scan/vm/summary/?action=list&scan_datetime_since=DATETIME"
        

  * To test the endpoint for the API type `SCAN_COMPLIANCE_OUTPUT`, use the following `curl` command: 
        
        curl -H "X-Requested-With: Curl Sample" -u "USERNAME:PASSWORD" \
        "https://qualysapi.qg3.apps.qualys.com/api/2.0/fo/scan/compliance/?action=list&launched_after_datetime=DATETIME"
        

  * To test the endpoint for the API type `SCAN_COMPLIANCE_CONTROL_OUTPUT`, use the following `curl` command: 
        
        curl -H "X-Requested-With: Curl Sample" -u "USERNAME:PASSWORD" \
        "https://qualysapi.qg3.apps.qualys.com/api/2.0/fo/compliance/control/?action=list&updated_after_datetime=DATETIME"
        




Replace the following:

  * USERNAME: username of your Qualys account
  * PASSWORD: password of your Qualys account
  * DATETIME: timestamp in UTC format according to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601), separating date and time with a `T`. For example: `2024-01-31T18:00:42Z`. The API will fetch the logs recorded after the specified timestamp.



#### Sample create feed request for Qualys Scan API
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "QUALYS_SCAN",
         "qualysScanSettings": {
           "authentication": {
             "user": "USERNAME",
             "secret": "PASSWORD"
           },
           "hostname": "qualysapi.qualys.com",
           "api_type": "SCAN_SUMMARY_OUTPUT"
         }
       }
    }
    

### Rapid7 InsightVM

This section provides API reference details for the `RAPID7_INSIGHT` log type. For details about the data source, see the [Rapid7 InsightVM](https://help.rapid7.com/insightvm/en-us/api/integrations.html#tag/Vulnerability) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
The REST endpoint, which must be either `vulnerabilities` or `assets` on your Rapid7 InsightVM instance (for example: `us.api.insight.rapid7.com`).  | Every 24 hours | `API`  
  
#### Prerequisites

  * Get the values for all authentication fields.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.rapid7InsightSettings.authentication.headerKeyValues` | Yes | The HTTP header used to authenticate `us.api.insight.rapid7.com` in key-value format.  
`details.rapid7InsightSettings.endpoint` | Yes | The REST endpoint to connect to. The `endpoint` value must be either `vulnerabilities` or `assets`.  
`details.rapid7InsightSettings.hostname` | No | The fully qualified domain name of the Rapid7 endpoint, such as `us.api.insight.rapid7.com`.  
  
#### Optional fields

`initialStartTime`

#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example shows a `curl` request to retrieve a list of vulnerabilities:
    
    
    "curl --location 'https://us.api.insight.rapid7.com/vm/v4/integration/vulnerabilities?page=3&size=10&sort=modified&cursor=-2034101655%3A%3A%3A_L%3A%3A%3A1746144000000%3A%3A%3A_S%3A%3A%3Azimbra-collaboration-cve-2024-45519' \
    --header 'X-Api-Key: XXXX' \
    --header 'Content-Type: application/json' \
    --header 'Cookie: JSESSIONID=XXX' \
    --data '{""vulnerability"":""modified >= 2025-05-02T00:00:00Z""}'"
    

The following example shows a `curl` request to retrieve a list of assets:
    
    
    "curl --location 'https://us.api.insight.rapid7.com/vm/v4/integration/assets?size=10&page=3&cursor=-221057366%3A%3A%3A_L%3A%3A%3A1745933722742%3A%3A%3A_S%3A%3A%3Aec99b8c2-6ceb-4398-a0d6-ae4b242a4a05-default-asset-21432&sort=last_assessed_for_vulnerabilities' \
    --header 'X-Api-Key: XXXX' \
    --header 'Content-Type: application/json' \
    --header 'Cookie: JSESSIONID=XXXX; JSESSIONID=XXXX' \
    --data '{""assets"":""last_assessed_for_vulnerabilities > 2021-01-01T00:00:00Z""}'"
    

#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "RAPID7_INSIGHT",
         "rapid7InsightSettings": {
           "authentication": {
             "headerKeyValues": [{
                "key": "X-Api-Key",
                "value": ApiToken "API_TOKEN"
             }],
           },
           "endpoint": "assets"
           "hostname": "us.api.insight.rapid7.com"
         }
       }
    }
    

Replace API_TOKEN with your API token.

### Recorded Future

This section provides API reference details for the `RECORDED_FUTURE_IOC` log type. For details about the data source, see the [Recorded Future](https://www.recordedfuture.com/threat-intelligence/) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
`api.recordedfuture.com/v2/fusion/files`.  | Every two hours | `API`  
  
#### Prerequisites

  * Get the values for all authentication fields.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.recordedFutureIocSettings.authentication.headerKeyValues` | Yes | The HTTP header used to authenticate to `api.recordedfuture.com` in key-value format.  
  
#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example shows a `curl` request to download files for domain risk:
    
    
    curl --location 'api.recordedfuture.com/v2/fusion/files?path=%2Fpublic%2Frisklists%2Fdefault_domain_risklist.csv' \ --header 'X-RFToken: token' \ --header 'X-RF-User-Agent: RF-Backstory+v1.0'
    

The following is an example request to download files for IP risk using curl:
    
    
    curl --location 'api.recordedfuture.com/v2/fusion/files?path=%2Fpublic%2Frisklists%2Fdefault_ip_risklist.csv' \ --header 'X-RFToken: token' \ --header 'X-RF-User-Agent: RF-Backstory+v1.0'
    

#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "RECORDED_FUTURE_IOC",
         "recordedFutureIocSettings": {
           "authentication": {
             "user": "user",
             "secret": "secret"
           },
         }
       }
    }
    

### RH-ISAC

This section provides API reference details for the `RH_ISAC_IOC` log type. For details about the data source, see the [RH-ISAC](https://docs.trustar.co/api/v13/indicators/search_indicators.html) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
`api.trustar.co/api/1.3/indicators/search`. | Every 24 hours | `API`  
  
#### Prerequisites

  * Get the values for all authentication fields.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.rhIsacIocSettings.authentication.tokenEndpoint` | Yes | The endpoint to retrieve the OAuth token.  
`details.rhIsacIocSettings.authentication.clientId` | Yes | The application ID.  
`details.rhIsacIocSettings.authentication.clientSecret` | Yes | The client secret.  
  
#### Other fields

`tags`, `queueDelay`

#### Optional fields

`initialStartTime`

#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example shows a `curl` request to retrieve indicators:
    
    
    curl --location --request POST 'https://api.trustar.co/api/1.3/indicators/search?pageSize=2&from=1719810991000&pageNumber=2' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer XXXXXX' \
    --header 'Cookie: JSESSIONID=XXXXX' \
    --data ''
    

#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "RH_ISAC_IOC",
         "rhIsacIocSettings": {
           "authentication": {
             "tokenEndPoint": "endpoint",
             "clientId": "clientId",
             "clientSecret": "clientSecret"
           }
         }
       }
    }
    

### Salesforce

This section provides API reference details for the `SALESFORCE` log type. For details about the data source, see the [Salesforce](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/dome_event_log_file_query.htm) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
`API_HOSTNAME/services/data/v50.0/query` Replace `API_HOSTNAME` with the fully qualified domain name of your Salesforce REST API endpoint, such as `myinstance.salesforce.com`. | Every minute | `API`  
  
#### Prerequisites

  * Salesforce Shield is required.
  * Get the values for all authentication fields as described in [OAuth 2.0 Username-Password Flow for Special Scenarios](https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_username_password_flow.htm&type=5).
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.salesforceSettings.hostname` | Yes | The fully qualified domain name of your Salesforce REST API endpoint, such as `myinstance.salesforce.com`.  
`details.salesforceSettings.oauthPasswordGrantAuth.tokenEndpoint` | No | The endpoint to retrieve the OAuth token. This field must be specified in the following format: `https://SF_INSTANCE.my.salesforce.com/services/oauth2/token?grant_type=password`. Replace `SF_INSTANCE` with your Salesforce instance name. This field is required only for OAuth password grant.  
`details.salesforceSettings.oauthPasswordGrantAuth.clientId` | No | The application ID. This field is required only for OAuth password grant.  
`details.salesforceSettings.oauthPasswordGrantAuth.clientSecret` | No | The client secret. This field is required only for OAuth password grant.  
`details.salesforceSettings.oauthPasswordGrantAuth.user` | No | The username used for authentication. This field is required only for OAuth password grant.  
`details.salesforceSettings.oauthPasswordGrantAuth.password` | No | The password used for authentication. This field is required only for OAuth password grant.  
`details.salesforceSettings.oauthJwtCredentials.tokenEndpoint` | No | The endpoint to retrieve the OAuth JSON web token. This field is required only for OAuth JWT grant. This field must be specified in the following format:  
  
`https://SF_INSTANCE.my.salesforce.com/services/oauth2/token?grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer`.   
  
Replace `SF_INSTANCE` with your Salesforce instance name.  
`details.salesforceSettings.oauthJwtCredentials.claims.issuer` | No | The JWT claims issuer, which is usually a client ID. This field is required only for OAuth JWT grant.  
`details.salesforceSettings.oauthJwtCredentials.claims.subject` | No | The JWT claims subject, which is usually an email ID. This field is required only for OAuth JWT grant.  
`details.salesforceSettings.oauthJwtCredentials.claims.audience` | No | The JWT claims audience. This field is required only for OAuth JWT grant. Set as `https://login.salesforce.com` or `https://test.salesforce.com`. Reference the following commnity topic: [JWT bearer Flow: audience is invalid](https://trailhead.salesforce.com/trailblazer-community/feed/0D54V00007T42ehSAB).  
`details.salesforceSettings.oauthJwtCredentials.rsCredentials.privateKey` | No | An RSA private key in PEM format. This field is required only for OAuth JWT grant.  
  
#### Optional fields

`initialStartTime`

#### Test the endpoint

Before you create the feed, you can test the REST API endpoint by sending a GET request to `/services/data/vAPI_VERSION/query`. The [`Query`](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_query.htm#topic-title) resource is used to retrieve field values from a record.

To query event monitoring records based on fields, such as `LogDate` and `EventType`, use a GET request as follows:
    
    
    curl https://SUBDOMAIN.my.salesforce.com/services/data/vAPI_VERSION/query \
        -X GET \
        -H "Authorization: Bearer AUTH_TOKEN" \
        -G \
        --data-urlencode "q=SELECT Id, EventType, LogFile, LogDate, LogFileLength FROM EventLogFile WHERE LogDate > Yesterday AND EventType = 'API'"
    

Replace the following:

  * SUBDOMAIN: the subdomain name relevant to the Salesforce instance being accessed.
  * API_VERSION: version number of the API endpoint. For example, `60.0`.
  * AUTH_TOKEN: OAuth access token.



#### Sample create feed request using OAuth password grant
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "SALESFORCE",
         "salesforceSettings": {
           "authentication": {
             "tokenEndpoint": "endpoint",
             "clientId": "clientId",
             "clientSecret": "clientSecret",
             "user": "user",
             "password": "password"
           },
           "hostname": "hostname"
         }
       }
    }
    

#### Sample create feed request using OAuth JWT grant
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "SALESFORCE",
         "salesforceSettings": {
           "authentication": {
             "tokenEndpoint": "endpoint",
             "issuer": "clientId",
             "subject": "emailID",
             "audience": "audience",
             "privateKey": "RSAKey"
           },
           "hostname": "hostname"
         }
       }
    }
    

### SentinelOne Alert

This section provides API reference details for the `SENTINELONE_ALERT` log type. For details about the data source, see the [SentinelOne Alert](https://usea1-dfir.sentinelone.net/api-doc/api-details?category=threats&api=get-threats) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
`API_HOSTNAME/web/api/v2.1/cloud-detection/alerts` Replace `API_HOSTNAME` with the fully qualified domain name of SentinelOne API. | Every five minutes | `API`  
**Note:** Ingestion delays for `SENTINELONE_ALERT` can occur due to the timing of event availability in the SentinelOne API. Events might be detected by SentinelOne earlier than they are published to the API endpoint. Since Google SecOps fetches based on the API's `createdAtTime`, any latency between the actual event time and the API publication time will result in a delay. This delay originates from the source system, not the Google SecOps ingestion pipeline.

#### Prerequisites

  * Get the values for all authentication fields.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.sentineloneAlertSettings.authentication.headerKeyValues` | Yes | The HTTP headers to authenticate the SentinelOne alerts, threats, and static-indicator API in key-value format.  
`details.sentineloneAlertSettings.hostname` | Yes | The fully qualified domain name of the SentinelOne API.  
`details.sentineloneAlertSettings.initialStartTime` | No | The time when the alerts must be fetched.  
`details.sentineloneAlertSettings.isAlertApiSubscribed` | No | Indicates whether the alerts API is subscribed.  
  
#### Test the API endpoint

Before you create the feed, use curl to test the API endpoint.

The following example uses `curl` to retrieve a host description:
    
    
    curl --location 'https://usea1-altostrat.sentinelone.net/web/api/v2.1/cloud-detection/alerts?limit=100&sortOrder=asc&sortBy=alertInfoCreatedAt' \
    --header 'Authorization: ApiToken eyJraWQiOiJ1cy1lYXN0LTEtcHJvZC0wIiwiYWxnIjoiRVMyNTYifQ.eyJzdWIiOiJzZXJ2aWNldXNlci0yNDRlMDg4Ny03ZWViLTQ3NGQtYjlmYy1jNWE3MmJiMWIyZjRAbWdtdC01OTAyNC5zZW50aW5lbG9uZS5uZXQiLCJpc3MiOiJhdXRobi11cy1lYXN0LTEtcHJvZCIsImRlcGxveW1lbnRfaWQiOiI1OTAyNCIsInR5cGUiOiJ1c2VyIiwiZXhwIjoxNzk0Njg0ODY0LCJpYXQiOjE3MzE2MTI5NDYsImp0aSI6ImFkZjBmZTA4LTBlOTctNDQxOS04ZTA4LWUzZTAyOTQ0MzUyMSJ9.Vu5wmyAX50vVW3FJwFCO8RW49piZEtjZZJClfZifptDLB7gwz69HvIzmzFU1LE-bnu8kF-0jX4INTaHcSch4Qw'
    

#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "SENTINELONE_ALERT",
         "sentineloneAlertSettings": {
           "authentication": {
             "headerKeyValues": [{
                "key": "Authorization",
                "value": "ApiToken"
              }]
           },
           "hostname": "hostname",
           "isAlertApiSubscribed": false
         }
       }
    }
    

### ServiceNow CMDB

This section provides API reference details for the `SERVICENOW_CMDB` log type. For details about the data source, see the [ServiceNow CMDB](https://developer.servicenow.com/dev.do#!/reference/api/orlando/rest/c_TableAPI) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
The fully qualified domain name of your ServiceNow REST API endpoint, such as `myinstance.servicenow.com`.  | Every 24 hours | `API`  
  
#### Prerequisites

  * Get the values for all the required fields.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.serviceNowCmdbSettings.authentication.user` | Yes | The username required for authentication.  
`details.serviceNowCmdbSettings.authentication.secret` | Yes | The secret required for authentication.  
`details.serviceNowCmdbSettings.hostname` | Yes | The fully qualified domain name of your ServiceNow REST API endpoint, such as `myinstance.servicenow.com`.  
`details.serviceNowCmdbSettings.feedname` | Yes | The ServiceNow table, which corresponds to a collection of records.  
  
#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example uses `curl` to retrieve a host description:
    
    
    curl --location 'https://directvtest.service-now.com/api/now/table/cmdb_ci?sysparm_display_value=true&sysparm_limit=1500&sysparm_offset=0' --header 'Authorization: Basic AUTH_TOKEN'
    

#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "SERVICENOW_CMDB",
         "servicenowCmdbSettings": {
           "authentication": {
             "user": "user",
             "secret": "secret"
           },
           "hostname": "hostname",
           "feedname": "feedname"
         }
       }
    }
    

If the feed returns a 403 error, check whether IP allowlisting is enabled on the CMDB data source. If yes, add the IP ranges from [goog.json](https://www.gstatic.com/ipranges/goog.json) and [cloud.json](https://www.gstatic.com/ipranges/cloud.json).

### Thinkst Canary

This section provides API reference details for the `THINKST_CANARY` log type. For details about the data source, see the [Thinkst Canary](https://docs.canary.tools/incidents/queries.html#all-incidents) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
`API_HOSTNAME/api/v1/incidents/all` Replace `API_HOSTNAME` with the domain name of Thinkst Canary REST API endpoint. | Every 30 minutes | `API`  
  
#### Prerequisites

  * Get the values for all the required fields.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.thinkstCanarySettings.authentication.headerKeyValues` | Yes | The HTTP headers in key-value format.  
`details.thinkstCanarySettings.hostname` | Yes | The fully qualified domain name of the Thinkst Canary REST API endpoint, such as `myinstance.canary.tools`.  
  
#### Test the API endpoint

Before you create the feed, use `curl` to test the Thinkst Canary API endpoint:

The following example uses `curl` to retrieve a list of all hosts (Birds):
    
    
    curl https://EXAMPLE.canary.tools/api/v1/devices/all \
      -d auth_token=KEY \
      -G
    

Replace KEY with the Thinkst Canary API key.

#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "THINKST_CANARY",
         "thinkstCanarySettings": {
           "authentication": {
             "user": "user",
             "secret": "secret"
           },
           "hostname": "hostname"
         }
       }
    }
    

### ThreatConnect

This section provides API reference details for the `THREATCONNECT_IOC` log type. For details about the data source, see the [ThreatConnect](https://docs.threatconnect.com/en/latest/rest_api/v2/indicators/indicators.html) documentation.

**Data source** | **Ingest schedule** | **`details.feedSourceType`**  
---|---|---  
The fully qualified domain name of the ThreatConnect REST API endpoint, such as `myinstance.threatconnect.com`.  | Every five minutes | `API`  
  
#### Prerequisites

  * Get the values for all the required fields.
  * Get the following required permissions: 
    * None



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.threatConnectIocSettings.authentication.user` | Yes | The username required for authentication.  
`details.threatConnectIocSettings.authentication.password` | Yes | The password required for authentication  
`details.threatConnectIocSettings.hostname` | Yes | The fully qualified domain name of the ThreatConnect REST API endpoint, such as `myinstance.threatconnect.com`.  
`details.threatConnectIocSettings.owners` | Yes | All the owner names, where an owner identifies a collection of IoCs.  
  
#### Other fields

`queueDelay`

#### Optional fields

`initialStartTime`

#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

The following example shows a `curl` request to retrieve indicators:
    
    
    curl --location 'https://workday.threatconnect.com/api/v2/indicators?resultStart=0&owner=2&resultLimit=10000&modifiedSince=2025-05-26T07%3A10%3A31+00%3A00' \
    --header 'Timestamp: 1748254416' \
    --header 'Authorization: TC TOKEN'
    

Replace the following placeholder:

  * TOKEN: OAuth access token



#### Sample create feed request
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "THREATCONNECT_IOC",
         "threatConnectIocSettings": {
           "authentication": {
             "user": "user",
             "secret": "secret"
           },
           "hostname": "hostname",
           "owners": [{
             "owner"
           }]
         }
       }
    }
    

### Trellix HX alerts

This section provides API reference details for the `TRELLIX_HX_ALERTS` log type. The poller downloads the details of the alerts generated from Trellix endpoints. For details about the alerts that the API returns, see [Alerts table](https://docs.trellix.com/bundle/hx_10.x_ug/page/UUID-d67eff46-230c-c5fc-1990-5afa0caf1b9b.html).

Data source | Ingest schedule | `details.feedSourceType` | `details.logType`  
---|---|---|---  
Trellix Endpoint Security (HX) API | Chronological polling | `API` | `TRELLIX_HX_ALERTS`  
  
#### Prerequisites

  * Obtain privileged access to the Trellix Endpoint Security (HX) management console.
  * Create an API user account on the Endpoint Security (HX) server.



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.trellixHxAlertsSettings.endpoint` | Yes | The base URL of your HX appliance (for example, `https://hxurl.hx.helix1.trellix.com...`).  
`details.trellixHxAlertsSettings.authentication.trellix_local.username` | Conditional | The local HX account username.  
`details.trellixHxAlertsSettings.authentication.trellix_local.password` | Conditional | The local HX account password.  
`details.trellixHxAlertsSettings.authentication.trellix_local.token_endpoint` | Conditional | The API endpoint path used to request the token (for example, `/hx/api/v3/token`).  
`details.trellixHxAlertsSettings.authentication.trellix_local.token_header` | Conditional | The HTTP header used for the authentication token (for example, `X-FeApi-Token`).  
  
#### Sample create feed request
    
    
    {
      "details": {
        "feedSourceType": "API",
        "logType": "TRELLIX_HX_ALERTS",
        "trellixHxAlertsSettings": {
            "endpoint": "[https://your-hx-appliance.local](https://your-hx-appliance.local)",
            "authentication": {
                "trellix_local": {
                    "username": "API_USERNAME",
                    "password": "API_USER_PASSWORD",
                    "token_endpoint": "/hx/api/v3/token",
                    "token_header": "X-FeApi-Token"
                    }
                }
            }
        }
    }
    

### Trellix HX audit

This section provides API reference details for the `TRELLIX_HX_AUDIT` log type. A bulk acquisition needs to be created outside of Google SecOps. This poller downloads any acquisitions that are created with a comment of `Created by Google SecOps`. 

**Important:** Bulk acquisitions aren't managed by the poller.Data source | Ingest schedule | `details.feedSourceType` | `details.logType`  
---|---|---|---  
Trellix Endpoint Security (HX) API | Chronological polling | `API` | `TRELLIX_HX_AUDIT`  
  
#### Prerequisites

  * Obtain privileged access to the Trellix Endpoint Security (HX) management console.
  * Ensure Trellix Endpoint Security (HX) API access is enabled.
  * Create an API user account on the Endpoint Security (HX) server.



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.trellixHxBulkAcqsSettings.endpoint` | Yes | The base URL of your HX appliance (for example, `https://hxurl.hx.helix1.trellix.com...`).  
`details.trellixHxBulkAcqsSettings.authentication.trellix_local.username` | Conditional | The local HX account username.  
`details.trellixHxBulkAcqsSettings.authentication.trellix_local.password` | Conditional | The local HX account password.  
`details.trellixHxBulkAcqsSettings.authentication.trellix_local.token_endpoint` | Conditional | The API endpoint path used to request the token (for example, `/hx/api/v3/token`).  
`details.trellixHxBulkAcqsSettings.authentication.trellix_local.token_header` | Conditional | The HTTP header used for the authentication token (for example, `X-FeApi-Token`).  
  
#### Sample create feed request
    
    
    {
      "details": {
        "feedSourceType": "API",
        "logType": "TRELLIX_HX_AUDIT",
        "trellixHxBulkAcqsSettings": {
            "endpoint": "[https://your-hx-appliance.local](https://your-hx-appliance.local)",
            "authentication": {
                "trellix_local": {
                    "username": "API_USERNAME",
                    "password": "API_USER_PASSWORD",
                    "token_endpoint": "/hx/api/v3/token",
                    "token_header": "X-FeApi-Token"
                    }
                }
            }
        }
    }      
    

### Trellix HX hosts

This section provides API reference details for the `TRELLIX_HX_HOSTS` log type, which downloads the host list from the Trellix HX server. For details about the data source, see the [Trellix Endpoint Security (HX) hosts documentation](https://docs.trellix.com/bundle/hx_10.x_ug/page/UUID-513e94b2-0914-147f-bbc2-8b0a707a4777.html).

Data source | Ingest schedule | `details.feedSourceType` | `details.logType`  
---|---|---|---  
Trellix Endpoint Security (HX) API | Chronological polling | `API` | `TRELLIX_HX_HOSTS`  
**Note:** Trellix HX requires a local API account provisioned from the Trellix HX instance. 

#### Prerequisites

  * Obtain privileged access to the Trellix Endpoint Security (HX) management console.
  * Create an API user account on the Endpoint Security (HX) server.



#### Type-specific request fields

Field | Required | Description  
---|---|---  
`details.trellixHxHostsSettings.endpoint` | Yes | The base URL of your HX appliance (for example, `https://hxurl.hx.helix1.trellix.com...`).  
`details.trellixHxHostsSettings.authentication.trellix_local.username` | Conditional | The local HX account username.  
`details.trellixHxHostsSettings.authentication.trellix_local.password` | Conditional | The local HX account password.  
`details.trellixHxHostsSettings.authentication.trellix_local.token_endpoint` | Conditional | The API endpoint path used to request the token (for example, `/hx/api/v3/token`).  
`details.trellixHxHostsSettings.authentication.trellix_local.token_header` | Conditional | The HTTP header used for the authentication token (for example, `X-FeApi-Token`).  
  
#### Sample create feed request
    
    
    {
      "details": {
        "feedSourceType": "API",
        "logType": "TRELLIX_HX_HOSTS",
        "trellixHxHostsSettings": {
            "endpoint": "[https://your-hx-appliance.local](https://your-hx-appliance.local)",
            "authentication": {
                "trellix_local": {
                    "username": "API_USERNAME",
                    "password": "API_USER_PASSWORD",
                    "token_endpoint": "/hx/api/v3/token",
                    "token_header": "X-FeApi-Token"
                    }
                }
            }
        }
    }
    

### Workday

This section provides API reference details for the `WORKDAY` log type. For details about the data source, see the [Workday Administrator Guide](https://doc.workday.com/home) (Integrations > Workday REST API).

**Data source** | **Ingest schedule** | **`details.feedSourceType`** | **`details.logType`**  
---|---|---|---  
  
  * {hostname}/ccx/api/v1/{mytentant}/workers
  * {hostname}/ccx/api/v1/{mytentant}/workers/{id}/timeOffEntries
  * {hostname}/ccx/api/v1/{mytentant}/workers/{id}/history
  * {hostname}/ccx/api/v1/{mytentant}/supervisoryOrganizations

| Every 24 hours | `API` | `WORKDAY`  
  
#### Prerequisites

  * In the Workday documentation for configuring OAuth 2.0 for your REST API client, follow the steps in **Register API Clients**.
  * Ensure that the Workday administrator provides you the `Get` and `View` permissions for the required security domain policies and provides access to the Workday API endpoints.



#### Type-specific request fields

**Field** | **Required** | **Description**  
---|---|---  
`details.workdaySettings.authentication.secret` | Yes | The access token generated by Workday after completing the steps to register OAuth 2.0 clients with Workday. To set up authentication, you must either specify the access token or all of the following OAuth fields: token endpoint, client ID, client secret, and refresh token.  
`details.workdaySettings.authentication.tokenEndpoint"` | Yes | The endpoint from which to get the access token.  
`details.workdaySettings.authentication.user` | Yes | The client ID generated by Workday after completing the steps to register OAuth 2.0 clients with Workday.  
`details.workdaySettings.authentication.secret` | Yes | The client secret generated by Workday after completing the steps to register OAuth 2.0 clients with Workday.  
`details.workdaySettings.authentication.refreshToken` | Yes | The refresh token generated by Workday after completing the steps to register OAuth 2.0 clients with Workday.  
`details.workdaySettings.hostname` | Yes | The hostname of the Workday REST web service. Example: `services1.workday.com`.  
`details.workdaySettings.tenantId` | Yes | The name of the tenant.  
  
#### Test the API endpoint

Before you create the feed, use `curl` to test the API endpoint.

  1. Request an OAuth token to authenticate your request to the API resource: 
         
         Get token:
         curl --location --request GET 'https://services1.myworkday.com/ccx/oauth2/examplecompany/token'   
         
         --header 'Content-Type: application/x-www-form-urlencoded'   
         
         --data-urlencode 'grant_type=refresh_token'   
         
         --data-urlencode 'refresh_token='   
         
         --data-urlencode 'client_id='   
         
         --data-urlencode 'client_secret='
         

  2. Use the OAuth token to send a request to the Workday API: 
         
         Fetch worker:
         curl --location 'https://services1.myworkday.com/ccx/api/v1/examplecompany/workers/f04e6fa2b771018771b0f716d500299a'   
         
         --header 'Authorization: Bearer '
         




#### Sample create feed request

The following sample uses a token endpoint, client ID, client secret, and refresh token:
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "WORKDAY",
         "workdaySettings": {
           "authentication": {
             "tokenEndpoint": "TokenEndpoint",
             "user": "ClientID",
             "clientSecret": "ClientSecret"
             "refreshToken": "RefreshToken"
           },
           "hostname": "hostname",
           "tenantId": "ID"
         }
       }
    }
    

The following sample uses an access token:
    
    
    {
       "details": {
         "feedSourceType": "API",
         "logType": "WORKDAY",
         "workdaySettings": {
           "authentication": {
             "secret": "AccessToken"
           },
           "hostname": "hostname",
           "tenantId": "ID"
         }
       }
    }
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
