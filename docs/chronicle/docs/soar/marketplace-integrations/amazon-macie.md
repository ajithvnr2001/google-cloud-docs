---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/amazon-macie/
title: Integrate Amazon Macie with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:45.018452+00:00
---

# Integrate Amazon Macie with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/amazon-macie/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Amazon Macie with Google SecOps 

This document describes how to integrate Amazon Macie with Google Security Operations (Google SecOps).

## Integration parameters

Use the following parameters to configure the integration:

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
AWS Access Key ID | String | N/A | Yes | AWS Access Key ID to use in integration.  
AWS Secret Key | Password | N/A | Yes | AWS Secret Key to use in integration.  
AWS Default Region | String | N/A | Yes | AWS default region to use in integration, for example us-west-1.  
Run Remotely | Checkbox | Unchecked | No | Select the checkbox to run the configured integration remotely. Once selected, the option appears to select the remote user (agent).  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Test the connectivity.

#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful:_ "Successfully connected to the Amazon Macie service with the provided connection parameters!" **The action should fail and stop a playbook execution:** _If a critical error, like wrong credentials or lost connectivity is reported:_ "Failed to connect to the Amazon Macie service! Error is {0}".format(exception.stacktrace) | Genera  
  
### List Findings

List Amazon Macie findings based on the specified action input parameters.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Finding Type | String | N/A | No | Finding type to search for, for example SensitiveData:S3Object/Credentials or SensitiveData:S3Object/Multiple. Parameter accepts multiple values as a comma-separated string. If nothing is specified, the action returns all types of findings.  
Severity | String | 4 | No | Finding severity to search - High, Medium or Low. Parameter accepts multiple values as a comma-separated string. If nothing is specified, the action returns all findings regardless of severity.  
Include Archived Findings? | Checkbox | Unchecked | No | Specify whether to include archived findings in results or not.  
Time Frame | Integer | 4 | No | Specify a timeframe in hours for which to fetch findings.  
Record limit | Integer | 20 | No | Specify how many records can be returned by the action.  
Sort by | String | N/A | No | Specify a parameter for sorting the data. Example: updatedAt  
Sort order | DDL | ASC | No | Sort order.  
  
#### Use cases

List Amazon Macie findings to see what findings are available.

#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### JSON result
    
    
    {
      "ResponseMetadata":{
        "HTTPHeaders":{
          "connection":"keep-alive",
          "content-length":"2741",
          "content-type":"application/json",
          "date":"Thu, 22 Oct 2020 11:08:58 GMT",
          "x-amz-apigw-id":"ID",
          "x-amzn-remapped-content-length":"2741",
          "x-amzn-remapped-date":"Thu, 22 Oct ""2020 11:08:57 ""GMT",
          "x-amzn-remapped-x-amzn-requestid":"eaea00d2-11f8-40d8-adce-f6c9f17e9815",
          "x-amzn-requestid":"4102349a-a5da-4bfc-ad78-40f48885985f"
        },
        "HTTPStatusCode":200,
        "RequestId":"4102349a-a5da-4bfc-ad78-40f48885985f",
        "RetryAttempts":0
      },
      "findings":[
        {
          "accountId":"ACCOUNT_ID",
          "archived":false,
          "category":"CLASSIFICATION",
          "classificationDetails":{
            "detailedResultsLocation":"s3://[export-config-not-set]/AWSLogs/ACCOUNT_ID/Macie/us-east-1/",
            "jobArn":"arn:aws:macie2:us-east-1",
            "jobId":"088009521d393eda440a24f3c7ad8fbd",
            "result":{
              "additionalOccurrences":false,
              "customDataIdentifiers":{
                "detections":[
                ],
                "totalCount":0
              },
              "mimeType":"application/zip",
              "sensitiveData":[
                {
                  "category":"PERSONAL_INFORMATION",
                  "detections":[
                    {
                      "count":80,
                      "type":"PHONE_NUMBER"
                    },
                    {
                      "count":5,
                      "type":"ADDRESS"
                    },
                    {
                      "count":207,
                      "type":"NAME"
                    }
                  ],
                  "totalCount":292
                },
                {
                  "category":"CREDENTIALS",
                  "detections":[
                    {
                      "count":5,
                      "type":"AWS_CREDENTIALS"
                    }
                  ],
                  "totalCount":5
                }
              ],
              "sizeClassified":44213802,
              "status":{
                "code":"PARTIAL",
                "reason":"ARCHIVE_CONTAINS_UNPROCESSED_FILES"
              }
            }
          },
          "count":1,
          "createdAt":datetime.datetime(2020,
          10,
          22,
          3,
          12,
          9,
          364000,
          "tzinfo=tzutc())",
          "description":"The object contains more than one type of ""sensitive information.",
          "id":"FINDING_ID",
          "partition":"aws",
          "region":"us-east-1",
          "resourcesAffected":{
            "s3Bucket":{
              "arn":"arn:aws:s3:::testexample",
              "createdAt":datetime.datetime(2020,
              9,
              14,
              10,
              31,
              56,
              "tzinfo=tzutc())",
              "defaultServerSideEncryption":{
                "encryptionType":"NONE"
              },
              "name":"testexample",
              "owner":{
                "displayName":"lab_aws",
                "id":"OWNER_ID"
              },
              "publicAccess":{
                "effectivePermission":"PUBLIC",
                "permissionConfiguration":{
                  "accountLevelPermissions":{
                    "blockPublicAccess":{
                      "blockPublicAcls":false,
                      "blockPublicPolicy":false,
                      "ignorePublicAcls":false,
                      "restrictPublicBuckets":false
                    }
                  },
                  "bucketLevelPermissions":{
                    "accessControlList":{
                      "allowsPublicReadAccess":false,
                      "allowsPublicWriteAccess":false
                    },
                    "blockPublicAccess":{
                      "blockPublicAcls":false,
                      "blockPublicPolicy":false,
                      "ignorePublicAcls":false,
                      "restrictPublicBuckets":false
                    },
                    "bucketPolicy":{
                      "allowsPublicReadAccess":true,
                      "allowsPublicWriteAccess":false
                    }
                  }
                }
              },
              "tags":[
              ]
            },
            "s3Object":{
              "bucketArn":"arn:aws:s3:::testsiemplify",
              "eTag":"8dfbe2ba101b3ca0a62f8fde823503b4-5",
              "extension":"zip",
              "key":"awscliv2.zip",
              "lastModified":datetime.datetime(2020,
              9,
              28,
              18,
              47,
              30,
              "tzinfo=tzutc())",
              "path":"testexample/awscliv2.zip",
              "publicAccess":false,
              "serverSideEncryption":{
                "encryptionType":"NONE"
              },
              "size":33775890,
              "storageClass":"STANDARD",
              "tags":[
              ],
              "versionId":""
            }
          },
          "sample":false,
          "schemaVersion":"1.0",
          "severity":{
            "description":"High",
            "score":3
          },
          "title":"The S3 object contains multiple types of sensitive ""information.",
          "type":"SensitiveData:S3Object/Multiple",
          "updatedAt":datetime.datetime(2020,
          10,
          22,
          3,
          12,
          9,
          364000,
          "tzinfo=tzutc())"
        }
      ]
    }
    

##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful:_ "Amazon Macie findings found" _If is_success=False, for example no findings were found:_ "No findings were returned." **The action should fail and stop a playbook execution:** _If a critical error, like wrong credentials or lost connectivity is reported:_ "Failed to connect to the Amazon Macie service! Error is {0}".format(exception.stacktrace) | General  
Table | **Table Name:** Amazon Macie Findings **Table Columns:**

  * Finding ID - "id"
  * Category
  * Title
  * Severity
  * Type
  * Is Archived - archived
  * Created At
  * Updated At

| General  
  
### Get Findings

Get Amazon Macie findings based on specified Finding ID.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Finding ID | String | N/A | Yes | Finding ID to get details for. Parameter can take multiple values as a comma-separated string.  
  
#### Use Cases

Get Findings details while analyzing the alert. Finding in this case will not be "flat" out as if it will be from connector, and finding data might be easier to process.

#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### JSON Result
    
    
    {
        "Policy": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "AddPerm",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": "s3:GetObject",
                    "Resource": "arn:aws:s3:::testexample/*"
                }
            ]
        }
    

##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful:_ "Amazon Macie findings found" _If is_success=False, for example no findings were found:_ "No findings were returned." **The action should fail and stop a playbook execution:** _If a critical error, like wrong credentials or lost connectivity is reported:_ "Failed to connect to the Amazon Macie service! Error is {0}".format(exception.stacktrace) | General  
Table | **Table Name:** Amazon Macie Findings **Table Columns:**
* Finding ID - "id"
* Category
* Title
* Severity
* Type
* Is Archived - archived
* Created At
* Updated At
| General  
  
### Create Custom Data Identifier

Create Amazon Macie Custom Data Identifier.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Custom Data Identifier Name | String | N/A | Yes | Amazon Macie new custom data identifier name.  
Custom Data Identifier Description | String | N/A | No | Amazon Macie new custom data identifier description.  
Custom Data Identifier Regular Expression | String | N/A | Yes | Amazon Macie new custom data identifier regular expression. Example: I[a@]mAB[a@]dRequest  
Custom Data Identifier Keywords | String | N/A | No | Amazon Macie new custom data identifier keywords.  
Custom Data Identifier Ignore Words | String | N/A | No | Amazon Macie new custom data identifier ignore words.  
Custom Data Identifier Maximum Match Distance | Integer | 50 | No | Amazon Macie new custom data identifier maximum match distance.  
  
#### Use cases

Create Amazon Macie custom data identifier based on the observed data, so later new custom data identifier can be used in classification jobs.

#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### JSON Result
    
    
    {
      "ResponseMetadata":{
        "HTTPHeaders":{
          "connection":"keep-alive",
          "content-length":"65",
          "content-type":"application/json",
          "date":"Mon, 26 Oct 2020 05:15:07 GMT",
          "x-amz-apigw-id":"ID",
          "x-amzn-remapped-content-length":"65",
          "x-amzn-remapped-date":"Mon, 26 Oct ""2020 05:15:07 ""GMT",
          "x-amzn-remapped-x-amzn-requestid":"61217a30-189e-4573-9f76-257b7065a04d",
          "x-amzn-requestid":"509e1c12-ab86-459e-9d6d-790a359686b2"
        },
        "HTTPStatusCode":200,
        "RequestId":"509e1c12-ab86-459e-9d6d-790a359686b2",
        "RetryAttempts":0
      },
      "customDataIdentifierId":"ff43487b-5643-4de1-b651-9ecbeb3021ed"
    }
    

##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful:_ "New Amazon Macie custom data identifier created: {0}".format(new identifier_id from response) _If is_success=False, for example no findings were found:_ "Failed to create Amazon Macie Identifier. Error is: {0}".format(error from response) **The action should fail and stop a playbook execution:** _If a critical error, like wrong credentials or lost connectivity is reported:_ "Failed to connect to the Amazon Macie service! Error is {0}".format(exception.stacktrace) | General  
  
### Delete Custom Data Identifier

Delete Amazon Macie Custom Data Identifier.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Custom Data Identifier ID | String | N/A | No | Amazon Macie custom data identifier id to delete.  
  
#### Use Cases

Delete Amazon Macie Custom Data Identifier.

#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful:_ "Amazon Macie custom data identifier {0} deleted".format(custom data identifier id) _If is_success=False, for example no findings were found:_ "Failed to delete Amazon Macie Identifier {0}. Error is: {1}".format(custom data identifier id, error from response) **The action should fail and stop a playbook execution:** _If a critical error, like wrong credentials or lost connectivity is reported:_ "Failed to connect to the Amazon Macie service! Error is {0}".format(exception.stacktrace) | General  
  
### Enable Macie

Enable the Amazon Macie service.

#### Parameters

N/A

#### Use cases

Enable Amazon Macie after service window is completed.

#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful:_ "Successfully enabled Amazon Macie service" _If is_success=False:_ "Failed to enable Amazon Macie service. Error is: {0}".format(error from response) **The action should fail and stop a playbook execution:** _If a critical error, like wrong credentials or lost connectivity is reported:_ "Failed to connect to the Amazon Macie service! Error is {0}".format(exception.stacktrace) | General  
  
### Disable Macie

Disable Amazon Macie service.

#### Use Cases

Disable Amazon Macie for service window - to make some change is AWS buckets and not cause a lot of false positives.

#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True or False | is_success:False  
  
##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful:_ "Successfully disabled Amazon Macie service" _If is_success=False:_ "Failed to disable Amazon Macie service. Error is: {0}".format(error from response) **The action should fail and stop a playbook execution:** _If a critical error, like wrong credentials or lost connectivity is reported:_ "Failed to connect to the Amazon Macie service! Error is {0}".format(exception.stacktrace) | General  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### Amazon Macie - Findings Connector

Ingest Amazon Macie findings.

##### Connector parameters

Use the following parameters to configure the connector:

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Product Field Name | String | N/A | Yes |  The name of the field where the product name is stored. The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default. The default value is `Product Name`.  
Event Field Name | String | N/A | Yes | The name of the field that determines the event name (subtype).  
Environment Field Name | String | N/A | No | The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value.  
`Environment Regex Pattern` | String | N/A | No |  A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | The timeout limit, in seconds, for the Python process that runs the current script.  
AWS Access Key ID | String | N/A | True | AWS Access Key ID to use in integration.  
AWS Secret Key | Password | N/A | True | AWS Secret Key to use in integration.  
AWS Default Region | String | N/A | True | AWS default region to use in integration, for example us-west-2.  
Finding severity to ingest | String | N/A | No | Finding severity to ingest - `High`, `Medium`, or `Low`. Parameter accepts multiple values as a comma-separated string. If nothing is specified, the connector ingests all findings regardless of severity.  
Max findings to fetch | Integer | 50 | No | Number of findings to process per one connector iteration.  
Fetch Max Hours Backwards | Integer | 1 | No | The number of hours prior to now to retrieve alerts. This parameter can apply to the initial connector iteration after you enable the connector for the first time, or the fallback value for an expired connector timestamp.  
`Use whitelist as a blacklist` | Checkbox | Unchecked | Yes | If selected, the connector uses the dynamic list as a blocklist.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector Rules

The blocklist is disabled by default.

The connector supports the dynamic list that ingests only findings of specific type.

The connector supports proxies.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
