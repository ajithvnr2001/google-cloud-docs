---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/guardduty/
title: Collect AWS GuardDuty logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:37.976738+00:00
---

# Collect AWS GuardDuty logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/guardduty/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect AWS GuardDuty logs

**Parser Version:** 22.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes how you can collect AWS GuardDuty logs by setting up a Google Security Operations feed.

For more information, see [Data ingestion to Google Security Operations](https://docs.cloud.google.com/chronicle/docs/data-ingestion-flow).

An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the `GUARDDUTY` ingestion label.

## Before you begin

Ensure that you have the following prerequisites:

  * AWS S3 bucket is created. To create the AWS S3 bucket, see [Create your first S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html).
  * KMS key is created. To create the KMS key, see [Creating asymmetric KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/asymm-create-key.html).
  * AWS GuardDuty has permission to access the KMS key. To grant access to the KMS key, see [Exporting findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_exportfindings.html). GuardDuty encrypts the findings data in your bucket by using an AWS KMS key.



## Configure AWS GuardDuty

To configure AWS GuardDuty, do the following:

  1. Sign in to the AWS console.
  2. Search for **GuardDuty**.
  3. Select **Settings**.
  4. In the **Finding export option** section, do the following: 

     1. From the **Frequency for updated findings** list, select **Update CWE and S3 every 15 minutes**. The frequency selection is for the updated findings. The new findings are exported after 5 minutes from the time of creation.
     2. In the **S3 bucket** section, select the S3 bucket in which you want to export the GuardDuty findings.
     3. In the **Log file prefix** section, provide the log file prefix.
     4. In the **KMS encryption** section, select the KMS encryption.
     5. From the **Key alias** list, select the key.
     6. Click **Save**.
  5. After the log files are stored in the S3 bucket, create an SQS queue and attach it with the S3 bucket.




## Sample KMS policy

The following is a sample KMS policy:
    
    
    {
                "Sid": "Allow GuardDuty to encrypt findings",
                "Effect": "Allow",
                "Principal": {
                    "Service": "guardduty.AWS_REGION.amazonaws.com"
                },
                "Action": [
                    "kms:Encrypt",
                    "kms:GenerateDataKey"
                ],
                "Resource": "KEY_ARN"
            }
    
    

Replace the following:

  * AWS_REGION: the chosen region.
  * KEY_ARN: Amazon Resource Name (ARN) of the KMS key.



Check the required IAM user and KMS key policies for S3, SQS, and KMS.

Based on the service and region, identify the endpoints for connectivity by referring to the following AWS documentation:

  * For information about any logging sources, see [AWS Identity and Access Management endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/iam-service.html).
  * For information about S3 logging sources, see [Amazon Simple Storage Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/s3.html).
  * For information about SQS logging sources, see [Amazon Simple Queue Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/sqs-service.html).



## Set up feeds

To configure a feed, follow these steps:

  1. Go to **SIEM Settings** > **Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. Enter a unique name for the **Feed name**.
  5. Select **Amazon S3 V2** or **Amazon SQS V2** as the **Source type**.
  6. Select **AWS GuardDuty** as the **Log type**.
  7. Click **Next** and then click **Submit**.
  8. Google Security Operations supports log collection using an access key ID and secret method. To create the access key ID and secret, see [Configure tool authentication with AWS](https://docs.aws.amazon.com/powershell/latest/userguide/creds-idc.html).
  9. Based on the AWS GuardDuty configuration that you created, specify values for the following fields. 

     1. If using Amazon S3 V2
        * **S3 URI**
        * **Source deletion option**
        * **Maximum File Age**

     2. If using Amazon SQS V2
        * **Queue name**
        * **Account number**
        * **Queue access key ID**
        * **Queue secret access key**
        * **Source deletion option**
        * **Maximum File Age**
  10. Click **Next** and then click **Submit**.




For more information about Google Security Operations feeds, see [Google Security Operations feeds documentation](https://docs.cloud.google.com/chronicle/docs/administration/feed-management). For information about requirements for each feed type, see [Feed configuration by type](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api#feed_configuration_by_type). If you encounter issues when you create feeds, [contact Google Security Operations support](https://docs.cloud.google.com/chronicle/docs/getting-support)

## Field mapping reference

This parser code processes AWS GuardDuty findings in JSON format, extracting relevant fields and mapping them to a unified data model (UDM). It performs data transformations, including string replacements, merging arrays, and converting data types, to create a structured representation of the security event for analysis and correlation. 

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
accountId | principal.group.product_object_id | The AWS account ID associated with the finding.  
additionalInfo.portsScannedSample | event.idm.read_only_udm.about.port | List of ports scanned during a port sweep.  
additionalInfo.sample | security_result.about.labels.value | Indicates whether the finding is a sample finding.  
additionalInfo.threatListName | security_result.threat_feed_name | The name of the threat list that triggered the finding.  
additionalInfo.threatName | security_result.threat_name | The name of the threat that triggered the finding.  
additionalInfo.userAgent  
.fullUserAgent | network.http.user_agent | The full user agent string associated with the finding.  
additionalInfo.userAgent  
.userAgentCategory | security_result.detection_fields.value | The category of the user agent associated with the finding.  
arn | target.asset.attribute  
.cloud.project.product_object_id | The Amazon Resource Name (ARN) of the finding.  
detail.accountId | principal.group.product_object_id | The AWS account ID associated with the finding.  
detail.description | security_result.description | A detailed description of the finding.  
detail.id | target.asset.attribute.cloud.project.id | A unique ID for the finding.  
detail.resource.accessKeyDetails | principal.user | Details about the AWS access key involved in the finding.  
detail.resource.accessKeyDetails  
.accessKeyId | principal.user.userid | The ID of the AWS access key involved in the finding.  
detail.resource.accessKeyDetails  
.principalId | principal.user.userid | The principal ID of the AWS access key involved in the finding.  
detail.resource.accessKeyDetails  
.userType | principal.user.attribute.roles.name | The type of user associated with the AWS access key involved in the finding.  
detail.resource.accessKeyDetails  
.userName | principal.user.user_display_name | The name of the user associated with the AWS access key involved in the finding.  
detail.resource.s3BucketDetails  
.0.arn | target.resource.name | The ARN of the S3 bucket involved in the finding.  
detail.resource.s3BucketDetails  
.0.defaultServerSideEncryption.encryptionType | network.tls.client.supported_ciphers | The type of server-side encryption used for the S3 bucket involved in the finding.  
detail.resource.s3BucketDetails  
.0.name | target.resource.name | The name of the S3 bucket involved in the finding.  
detail.resource.s3BucketDetails  
.0.owner.id | target.resource.attribute.labels.value | The ID of the owner of the S3 bucket involved in the finding.  
detail.resource.s3BucketDetails  
.0.publicAccess.effectivePermission | target.resource.attribute.labels.value | The effective permission of the S3 bucket involved in the finding.  
detail.resource.s3BucketDetails  
.0.publicAccess.permissionConfiguration  
.accountLevelPermissions.blockPublicAccess  
.blockPublicAcls | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether public access blocks are enabled for the account.  
detail.resource.s3BucketDetails  
.0.publicAccess.permissionConfiguration  
.accountLevelPermissions.blockPublicAccess  
.blockPublicPolicy | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether public access blocks are enabled for the account.  
detail.resource.s3BucketDetails  
.0.publicAccess.permissionConfiguration  
.accountLevelPermissions.blockPublicAccess  
.ignorePublicAcls | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether public access blocks are enabled for the account.  
detail.resource.s3BucketDetails  
.0.publicAccess.permissionConfiguration  
.accountLevelPermissions.blockPublicAccess  
.restrictPublicBuckets | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether public access blocks are enabled for the account.  
detail.resource.s3BucketDetails  
.0.publicAccess.permissionConfiguration  
.bucketLevelPermissions.accessControlList  
.allowsPublicReadAccess | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether the access control list (ACL) allows public read access.  
detail.resource.s3BucketDetails  
.0.publicAccess.permissionConfiguration  
.bucketLevelPermissions.accessControlList  
.allowsPublicWriteAccess | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether the access control list (ACL) allows public write access.  
detail.resource.s3BucketDetails  
.0.publicAccess.permissionConfiguration  
.bucketLevelPermissions.blockPublicAccess  
.blockPublicAcls | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether public access blocks are enabled for the bucket.  
detail.resource.s3BucketDetails  
.0.publicAccess.permissionConfiguration  
.bucketLevelPermissions.blockPublicAccess  
.blockPublicPolicy | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether public access blocks are enabled for the bucket.  
detail.resource.s3BucketDetails  
.0.publicAccess.permissionConfiguration  
.bucketLevelPermissions.blockPublicAccess  
.ignorePublicAcls | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether public access blocks are enabled for the bucket.  
detail.resource.s3BucketDetails  
.0.publicAccess.permissionConfiguration  
.bucketLevelPermissions.blockPublicAccess  
.restrictPublicBuckets | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether public access blocks are enabled for the bucket.  
detail.resource.s3BucketDetails  
.0.publicAccess.permissionConfiguration  
.bucketLevelPermissions.bucketPolicy  
.allowsPublicReadAccess | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether the bucket policy allows public read access.  
detail.resource.s3BucketDetails  
.0.publicAccess.permissionConfiguration  
.bucketLevelPermissions.bucketPolicy  
.allowsPublicWriteAccess | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether the bucket policy allows public write access.  
detail.resource.s3BucketDetails  
.0.type | target.resource.attribute.labels.value | The type of S3 bucket involved in the finding.  
detail.service.action  
.actionType | principal.group.attribute.labels.value | The type of action associated with the finding.  
detail.service.action  
.awsApiCallAction.api | principal.application | The name of the AWS API call involved in the finding.  
detail.service.action  
.awsApiCallAction.callerType | principal.group.attribute.labels.value | The type of caller that made the AWS API call involved in the finding.  
detail.service.action  
.awsApiCallAction.domainDetails.domain | network.dns.questions.name | The domain name associated with the AWS API call involved in the finding.  
detail.service.action.awsApiCallAction  
.remoteIpDetails.country.countryName | target.location.country_or_region | The country name associated with the remote IP address that made the AWS API call involved in the finding.  
detail.service.action.awsApiCallAction  
.remoteIpDetails.geoLocation.lat | target.location.region_latitude | The latitude of the remote IP address that made the AWS API call involved in the finding.  
detail.service.action.awsApiCallAction  
.remoteIpDetails.geoLocation.lon | target.location.region_longitude | The longitude of the remote IP address that made the AWS API call involved in the finding.  
detail.service.action  
.awsApiCallAction.remoteIpDetails.ipAddressV4 | target.ip | The IP address that made the AWS API call involved in the finding.  
detail.service.action  
.awsApiCallAction.serviceName | metadata.description | The name of the AWS service involved in the finding.  
detail.service.action  
.dnsRequestAction.blocked | security_result.action | Whether the DNS request was blocked.  
detail.service.action  
.dnsRequestAction.domain | principal.administrative_domain | The domain name associated with the DNS request involved in the finding.  
detail.service.action  
.dnsRequestAction.protocol | network.ip_protocol | The protocol used for the DNS request involved in the finding.  
detail.service.action  
.networkConnectionAction.blocked | security_result.action | Whether the network connection was blocked.  
detail.service.action  
.networkConnectionAction.connectionDirection | network.direction | The direction of the network connection involved in the finding.  
detail.service.action  
.networkConnectionAction.localIpDetails  
.ipAddressV4 | principal.ip | The local IP address involved in the network connection.  
detail.service.action  
.networkConnectionAction.localPortDetails  
.port | principal.port | The local port involved in the network connection.  
detail.service.action  
.networkConnectionAction.localPortDetails  
.portName | principal.application | The name of the local port involved in the network connection.  
detail.service.action  
.networkConnectionAction.protocol | network.ip_protocol | The protocol used for the network connection involved in the finding.  
detail.service.action  
.networkConnectionAction.remoteIpDetails  
.city.cityName | target.location.city | The city name associated with the remote IP address involved in the network connection.  
detail.service.action  
.networkConnectionAction.remoteIpDetails  
.country.countryName | target.location.country_or_region | The country name associated with the remote IP address involved in the network connection.  
detail.service.action  
.networkConnectionAction.remoteIpDetails  
.ipAddressV4 | target.ip | The remote IP address involved in the network connection.  
detail.service.action  
.networkConnectionAction.remotePortDetails  
.port | target.port | The remote port involved in the network connection.  
detail.service.action  
.networkConnectionAction.remotePortDetails  
.portName | target.application | The name of the remote port involved in the network connection.  
detail.service.action  
.portProbeAction.blocked | security_result.action | Whether the port probe was blocked.  
detail.service.action  
.portProbeAction.portProbeDetails  
.0.localPortDetails.port | target.port | The local port that was probed.  
detail.service.action  
.portProbeAction.portProbeDetails  
.0.localPortDetails.portName | principal.application | The name of the local port that was probed.  
detail.service.action  
.portProbeAction.portProbeDetails  
.0.remoteIpDetails.city.cityName | target.location.city | The city name associated with the remote IP address that performed the port probe.  
detail.service.action  
.portProbeAction.portProbeDetails  
.0.remoteIpDetails.country.countryName | target.location.country_or_region | The country name associated with the remote IP address that performed the port probe.  
detail.service.action  
.portProbeAction.portProbeDetails  
.0.remoteIpDetails.geoLocation.lat | target.location.region_latitude | The latitude of the remote IP address that performed the port probe.  
detail.service.action  
.portProbeAction.portProbeDetails  
.0.remoteIpDetails.geoLocation.lon | target.location.region_longitude | The longitude of the remote IP address that performed the port probe.  
detail.service.action  
.portProbeAction.portProbeDetails  
.0.remoteIpDetails.ipAddressV4 | target.ip | The remote IP address that performed the port probe.  
detail.service.additionalInfo  
.threatListName | security_result.threat_feed_name | The name of the threat list that triggered the finding.  
detail.service.additionalInfo  
.threatName | security_result.threat_name | The name of the threat that triggered the finding.  
detail.service.additionalInfo  
.userAgent.fullUserAgent | network.http.user_agent | The full user agent string associated with the finding.  
detail.service.additionalInfo  
.userAgent.userAgentCategory | security_result.detection_fields.value | The category of the user agent associated with the finding.  
detail.service.additionalInfo  
.value | security_result.about  
.resource.attribute.labels.value | Additional information about the finding.  
detail.title | security_result.summary | A short title for the finding.  
detail.type | metadata.product_event_type | The type of finding.  
detail.updatedAt | metadata.event_timestamp | The time the finding was last updated.  
detail-type | event.idm.read_only_udm  
.additional.fields.value.string_value | The type of event that triggered the finding.  
partition | target.asset.attribute  
.cloud.project.type | The AWS partition that the finding occurred in.  
resource.accessKeyDetails | principal.user | Details about the AWS access key involved in the finding.  
resource.accessKeyDetails.accessKeyId | principal.user.userid | The ID of the AWS access key involved in the finding.  
resource.accessKeyDetails.principalId | principal.user.userid | The principal ID of the AWS access key involved in the finding.  
resource.accessKeyDetails.userType | principal.user.attribute.roles.name | The type of user associated with the AWS access key involved in the finding.  
resource.accessKeyDetails.userName | principal.user.user_display_name | The name of the user associated with the AWS access key involved in the finding.  
resource.instanceDetails.availabilityZone | target.asset.attribute.cloud.availability_zone | The availability zone of the EC2 instance involved in the finding.  
resource.instanceDetails.imageDescription | event.idm.read_only_udm  
.principal.resource.attribute.labels.value | The description of the AMI used to launch the EC2 instance involved in the finding.  
resource.instanceDetails.imageId | event.idm.read_only_udm  
.additional.fields.value.string_value | The ID of the AMI used to launch the EC2 instance involved in the finding.  
resource.instanceDetails  
.iamInstanceProfile.arn | target.resource.attribute.labels.value | The ARN of the IAM instance profile associated with the EC2 instance involved in the finding.  
resource.instanceDetails  
.iamInstanceProfile.id | target.resource.attribute.labels.value | The ID of the IAM instance profile associated with the EC2 instance involved in the finding.  
resource.instanceDetails.instanceId | target.resource.product_object_id | The ID of the EC2 instance involved in the finding.  
resource.instanceDetails.instanceState | target.resource.attribute.labels.value | The state of the EC2 instance involved in the finding.  
resource.instanceDetails.instanceType | target.resource.attribute.labels.value | The type of the EC2 instance involved in the finding.  
resource.instanceDetails  
.launchTime | target.resource.attribute.creation_time | The time the EC2 instance involved in the finding was launched.  
resource.instanceDetails  
.networkInterfaces.0.networkInterfaceId | target.resource.attribute.labels.value | The ID of the network interface associated with the EC2 instance involved in the finding.  
resource.instanceDetails  
.networkInterfaces.0.privateDnsName | target.resource.attribute.labels.value | The private DNS name of the network interface associated with the EC2 instance involved in the finding.  
resource.instanceDetails  
.networkInterfaces.0.publicDnsName | target.resource.attribute.labels.value | The public DNS name of the network interface associated with the EC2 instance involved in the finding.  
resource.instanceDetails  
.networkInterfaces.0.publicIp | principal.ip | The public IP address of the network interface associated with the EC2 instance involved in the finding.  
resource.instanceDetails  
.networkInterfaces.0.privateIpAddress | principal.ip | The private IP address of the network interface associated with the EC2 instance involved in the finding.  
resource.instanceDetails  
.networkInterfaces.0.securityGroups  
.0.groupId | target.user.group_identifiers | The ID of the security group associated with the network interface of the EC2 instance involved in the finding.  
resource.instanceDetails  
.networkInterfaces.0.securityGroups  
.0.groupName | target.user.group_identifiers | The name of the security group associated with the network interface of the EC2 instance involved in the finding.  
resource.instanceDetails  
.networkInterfaces.0.subnetId | target.resource.attribute.labels.value | The ID of the subnet associated with the network interface of the EC2 instance involved in the finding.  
resource.instanceDetails  
.networkInterfaces.0.vpcId | target.asset.attribute.cloud.vpc.id | The ID of the VPC associated with the network interface of the EC2 instance involved in the finding.  
resource.instanceDetails.outpostArn | target.resource.attribute.labels.value | The ARN of the outpost associated with the EC2 instance involved in the finding.  
resource.instanceDetails.platform | target.asset.platform_software.platform_version | The platform of the EC2 instance involved in the finding.  
resource.instanceDetails  
.productCodes.0.productCodeType | target.resource.type | The type of product code associated with the EC2 instance involved in the finding.  
resource.instanceDetails.tags | target.asset.attribute.labels | The tags associated with the EC2 instance involved in the finding.  
resource.kubernetesDetails  
.kubernetesUserDetails.username | principal.user.userid | The username of the Kubernetes user involved in the finding.  
resource.rdsDbInstanceDetails  
.dbClusterIdentifier | event.idm.read_only_udm  
.target.resource_ancestors.product_object_id | The identifier of the RDS DB cluster involved in the finding.  
resource.rdsDbInstanceDetails  
.dbInstanceArn | target.resource.name | The ARN of the RDS DB instance involved in the finding.  
resource.rdsDbInstanceDetails  
.dbInstanceIdentifier | target.resource.product_object_id | The identifier of the RDS DB instance involved in the finding.  
resource.rdsDbUserDetails.user | principal.user.userid | The username of the RDS DB user involved in the finding.  
resource.resourceType | target.resource.resource_subtype | The type of resource involved in the finding.  
resource.s3BucketDetails | principal.resource.attribute.labels | Details about the S3 bucket involved in the finding.  
resource.s3BucketDetails.0.arn | target.resource.name | The ARN of the S3 bucket involved in the finding.  
resource.s3BucketDetails.0.createdAt | event.idm.read_only_udm  
.principal.resource.attribute.labels.value | The time the S3 bucket involved in the finding was created.  
resource.s3BucketDetails.0  
.defaultServerSideEncryption.encryptionType | network.tls.client.supported_ciphers | The type of server-side encryption used for the S3 bucket involved in the finding.  
resource.s3BucketDetails.0.name | target.resource.name | The name of the S3 bucket involved in the finding.  
resource.s3BucketDetails.0.owner.id | target.resource.attribute.labels.value | The ID of the owner of the S3 bucket involved in the finding.  
resource.s3BucketDetails  
.0.publicAccess.effectivePermission | target.resource.attribute.labels.value | The effective permission of the S3 bucket involved in the finding.  
resource.s3BucketDetails  
.0.publicAccess.permissionConfiguration  
.accountLevelPermissions.blockPublicAccess  
.blockPublicAcls | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether public access blocks are enabled for the account.  
resource.s3BucketDetails  
.0.publicAccess.permissionConfiguration  
.accountLevelPermissions.blockPublicAccess  
.blockPublicPolicy | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether public access blocks are enabled for the account.  
resource.s3BucketDetails  
.0.publicAccess.permissionConfiguration  
.accountLevelPermissions.blockPublicAccess  
.ignorePublicAcls | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether public access blocks are enabled for the account.  
resource.s3BucketDetails  
.0.publicAccess.permissionConfiguration  
.accountLevelPermissions.blockPublicAccess  
.restrictPublicBuckets | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether public access blocks are enabled for the account.  
resource.s3BucketDetails  
.0.publicAccess.permissionConfiguration  
.bucketLevelPermissions.accessControlList  
.allowsPublicReadAccess | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether the access control list (ACL) allows public read access.  
resource.s3BucketDetails  
.0.publicAccess.permissionConfiguration  
.bucketLevelPermissions.accessControlList  
.allowsPublicWriteAccess | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether the access control list (ACL) allows public write access.  
resource.s3BucketDetails  
.0.publicAccess.permissionConfiguration  
.bucketLevelPermissions.blockPublicAccess  
.blockPublicAcls | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether public access blocks are enabled for the bucket.  
resource.s3BucketDetails  
.0.publicAccess.permissionConfiguration  
.bucketLevelPermissions.blockPublicAccess  
.blockPublicPolicy | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether public access blocks are enabled for the bucket.  
resource.s3BucketDetails  
.0.publicAccess.permissionConfiguration  
.bucketLevelPermissions.blockPublicAccess  
.ignorePublicAcls | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether public access blocks are enabled for the bucket.  
resource.s3BucketDetails  
.0.publicAccess.permissionConfiguration  
.bucketLevelPermissions.blockPublicAccess  
.restrictPublicBuckets | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether public access blocks are enabled for the bucket.  
resource.s3BucketDetails  
.0.publicAccess.permissionConfiguration  
.bucketLevelPermissions.bucketPolicy  
.allowsPublicReadAccess | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether the bucket policy allows public read access.  
resource.s3BucketDetails  
.0.publicAccess.permissionConfiguration  
.bucketLevelPermissions.bucketPolicy  
.allowsPublicWriteAccess | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether the bucket policy allows public write access.  
resource.s3BucketDetails.0.tags | event.idm.read_only_udm  
.principal.resource.attribute.labels | The tags associated with the S3 bucket involved in the finding.  
resource.s3BucketDetails.0.type | target.resource.attribute.labels.value | The type of S3 bucket involved in the finding.  
service.action  
.actionType | principal.group.attribute.labels.value | The type of action associated with the finding.  
service.action  
.awsApiCallAction.affectedResources  
.AWS_CloudTrail_Trail | event.idm.read_only_udm  
.principal.resource.attribute.labels.value | The name of the AWS CloudTrail trail involved in the finding.  
service.action  
.awsApiCallAction.affectedResources  
.AWS_S3_Bucket | event.idm.read_only_udm  
.principal.resource.attribute.labels.value | The name of the S3 bucket involved in the finding.  
service.action  
.awsApiCallAction.api | principal.application | The name of the AWS API call involved in the finding.  
service.action  
.awsApiCallAction.callerType | principal.group.attribute.labels.value | The type of caller that made the AWS API call involved in the finding.  
service.action  
.awsApiCallAction.domainDetails.domain | network.dns.questions.name | The domain name associated with the AWS API call involved in the finding.  
service.action  
.awsApiCallAction.errorCode | security_result.rule_type | The error code associated with the AWS API call involved in the finding.  
service.action  
.awsApiCallAction.remoteIpDetails  
.country.countryName | target.location.country_or_region | The country name associated with the remote IP address that made the AWS API call involved in the finding.  
service.action  
.awsApiCallAction.remoteIpDetails  
.geoLocation.lat | target.location.region_latitude | The latitude of the remote IP address that made the AWS API call involved in the finding.  
service.action  
.awsApiCallAction.remoteIpDetails  
.geoLocation.lon | target.location.region_longitude | The longitude of the remote IP address that made the AWS API call involved in the finding.  
service.action  
.awsApiCallAction.remoteIpDetails  
.ipAddressV4 | target.ip | The IP address that made the AWS API call involved in the finding.  
service.action  
.awsApiCallAction.remoteIpDetails  
.organization.asn | event.idm.read_only_udm  
.additional.fields.value.string_value | The Autonomous System Number (ASN) of the organization associated with the remote IP address that made the AWS API call involved in the finding.  
service.action  
.awsApiCallAction.remoteIpDetails  
.organization.asnOrg | event.idm.read_only_udm  
.additional.fields.value.string_value | The name of the organization associated with the remote IP address that made the AWS API call involved in the finding.  
service.action  
.awsApiCallAction.remoteIpDetails  
.organization.isp | event.idm.read_only_udm  
.additional.fields.value.string_value | The name of the internet service provider (ISP) associated with the remote IP address that made the AWS API call involved in the finding.  
service.action  
.awsApiCallAction.remoteIpDetails  
.organization.org | event.idm.read_only_udm  
.additional.fields.value.string_value | The name of the organization associated with the remote IP address that made the AWS API call involved in the finding.  
service.action  
.awsApiCallAction.serviceName | metadata.description | The name of the AWS service involved in the finding.  
service.action  
.dnsRequestAction.blocked | security_result.action | Whether the DNS request was blocked.  
service.action  
.dnsRequestAction.domain | principal.administrative_domain | The domain name associated with the DNS request involved in the finding.  
service.action  
.dnsRequestAction.protocol | network.ip_protocol | The protocol used for the DNS request involved in the finding.  
service.action  
.kubernetesApiCallAction.remoteIpDetails  
.country.countryName | target.location.country_or_region | The country name associated with the remote IP address that made the Kubernetes API call involved in the finding.  
service.action  
.kubernetesApiCallAction.remoteIpDetails  
.geoLocation.lat | target.location.region_latitude | The latitude of the remote IP address that made the Kubernetes API call involved in the finding.  
service.action  
.kubernetesApiCallAction.remoteIpDetails  
.geoLocation.lon | target.location.region_longitude | The longitude of the remote IP address that made the Kubernetes API call involved in the finding.  
service.action  
.kubernetesApiCallAction.remoteIpDetails  
.ipAddressV4 | target.ip | The IP address that made the Kubernetes API call involved in the finding.  
service.action  
.networkConnectionAction.blocked | security_result.action | Whether the network connection was blocked.  
service.action  
.networkConnectionAction.connectionDirection | network.direction | The direction of the network connection involved in the finding.  
service.action  
.networkConnectionAction.localIpDetails  
.ipAddressV4 | principal.ip | The local IP address involved in the network connection.  
service.action  
.networkConnectionAction.localPortDetails  
.port | principal.port | The local port involved in the network connection.  
service.action  
.networkConnectionAction.localPortDetails  
.portName | principal.application | The name of the local port involved in the network connection.  
service.action  
.networkConnectionAction.protocol | network.ip_protocol | The protocol used for the network connection involved in the finding.  
service.action  
.networkConnectionAction.remoteIpDetails  
.city.cityName | target.location.city | The city name associated with the remote IP address involved in the network connection.  
service.action  
.networkConnectionAction.remoteIpDetails  
.country.countryName | target.location.country_or_region | The country name associated with the remote IP address involved in the network connection.  
service.action  
.networkConnectionAction.remoteIpDetails  
.ipAddressV4 | target.ip | The remote IP address involved in the network connection.  
service.action  
.networkConnectionAction.remotePortDetails  
.port | target.port | The remote port involved in the network connection.  
service.action  
.networkConnectionAction.remotePortDetails  
.portName | target.application | The name of the remote port involved in the network connection.  
service.action  
.portProbeAction.blocked | security_result.action | Whether the port probe was blocked.  
service.action.portProbeAction  
.portProbeDetails  
.0.localPortDetails.port | target.port | The local port that was probed.  
service.action.portProbeAction  
.portProbeDetails  
.0.localPortDetails.portName | principal.application | The name of the local port that was probed.  
service.action.portProbeAction  
.portProbeDetails  
.0.remoteIpDetails.city  
.cityName | target.location.city | The city name associated with the remote IP address that performed the port probe.  
service.action.portProbeAction  
.portProbeDetails  
.0.remoteIpDetails.country  
.countryName | target.location.country_or_region | The country name associated with the remote IP address that performed the port probe.  
service.action.portProbeAction  
.portProbeDetails  
.0.remoteIpDetails.geoLocation  
.lat | target.location.region_latitude | The latitude of the remote IP address that performed the port probe.  
service.action.portProbeAction  
.portProbeDetails  
.0.remoteIpDetails.geoLocation  
.lon | target.location.region_longitude | The longitude of the remote IP address that performed the port probe.  
service.action.portProbeAction  
.portProbeDetails  
.0.remoteIpDetails.ipAddressV4 | target.ip | The remote IP address that performed the port probe.  
service.additionalInfo  
.portsScannedSample | event.idm.read_only_udm.about.port | A sample of the ports that were scanned.  
service.additionalInfo  
.recentCredentials | event.idm.read_only_udm.intermediary | A list of recent credentials that were used.  
service.additionalInfo.sample | security_result.about  
.labels.value | Indicates whether the finding is a sample finding.  
service.additionalInfo.threatListName | security_result.threat_feed_name | The name of the threat list that triggered the finding.  
service.additionalInfo.threatName | security_result.threat_name | The name of the threat that triggered the finding.  
service.additionalInfo  
.userAgent.fullUserAgent | network.http.user_agent | The full user agent string associated with the finding.  
service.additionalInfo  
.userAgent.userAgentCategory | security_result.detection_fields  
.value | The category of the user agent associated with the finding.  
service.additionalInfo.value | security_result.about  
.resource.attribute.labels.value | Additional information about the finding.  
service.archived | event.idm.read_only_udm  
.additional.fields.value.bool_value | Whether the finding is archived.  
service.count | event.idm.read_only_udm  
.principal.resource.attribute.labels.value | The number of times the event occurred.  
service.detectorId | event.idm.read_only_udm  
.additional.fields.value.string_value | The ID of the GuardDuty detector that generated the finding.  
service.ebsVolumeScanDetails  
.scanDetections  
.threatDetectedByName.itemCount |  | The total number of threats detected during the EBS volume scan.  
`detail.service.detection.sequence.uid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detail.service.detection.sequence.description` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detail.service.additionalInfo.type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.resourceUids` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.endpointIds` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.signalIndicators.values` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.uid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.description` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.createdAt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.updatedAt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.firstSeenAt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.lastSeenAt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.severity` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.count` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.domain` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.port` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource2.uid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource2.cloudPartition` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource2.data.ec2Instance.availabilityZone` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource2.data.ec2Instance.imageDescription` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource2.data.ec2Instance.instanceState` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource2.data.ec2Instance.instanceType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource2.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource2.accountId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource2.data.ec2Instance.ec2NetworkInterfaceUids` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`prodcode.productCodeId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`prodcode.productCodeType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource2.data.ec2Image.ec2InstanceUids` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource2.resourceType` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sequenceIndicator.values` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detail.createdAt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`detail.id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`detail.service.eventFirstSeen` | `event.idm.read_only_udm.principal.asset.first_discover_time` | Mapped from changelog  
`detail.service.eventLastSeen` | `event.idm.read_only_udm.principal.asset.last_discover_time` | Mapped from changelog  
`data.location` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`data.autonomousSystem` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`detail.associatedAttackSequenceArn` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Record.requestParameters.bucketName` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`Record.additionalEventData.bytesTransferredIn` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`Record.additionalEventData.bytesTransferredOut` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`Record.userIdentity.userName` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`Record.userIdentity.accountId` | `event.idm.read_only_udm.principal.user.group_identifiers` | Mapped from changelog  
`Record_eventName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Record.requestParameters.encoding-type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Record.requestParameters.delimiter` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Record.additionalEventData.SignatureVersion` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Record.additionalEventData.x-amz-id-2` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Record.requestParameters.prefix` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`resource` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`Record.recipientAccountId` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`Record.additionalEventData.AuthenticationMethod` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`awsAccountId` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`digestS3Object` | `event.idm.read_only_udm.target.file.full_path` | Mapped from changelog  
`digestS3Bucket` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`digestPublicKeyFingerprint` | `event.idm.read_only_udm.target.artifact.last_https_certificate.thumbprint_sha256` | Mapped from changelog  
`digestSignatureAlgorithm` | `event.idm.read_only_udm.target.artifact.last_https_certificate.cert_signature.signature_algorithm` | Mapped from changelog  
`previousDigestHashValue` | `event.idm.read_only_udm.target.file.sha256` | Mapped from changelog  
`newestEventTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`oldestEventTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`previousDigestHashAlgorithm` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`previousDigestS3Bucket` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`previousDigestS3Object` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`actor_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resources_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resources_accountId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sequenceIndicator.key` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`image` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`imageUid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`createdAt` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`containerUids` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`actors_path` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`actors_sha256` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`associatedAttackSequenceArn` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`updatedAt` | `event.idm.read_only_udm.metadata.collected_timestamp` | Mapped from changelog  
`resources_region` | `event.idm.read_only_udm.security_result.about.location.name` | Mapped from changelog  
`actors_name` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`INBOUND` | `event.idm.read_only_udm.network.direction` | Mapped from changelog  
`status` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`vpcId` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`namespace` | `event.idm.read_only_udm.principal.namespace` | Mapped from changelog  
`remoteIpDetails_ipAddressV4` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`remoteIpDetails_city_cityName` | `event.idm.read_only_udm.principal.location.city` | Mapped from changelog  
`remoteIPDetails_geoLocation_lat` | `event.idm.read_only_udm.principal.location.region_latitude` | Mapped from changelog  
`remoteIPDetails_geoLocation_lon` | `event.idm.read_only_udm.principal.location.region_longitude` | Mapped from changelog  
`remoteIPDetails_organization_asn` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`remoteIPDetails_organization_isp` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`remoteIPDetails_organization_asnOrg` | `event.idm.read_only_udm.principal.network.organization_name` | Mapped from changelog  
`remoteIPDetails_organization_org` | `event.idm.read_only_udm.target.administrative_domain` | Mapped from changelog  
`kubernetesApiCallAction_requestUri` | `event.idm.read_only_udm.principal.url` | Mapped from changelog  
`kubernetesApiCallAction_statusCode` | `event.idm.read_only_udm.network.http.response_code` | Mapped from changelog  
`kubernetesApiCallAction_userAgent` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`kubernetesApiCallAction_userAgentOrg` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`unmapped_username` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`resource_uid` | `event.idm.read_only_udm.principal.resource.id` | Mapped from changelog  
`remoteIpDetails_ipAddressV4` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`resource.kubernetesDetails.kubernetesWorkloadDetails.namespace` | `event.idm.read_only_udm.target.namespace` | Mapped from changelog  
`resource.kubernetesDetails.kubernetesWorkloadDetails.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.kubernetesDetails.kubernetesWorkloadDetails.uid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.kubernetesDetails.kubernetesWorkloadDetails.type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.kubernetesDetails.kubernetesWorkloadDetails.serviceAccountName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.kubernetesDetails.kubernetesUserDetails.uid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`service.action.kubernetesApiCallAction.sourceIPs` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`service.runtimeDetails.process.lineage.executablePath` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`service.runtimeDetails.process.lineage.name` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`service.runtimeDetails.process.lineage.namespacePid` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`service.runtimeDetails.process.lineage.userId` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`service.runtimeDetails.process.lineage.uuid` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`service.runtimeDetails.process.lineage.euid` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`service.runtimeDetails.process.lineage.parentUuid` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`service.runtimeDetails.process.namespacePid` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`service.detectorId` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`service.runtimeDetails.process.lineage.startTime` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`service.runtimeDetails.process.euid` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`service.runtimeDetails.process.executableSha256` | `event.idm.read_only_udm.target.file.sha256` | Mapped from changelog  
`service.runtimeDetails.process.name` | `event.idm.read_only_udm.target.process.file.names` | Mapped from changelog  
`service.runtimeDetails.process.executablePath` | `event.idm.read_only_udm.target.process.file.full_path` | Mapped from changelog  
`service.runtimeDetails.process.pid` | `event.idm.read_only_udm.target.process.pid` | Mapped from changelog  
`service.runtimeDetails.process.uuid` | `event.idm.read_only_udm.target.process.product_specific_process_id` | Mapped from changelog  
`service.runtimeDetails.process.parentUuid` | `event.idm.read_only_udm.target.process.parent_process.product_specific_process_id` | Mapped from changelog  
`service.runtimeDetails.process.user` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`service.runtimeDetails.process.startTime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`service.runtimeDetails.process.pwd` | `event.idm.read_only_udm.target.file.full_path` | Mapped from changelog  
`service.runtimeDetails.process.userId` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`service.runtimeDetails.process.lineage.pid` | `event.idm.read_only_udm.target.process.parent_process.pid` | Mapped from changelog  
`detail.resource.kubernetesDetails.kubernetesUserDetails.username` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`"service.detection.sequence.signals"` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`"service.detection.sequence.actors"` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`"service.detection.sequence.endpoints"` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`"service.detection.sequence.resources"` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`"service.featureName"` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`"service.detectorId"` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`"service.resourceRole"` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`and "service.serviceName"` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`"service.detection.sequence.endpoints.ip"` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`"service.detection.sequence.actors.user"` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`"schemaVersion"` | `event.idm.read_only_udm.security_result.rule_version` | Mapped from changelog  
`service.eventFirstSeen` | `event.idm.read_only_udm.principal.asset.first_discover_time` | Mapped from changelog  
`service.eventLastSeen` | `event.idm.read_only_udm.principal.asset.last_discover_time` | Mapped from changelog  
`service.additionalInfo.value` | `security_result.about.resource.attribute.labels` | Mapped from changelog  
`service.additionalInfo.unusualBehavior" and "service.additionalInfo.profiledBehavior` | `security_result.about.resource.attribute.labels` | Mapped from changelog  
`resource.eksClusterDetails.status", "resource.kubernetesDetails.kubernetesUserDetails.impersonatedUser", "resource.kubernetesDetails.kubernetesUserDetails.groups", "resource.kubernetesDetails.kubernetesUserDetails.sessionName", "service.action.kubernetesApiCallAction.verb", "service.detection.anomaly.profiles.namespace.asnInfo", "service.detection.anomaly.profiles.namespace.userAgent", "service.detection.anomaly.profiles.namespace.dayOfWeek", "service.detection.anomaly.profiles.namespace.impersonatedUsername", "service.detection.anomaly.profiles.namespace.api", "service.detection.anomaly.profiles.namespace.username", "service.detection.anomaly.profiles.cluster.asnInfo", "service.detection.anomaly.profiles.cluster.userAgent", "service.detection.anomaly.profiles.cluster.dayOfWeek", "service.detection.anomaly.profiles.cluster.impersonatedUsername", "service.detection.anomaly.profiles.cluster.api", "service.detection.anomaly.profiles.cluster.username", "service.detection.anomaly.profiles.account.asnInfo", "service.detection.anomaly.profiles.account.userAgent", "service.detection.anomaly.profiles.account.dayOfWeek", "service.detection.anomaly.profiles.account.impersonatedUsername", "service.detection.anomaly.profiles.account.api", "service.detection.anomaly.profiles.account.username", "service.detection.anomaly.profiles.username.asnInfo", "service.detection.anomaly.profiles.username.userAgent", "service.detection.anomaly.profiles.username.dayOfWeek", "service.detection.anomaly.profiles.username.impersonatedUsername", "service.detection.anomaly.profiles.username.api", "service.detection.anomaly.profiles.username.username", "service.detection.anomaly.unusual.behavior.namespace.asnInfo", "service.detection.anomaly.unusual.behavior.namespace.userAgent", "service.detection.anomaly.unusual.behavior.namespace.dayOfWeek", "service.detection.anomaly.unusual.behavior.namespace.impersonatedUsername", "service.detection.anomaly.unusual.behavior.namespace.api", "service.detection.anomaly.unusual.behavior.namespace.username", "service.detection.anomaly.unusual.behavior.cluster.asnInfo", "service.detection.anomaly.unusual.behavior.cluster.userAgent", "service.detection.anomaly.unusual.behavior.cluster.dayOfWeek", "service.detection.anomaly.unusual.behavior.cluster.impersonatedUsername", "service.detection.anomaly.unusual.behavior.cluster.api", "service.detection.anomaly.unusual.behavior.cluster.username", "service.detection.anomaly.unusual.behavior.account.asnInfo", "service.detection.anomaly.unusual.behavior.account.userAgent", "service.detection.anomaly.unusual.behavior.account.dayOfWeek", "service.detection.anomaly.unusual.behavior.account.impersonatedUsername", "service.detection.anomaly.unusual.behavior.account.api", "service.detection.anomaly.unusual.behavior.account.username", "service.detection.anomaly.unusual.behavior.username.asnInfo", "service.detection.anomaly.unusual.behavior.username.userAgent", "service.detection.anomaly.unusual.behavior.username.dayOfWeek", "service.detection.anomaly.unusual.behavior.username.impersonatedUsername", "service.detection.anomaly.unusual.behavior.username.api", and "service.detection.anomaly.unusual.behavior.username.username` | `additional.fields` | Mapped from changelog  
`service.action.kubernetesApiCallAction.statusCode` | `network.http.response_code` | Mapped from changelog  
`resource.eksClusterDetails.vpcId` | `principal.cloud.vpc.id` | Mapped from changelog  
`service.action.kubernetesApiCallAction.namespace` | `principal.namespace` | Mapped from changelog  
`service.action.kubernetesApiCallAction.requestUri` | `target.url` | Mapped from changelog  
`service.action.awsApiCallAction.domainDetails.domain` | `network.dns.questions.name` | Mapped from changelog  
`service.action.awsApiCallAction.affectedResources.AWS_CloudTrail_Trail` | `principal.resource.attribute.labels` | Mapped from changelog  
`resource.eksClusterDetails.createdAt` | `target.resource.attribute.labels` | Mapped from changelog  
`resource.s3BucketDetails.createdAt` | `principal.resource.attribute.labels` | Mapped from changelog  
`resource.eksClusterDetails.tags` | `target.resource.attribute.labels` | Mapped from changelog  
`resource.s3BucketDetails.tags` | `principal.resource.attribute.labels` | Mapped from changelog  
`threatdetails.threatListName` | `security_result.threat_feed_name` | Mapped from changelog  
`T1071` | `technique_label.value` | Mapped from changelog  
`T1078` | `technique_label.value` | Mapped from changelog  
`T1087` | `technique_label.value` | Mapped from changelog  
`T1098` | `technique_label.value` | Mapped from changelog  
`T1110` | `technique_label.value` | Mapped from changelog  
`T1133` | `technique_label.value` | Mapped from changelog  
`T1189` | `technique_label.value` | Mapped from changelog  
`T1484` | `technique_label.value` | Mapped from changelog  
`T1496` | `technique_label.value` | Mapped from changelog  
`T1498` | `technique_label.value` | Mapped from changelog  
`T1526` | `technique_label.value` | Mapped from changelog  
`T1538` | `technique_label.value` | Mapped from changelog  
`T1552` | `technique_label.value` | Mapped from changelog  
`T1555` | `technique_label.value` | Mapped from changelog  
`T1562` | `technique_label.value` | Mapped from changelog  
`T1565` | `technique_label.value` | Mapped from changelog  
`T1566` | `technique_label.value` | Mapped from changelog  
`T1567` | `technique_label.value` | Mapped from changelog  
`T1568` | `technique_label.value` | Mapped from changelog  
`T1589` | `technique_label.value` | Mapped from changelog  
`T1595` | `technique_label.value` | Mapped from changelog  
`Reconnaissance` | `tatic_label.value` | Mapped from changelog  
`ResourceDevelopment` | `tatic_label.value` | Mapped from changelog  
`InitialAccess` | `tatic_label.value` | Mapped from changelog  
`Execution` | `tatic_label.value` | Mapped from changelog  
`Persistence` | `tatic_label.value` | Mapped from changelog  
`PrivilegeEscalation` | `tatic_label.value` | Mapped from changelog  
`DefenseEvasion` | `tatic_label.value` | Mapped from changelog  
`CredentialAccess` | `tatic_label.value` | Mapped from changelog  
`Discovery` | `tatic_label.value` | Mapped from changelog  
`LateralMovement` | `tatic_label.value` | Mapped from changelog  
`Collection` | `tatic_label.value` | Mapped from changelog  
`CommandAndControl` | `tatic_label.value` | Mapped from changelog  
`Exfiltration` | `tatic_label.value` | Mapped from changelog  
`Impact` | `tatic_label.value` | Mapped from changelog  
`service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.hash` | `principal.file.sha256` | Mapped from changelog  
`service.ebsVolumeScanDetails.scanDetections.threatDetectedByName.threatNames.filePaths.filePath` | `principal.file.full_path` | Mapped from changelog  
`service.action.dnsRequestAction.domain` | `network.dns.questions.name` | Mapped from changelog  
`resource.kubernetesDetails.kubernetesUserDetails.username` | `principal.user.userid` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/guardduty-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
