---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/aws/clusters/create/
title: gcloud alpha container aws clusters create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:59:16.000358+00:00
---

# gcloud alpha container aws clusters create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/aws/clusters/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container aws clusters create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container aws clusters create - create an Anthos cluster on AWS 
SYNOPSIS
    

`gcloud alpha container aws clusters create` (`CLUSTER` : `--location`=`LOCATION`) `--aws-region`=`AWS_REGION` `--cluster-version`=`CLUSTER_VERSION` `--config-encryption-kms-key-arn`=`CONFIG_ENCRYPTION_KMS_KEY_ARN` `--database-encryption-kms-key-arn`=`DATABASE_ENCRYPTION_KMS_KEY_ARN` `--fleet-project`=`FLEET_PROJECT` `--iam-instance-profile`=`IAM_INSTANCE_PROFILE` `--pod-address-cidr-blocks`=`POD_ADDRESS_CIDR_BLOCKS` `--role-arn`=`ROLE_ARN` `--service-address-cidr-blocks`=`SERVICE_ADDRESS_CIDR_BLOCKS` `--subnet-ids`=[`SUBNET_ID`,…] `--vpc-id`=`VPC_ID` [`--admin-groups`=[`GROUP`,…]] [`--admin-users`=`USER`,[`USER`,…]] [`--annotations`=`ANNOTATION`,[`ANNOTATION`,…]] [`--async`] [`--binauthz-evaluation-mode`=`BINAUTHZ_EVALUATION_MODE`] [`--description`=`DESCRIPTION`] [`--disable-per-node-pool-sg-rules`] [`--enable-managed-prometheus`] [`--instance-placement`=`INSTANCE_PLACEMENT`] [`--instance-type`=`INSTANCE_TYPE`] [`--logging`=`COMPONENT`,[`COMPONENT`,…]] [`--main-volume-iops`=`MAIN_VOLUME_IOPS`] [`--main-volume-kms-key-arn`=`MAIN_VOLUME_KMS_KEY_ARN`] [`--main-volume-size`=`MAIN_VOLUME_SIZE`] [`--main-volume-throughput`=`MAIN_VOLUME_THROUGHPUT`] [`--main-volume-type`=`MAIN_VOLUME_TYPE`] [`--role-session-name`=`ROLE_SESSION_NAME`] [`--root-volume-iops`=`ROOT_VOLUME_IOPS`] [`--root-volume-kms-key-arn`=`ROOT_VOLUME_KMS_KEY_ARN`] [`--root-volume-size`=`ROOT_VOLUME_SIZE`] [`--root-volume-throughput`=`ROOT_VOLUME_THROUGHPUT`] [`--root-volume-type`=`ROOT_VOLUME_TYPE`] [`--security-group-ids`=[`SECURITY_GROUP_ID`,…]] [`--ssh-ec2-key-pair`=`SSH_EC2_KEY_PAIR`] [`--tags`=`TAG`,[`TAG`,…]] [`--validate-only`] [`--proxy-secret-arn`=`PROXY_SECRET_ARN` `--proxy-secret-version-id`=`PROXY_SECRET_VERSION_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `(DEPRECATED)` Create an Anthos cluster on AWS. 

This command is deprecated. See <https://cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement> for more details. 

EXAMPLES
     To create a cluster named ``my-cluster`` managed in location ``us-west1``, run: 
    
    
    gcloud alpha container aws clusters create my-cluster --location=us-west1 --aws-region=AWS_REGION --cluster-version=CLUSTER_VERSION --database-encryption-kms-key-arn=KMS_KEY_ARN --iam-instance-profile=IAM_INSTANCE_PROFILE --pod-address-cidr-blocks=POD_ADDRESS_CIDR_BLOCKS --role-arn=ROLE_ARN --service-address-cidr-blocks=SERVICE_ADDRESS_CIDR_BLOCKS --subnet-ids=SUBNET_ID --vpc-id=VPC_ID

POSITIONAL ARGUMENTS
    

Cluster resource - cluster to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `cluster` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CLUSTER`
     ID of the cluster or fully qualified identifier for the cluster. 

To set the `cluster` attribute: 

  * provide the argument `cluster` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Google Cloud location for the cluster. 

To set the `location` attribute: 

  * provide the argument `cluster` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `container_aws/location`. 


REQUIRED FLAGS
    

`--aws-region`=`AWS_REGION`
     AWS region to deploy the cluster. 
`--cluster-version`=`CLUSTER_VERSION`
     Kubernetes version to use for the cluster. 
`--config-encryption-kms-key-arn`=`CONFIG_ENCRYPTION_KMS_KEY_ARN`
     Amazon Resource Name (ARN) of the AWS KMS key to encrypt the user data. 
`--database-encryption-kms-key-arn`=`DATABASE_ENCRYPTION_KMS_KEY_ARN`
     Amazon Resource Name (ARN) of the AWS KMS key to encrypt the cluster secrets. 
`--fleet-project`=`FLEET_PROJECT`
     ID or number of the Fleet host project where the cluster is registered. 
`--iam-instance-profile`=`IAM_INSTANCE_PROFILE`
     Name or ARN of the IAM instance profile associated with the cluster. 
`--pod-address-cidr-blocks`=`POD_ADDRESS_CIDR_BLOCKS`
     IP address range for the pods in this cluster in CIDR notation (e.g. 10.0.0.0/8). 
`--role-arn`=`ROLE_ARN`
     Amazon Resource Name (ARN) of the IAM role to assume when managing AWS resources. 
`--service-address-cidr-blocks`=`SERVICE_ADDRESS_CIDR_BLOCKS`
     IP address range for the services IPs in CIDR notation (e.g. 10.0.0.0/8). 
`--subnet-ids`=[`SUBNET_ID`,…]
     Subnet ID of an existing VNET to use for the cluster control plane. 
`--vpc-id`=`VPC_ID`
     VPC associated with the cluster. 
OPTIONAL FLAGS
    

`--admin-groups`=[`GROUP`,…]
     Groups of users that can perform operations as a cluster administrator. 
`--admin-users`=`USER`,[`USER`,…]
     Users that can perform operations as a cluster administrator. If not specified, the value of property core/account is used. 
`--annotations`=`ANNOTATION`,[`ANNOTATION`,…]
     Annotations for the cluster. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--binauthz-evaluation-mode`=`BINAUTHZ_EVALUATION_MODE`
     Set Binary Authorization evaluation mode for this cluster. `BINAUTHZ_EVALUATION_MODE` must be one of: `DISABLED`, `PROJECT_SINGLETON_POLICY_ENFORCE`. 
`--description`=`DESCRIPTION`
     Description for the cluster. 
`--disable-per-node-pool-sg-rules`
     Disable the default per node pool subnet security group rules on the control plane security group. When disabled, at least one security group that allows node pools to send traffic to the control plane on ports TCP/443 and TCP/8132 must be provided. 
`--enable-managed-prometheus`
     Enables managed collection for Managed Service for Prometheus in the cluster. 

See <https://cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#enable-mgdcoll-gke> for more info. 

Managed Prometheus is enabled by default for cluster versions 1.27 or greater, use --no-enable-managed-prometheus to disable. 

`--instance-placement`=`INSTANCE_PLACEMENT`
     Type of the tenancy. `INSTANCE_PLACEMENT` must be one of: `dedicated`, `default`, `host`. 
`--instance-type`=`INSTANCE_TYPE`
     AWS EC2 instance type for the control plane's nodes. 
`--logging`=`COMPONENT`,[`COMPONENT`,…]
     Set the components that have logging enabled. 

Examples: 
    
    
    gcloud alpha container aws clusters create --logging=SYSTEM
    gcloud alpha container aws clusters create --logging=SYSTEM,WORKLOAD

`COMPONENT` must be one of: `SYSTEM`, `WORKLOAD`. 

`--main-volume-iops`=`MAIN_VOLUME_IOPS`
     Number of I/O operations per second (IOPS) to provision for the main volume. 
`--main-volume-kms-key-arn`=`MAIN_VOLUME_KMS_KEY_ARN`
     Amazon Resource Name (ARN) of the AWS KMS key to encrypt the main volume. 
`--main-volume-size`=`MAIN_VOLUME_SIZE`
     Size of the main volume. The value must be a whole number followed by a size unit of `GB` for gigabyte, or `TB` for terabyte. If no size unit is specified, GB is assumed. 
`--main-volume-throughput`=`MAIN_VOLUME_THROUGHPUT`
     Throughput to provision for the main volume, in MiB/s. Only valid if the volume type is GP3. If volume type is GP3 and throughput is not provided, it defaults to 125. 
`--main-volume-type`=`MAIN_VOLUME_TYPE`
     Type of the main volume. `MAIN_VOLUME_TYPE` must be one of: `gp2`, `gp3`. 
`--role-session-name`=`ROLE_SESSION_NAME`
     Identifier for the assumed role session. 
`--root-volume-iops`=`ROOT_VOLUME_IOPS`
     Number of I/O operations per second (IOPS) to provision for the root volume. 
`--root-volume-kms-key-arn`=`ROOT_VOLUME_KMS_KEY_ARN`
     Amazon Resource Name (ARN) of the AWS KMS key to encrypt the root volume. 
`--root-volume-size`=`ROOT_VOLUME_SIZE`
     Size of the root volume. The value must be a whole number followed by a size unit of `GB` for gigabyte, or `TB` for terabyte. If no size unit is specified, GB is assumed. 
`--root-volume-throughput`=`ROOT_VOLUME_THROUGHPUT`
     Throughput to provision for the root volume, in MiB/s. Only valid if the volume type is GP3. If volume type is GP3 and throughput is not provided, it defaults to 125. 
`--root-volume-type`=`ROOT_VOLUME_TYPE`
     Type of the root volume. `ROOT_VOLUME_TYPE` must be one of: `gp2`, `gp3`. 
`--security-group-ids`=[`SECURITY_GROUP_ID`,…]
     IDs of additional security groups to add to the control plane's nodes. 
`--ssh-ec2-key-pair`=`SSH_EC2_KEY_PAIR`
     Name of the EC2 key pair authorized to login to the control plane's nodes. 
`--tags`=`TAG`,[`TAG`,…]
     Applies the given tags (comma separated) on the cluster. Example: 
    
    
    gcloud alpha container aws clusters create EXAMPLE_CLUSTER --tags=tag1=one,tag2=two

`--validate-only`
     Validate the cluster to create, but don't actually perform it. 
Proxy config 
`--proxy-secret-arn`=`PROXY_SECRET_ARN`
     ARN of the AWS Secrets Manager secret that contains a proxy configuration. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--proxy-secret-version-id`=`PROXY_SECRET_VERSION_ID`
     Version ID string of the AWS Secrets Manager secret that contains a proxy configuration. 

This flag argument must be specified if any of the other arguments in this group are specified. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud container aws clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/container/aws/clusters/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
