---
url: https://docs.cloud.google.com/security-command-center/docs/security-posture-extended-vpc-template/
title: Predefined posture template for VPC networking, extended \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:56.347523+00:00
---

# Predefined posture template for VPC networking, extended  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/security-posture-extended-vpc-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Predefined posture template for VPC networking, extended Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page describes the preventative and detective policies that are included in the v.1.0 version of the predefined posture template for Virtual Private Cloud (VPC) networking, extended. This posture template includes two policy sets:

  * A policy set that includes organization policy constraints that apply to VPC networking.

  * A policy set that includes Security Health Analytics detectors that apply to VPC networking.




You can use this predefined posture template to configure a security posture that helps protect VPC networking. If you want to deploy this predefined posture template, you must customize some of the policies so that they apply to your environment.

## Organization policy constraints

The following table describes the organization policy constraints that are included in this posture.

Policy | Description | Compliance standard  
---|---|---  
`compute.skipDefaultNetworkCreation` | This boolean constraint disables the automatic creation of a default VPC network and default firewall rules in each new project, ensuring that network and firewall rules are intentionally created. The value is `true` to avoid creating the default VPC network. | NIST SP 800-53 control: SC-7 and SC-8  
`ainotebooks.restrictPublicIp` | This boolean constraint restricts public IP access to newly created Vertex AI Workbench notebooks and instances. By default, public IP addresses can access Vertex AI Workbench notebooks and instances. The value is `true` to restrict public IP access on new Vertex AI Workbench notebooks and instances. | NIST SP 800-53 control: SC-7 and SC-8  
`compute.disableNestedVirtualization` | This boolean constraint disables nested virtualization for all Compute Engine VMs to decrease the security risk related to unmonitored nested instances.The value is `true` to turn off VM nested virtualization. | NIST SP 800-53 control: SC-7 and SC-8  
`compute.vmExternalIpAccess` | This list constraint defines the Compute Engine VM instances that are allowed to use external IP addresses. By default, all VM instances are allowed to use external IP addresses. The constraint uses the format `projects/PROJECT_ID/zones/ZONE/instances/INSTANCE`. You must configure this value when you adopt this predefined posture. | NIST SP 800-53 control: SC-7 and SC-8  
`ainotebooks.restrictVpcNetworks` | This list constraint defines the VPC networks a user can select when creating new Vertex AI Workbench instances where this constraint is enforced. You must configure this value when you adopt this predefined posture. | NIST SP 800-53 control: SC-7 and SC-8  
`compute.vmCanIpForward` | This list constraint defines the VPC networks that a user can select when creating new Vertex AI Workbench instances. By default, you can create a Vertex AI Workbench instance with any VPC network. You must configure this value when you adopt this predefined posture. | NIST SP 800-53 control: SC-7 and SC-8  
  
## Security Health Analytics detectors

The following table describes the Security Health Analytics detectors that are included in the predefined posture template. For more information about these detectors, see [Vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings).

Detector name | Description  
---|---  
`FIREWALL_NOT_MONITORED` | This detector checks whether log metrics and alerts aren't configured to monitor VPC firewall rule changes.  
`NETWORK_NOT_MONITORED` | This detector checks whether log metrics and alerts aren't configured to monitor VPC network changes.  
`ROUTE_NOT_MONITORED` | This detector checks whether log metrics and alerts aren't configured to monitor VPC network route changes.  
`DNS_LOGGING_DISABLED` | This detector checks whether DNS logging is enabled on the VPC network.  
`FLOW_LOGS_DISABLED` | This detector checks whether flow logs are enabled on the VPC subnetwork.  
`VPC_FLOW_LOGS_SETTINGS_NOT_RECOMMENDED` | This detector checks whether the `enableFlowLogs` property of VPC subnetworks is missing or set to `false`.  
  
## View the posture template

To view the posture template for VPC networking, extended, do the following: 

### gcloud

Before using any of the command data below, make the following replacements: 

  * `ORGANIZATION_ID`: the numeric ID of the organization. 



Execute the [`gcloud scc posture-templates describe`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/posture-templates/describe) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc posture-templates describe \
        organizations/ORGANIZATION_ID/locations/global/postureTemplates/vpc_networking_extended

#### Windows (PowerShell)
    
    
    gcloud scc posture-templates describe `
        organizations/ORGANIZATION_ID/locations/global/postureTemplates/vpc_networking_extended

#### Windows (cmd.exe)
    
    
    gcloud scc posture-templates describe ^
        organizations/ORGANIZATION_ID/locations/global/postureTemplates/vpc_networking_extended

The response contains the posture template.

### REST

Before using any of the request data, make the following replacements: 

  * `ORGANIZATION_ID`: the numeric ID of the organization. 



HTTP method and URL: 
    
    
    GET https://securityposture.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/postureTemplates/vpc_networking_extended

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://securityposture.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/postureTemplates/vpc_networking_extended"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://securityposture.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/postureTemplates/vpc_networking_extended" | Select-Object -Expand Content

The response contains the posture template.

## What's next

  * [Create a security posture using this predefined posture template](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
