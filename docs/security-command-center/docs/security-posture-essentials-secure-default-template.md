---
url: https://docs.cloud.google.com/security-command-center/docs/security-posture-essentials-secure-default-template/
title: Predefined posture template for secure by default, essentials \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:02.025352+00:00
---

# Predefined posture template for secure by default, essentials  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/security-posture-essentials-secure-default-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Predefined posture template for secure by default, essentials Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page describes the preventative policies that are included in the v1.0 version of the predefined posture template for secure by default, essentials. This posture template helps prevent common misconfigurations and common security issues caused by default settings.

You can use this predefined posture template to configure a security posture that helps protect Google Cloud resources. You can deploy this predefined posture template without making any changes.

Policy | Description | Compliance standards  
---|---|---  
`iam.disableServiceAccountKeyCreation` | This constraint prevents users from creating persistent keys for service accounts to decrease the risk of exposed service account credentials.The value is `true` to disable service account key creation. | NIST SP 800-53 control: AC-2  
`iam.automaticIamGrantsForDefaultServiceAccounts` | This constraint prevents default service accounts from receiving the overly-permissive Identity and Access Management (IAM) role Editor at creation.The value is `true` to disable automatic IAM grants for default service accounts. | NIST SP 800-53 control: AC-3  
`iam.disableServiceAccountKeyUpload` | This constraint avoids the risk of leaked and reused custom key material in service account keys.The value is `true` to disable service account key uploads. | NIST SP 800-53 control: AC-6  
`storage.publicAccessPrevention` | This policy prevents Cloud Storage buckets from being open to unauthenticated public access.The value is `true` to prevent public access to buckets. | NIST SP 800-53 control: AC-3 and AC-6  
`storage.uniformBucketLevelAccess` | This policy prevents Cloud Storage buckets from using per-object ACL (a separate system from IAM policies) to provide access, enforcing consistency for access management and auditing. The value is `true` to enforce [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access). | NIST SP 800-53 control: AC-3 and AC-6  
`compute.requireOsLogin` | This policy requires [OS Login](https://docs.cloud.google.com/compute/docs/oslogin) on newly created VMs to more easily manage SSH keys, provide resource-level permission with IAM policies, and log user access. The value is `true` to require OS Login. | NIST SP 800-53 control: AC-3 and AU-12  
`compute.disableSerialPortAccess` | This policy prevents users from accessing the VM serial port which can be used for backdoor access from the Compute Engine API control plane. The value is `true` to disable VM serial port access. | NIST SP 800-53 control: AC-3 and AC-6  
`compute.restrictXpnProjectLienRemoval` | This policy prevents the accidental deletion of Shared VPC host projects by restricting the removal of project liens.The value is `true` to restrict Shared VPC project lien removal. | NIST SP 800-53 control: AC-3 and AC-6  
`compute.vmExternalIpAccess` | This policy prevents the creation of Compute Engine instances with a public IP address, which can expose them to incoming internet traffic and outgoing internet traffic.The value is `denyAll` to turn off all access from public IP addresses. If you want to change it to permit certain VM instances to have public access, set the allowed values:
    
    
    policy_rules:
        - values:
          allowed_values:
          - is:projects/PROJECT_ID/zones/ZONE/instances/INSTANCE
    

| NIST SP 800-53 control: AC-3 and AC-6  
`compute.skipDefaultNetworkCreation` | This policy disables the automatic creation of a default VPC network and default firewall rules in each new project, ensuring that network and firewall rules are intentionally created. The value is `true` to avoid creating the default VPC network. | NIST SP 800-53 control: AC-3 and AC-6  
`compute.setNewProjectDefaultToZonalDNSOnly` | This policy restricts application developers from choosing legacy DNS settings for Compute Engine instances that have lower service reliability than modern DNS settings. The value is `Zonal DNS only` for new projects. | NIST SP 800-53 control: AC-3 and AC-6  
`sql.restrictPublicIp` | This policy prevents the creation of Cloud SQL instances with public IP addresses, which can expose them to incoming internet traffic and outgoing internet traffic.The value is `true` to restrict access to Cloud SQL instances by public IP addresses. | NIST SP 800-53 control: AC-3 and AC-6  
`sql.restrictAuthorizedNetworks` | This policy prevents public or non-RFC 1918 network ranges from accessing Cloud SQL databases.The value is `true` to restrict authorized networks on Cloud SQL instances. | NIST SP 800-53 control: AC-3 and AC-6  
`compute.restrictProtocolForwardingCreationForTypes` | This policy allows VM protocol forwarding for internal IP addresses only.The value is `INTERNAL` to restrict protocol forwarding based on the type of IP address. | NIST SP 800-53 control: AC-3 and AC-6  
`compute.disableVpcExternalIpv6` | This policy prevents the creation of external IPv6 subnets, which can be exposed to incoming and outgoing internet traffic.The value is `true` to disable external IPv6 subnets. | NIST SP 800-53 control: AC-3 and AC-6  
`compute.disableNestedVirtualization` | This policy disables nested virtualization for all Compute Engine VMs to decrease the security risk related to unmonitored nested instances.The value is `true` to turn off VM nested virtualization. | NIST SP 800-53 control: AC-3 and AC-6  
  
## View the posture template

To view the posture template for secure by default, essentials, do the following: 

### gcloud

Before using any of the command data below, make the following replacements: 

  * `ORGANIZATION_ID`: the numeric ID of the organization. 



Execute the [`gcloud scc posture-templates describe`](https://docs.cloud.google.com/sdk/gcloud/reference/scc/posture-templates/describe) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud scc posture-templates describe \
        organizations/ORGANIZATION_ID/locations/global/postureTemplates/secure_by_default_essential

#### Windows (PowerShell)
    
    
    gcloud scc posture-templates describe `
        organizations/ORGANIZATION_ID/locations/global/postureTemplates/secure_by_default_essential

#### Windows (cmd.exe)
    
    
    gcloud scc posture-templates describe ^
        organizations/ORGANIZATION_ID/locations/global/postureTemplates/secure_by_default_essential

The response contains the posture template.

### REST

Before using any of the request data, make the following replacements: 

  * `ORGANIZATION_ID`: the numeric ID of the organization. 



HTTP method and URL: 
    
    
    GET https://securityposture.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/postureTemplates/secure_by_default_essential

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://securityposture.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/postureTemplates/secure_by_default_essential"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://securityposture.googleapis.com/v1/organizations/ORGANIZATION_ID/locations/global/postureTemplates/secure_by_default_essential" | Select-Object -Expand Content

The response contains the posture template.

## What's next

  * [Create a security posture using this predefined posture template](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
