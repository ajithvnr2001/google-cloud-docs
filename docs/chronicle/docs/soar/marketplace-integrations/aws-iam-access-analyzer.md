---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/aws-iam-access-analyzer/
title: AWS IAM Access Analyzer \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:33.494436+00:00
---

# AWS IAM Access Analyzer  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/aws-iam-access-analyzer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# AWS IAM Access Analyzer

This document describes how to integrate AWS IAM Access Analyzer with Google Security Operations.

## Use Cases

  1. Ingest findings into Google Security Operations for investigation
  2. Active actions - update insights, scan resources



## Configure AWS IAM Access Analyzer integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
AWS Access Key ID | String | N/A | Yes | AWS Access Key ID to use in integration.  
AWS Secret Key | Password | N/A | Yes | AWS Secret Key to use in integration.  
AWS Default Region | String | N/A | Yes | AWS default region to use in integration, for example us-west-2.  
Analyzer Name | String | N/A | Yes | Name of the analyzer that should be used in the integration.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to AWS IAM Access Analyzer with parameters provided at the integration configuration page in Google SecOps Content Hub page.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if successful:** print "Successfully connected to the AWS IAM Access Analyzer server with the provided connection parameters!" **The action should fail and stop a playbook execution:**   
**if not successful:** print "Failed to connect to the AWS IAM Access Analyzer server! Error is {0}".format(exception.stacktrace) | General  
  
### Scan Resources

#### Description

Scan resources using AWS IAM Access Analyzer.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Resource ARNs | CSV | N/A | Yes | Specify a comma-separated list of resource ARNs that need to be scanned.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {"ResponseMetadata": {"HTTPHeaders": {"connection": "keep-alive",
        "content-length": "178",
        "content-type": "application/json",
        "date": "Sun, 22 Nov 2020 09:22:03 GMT",
        "x-amz-apigw-id": "WZwVQFICIAMFjnQ=",
        "x-amzn-requestid": "c15d8ab2-afc7-4cb0-bea2-a47ebc649cb8",
        "x-amzn-trace-id": "Root=1-5fba2dbb-042d89bb2964e4f635bd7843"},
    "HTTPStatusCode": 200,
    "RequestId": "c15d8ab2-afc7-4cb0-bea2-a47ebc649cb8",
    "RetryAttempts": 0},
    "resource": {"analyzedAt": datetime.datetime(2020, 11, 22, 9, 21, 50, 919000, tzinfo=tzutc()),
    "isPublic": False,
    "resourceArn": "arn:aws:s3:::asddsa",
    "resourceOwnerAccount": "582302349248",
    "resourceType": "AWS::S3::Bucket"}}
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If successfully returned scans for at least one (is_success = true) :** print"Successfully scanned the following resources using AWS IAM Access Analyzer: \n".format(Resource IDs) **If fail for at least one (is_success = true):** print"Action wasn't able to scan the following resources using AWS IAM Access Analyzer: \n".format(Resource IDs) **If fail for all (is_success = false):** print"No resources were scanned."  Async Message: "Waiting for the following resources to be scanned using AWS IAM Access Analyzer: {0}".format(unprocessed resources)**The action should fail and stop a playbook execution:** **if fatal error, SDK error, like wrong credentials, no connection to server, other:** print "Error executing action "Scan Resources". Reason: {0}''.format(error.Stacktrace) **If Analyzer is not found:** print "Error executing action "Scan Resources". Reason: '{0}' analyzer was not found''.format(Analyzer Name). | General  
  
### Archive Finding

Archive finding in AWS Security Hub.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Finding ID | String | N/A | Yes | Specify ID of the finding that you want to archive.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If no raised errors from SDK (is_success = true) :** print"Successfully archived finding with ID '{0}' in AWS IAM Access Analyzer".format(Finding ID) **The action should fail and stop a playbook execution:** **if fatal error, SDK error, like wrong credentials, no connection to server, other:** print "Error executing action "Archive Finding". Reason: {0}''.format(error.Stacktrace) **If Analyzer is not found:** print "Error executing action "Archive Finding". Reason: '{0}' analyzer was not found''.format(Analyzer Name). | General  
  
## Connector

### AWS IAM Access Analyzer - Findings Connector

#### Description

Pull findings from AWS IAM Access Analyzer.

**Note:** Whitelist works on resource types.

#### Configure AWS IAM Access Analyzer - Findings Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | resourceType | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
AWS Access Key ID | String | N/A | True | AWS Access Key ID to use in integration.  
AWS Secret Key | Password | N/A | True | AWS Secret Key to use in integration.  
AWS Default Region | String | N/A | True | AWS default region to use in integration, for example us-west-2.  
Analyzer Name | String | N/A | True | Name of the analyzer that should be used in the integration.  
Alert Severity | String | Medium | False | Severity of the Google SecOps Alerts created from this connector. Possible values: Critical, High, Medium,Low,Informational  
Max Findings To Fetch | Integer | 50 | No | How many findings to process per one connector iteration.  
Max Hours Backwards | Integer | 1 | No | How many hours backwards to fetch findings.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist will be used as a blacklist.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verify the SSL certificate for the connection to the AWS IAM Access Analyzer server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy Support

The connector supports Proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
