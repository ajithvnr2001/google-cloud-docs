---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/aws-elastic-compute-cloud-ec2/
title: Integrate Amazon EC2 with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:16:51.723439+00:00
---

# Integrate Amazon EC2 with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/aws-elastic-compute-cloud-ec2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Amazon EC2 with Google SecOps

This document describes how to integrate AWS Elastic Compute Cloud (Amazon EC2) with Google Security Operations.

## Use cases

  1. **Secure the Amazon Elastic Compute Cloud (Amazon EC2) instances**

     1. Create security groups to restrict inbound and outbound internet access to Amazon EC2.
     2. Allocate a new Elastic IP address
     3. Associate a new Elastic IP address
  2. **Resource management - use instance custom tags to track and identify AWS resources.**




## Before you begin

Before you configure the AWS Elastic Compute Cloud (EC2) integration in Google SecOps, verify that your network environment and AWS credentials satisfy all operational prerequisites.

To prepare your environment for integration, make sure you complete the following:

  1. Verify network line-of-sight between Google SecOps and AWS EC2 regional service endpoints.

  2. Obtain AWS programmatic API credentials (an Access Key ID and Secret Access Key) with appropriate IAM permissions.

  3. Configure and test the integration instance within Google SecOps.




### Network requirements

Google SecOps communicates directly with the AWS EC2 service using HTTPS REST APIs and the AWS Python SDK (`boto3`).

Make sure your network environment meets the following connectivity rules:

  * **Outbound HTTPS access** : Enable outbound HTTPS communication from your Google SecOps instance or Remote Agent to the AWS EC2 regional endpoint (`ec2.<region>.amazonaws.com`) over port `443/TCP`.

For more information, see [AWS Service Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) in AWS documentation.

  * **Proxy configuration** : If your organization routes outbound traffic through an HTTP/HTTPS proxy, configure standard environment proxy variables (`HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY`) on the Google SecOps server or Remote Agent host.




### Authentication and credentials

The AWS EC2 integration requires programmatic API credentials to authenticate requests using AWS Signature Version 4.

Make sure your AWS environment satisfies the following authentication requirements:

  * **Programmatic credentials** : Obtain a valid AWS Access Key ID and AWS Secret Key associated with an AWS IAM user or role.

For information on creating IAM identities and generating credentials, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) and [IAM Identities](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) in AWS documentation.

  * **Least privilege** : Restrict permissions to only the actions and compute resources required for your automated workflows, and rotate credentials periodically.

For details on security recommendations, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in AWS documentation.




### Configure action permissions

Grant the authenticating AWS IAM identity the specific permissions required for the actions your Google SecOps playbooks execute.

**Important:** Several AWS EC2 actions in Google SecOps execute an internal connectivity check during initialization that calls `ec2:DescribeRegions`. Make sure that **`ec2:DescribeRegions`** is granted to prevent action initialization errors.

Refer to the minimal permissions for **AWS Elastic Compute Cloud (EC2)** actions in the following table:

Action Name | Required AWS IAM Permission (`ActionName:Permission`) | Prerequisite Permission | Description / Resource Scope  
---|---|---|---  
**Authorize Security Group Egress** | `ec2:AuthorizeSecurityGroupEgress` | `ec2:DescribeRegions` | Adds outbound rules to an EC2 security group. Resource: target security group ARN.  
**Authorize Security Group Ingress** | `ec2:AuthorizeSecurityGroupIngress` | `ec2:DescribeRegions` | Adds inbound rules to an EC2 security group. Resource: target security group ARN.  
**Create Tags** | `ec2:CreateTags` | `ec2:DescribeRegions` | Adds or overwrites tags on EC2 resources. Resource: target EC2 resource ARN.  
**List Instances** | `ec2:DescribeInstances` | `ec2:DescribeRegions` | Retrieves status and metadata for EC2 instances. Resource: `*`.  
**List Security Groups** | `ec2:DescribeSecurityGroups` | — | Retrieves security group configurations and rules. Resource: `*`.  
**Ping** | `ec2:DescribeRegions` | — | Validates integration connectivity. Resource: `*`.  
**Revoke Security Group Egress** | `ec2:RevokeSecurityGroupEgress` | `ec2:DescribeRegions` | Removes outbound rules from an EC2 security group. Resource: target security group ARN.  
**Revoke Security Group Ingress** | `ec2:RevokeSecurityGroupIngress` | `ec2:DescribeRegions` | Removes inbound rules from an EC2 security group. Resource: target security group ARN.  
**Start Instance** | `ec2:StartInstances` | — | Starts stopped EC2 instances. Resource: target EC2 instance ARN.  
**Stop Instance** | `ec2:StopInstances` | — | Stops running EC2 instances. Resource: target EC2 instance ARN.  
**Take Snapshot** | `ec2:CreateSnapshots` | `ec2:DescribeRegions` | Creates point-in-time EBS snapshots for instance volumes. Resource: instance and volume ARNs.  
**Terminate Instance** | `ec2:TerminateInstances` | — | Shuts down and terminates EC2 instances. Resource: target EC2 instance ARN.  
  
#### Quick reference (`ActionName:Permission`)

Use the following quick reference to review the required permissions for each action:
    
    
    Ping: ec2:DescribeRegions
    Authorize Security Group Egress: ec2:AuthorizeSecurityGroupEgress, ec2:DescribeRegions
    Authorize Security Group Ingress: ec2:AuthorizeSecurityGroupIngress, ec2:DescribeRegions
    Create Tags: ec2:CreateTags, ec2:DescribeRegions
    List Instances: ec2:DescribeInstances, ec2:DescribeRegions
    List Security Groups: ec2:DescribeSecurityGroups
    Revoke Security Group Egress: ec2:RevokeSecurityGroupEgress, ec2:DescribeRegions
    Revoke Security Group Ingress: ec2:RevokeSecurityGroupIngress, ec2:DescribeRegions
    Start Instance: ec2:StartInstances
    Stop Instance: ec2:StopInstances
    Take Snapshot: ec2:CreateSnapshots, ec2:DescribeRegions
    Terminate Instance: ec2:TerminateInstances
    

### Sample IAM policy (least privilege)

The following example policy demonstrates the permissions required to run all AWS EC2 actions in Google SecOps.

For instructions on creating and attaching IAM policies, see [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in AWS documentation.
    
    
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "SecOpsEC2Discovery",
          "Effect": "Allow",
          "Action": [
            "ec2:DescribeRegions",
            "ec2:DescribeInstances",
            "ec2:DescribeSecurityGroups"
          ],
          "Resource": "*"
        },
        {
          "Sid": "SecOpsEC2InstanceRemediation",
          "Effect": "Allow",
          "Action": [
            "ec2:StartInstances",
            "ec2:StopInstances",
            "ec2:TerminateInstances",
            "ec2:CreateTags",
            "ec2:CreateSnapshots"
          ],
          "Resource": "*"
        },
        {
          "Sid": "SecOpsEC2SecurityGroupManagement",
          "Effect": "Allow",
          "Action": [
            "ec2:AuthorizeSecurityGroupIngress",
            "ec2:RevokeSecurityGroupIngress",
            "ec2:AuthorizeSecurityGroupEgress",
            "ec2:RevokeSecurityGroupEgress"
          ],
          "Resource": "arn:aws:ec2:*:*:security-group/*"
        }
      ]
    }
    

## Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
AWS Access Key ID | String | N/A | Yes | AWS Access Key ID to use in integration.  
AWS Secret Key | Password | N/A | Yes | AWS Secret Key to use in integration.  
AWS Default Region | String | N/A | Yes | AWS default region to use in integration, for example us-west-2.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Authorize Security Group Egress

Adds the specified egress rule to a security group for use with a VPC. An outbound rule permits instances to send traffic to the specified IPv4 or IPv6 CIDR address ranges. Rule changes are propagated to affected instances as quickly as possible. However, a small delay might occur.

For more information about VPC security group limits, see [Amazon VPC Limits](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html).

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Security Group IDs | String | N/A | Yes | One or more security group IDs. Separated by comma. Note for dev: every ID in a separate request  
IP Protocol | DDL | all | No | The IP protocol name. Use 'all' to specify all protocols. Specifying 'all' allows traffic on all ports, regardless of any port range you specify. Possible values: tcp , udp , icmp, all Note for dev: 'all' equals -1 from code  
From Port | Integer |  | No | The start of port range for the TCP and UDP protocols, or an ICMP type number.  
To Port | Integer |  | No | The end of port range for the TCP and UDP protocols allows traffic on all ports, regardless of any port range you specify.  
IP Ranges - CidrIP | String | N/A | No | The IPv4 CIDR range. To specify a single IPv4 address, use the /32 prefix length.  
IPv6 Ranges - CidrIP | String | N/A | No | The IPv6 CIDR range. To specify a single IPv6 address, use the /128 prefix length.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **if successfully added the specified egress rules to at least one (or all) security groups: (is_success = true):** "Successfully added the specified egress rule to the following security groups: {group_ids}" **if failed to add the specified egress rules because of permissions rule error (invalid port,etc): (is_success = false):** "Failed to add the specified egress rule to the following security groups: {group_ids}. Reason: Invalid IP Permissions set. For more details please check the logs." **if failed to add the specified egress rules because of invalid security group id: (is_success = false):** "Failed to add the specified egress rule to the following security groups: {group_ids}. Reason: Invalid Security Group ID was provided. For more details please check the logs.`` **If failed to add the specified egress rules to all groups: is_success=false** **The action should fail and stop a playbook execution:** **if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Authorize Security Group Egress". Reason: {0}''.format(error.Stacktrace) | General  
  
### Authorize Security Group Ingress

Adds the specified ingress rule to a security group. An inbound rule permits instances to receive traffic from the specified IPv4 or IPv6 CIDR address ranges. Rule changes are propagated to affected instances as quickly as possible. However, a small delay might occur.

For more information about VPC security group limits, see [Amazon VPC Limits](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html).

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Security Group IDs | String | N/A | Yes | One or more security group IDs. Separated by comma. Note for dev: every ID in a separate request  
IP Protocol | DDL | all | No | The IP protocol name. Use 'all' to specify all protocols. Specifying 'all' allows traffic on all ports, regardless of any port range you specify. Possible values: tcp , udp , icmp, all Note for dev: 'all' equals -1 from code  
From Port | Integer |  | No | The start of port range for the TCP and UDP protocols, or an ICMP type number.  
To Port | Integer |  | No | The end of port range for the TCP and UDP protocols allows traffic on all ports, regardless of any port range you specify.  
IP Ranges - CidrIP | String | N/A | No | The IPv4 address in CIDR format. To specify a single IPv4 address, use the /32 prefix length.  
IPv6 Ranges - CidrIP | String | N/A | No | The IPv6 CIDR range. To specify a single IPv6 address, use the /128 prefix length.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **if successfully added the specified ingress rules to at least one security groups: (if all were successfully updated - is_success = true):** "Successfully added the specified ingress rule to the following security groups: {group_ids}" **if failed to add the specified ingress rules because of permissions rule error (invalid port,etc): (is_success =false):** "Failed to add the specified ingress rule to the following security groups: {group_ids}. Reason: Invalid IP Permissions set. For more details please check the logs." **if failed to add the specified ingress rules because of invalid security group id: (is_success =false):** "Failed to add the specified ingress rule to the following security groups: {group_ids}. Reason: Invalid Security Group ID was provided. For more details please check the logs.`` **The action should fail and stop a playbook execution:** **if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Authorize Security Group Ingress". Reason: {0}''.format(error.Stacktrace) | General  
  
### Create Tags

A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your AWS costs. Adds or overwrites only the specified tags for the specified Amazon EC2 resource or resources. When you specify an existing tag key, the value is overwritten with the new value. Each resource can have a maximum of 50 tags. Tag keys must be unique per resource.

For more information about tags, see [Tagging Your Resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the Amazon Elastic Compute Cloud User Guide.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Resource IDs | String | N/A | Yes | One or more resource IDs. Separated by comma.  
Tags | String | N/A | Yes | The key-value combination of a tag to be assigned to the resource. For example, to add to all specified resources a tag with the key `Owner` and the value `TeamA`, specify `Owner:TeamA`. You can specify multiple key-value combinations by separating them with commas.You can add or overwrite the specified tags. The tag keys must be unique per resource.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **if successful:** "Successfully added {tags_list} tags to the following resources: "resource_ids" **For invalid resource ids (is_success = false):** "Failed to add {tag_list} tags to the following resources: {resource_ids}. Reason: Invalid resource ID **If resource has more than 50 tags (is_success = false):** "Failed to add {tag_list} tags to the following resources: {resource_ids}. Reason: resource can have a maximum of 50 tags. **If tag key is not unique: (is_success = false):** "Failed to add {tag_list} tags to the following resources: {resource_ids}. Reason: Tag keys must be unique per resource. **If the given tag is in invalid format (meaning only key or only value without the full structure of key:value) (is_success = false):** "Failed to add {invalid_tags} tags to the following resources: {ids}. Reason: Invalid format. Tag should include key and value. **The action should fail and stop a playbook execution:** **if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Create Tags". Reason: {0}''.format(error.Stacktrace) | General  
  
### List Instances

Describes the specified instances or all instances.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance IDs | String | N/A | No | One or more instance IDs. specify instance IDs, the output includes information for only the specified instances. This parameter cannot be used with the parameter 'Max Results'. 'Instance IDs' has priority over the 'Max Result' parameter.  
Tag Filters | String | N/A | No | The key/value combination of a tag assigned to the resource. For example, to find all resources that have a tag with the key Owner and the value TeamA, specify Owner:TeamA. Comma separated tag filters. Example: Name:Name1,Owner:TeamA. Returned instances will be fit to all filters.  
Max Results | Integer | 50 | No | Specify how many instances to return. Default is 50. Maximum is 1000. The parameter 'Instance IDs' cannot be used with the parameter 'Max Results'. 'Instance IDs' has priority over the 'Max Result' parameter.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    "EC2_Instances": [
        {
       "AmiLaunchIndex":0,
       "ImageId":"ami-047a51fa27710816e",
       "InstanceId":"i-044c08c5bfe1a7f98",
       "InstanceType":"t2.micro",
       "KeyName":"\"Key\": \"Test\", \"Value\":\"Test\"",
       "LaunchTime":"2021-1-30",
       "Monitoring":{
          "State":"disabled"
       },
       "Placement":{
          "AvailabilityZone":"us-east-1d",
          "GroupName":"",
          "Tenancy":"default"
       },
       "PrivateDnsName":"ip-192-0-2-220.ec2.internal",
       "PrivateIpAddress":"192.0.2.220",
       "ProductCodes":[
    
       ],
       "PublicDnsName":"ec2-192-0-2-218.compute-1.amazonaws.com",
       "PublicIpAddress":"192.0.2.218",
       "State":{
          "Code":16,
          "Name":"running"
       },
       "StateTransitionReason":"",
       "SubnetId":"subnet-1b1fda3a",
       "VpcId":"vpc-ID",
       "Architecture":"x86_64",
       "BlockDeviceMappings":[
          {
             "DeviceName":"/dev/xvda",
             "Ebs":{
                "AttachTime":"2021-1-30",
                "DeleteOnTermination":true,
                "Status":"attached",
                "VolumeId":"vol-00f70681a43e5d86e"
             }
          }
       ],
       "ClientToken":"",
       "EbsOptimized":false,
       "EnaSupport":true,
       "Hypervisor":"xen",
       "NetworkInterfaces":[
          {
             "Association":{
                "IpOwnerId":"amazon",
                "PublicDnsName":"ec2-192-0-2-218.compute-1.amazonaws.com",
                "PublicIp":"192.0.2.218"
             },
             "Attachment":{
                "AttachTime":"",
                "AttachmentId":"eni-attach-06bc5e5901ce99ef2",
                "DeleteOnTermination":true,
                "DeviceIndex":0,
                "Status":"attached",
                "NetworkCardIndex":0
             },
             "Description":"",
             "Groups":[
                {
                   "GroupName":"launch-wizard-2",
                   "GroupId":"sg-001700ccddac4189a"
                }
             ],
             "Ipv6Addresses":[
    
             ],
             "MacAddress":"12:34:56:ab:cd:ef",
             "NetworkInterfaceId":"eni-020fa83efd417e32d",
             "OwnerId":"ID",
             "PrivateDnsName":"ip-192-0-2-220.ec2.internal",
             "PrivateIpAddress":"192.0.2.220",
             "PrivateIpAddresses":[
                {
                   "Association":{
                      "IpOwnerId":"amazon",
                      "PublicDnsName":"ec2-192-0-2-218.compute-1.amazonaws.com",
                      "PublicIp":"192.0.2.218"
                   },
                   "Primary":true,
                   "PrivateDnsName":"ip-192-0-2-220.ec2.internal",
                   "PrivateIpAddress":"192.0.2.220"
                }
             ],
             "SourceDestCheck":true,
             "Status":"in-use",
             "SubnetId":"subnet-1b1fda3a",
             "VpcId":"vpc-ID",
             "InterfaceType":"interface"
          }
       ],
       "RootDeviceName":"/dev/xvda",
       "RootDeviceType":"ebs",
       "SecurityGroups":[
          {
             "GroupName":"launch-wizard-2",
             "GroupId":"sg-001700ccddac4189a"
          }
       ],
       "SourceDestCheck":true,
       "Tags":[
          {
             "Key":"Owner",
             "Value":"Example"
          },
          {
             "Key":"Name",
             "Value":"Example test"
          }
       ],
       "VirtualizationType":"hvm",
       "CpuOptions":{
          "CoreCount":1,
          "ThreadsPerCore":1
       },
       "CapacityReservationSpecification":{
          "CapacityReservationPreference":"open"
       },
       "HibernationOptions":{
          "Configured":false
       },
       "MetadataOptions":{
          "State":"applied",
          "HttpTokens":"optional",
          "HttpPutResponseHopLimit":1,
          "HttpEndpoint":"enabled"
       },
       "EnclaveOptions":{
          "Enabled":false
       }
    }
     ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **If successfully listed instances(is_success = true):** "Successfully described Amazon EC2 instances."
  * **If no available values(is_success = false):** "No instances were found in Amazon EC2"

**The action should fail and stop a playbook execution:** **if fatal error, invalid instance ID, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "List Instances". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** Amazon EC2 Instances **Table Columns:** ID State Type Availability Zone Public IPv4 DNS Public IPv4 address Monitoring Security group name Key name Launch time |   
  
### List Security Groups

Describes the specified security groups or all of your security groups. A security group is for use with instances either in the EC2-Classic platform or in a specific VPC.

For more information, see [Amazon EC2 Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html).

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Security Group Names | String | N/A | False | One or more security group Names [EC2-Classic and default VPC only]. Separated by comma.If you specify security group Names, the output includes information for only the specified names.  
Security Group IDs | String | N/A | False | One or more security group IDs. Separated by comma.If you specify security group IDs, the output includes information for only the specified ids. Required for security groups in a non default VPC.  
Tag Filters | String | N/A | False | The key-value combination of a tag assigned to the securoty group. For example, to find all groups with a tag that includes the key `Owner` and the value `TeamA`, enter `Owner:TeamA`. You can use comma-separated tag filters, such as `Name:Name1,Owner:TeamA`. Returned groups must match all filters.  
Max Results | Integer | 50 | False | The number of security groups to return. The default value is `50`. The maximum value is `1000`. Note: The 'Security Group IDs' and 'Security Group Names' parameters cannot be used with the 'Max Results' parameter.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    "EC2_Security_Groups": [
    {
       "Description":"launch-wizard-2 created 2021-01-30T19:37:11.523+02:00",
       "GroupName":"launch-wizard-2",
       "IpPermissions":[
          {
             "FromPort":22,
             "IpProtocol":"tcp",
             "IpRanges":[
                {
                   "CidrIp":"192.0.2.0/0"
                }
             ],
             "Ipv6Ranges":[
    
             ],
             "PrefixListIds":[
    
             ],
             "ToPort":22,
             "UserIdGroupPairs":[
    
             ]
          }
       ],
       "OwnerId":"582302349248",
       "GroupId":"sg-001700ccddac4189a",
       "IpPermissionsEgress":[
          {
             "IpProtocol":"-1",
             "IpRanges":[
                {
                   "CidrIp":"192.0.2.0/0"
                }
             ],
             "Ipv6Ranges":[
    
             ],
             "PrefixListIds":[
    
             ],
             "UserIdGroupPairs":[
    
             ]
          }
       ],
       "Tags":[
          {
             "Key":"Team",
             "Value":"A-Team"
          },
          {
             "Key":"Owner",
             "Value":"Example"
          }
       ],
       "VpcId":"vpc-ID"
    }
    ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **If successfully listed groups(is_success = true):** "Successfully described Amazon EC2 security groups."
  * **If no available values(is_success = false):** "No security groups were found in Amazon EC2"

**The action should fail and stop a playbook execution:** **if fatal error, invalid group ID/Name, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "List Security Groups". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** Amazon EC2 Instances **Table Columns:** Security group ID Security group name VPC ID Description Owner ID |   
  
### Ping

Test the connectivity to AWS EC2.

#### Parameters

N/A

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **if successful:** "Successfully connected to the Amazon EC2 with the provided connection parameters!" **The action should fail and stop a playbook execution:** **if not successful:** "Failed to connect to the Amazon EC2 server! Error is {0}".format(exception.stacktrace) | General  
  
### Revoke Security Group Egress

Removes the specified egress rules (outbound rules) from a security group for EC2-VPC. This action does not apply to security groups for use in EC2-Classic. To remove a rule, the values that you specify (for example, ports) must match the existing rule's values exactly. Rule changes are propagated to instances within the security group as quickly as possible. However, a small delay might occur.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Security Group IDs | String | N/A | Yes | One or more security group IDs. Separated by comma. Note for dev: every ID in a separate request  
IP Protocol | DDL | all | No | The IP protocol name. Use 'all' to specify all protocols. Specifying 'all' allows traffic on all ports, regardless of any port range you specify. Possible values: tcp , udp , icmp, all Note for dev: 'all' equals -1 from code  
From Port | Integer |  | No | The start of port range for the TCP and UDP protocols, or an ICMP type number.  
To Port | Integer |  | No | The end of port range for the TCP and UDP protocols allows traffic on all ports, regardless of any port range you specify.  
IP Ranges - CidrIP | String | N/A | No | The IPv4 address in CIDR format. To specify a single IPv4 address, use the /32 prefix length.  
IPv6 Ranges - CidrIP | String | N/A | No | The IPv6 CIDR range. To specify a single IPv6 address, use the /128 prefix length.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **if successfully revoked the specified egress rules from at least one (or all) security groups: (is_success = true):** "Successfully revoked the specified egress rule from the following security groups: {group_ids}" **if failed to revoke the specified egress rules because of permissions rule error (invalid port as 205,etc): (is_success =false):** "Failed to revoke the specified egress rule from the following security groups: {group_ids}. Reason: Invalid IP Permissions set. For more details please check the logs." **if failed to revoke the specified egress rules because of invalid security group id: (is_success =false):** "Failed to revoke the specified egress rule from the following security groups: {group_ids}. Reason: Invalid Security Group ID was provided. For more details please check the logs.`` **The action should fail and stop a playbook execution:** **if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Revoke Security Group Egress". Reason: {0}''.format(error.Stacktrace) | Gener  
  
### Revoke Security Group Ingress

Removes the specified ingress rules (inbound rules) from a security group. To remove a rule, the values that you specify (for example, ports) must match the existing rule's values exactly. Rule changes are propagated to instances within the security group as quickly as possible. However, a small delay might occur.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Security Group IDs | String | N/A | Yes | One or more security group IDs. Separated by comma. Note for dev: every ID in a separate request  
IP Protocol | DDL | all | No | The IP protocol name. Use 'all' to specify all protocols. Specifying 'all' allows traffic on all ports, regardless of any port range you specify. Possible values: tcp , udp , icmp, all Note for dev: 'all' equals -1 from code  
From Port | Integer |  | No | The start of port range for the TCP and UDP protocols, or an ICMP type number.  
To Port | Integer |  | No | The end of port range for the TCP and UDP protocols allows traffic on all ports, regardless of any port range you specify.  
IP Ranges - CidrIP | String | N/A | No | The IPv4 address in CIDR format. To specify a single IPv4 address, use the /32 prefix length.  
IPv6 Ranges - CidrIP | String | N/A | No | The IPv6 CIDR range. To specify a single IPv6 address, use the /128 prefix length.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **if successfully revoked the specified ingress rules to at least one (or all) security groups: (is_success = true):** "Successfully revoked the specified ingress rule from the following security groups: {group_ids}" **if failed to revoke the specified ingress rules because of permissions rule error (invalid port as 205,etc): (is_success =false):** "Failed to revoke the specified ingress rule from the following security groups: {group_ids}. Reason: Invalid IP Permissions set. For more details please check the logs." **if failed to revoke the specified ingress rules because of invalid security group id: (is_success =false):** "Failed to revoke the specified ingress rule from the following security groups: {group_ids}. Reason: Invalid Security Group ID was provided. For more details please check the logs.`` **The action should fail and stop a playbook execution:** **if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Revoke Security Group Ingress". Reason: {0}''.format(error.Stacktrace) | General  
  
### Start Instance

Starts an Amazon Elastic Block Store (Amazon EBS)-backed instance that you have previously stopped. It can take a few minutes for the instance to enter the running state. Notice that you can't start an instance store-backed instance. For more information about instance store-backed instances, see [Storage for the root device](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-for-the-root-device).

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance IDs | String | N/A | Yes | One or more instance IDs. Separated by comma  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
      {
          "CurrentState": "pending",
            "InstanceId": "string",
            "PreviousState":"stopped"
        }
    ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **If current state of all/few instances is different from: pending, running: ( Is_success = false):** Can not start the following instances from their current state: <failed_instance ids>
  * **If current state is pending → action still in progress:** Continuing….the requested instances are still pending
  * **If current state is running:(is_success=true:** Print: The following instances were started successfully : <running_instance ids>
  * **If one of the instances is not valid (is_success =false):** The following instances are not valid: <not valid ids>. Please try again.

**The action should fail and stop a playbook execution:** **if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Start Instance". Reason: {0}''.format(error.Stacktrace) | General  
  
### Stop Instance

Stops an Amazon EBS-backed instance. When you stop an instance, the system attempts to shut it down forcibly after a short delay. It can take a few minutes for the instance to stop. You can restart the instance at any time. You can't stop an instance store-backed instance; you must terminate it instead. For more information about instance store-backed instances, see https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-for-the-root-device

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance IDs | String | N/A | Yes | A comma-separated list of instance IDs.  
Force | Bool | N/A | No | If selected, the action performs an ungraceful (hard) shutdown, immediately halting the instance without letting it flush file system caches or metadata. This process requires mandatory file system check and repair procedures before the instance can resume operation. Not recommended for Windows instances. Not enabled by default.  
  
#### Run On

This action doesn't run on entities.

### Take snapshot

Take snapshot of the instance.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance ID | String | N/A | Yes | Specify the Instance ID.  
Description | String | N/A | No | Specify the description of the snapshot.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
      "EC2_Snapshot": [
        {
          "Description": "",
          "Tags": [],
          "Encrypted": false,
          "VolumeId": "vol-ID",
          "State": "pending",
          "VolumeSize": 8,
          "StartTime": "2022-11-13 15:45:44.795000+00:00",
          "Progress": "",
          "OwnerId": "OWNER_ID",
          "SnapshotId": "snap-ID"
        }
      ]
    }
    

### Terminate Instance

Terminates an instance.

Terminated instances cannot be restarted. Only instance store-backed instances can be terminated. For more information about instance store-backed instances, see [Storage for the root device](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ComponentsAMIs.html#storage-for-the-root-device).

If you terminate an instance more than once, every call succeeds. If you specify multiple instances and the request fails (for example, because of a single incorrect instance ID), none of the instances are terminated.

Terminated instances remain visible after termination (for approximately one hour). By default, Amazon EC2 deletes all EBS volumes that were attached when the instance launched. Volumes attached after instance launch continue running. For more information, see [Amazon user guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html).

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance IDs | String | N/A | Yes | One or more instance IDs. Separated by comma.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    "StoppingInstances": [
          {
          "CurrentState": "shutting-down",
            "InstanceId": "string",
            "PreviousState":"running"
          }
       ]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **If current state of all/few instances is different from: shutting-down, terminated: ( Is_success = false):** Cannot terminate the following instances from their current state: <failed_instance ids>
  * **If current state is shutting-down: (is_success=true) → action still in progress:** Continuing….the requested instances are still shutting-down
  * **If current state is terminated:(is_success=true):** The following instances were terminated successfully : <stopped_instance ids>
  * **If one of the instances is not valid (is_success =false):** The following instances are not valid: <not valid ids>. Please try again.

**The action should fail and stop a playbook execution:** **if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Terminate Instance". Reason: {0}''.format(error.Stacktrace) | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
