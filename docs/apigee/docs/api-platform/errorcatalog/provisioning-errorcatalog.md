---
url: https://docs.cloud.google.com/apigee/docs/api-platform/errorcatalog/provisioning-errorcatalog/
title: Apigee provisioning error catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:25.069521+00:00
---

# Apigee provisioning error catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/errorcatalog/provisioning-errorcatalog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Apigee provisioning error catalog Stay organized with collections  Save and categorize content based on your preferences. 

This error catalog is intended to help troubleshoot and resolve common errors you may encounter when provisioning Apigee resources. It provides detailed information about the errors that may be returned in the UI or on the command line during provisioning.

The catalog includes the following information: 

  * The error code
  * The error message
  * The possible cause of the error
  * Steps to resolve the error



## Errors returned during provisioning

API calls are made during the provisioning of Apigee resources, whether you are provisioning from the [Apigee UI in Cloud console](https://cloud.google.com/apigee/docs/api-platform/fundamentals/ui-overview) or the command line interface (CLI). API calls made during provisioning, or to check provisioning status, can return errors under a variety of circumstances, including the following: 

  * Google Cloud billing is not enabled for the project
  * Required APIs are not enabled for the project
  * Region, peering range, or other networking configuration issues



Usually, the error message will contain information that you can use to correct any issues, resolve the error, and unblock provisioning.

## Error format

If the error is a common error listed in this catalog, there will be an error message displayed in the Apigee UI in Cloud Console. For example: 
    
    
      {
        "error": {
          "code": "FAILED_PRECONDITION",
          "message": "Error finding one or more network address ranges to use for the Instance. Verify
           the network configuration provided for the Instance and try again."
          }
      }

Use the message provided to search this reference for more information about possible causes of the error and potential steps you can take to resolve the problem.

## Common errors

### Location does not have enough resources available

#### Error message
    
    
    location "[loc]" does not have enough resources available to fulfill the request. Try again later
    or choose a different location

#### Possible cause

This error may occur when a request is made to provision an Apigee instance in a zone or region where one or more resources is not available. This error is not a result of any problems with the instance configuration.

#### Steps to resolve

To resolve the error, you can choose to provision your instance in another region, or wait for the issue to be resolved (typically within a few hours).

### Validation failed for service networking 

#### Error message

You will see an initial network validation error message, which may be followed by one or more of the following detailed error messages: 
    
    
    generic::failed_precondition: validation failed for service networking for network "[network]",
    COMPUTE_API_NOT_ENABLED
    
    generic::failed_precondition: validation failed for service networking for network "[network]",
    RANGES_DELETED_LATER
    
    generic::internal: error validating service networking consumer config for network "[network]":
    This API method requires billing to be enabled. Please enable billing on project [project] by visiting
    ... then retry.

#### Possible cause

This error may occur if the pre-provisioning validation of your network configuration fails.

#### Steps to resolve

The following table lists actions you can perform to resolve these error messages: 

message  | Steps to resolve   
---|---  
COMPUTE_API_NOT_ENABLED  | [Enable the Compute Engine API](https://cloud.google.com/apis/docs/getting-started#enabling_apis).   
RANGES_DELETED_LATER  | [Confirm that the provided IP ranges are valid.](https://cloud.google.com/vpc/docs/subnets#valid-ranges)  
Require billing to be enabled ...  | [Confirm that billing is enabled on the project](https://cloud.google.com/apis/docs/getting-started#enabling_billing).   
  
### Couldn't find a free IP space of /22

#### Error message
    
    
    couldn't find a free IP space of /22 to launch an instance. Verify the peering ranges are available
    as per https://cloud.google.com/apigee/docs/api-platform/get-started/install-cli#service-networking
    and try again

#### Possible cause

This error may occur during subnet creation, if an IP space of /22 is not available in the provided ranges.

#### Steps to resolve

To resolve this error, confirm that the IP peering ranges provided [ meet the requirements for subnet creation in service networking](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#service-networking). Then, retry the operation.

### Error in allocating IPs 

#### Error message

You may encounter one of the following error messages: 
    
    
    Error in allocating IPs to use for the Instance. Please verify the network configuration provided
    for the Instance and try again.
    
    Error in allocating IPs for ServiceAttachment.
    
    Error finding one or more network address ranges to use for the Instance. Verify the network
    configuration provided for the Instance and try again.

You may also receive a detailed error message from the network client. For example: 
    
    
    Invalid resource usage: 'The resource 'projects/xxx' is already linked to another shared VPC host 
    'projects/yyy'.

#### Possible cause

This error may occur during Apigee instance creation when performing service networking operations, such as creating a subnet or searching for a network range. In some cases, [ Service Networking](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/getting-started) may return an error message.

#### Steps to resolve

Follow the instructions in the detailed message from Service Networking to resolve the error. You may need to: 

  * [Update the provided IP range allocations for the instance.](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/console-configure-networking)
  * Address other Service Networking configuration issues. 
  * Use another VPC network for instance configuration.



### KMS key permission denied

#### Error message
    
    
    apigee service agent <email> cannot encrypt/decrypt with kms key <keyID>: PermissionDenied

#### Possible cause

Before provisioning an Apigee instance, the KMS key provided is validated. This error indicates that the Apigee Service Agent does not have the correct permissions required for the Cloud KMS CryptoKey Encrypter/Decrypter role on the provided key.

#### Steps to resolve

Grant the Apigee Service Agent access to the provided KMS key. You can find the command to grant access in Step 1(f) of [Provision a paid org from the command line](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#create-org).

### Request prohibited by the organization's policy

#### Error message
    
    
    The request is prohibited by organization's policy. Please refer to
    https://cloud.google.com/vpc-service-controls/docs/troubleshooter
    to review the org policy for VPC Service Control. vpcServiceControlsUniqueIdentifier:
    <vpc-sc unique identifier>.

#### Possible cause

This error may occur when provisioning an Apigee instance. The instance creation request is blocked by one of the Google Cloud organization's policies for VPC Service Control.

#### Steps to resolve

To resolve this error, follow the steps outlined in [ Communicate, debug, and resolve VPC Service Controls issues with minimal effort](https://cloud.google.com/blog/products/identity-security/unique-identifier-helps-troubleshooting-vpc-service-controls-perimeter). These steps use the `vpcServiceControlsUniqueIdentifier` to fix the VPC-SC configuration.

### Maximum number of peerings reached

#### Error message
    
    
    The maximum number of peerings for the network (7) has been reached. Please delete unused peerings
    for the network and try again

#### Possible cause

This error may occur when provisioning an Apigee instance. In this case, there are no available network peerings.

#### Steps to resolve

To resolve the error, delete any unused peerings for the network, or use another VPC network for your instance.

### Exceeded maximum allowed routers

#### Error message
    
    
    exceeded maximum allowed routers in same network and region. Please use a different network + same
    region OR same network + different region

#### Possible cause

This error may occur during provisioning when creating a [ Cloud NAT (network address translation)](https://docs.cloud.google.com/nat/docs/overview). In this case, the choice of network and choice of region are invalid.

#### Steps to resolve

To resolve the error, you can select a different network in the same region, or use the same network in a different region.

### The resource was invalid

#### Error message
    
    
    the resource 'projects/.../regions/.../serviceAttachments/...' was invalid. Must be either a valid
    In-Project Forwarding Rule Target URL, a valid Service Attachment URL, or a supported Google API
    bundle (global-only)

#### Possible cause

This error may occur if the Service Attachment URL provided is invalid.

#### Steps to resolve

To resolve this issue, update the Service Attachment URL in your instance configuration to a valid URL.

### The resource was not found

#### Error message
    
    
    the resource 'projects/.../regions/.../serviceAttachments/...' was not found

#### Possible cause

This error may occur if the Service Attachment URL provided was not found.

#### Steps to resolve

To resolve this error, update the Service Attachment URL in your instance configuration to a valid URL.

### Network range deleted but still assigned

#### Error message
    
    
    a network range was deleted but still assigned in network <network>. Please refer to this guide
    to fix: https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/update. Valid ranges can
    be found at VPC networks -> Private service connection -> Allocated IP ranges for services

#### Possible cause

This error may occur if a network range allocated for the Apigee instance is deleted, partially deleted, or does not exist.

#### Steps to resolve

To resolve this error, run the following command to [ update the VPC peering](https://cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/update) for the allocated range: 
    
    
    gcloud services vpc-peerings update \
      --service=servicenetworking.googleapis.com \
      --ranges=$VALID_RANGES \
      --network=$NETWORK \
      --project=$PROJECT \
      --force

### IP range overlaps 

#### Error message
    
    
    An IP range in the peer network (10.128.0.0/28) overlaps with an IP range (10.128.0.0/20) in an
    active peer (peering-to-consumer) of the local network. Please use a different ipRange.
    If you've recently deleted an ApigeeInstance and wanted to use the same ipRange, please wait
    for some time and try again

#### Possible cause

This error may occur when provisioning an Apigee instance. In this case, the Apigee instance creation operation fails because the allocated IP range is invalid, or the allocated range has not been fully released after deleting a previously created Apigee instance.

#### Steps to resolve

To resolve the error, use a different IP range or try again later to use a fully released IP range.

### Couldn't connect to the private Google APIs ranges

#### Error message
    
    
    couldn't connect to the private Google APIs ranges. This is likely a DNS mis-configuration if you've
    set up peered-dns-domains. Please check
    https://cloud.google.com/vpc/docs/configure-private-google-access#config-domain

#### Possible cause

This error may occur when provisioning an Apigee instance. In this case, the Apigee instance cannot connect to the private Google API ranges.

#### Steps to resolve

To resolve the issue, confirm that the [ DNS configurations](https://cloud.google.com/vpc/docs/configure-private-google-access#config-domain) for private Google API ranges are correct and that private Google API ranges be reached from within the VPC network.

### Deletion triggered for project

#### Error message
    
    
    deletion had been triggered for project <project>

#### Possible cause

This error may occur if the deletion process for the project used for instance creation has started. This validation check is performed between each step of the provisioning operation.

#### Steps to resolve

If the project deletion is unintentional, you may be able to restore the project using the following command: 

`gcloud projects undelete PROJECT_ID`

For more information, see [Restoring a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#restoring_a_project).

### KMS key invalid argument

#### Error message
    
    
    apigee service agent <p4sa email> cannot encrypt/decrypt with kms key <kms key>: Invalid Argument

#### Possible cause

This error may occur when validating the provided KMS key during provisioning. In this case, one or more of the values in the Cloud KMS key fields are invalid.

#### Steps to resolve

To resolve this error, confirm the correct values for your Cloud KMS key and update the fields in your instance configuration.

### Google Cloud KMS API not enabled

#### Error message
    
    
    Google Cloud KMS API has not been used in project <project> before or it is disabled. Enable it by
    visiting https://console.developers.google.com/apis/api/cloudkms.googleapis.com/overview?project=<project> then retry.
    If you enabled this API recently, wait a few minutes for the action to propagate to our systems
    and retry.

#### Possible cause

This error may occur if the Cloud KMS API is not enabled in the project used for Apigee provisioning.

#### Steps to resolve

To resolve this error, enable [the Cloud KMS API](https://pantheon.corp.google.com/apis/library/cloudkms.googleapis.com).

### Apigee API not enabled

#### Error message
    
    
    Apigee API has not been used in project <project> before or it is disabled. Enable it by visiting
    https://console.developers.google.com/apis/api/apigee.googleapis.com/overview?project=<project> then retry.
    If you enabled this API recently, wait a few minutes for the action to propagate to our systems
    and retry.

#### Possible cause

This error may occur if the Apigee API is not enabled in the project used for Apigee provisioning.

#### Steps to resolve

To resolve this error, enable the [Apigee API](https://console.developers.google.com/apis/api/apigee.googleapis.com/overview).

### Google Cloud billing not enabled

#### Error message
    
    
    This API method requires billing to be enabled. Please enable billing on project <project number>
    by visiting https://console.developers.google.com/billing/enable?project=<project number> then
    retry. If you enabled billing for this project recently, wait a few minutes for the action to
    propagate to our systems and retry.

#### Possible cause

This error may occur if billing is not enabled for the Google Cloud project used for Apigee provisioning.

#### Steps to resolve

To resolve this error, [enable billing](https://console.developers.google.com/billing/enable) for your Google Cloud project. 

### Create Service Networking Connection again

#### Error message
    
    
    please create Service Networking connection with service 'servicenetworking.googleapis.com' from
    consumer project <project number> network <network> again

#### Possible cause

This error may occur if the Service Networking connection fails in your Google Cloud project while retrieving the Service Networking host project number. 

#### Steps to resolve

To resolve this issue, create a Service Networking connection as described in [Step 2: Set up networking](https://cloud.google.com/apigee/docs/api-platform/get-started/console-configure-networking).

### IAM permission denied

#### Error message
    
    
    IAM permission denied for service account  
    service-<project number>@gcp-sa-apigee.iam.gserviceaccount.com. Ensure that Apigee service
    account has Apigee service agent role to your consumer project.

#### Possible cause

This error may occur if the IAM permissions for the Apigee service account that is attempting to interact with the Google Cloud consumer project are not correct.

#### Steps to resolve

To resolve this issue, grant the `Apigee service agent` role to the service account initiating this operation. Permissions can be granted on the [IAM page](https://console.google.com/iam-admin/iam) in the Google Cloud console.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
