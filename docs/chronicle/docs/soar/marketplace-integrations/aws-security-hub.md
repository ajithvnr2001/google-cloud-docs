---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/aws-security-hub/
title: Integrate AWS Security Hub with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:58:04.571042+00:00
---

# Integrate AWS Security Hub with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/aws-security-hub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate AWS Security Hub with Google SecOps

This document explains how to integrate AWS Security Hub with Google Security Operations (Google SecOps).

## Use cases

In Google SecOps, the AWS Security Hub integration can help you solve the following use cases:

  * **Automated incident enrichment:** use the Google SecOps capabilities to automatically retrieve relevant context from other AWS services like VPC Flow Logs, GuardDuty findings, and CloudTrail logs when a potential security event is detected in Security Hub. The automated incident enrichment can help analysts quickly understand the scope and potential impact of the incident.

  * **Prioritized remediation:** use the Google SecOps capabilities to trigger automated responses to Security Hub findings based on predefined playbooks. For example, a high-severity finding related to an exposed S3 bucket can automatically trigger a playbook to remediate the misconfiguration and notify the appropriate teams.

  * **Threat intelligence integration:** use the Google SecOps capabilities to integrate with threat intelligence feeds and cross-reference Security Hub findings against known malicious indicators. The threat intelligence integration lets analysts identify and prioritize high-risk threats that require immediate attention.

  * **Compliance reporting and auditing:** use the Google SecOps capabilities to aggregate and normalize security data from Security Hub and other sources to simplify compliance reporting.

  * **Vulnerability management:** use the Google SecOps capabilities to automate the process of vulnerability triage, prioritization, and remediation by integrating with AWS Security Hub vulnerability scanning features. The vulnerability management can help you reduce the attack surface and improve the overall security posture of your organization.




## Before you begin

For the integration to function properly, you need to configure a custom identity and access policy in AWS.

For more information about creating custom policies in AWS, see [Creating policies using the JSON editor](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console#access_policies_create-json-editor) in AWS documentation.

To configure permissions that are required for the AWS Security Hub integration, and set the custom policy, use the following code:
    
    
    {
                "Sid": "SecurityHubServiceRolePermissions",
                "Effect": "Allow",
                "Action": [
                    "securityhub:GetMasterAccount",
                    "securityhub:GetInsightResults",
                    "securityhub:CreateInsight",
                    "securityhub:UpdateInsight",
                    "securityhub:BatchUpdateFindings",
                    "securityhub:GetFindings",
                    "securityhub:GetInsight",
                    "securityhub:DescribeHub",
                ],
                "Resource": "*"
    }
    

For more information about configuring permissions, see [AWS managed policy: `AWSSecurityHubServiceRolePolicy`](http://docs.aws.amazon.com/securityhub/latest/userguide/security-iam-awsmanpol#security-iam-awsmanpol-awssecurityhubservicerolepolicy) in AWS documentation.

## Integration parameters

The AWS Security Hub integration requires the following parameters:

Parameter | Description  
---|---  
`AWS Access Key ID` | _Required_ The AWS access key ID to use in integration.  
`AWS Secret Key` | _Required_ The AWS secret key to use in the integration.  
`AWS Default Region` | _Required_ The AWS default region to use in the integration, such as `us-west-2`.  
  
You can make changes at a later stage, if necessary. After you configure instances, you can use them in playbooks. For more information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

For instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Work with the Filter JSON Object parameter

For the **Create Insight** and **Update Insight** action, you can configure filters for findings.

To create an insight in AWS Security Hub, apply filters for the findings that are available in the system.

The structure of the filter with all possible configurations is as follows:
    
    
    {
        "ProductArn": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "AwsAccountId": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "Id": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "GeneratorId": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "Type": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "FirstObservedAt": [
            {
                "Start": "string",
                "End": "string",
                "DateRange": {
                    "Value": 123,
                    "Unit": "DAYS"
                }
            }
        ],
        "LastObservedAt": [
            {
                "Start": "string",
                "End": "string",
                "DateRange": {
                    "Value": 123,
                    "Unit": "DAYS"
                }
            }
        ],
        "CreatedAt": [
            {
                "Start": "string",
                "End": "string",
                "DateRange": {
                    "Value": 123,
                    "Unit": "DAYS"
                }
            }
        ],
        "UpdatedAt": [
            {
                "Start": "string",
                "End": "string",
                "DateRange": {
                    "Value": 123,
                    "Unit": "DAYS"
                }
            }
        ],
        "SeverityProduct": [
            {
                "Gte": 123.0,
                "Lte": 123.0,
                "Eq": 123.0
            }
        ],
        "SeverityNormalized": [
            {
                "Gte": 123.0,
                "Lte": 123.0,
                "Eq": 123.0
            }
        ],
        "SeverityLabel": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "Confidence": [
            {
                "Gte": 123.0,
                "Lte": 123.0,
                "Eq": 123.0
            }
        ],
        "Criticality": [
            {
                "Gte": 123.0,
                "Lte": 123.0,
                "Eq": 123.0
            }
        ],
        "Title": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "Description": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "RecommendationText": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "SourceUrl": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ProductFields": [
            {
                "Key": "string",
                "Value": "string",
                "Comparison": "EQUALS"|"NOT_EQUALS"
            }
        ],
        "ProductName": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "CompanyName": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "UserDefinedFields": [
            {
                "Key": "string",
                "Value": "string",
                "Comparison": "EQUALS"|"NOT_EQUALS"
            }
        ],
        "MalwareName": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "MalwareType": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "MalwarePath": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "MalwareState": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "NetworkDirection": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "NetworkProtocol": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "NetworkSourceIpV4": [
            {
                "Cidr": "string"
            }
        ],
        "NetworkSourceIpV6": [
            {
                "Cidr": "string"
            }
        ],
        "NetworkSourcePort": [
            {
                "Gte": 123.0,
                "Lte": 123.0,
                "Eq": 123.0
            }
        ],
        "NetworkSourceDomain": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "NetworkSourceMac": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "NetworkDestinationIpV4": [
            {
                "Cidr": "string"
            }
        ],
        "NetworkDestinationIpV6": [
            {
                "Cidr": "string"
            }
        ],
        "NetworkDestinationPort": [
            {
                "Gte": 123.0,
                "Lte": 123.0,
                "Eq": 123.0
            }
        ],
        "NetworkDestinationDomain": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ProcessName": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ProcessPath": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ProcessPid": [
            {
                "Gte": 123.0,
                "Lte": 123.0,
                "Eq": 123.0
            }
        ],
        "ProcessParentPid": [
            {
                "Gte": 123.0,
                "Lte": 123.0,
                "Eq": 123.0
            }
        ],
        "ProcessLaunchedAt": [
            {
                "Start": "string",
                "End": "string",
                "DateRange": {
                    "Value": 123,
                    "Unit": "DAYS"
                }
            }
        ],
        "ProcessTerminatedAt": [
            {
                "Start": "string",
                "End": "string",
                "DateRange": {
                    "Value": 123,
                    "Unit": "DAYS"
                }
            }
        ],
        "ThreatIntelIndicatorType": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ThreatIntelIndicatorValue": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ThreatIntelIndicatorCategory": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ThreatIntelIndicatorLastObservedAt": [
            {
                "Start": "string",
                "End": "string",
                "DateRange": {
                    "Value": 123,
                    "Unit": "DAYS"
                }
            }
        ],
        "ThreatIntelIndicatorSource": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ThreatIntelIndicatorSourceUrl": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ResourceType": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ResourceId": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ResourcePartition": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ResourceRegion": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ResourceTags": [
            {
                "Key": "string",
                "Value": "string",
                "Comparison": "EQUALS"|"NOT_EQUALS"
            }
        ],
        "ResourceAwsEc2InstanceType": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ResourceAwsEc2InstanceImageId": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ResourceAwsEc2InstanceIpV4Addresses": [
            {
                "Cidr": "string"
            }
        ],
        "ResourceAwsEc2InstanceIpV6Addresses": [
            {
                "Cidr": "string"
            }
        ],
        "ResourceAwsEc2InstanceKeyName": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ResourceAwsEc2InstanceVpcId": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ResourceAwsEc2InstanceSubnetId": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ResourceAwsEc2InstanceLaunchedAt": [
            {
                "Start": "string",
                "End": "string",
                "DateRange": {
                    "Value": 123,
                    "Unit": "DAYS"
                }
            }
        ],
        "ResourceAwsS3BucketOwnerId": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ResourceAwsS3BucketOwnerName": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ResourceAwsIamAccessKeyUserName": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ResourceAwsIamAccessKeyStatus": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ResourceAwsIamAccessKeyCreatedAt": [
            {
                "Start": "string",
                "End": "string",
                "DateRange": {
                    "Value": 123,
                    "Unit": "DAYS"
                }
            }
        ],
        "ResourceContainerName": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ResourceContainerImageId": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ResourceContainerImageName": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "ResourceContainerLaunchedAt": [
            {
                "Start": "string",
                "End": "string",
                "DateRange": {
                    "Value": 123,
                    "Unit": "DAYS"
                }
            }
        ],
        "ResourceDetailsOther": [
            {
                "Key": "string",
                "Value": "string",
                "Comparison": "EQUALS"|"NOT_EQUALS"
            }
        ],
        "ComplianceStatus": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "VerificationState": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "WorkflowState": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "WorkflowStatus": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "RecordState": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "RelatedFindingsProductArn": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "RelatedFindingsId": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "NoteText": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "NoteUpdatedAt": [
            {
                "Start": "string",
                "End": "string",
                "DateRange": {
                    "Value": 123,
                    "Unit": "DAYS"
                }
            }
        ],
        "NoteUpdatedBy": [
            {
                "Value": "string",
                "Comparison": "EQUALS"|"PREFIX"|"NOT_EQUALS"|"PREFIX_NOT_EQUALS"
            }
        ],
        "Keyword": [
            {
                "Value": "string"
            }
        ]
    }
    

An example of a filter that returns only findings with the critical severity is as follows:
    
    
    {
        "SeverityLabel": [
            {
                "Value": "CRITICAL",
                "Comparison": "EQUALS"
            }
        ]
    }
    

## Actions

To function properly, the AWS Security Hub actions require you to configure specific permissions. For more information about the permissions for the integration, see the Before you begin section of this document.

### Create Insight

Use the **Create Insight** action to create an insight in AWS Security Hub.

#### Action inputs

The **Create Insight** action requires the following parameters:

Parameter | Description  
---|---  
`Insight Name` | _Required_ The name of the insight.  
`Group By Attribute` | _Required_ The name of the attribute to group the findings by. The action groups the findings under one insight. The default value is `AWS Account ID`. The possible values are as follows:

  * `AWS Account ID`
  * `Company Name`
  * `Status`
  * `Generator ID`
  * `Malware Name`
  * `Process Name`
  * `Threat Intel Type`
  * `Product ARN`
  * `Product Name`
  * `Record State`
  * `EC2 Instance Image ID`
  * `EC2 Instance IPv4`
  * `EC2 Instance IPv6`
  * `EC2 Instance Key Name`
  * `EC2 Instance Subnet ID`
  * `EC2 Instance Type`
  * `EC2 Instance VPC ID`
  * `IAM Access Key User Name`
  * `S3 Bucket Owner Name`
  * `Container Image ID`
  * `Container Image Name`
  * `Container Name`
  * `Resource ID`
  * `Resource Type`
  * `Severity Label`
  * `Source URL`
  * `Type`
  * `Verification State`
  * `Workflow Status`

  
`Filter JSON Object` | _Required_ A filter to apply to findings. The filter is a JSON object that lets you specify different attributes and values. For more details about the filter configuration, see Work with the Filter JSON Object parameter section of this document.  
  
#### Action outputs

The **Create Insight** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Create Insight** action:
    
    
    {
        "InsightArn": "arn:aws:securityhub:ID",
    }
    

##### Output messages

The **Create Insight** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully created 'INSIGHT_NAME" insight in AWS Security Hub.` `Action wasn't able to create 'INSIGHT_NAME' insight.` | The action succeeded.  
`Error executing action "Create Insight". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Create Insight** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Insight Details

Use the **Get Insight Details** action to return detailed information about insights in AWS Security Hub.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Get Insight Details** action requires the following parameters:

Parameter | Description  
---|---  
`Insight ARN` | _Required_ The Amazon Resource Name (ARN) of the insight.  
`Max Results To Return` | _Required_ The number of results to return. The default value is 50.  
  
#### Action outputs

The **Get Insight Details** action provides the following outputs:

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

The **Get Insight Details** action can return the following table in Google SecOps:

Table name: **' NUMBER_OF_OBJECTS' Bucket Objects**

Columns:

  * **Name** (mapped as `GroupByAttributeValue`)
  * **Count** (mapped as `Count`)



##### JSON result

The following example shows the JSON result output received when using the **Get Insight Details** action:
    
    
    "InsightResults": {
            "InsightArn": "arn:aws:securityhub:ID",
            "GroupByAttribute": "ResourceId",
            "ResultValues": [
                {
                    "GroupByAttributeValue": "arn:aws:s3:::int-arcsight-v-27-0-getreportstatus",
                    "Count": 5
                },
                {
                    "GroupByAttributeValue": "arn:aws:s3:::int-arcsight-v-27-0-searchactionbug",
                    "Count": 5
                },
                {
                    "GroupByAttributeValue": "arn:aws:s3:::int-arcsight-v-27-0-unicodeandlogs",
                    "Count": 5
                },
                {
                    "GroupByAttributeValue": "arn:aws:s3:::int-automation-v-1-0",
                    "Count": 5
                },
                {
                    "GroupByAttributeValue": "arn:aws:s3:::int-awss3-v-1-0",
                    "Count": 5
                },
                {
                    "GroupByAttributeValue": "arn:aws:s3:::int-azureactivedirectory-v-4-0",
                    "Count": 5
                },
                {
                    "GroupByAttributeValue": "arn:aws:s3:::int-bootcamp-v-1-0",
                    "Count": 5
                },
                {
                    "GroupByAttributeValue": "arn:aws:s3:::int-categories",
                    "Count": 5
                }
            ]
        }
    

##### Output messages

The **Get Insight Details** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned details about Insight with ARN 'ARN' in AWS Security Hub.` | The action succeeded.  
`Error executing action "Get Insight Details". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Insight Details** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test the connectivity to AWS Security Hub.

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
`Successfully connected to the AWS Security Hub server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the AWS Security Hub! Error is ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Update Finding

Use the **Update Finding** action to update findings in AWS Security Hub.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Update Finding** action requires the following parameters:

Parameter | Description  
---|---  
`ID` | _Required_ The ID of the finding to update.  
`Product ARN` | _Required_ The product ARN of the finding to update.  
`Note` | _Optional_ A new text for the finding note.If you configure this parameter, also configure the `Note Author` parameter.  
`Note Author` | _Optional_ the author of the note.If you configure this parameter, also configure the `Note`parameter.  
`Severity` | _Optional_ A new severity for the finding. The possible values are as follows:

  * `Critical`
  * `High`
  * `Medium`
  * `Low`
  * `Informational`

  
`Verification State` | _Optional_ A new verification state for the finding. The possible values are as follows:

  * `Unknown`
  * `True Positive`
  * `False Positive`
  * `Benign Positive`

  
`Confidence` | _Optional_ A new confidence for the finding.The maximum value is 100.  
`Criticality` | _Optional_ A new criticality for the finding.The maximum value is 100.  
`Types` | _Optional_ A comma-separated list of types for the finding, such as `type1,type2`.  
`Workflow Status` | _Optional_ A new workflow status for the finding. The possible values are as follows:

  * `New`
  * `Notified`
  * `Resolved`
  * `Suppressed`

  
`Custom Fields` | _Optional_ The finding custom fields to update, such as `Custom_field_1:VALUE, Custom_field_2:VALUE`.  
  
#### Action outputs

The **Update Finding** action provides the following outputs:

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

The **Update Finding** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully updated finding with ID 'FINDING_ID' and Product ARN 'ARN' in AWS Security Hub.` `Action wasn't able to update finding with ID 'FINDING_ID' and Product ARN 'ARN' in AWS Security Hub.` | The action succeeded.  
`Error executing action "Update Findings". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Update Finding** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Update Insight

Use the **Update Insight** action to update an insight in AWS Security Hub.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Update Insight** action requires the following parameters:

Parameter | Description  
---|---  
`Insight ARN` | _Required_ The ARN of the insight.  
`Insight Name` | _Optional_ The name of the insight.  
`Group By Attribute` | _Optional_ The name of the attribute to group the findings by. The action groups the findings under one insight. The default value is `AWS Account ID`. The possible values are as follows:

  * `AWS Account ID`
  * `Company Name`
  * `Status`
  * `Generator ID`
  * `Malware Name`
  * `Process Name`
  * `Threat Intel Type`
  * `Product ARN`
  * `Product Name`
  * `Record State`
  * `EC2 Instance Image ID`
  * `EC2 Instance IPv4`
  * `EC2 Instance IPv6`
  * `EC2 Instance Key Name`
  * `EC2 Instance Subnet ID`
  * `EC2 Instance Type`
  * `EC2 Instance VPC ID`
  * `IAM Access Key User Name`
  * `S3 Bucket Owner Name`
  * `Container Image ID`
  * `Container Image Name`
  * `Container Name`
  * `Resource ID`
  * `Resource Type`
  * `Severity Label`
  * `Source URL`
  * `Type`
  * `Verification State`
  * `Workflow Status`

  
`Filter JSON Object` | _Optional_ A filter to apply to findings. The filter is a JSON object that lets you specify different attributes and values. For more details about the filter configuration, see Work with the Filter JSON Object parameter section of this document.  
  
#### Action outputs

The **Update Insight** action provides the following outputs:

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

The **Update Insight** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully updated 'INSIGHT_ARN' insight in AWS Security Hub` `Action wasn't able to update the 'INSIGHT_ARN' insight.` `` | The action succeeded.  
`Error executing action "Update Insight". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Update Insight** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
## Connectors

For more information about how to configure connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

### AWS Security Hub – Findings Connector

Use the **AWS Security Hub – Findings Connector** to retrieve findings from AWS Security Hub.

The connector requires the following parameters:

Parameters | Description  
---|---  
`Product Field Name` | _Required_ The name of the field where the product name is stored. The default value is `Product Name`.  
`Event Field Name` | _Required_ The field name used to determine the event name (subtype). The default value is `alertType`.  
`Environment Field Name` | _Optional_ The name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.The default value is `""`.  
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Script Timeout (Seconds)` | _Required_ The timeout limit for the Python process running the current script. the default value is 180.  
`AWS Access Key ID` | _Required_ The AWS access key ID to use in integration.  
`AWS Secret Key` | _Required_ The AWS secret key to use in the integration.  
`AWS Default Region` | _Required_ The AWS default region to use in the integration, such as `us-west-2`.  
`Lowest Severity To Fetch` | _Required_ The lowest severity of the findings to fetch.The possible values are as follows:

  * `Informational`
  * `Low`
  * `Medium`
  * `High`
  * `Critical`

The default value is `Medium`.  
`Fetch Max Hours Backwards` | _Optional_ The number of hours before the first connector iteration to retrieve the incidents from. This parameter applies only once to the initial connector iteration after you enable the connector for the first time.The default value is 1 hour.  
`Max Findings To Fetch` | _Optional_ The number of findings to process in a one connector iteration. The default value is 50.  
`Use whitelist as a blacklist` | _Required_ If selected, the connector uses the dynamic list as a blocklist. Not selected by default.  
`Verify SSL` | _Required_ If selected, Google SecOps verifies that the SSL certificate for the connection to the AWS Security Hub server is valid. Selected by default.  
`Proxy Server Address` | _Optional_ The address of the proxy server to use.  
`Proxy Username` | _Optional_ The proxy username to authenticate with.  
`Proxy Password` | _Optional_ The proxy password to authenticate with.  
  
#### Connector rules

The **AWS Security Hub – Findings Connector** supports proxies.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
