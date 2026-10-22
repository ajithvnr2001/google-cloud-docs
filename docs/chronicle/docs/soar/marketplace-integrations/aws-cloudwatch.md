---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/aws-cloudwatch/
title: Integrate AWS CloudWatch with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:23.686756+00:00
---

# Integrate AWS CloudWatch with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/aws-cloudwatch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate AWS CloudWatch with Google SecOps 

This document describes how to integrate AWS CloudWatch with Google Security Operations (Google SecOps).

## Use Cases

Active actions - search in logs, create log groups/streams, delete log groups/streams, update retention policies.

## Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name> | Type> | Default Value> | Is Mandatory> | Description>  
---|---|---|---|---  
AWS Access Key ID | String | N/A | Yes | AWS Access Key ID to use in integration.  
AWS Secret Key | Password | N/A | Yes | AWS Secret Key to use in integration.  
AWS Default Region | String | N/A | Yes | AWS default region to use in integration, for example us-west-2.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Test the connectivity to AWS CloudWatch.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name> | Value Options>  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if successful:** "Successfully connected to the AWS CloudWatch server with the provided connection parameters!"  
**The action should fail and stop a playbook execution:**   
**if not successful:** "Failed to connect to the AWS CloudWatch server! Error is {0}".format(exception.stacktrace) | General  
  
### List Log Groups

List available log groups in AWS CloudWatch.

#### Parameters

Parameter Display Name> | Type> | Default Value> | Is Mandatory> | Description>  
---|---|---|---|---  
Max Groups To Return | Integer | 50 | No | Specify how many groups to return. Default: 50.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name> | Value Options>  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    [
        {
            "arn": "arn:aws:logs:us-east-1:",
            "creationTime": 1611581795766,
            "logGroupName": "CloudTrail/DefaultLogGroup",
            "metricFilterCount": 0,
            "storedBytes": 24529015
        },
        {
            "arn": "arn:aws:logs:us-east-1:",
            "creationTime": 1606993203235,
            "logGroupName": "Example",
            "metricFilterCount": 1,
            "storedBytes": 730
        },
        {
            "arn": "arn:aws:logs:us-east-1:",
            "creationTime": 1611652265055,
            "logGroupName": "aws-cloudtrail-logs",
            "metricFilterCount": 0,
            "storedBytes": 51354815
        }
    ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if data is available (is_success = true):** "Successfully returned available log groups in AWS CloudWatch". **if no data is available (is_success = true):** "No log groups were found in AWS CloudWatch". **The action should fail and stop a playbook execution:**   
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Log Groups". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Name:** "Log Groups" **Column:** Name Metric Filter Count Stored Bytes Creation Time | General  
  
### List Log Streams

List available log streams in AWS CloudWatch.

#### Parameters

Parameter Display Name> | Type> | Default Value> | Is Mandatory> | Description>  
---|---|---|---|---  
Log Groups | CSV | N/A | Yes | Specify a comma-separated list of group names for which you want to retrieve log streams.  
Order By | DDL | Log Stream Name  
Possible Values: Log Stream Name Last Event Time  | No | Specify how the log streams should be ordered.  
Sort Order | DDL | Ascending Possible Values: Ascending Descending | No | Specify what sort order should be used.  
Max Streams To Return | Integer | 50 | No | Specify how many streams to return per log group.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name> | Value Options>  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    [{
        "group":"{group name}"
    "logStreams": [
            {
                "arn": "arn:aws:logs:us-east-1:log-group:aws-cloudtrail-logs:log-stream:CloudTrail_us-east-1",
                "creationTime": 1611652272827,
                "firstEventTimestamp": 1611652287716,
                "lastEventTimestamp": 1612271538268,
                "lastIngestionTime": 1612271538289,
                "logStreamName": "CloudTrail_us-east-1",
                "storedBytes": 0,
                "uploadSequenceToken": "49039859450784908968417870788122674924958823185025535393"
            }
        ]
    }
    ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if data is available for at least one log group (is_success = true):** "Successfully returned available log streams for the following log groups in AWS CloudWatch: {group names}". **if data is not available for at least one log group (is_success = true):** "Action wasn't able to return available log streams for the following log groups in AWS CloudWatch: {group names}". **if data is not available for at least one log group (is_success = false):** "No log streams were found for the provided log groups in AWS CloudWatch". **The action should fail and stop a playbook execution:**   
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Log Streams". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Name:** "{Group Name}: Log Streams" **Column:** Name Stored Bytes Creation Time Last Event Timestamp  | General  
  
### Search Log Event

Search log events in AWS CloudWatch.

#### Parameters

Parameter Display Name> | Type> | Default Value> | Is Mandatory> | Description>  
---|---|---|---|---  
Log Group | String | N/A | Yes | Specify the name of the log group, where you want to search for events.  
Log Streams | CSV | N/A | No | Specify a comma-separated list of log streams, where you want to search for events.  
Time Frame | DDL | Last Hour Possible Values: Last Hour Last 6 Hours Last 24 Hours Last Week Last Month Custom | No | Specify a timeframe for the search. If "Custom" is selected, you must also set a "Start Time".  
Start Time | String | N/A | No | Specify the start time for the search. This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. Format: ISO 8601  
End Time | String | N/A | No | Specify the end time for the search. Format: ISO 8601. If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter will use current time.  
Custom Filter | String | N/A | No | Specify the custom filter for the search. For additional information please refer to the documentation portal.  
Max Events To Return | Integer | 50 | No | Specify how many events to return. Default: 50.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name> | Value Options>  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    [
            {
                "eventId": "ID",
                "ingestionTime": 1611652287896,
                "logStreamName": "CloudTrail_us-east-1",
                "message": {
                    "eventVersion": "1.08",
                    "userIdentity": {
                        "type": "AssumedRole",
                        "principalId": "ID",
                        "arn":"arn:aw
    s:sts: : ACCOUNT_ID:assumed-role/AWSServiceRoleForAmazonMacie/AmazonMacieSession","accountId":"ACCOUNT_ID","accessKeyId":"KEY_ID","sessionC
    ontext":{"sessionIssuer":{"type":"Role","principalId":"ID","arn":"arn:aws:iam: : ACCOUNT_ID:role/aws-service-role/macie.amazonaws.com/AW
    SServiceRoleForAmazonMacie","accountId":"ACCOUNT_ID","userName":"AWSServiceRoleForAmazonMacie"},"webIdFederationData":{},"attributes":{"mfaAuthenticated": "false",
                        "creationDate": "2021-01-26T08:53:52Z"
                    }
                },
                "invokedBy": "AWS Internal",
                "eventTime": "2021-01-26T08:53:52Z",
                "eventSource": "s3.amazonaws.com",
                "eventName": "GetBucketLogging",
                "awsRegion": "us-east-1",
                "sourceIPAddress": "AWSInternal",
                "userAgent": "AWS Internal",
                "requestParameters": {
                    "logging": "",
                    "bucketName": "example",
                    "Host": "example.s3.amazonaws.com"
                },
                "responseElements": null,
                "additionalEventData": {
                    "SignatureVersion": "SigV4",
                    "CipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
                    "bytesTransferredIn": 0,
                    "AuthenticationMethod": "AuthHeader",
                    "x-amz-id-2": "PFM+6pyK/gCPy95gh8dtstgtXftrpHkL8s=",
                    "bytesTransferredOut": 289
                },
                "requestID": "8FA919A428BC82D7",
                "eventID": "7eb5dd44-7021-4945-b9be-27f5b1e0d8d0",
                "readOnly": true,
                "resources": [
                    {
                        "accountId": "ACCOUNT_ID",
                        "type": "AWS::S3::Bucket",
                        "ARN": "arn:aws:s3:::example"
                    }
                ],
                "eventType": "AwsApiCall",
                "managementEvent": true,
                "eventCategory": "Management",
                "recipientAccountId": "ACCOUNT_ID"
            },
            "timestamp": 1611652287716
        }
    ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if data is available for (is_success = true):** "Successfully executed search in AWS CloudWatch". **if data is not available (is_success = false):** "No data was found for the provided search.". **The action should fail and stop a playbook execution:**   
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Search Log Events". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Name:** "Search Results" **Column:** all of the keys available. | General  
  
### Set Retention Policy

Set the retention policy for log groups in AWS CloudWatch.

#### Parameters

Parameter Display Name> | Type> | Default Value> | Is Mandatory> | Description>  
---|---|---|---|---  
Log Group | String | N/A | Yes | Specify the name of the log group for which you want to set the retention policy.  
Retention Days | DDL | 1Possible Values 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653 | Yes | Specify for how many days the data should be retained in the log group.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name> | Value Options>  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if data success: (is_success = true):** "Successfully set the retention policy for log group {group} in AWS CloudWatch". **The action should fail and stop a playbook execution:**   
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Set Retention Policy". Reason: {0}''.format(error.Stacktrace) | General  
  
### Remove Retention Policy

Remove the retention policy from the log group in AWS CloudWatch.

#### Parameters

Parameter Display Name> | Type> | Default Value> | Is Mandatory> | Description>  
---|---|---|---|---  
Log Group | String | N/A | Yes | Specify the name of the log group from which you want to remove the retention policy.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name> | Value Options>  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if data success: (is_success = true):** "Successfully removed the retention policy from log group {group} in AWS CloudWatch". **The action should fail and stop a playbook execution:**   
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Remove Retention Policy". Reason: {0}''.format(error.Stacktrace) | General  
  
### Create Log Group

Create a log group in AWS CloudWatch.

#### Parameters

Parameter Display Name> | Type> | Default Value> | Is Mandatory> | Description>  
---|---|---|---|---  
Log Group Name | String | N/A | Yes | Specify the name for the new log group.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name> | Value Options>  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
    "group_name": "GROUP_NAME"
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if data success: (is_success = true):** "Successfully created a new log group {group} in AWS CloudWatch". **The action should fail and stop a playbook execution:**   
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Сreate Log Group". Reason: {0}''.format(error.Stacktrace) | General  
  
### Create Log Stream

Create a log stream for the log group in AWS CloudWatch.

#### Parameters

Parameter Display Name> | Type> | Default Value> | Is Mandatory> | Description>  
---|---|---|---|---  
Log Group | String | N/A | Yes | Specify the name of the log group, where you want to create a log stream.  
Log Stream Name | String | N/A | Yes | Specify the name for the new log stream.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name> | Value Options>  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
    "log_stream": "STREAM_NAME"
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if data success: (is_success = true):** "Successfully created a new log stream in log group {group} in AWS CloudWatch". **The action should fail and stop a playbook execution:**   
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Сreate Log Stream". Reason: {0}''.format(error.Stacktrace) | General  
  
### Delete Log Group

Delete a log group in AWS CloudWatch.

#### Parameters

Parameter Display Name> | Type> | Default Value> | Is Mandatory> | Description>  
---|---|---|---|---  
Log Group Name | String | N/A | Yes | Specify the name of the log group that needs to be deleted.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name> | Value Options>  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if data success: (is_success = true):** "Successfully deleted log group {group} in AWS CloudWatch". **If group doesn't exist (is_success=false):** "Action wasn't able to delete log group {group} in AWS CloudWatch. Reason: Log group {group} wasn't found in AWS CloudWatch." **The action should fail and stop a playbook execution:**   
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Delete Log Group". Reason: {0}''.format(error.Stacktrace) | General  
  
### Delete Log Stream

Delete a log stream in a log group in AWS CloudWatch.

#### Parameters

Parameter Display Name> | Type> | Default Value> | Is Mandatory> | Description>  
---|---|---|---|---  
Log Group Name | String | N/A | Yes | Specify the name of the log group that contains the log stream.  
Log Stream Name | String | N/A | Yes | Specify the name of the log stream that needs to be deleted.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name> | Value Options>  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if data success: (is_success = true):** "Successfully deleted log stream {stream} from log group {group} in AWS CloudWatch". **If stream doesn't exist (is_success=false):** "Action wasn't able to delete log stream {stream} from log group {group} in AWS CloudWatch. Reason: Log stream{stream} wasn't found in log group {group} in AWS CloudWatch." **If group doesn't exist (is_success=false):** "Action wasn't able to delete log stream {stream} from log group {group} in AWS CloudWatch. Reason: Log group {group} wasn't found in AWS CloudWatch." **The action should fail and stop a playbook execution:**   
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Delete Log Stream". Reason: {0}''.format(error.Stacktrace) | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
