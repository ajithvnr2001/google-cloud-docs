---
url: https://docs.cloud.google.com/workstations/docs/troubleshoot/
title: Troubleshoot Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:12.386619+00:00
---

# Troubleshoot Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Troubleshoot Cloud Workstations Stay organized with collections  Save and categorize content based on your preferences. 

This page contains troubleshooting information to help you resolve issues with Cloud Workstations.

## Pull system images onto VMs

When you create workstations using your workstation configuration, Cloud Workstations pulls system images onto your virtual machine (VM) instance from [Artifact Registry](https://docs.cloud.google.com/artifact-registry) (or Container Registry). The error message that appears is similar to the following:
    
    
    System images cannot be pulled onto workstation VMs using this configuration.
    Ensure that you have set up Cloud NAT or enabled Private Google Access for
    Artifact Registry (and Container Registry).
    

Failure to pull these images may prevent you from being able to start your workstations. Here are some recommendations:

  * Set up Cloud NAT or enable Private Google Access.
  * Make sure APIs are enabled and are VPC accessible.
  * Update firewall rules to allow TCP egress.
  * Examine your Compute Engine VM startup logs for possible errors.
  * Enable guest attributes on your project.



## Time out provisioning your VM

When you create workstations using your workstation configuration, Cloud Workstations creates a Compute Engine to back your workstation. If there is an error provisioning your VMs, the error message that appears is similar to the following:
    
    
    Workstations using this configuration cannot be provisioned due to an unknown error.
    

Here are some recommendations:

  * Examine your Compute Engine VM startup logs for possible errors.
  * Examine your Compute Engine API logs for possible errors.
  * Enable guest attributes on your project.



### Set up Cloud NAT or enable Private Google Access

If you disabled public IP addresses on your configuration, use one of the following options:

  * Set up [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) to allow Cloud Workstations to pull images on to your workstation VMs.

  * Enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) on your subnet. If you use the `private.googleapis.com` or the `restricted.googleapis.com` domain names, create DNS records to direct traffic to the IP addresses associated with those domains. Specifically, you need ensure you enable access to the Artifact Registry and Container Registry domains, which correspond respectively to `*.pkg.dev` and `*.gcr.io`.




For more information, see Configure Private Google Access > [ Advanced network configuration](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config).

### Make sure APIs are enabled and are VPC accessible

If your project is inside a VPC Service Controls perimeter, make sure that Cloud Storage API, Container Registry API, and Artifact Registry API are [Virtual Private Cloud (VPC) accessible](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services) within your service perimeter.

### Update firewall rules to allow TCP egress

Ensure that you allow TCP egress in your network on ports 80 and 443 to allow Cloud Workstations to pull images to your workstation.

### Examine your Compute Engine VM startup logs for possible errors

VMs created by Cloud Workstations output debug logs to the serial console on startup. These logs can be helpful when the service times out creating a VM. VM names created for workstations begin with `workstations-` followed by a unique identifier. Use the following filter to filter your logs in the [Log Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface):
    
    
    SEARCH("workstations-")
    sourceLocation.function="main.setupAndRunScript"
    

**Note:** Errors in the startup script logs won't necessarily be logged at severity `ERROR`. Don't add a severity filter while looking for errors in the logs.

If you don't see any logs with this filter ensure that you have [enabled serial port logging](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output#enable-stackdriver) on your project. If you specified a service account on your workstation configuration, ensure the service account has `logging.logEntries.create` permission on the project so it can write logs out to Cloud Logging. Try starting your workstation again after enabling serial port logging and adding the necessary permissions to ensure that the Compute Engine VM startup script is run again to generate the logs.

### Examine your Compute Engine API logs for possible errors

Use the following filter to your stackdriver logs:
    
    
    protoPayload.serviceName="compute.googleapis.com"
    severity>=ERROR
    

Compute Engine API errors may be blocking the creation of your workstation VMs.

### Enable guest attributes on your project

To aid your troubleshooting process, make sure you have not [disabled guest attributes](https://docs.cloud.google.com/compute/docs/metadata/manage-guest-attributes#disabling_guest%0A_attributes) for your project. Cloud Workstations uses these attributes to detect certain issues when you start a workstation and reports those issues as specific debug messages on the workstation configuration.

## Intermittent backend forwarding errors

If you intermittently see "Unable to forward your request to a backend" errors when starting a workstation, the workstation's web server might not be fully started yet.

To resolve this issue, add [readiness checks](https://docs.cloud.google.com/workstations/docs/reference/rest/v1/projects.locations.workstationClusters.workstationConfigs#ReadinessCheck) to your workstation configuration. A readiness check prevents the workstation from reporting that it has started until the server on the specified port is ready to accept requests.

## Debug stopped workstations

If your workstations stop unexpectedly, check the [platform logs](https://docs.cloud.google.com/workstations/docs/platform-logging) or [container output logs](https://docs.cloud.google.com/workstations/docs/container-output-logging) to determine the cause. These logs can help identify workstation startup failures, abrupt shutdowns, or general errors.

## Simultaneous workstation shutdowns when using CMEK

If all your workstations shut down at once and your workstation configuration uses customer-managed encryption keys (CMEK), verify that you have configured the proper permissions on your CMEK.

Specifically, check that the Compute Engine Service Agent (`service-PROJECT_NUMBER@compute-system.iam.gserviceaccount.com`) has the Cloud Key Management Service CryptoKey Encrypter/Decrypter (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) role on your CMEK. If the Compute Engine Service Agent doesn't have the required permissions to access the keys, Compute Engine automatically shuts down the underlying VMs. For more information, see [Encrypt workstation resources using CMEK](https://docs.cloud.google.com/workstations/docs/encrypt-workstation-resources-using-cmek).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
