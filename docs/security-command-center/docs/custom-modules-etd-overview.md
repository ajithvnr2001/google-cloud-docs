---
url: https://docs.cloud.google.com/security-command-center/docs/custom-modules-etd-overview/
title: Overview of custom modules for Event Threat Detection \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:31.366604+00:00
---

# Overview of custom modules for Event Threat Detection  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/custom-modules-etd-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Overview of custom modules for Event Threat Detection Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page provides an overview of custom modules for Event Threat Detection.

You can configure modules, also known as _detectors_ , to process your [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) stream and detect threats based on parameters you specify. This feature extends the monitoring capabilities of Event Threat Detection and lets you add modules with your own detection parameters, remediation guidance, and severity designations for configurations that the built-in detectors might not support.

Custom modules are useful if you need modules with detection rules that meet the unique needs of your organization. For example, you can add a custom module that creates findings if log entries show that a resource is connected to specific IP addresses or is created in a restricted region.

## How custom modules for Event Threat Detection work

Custom modules are a select group of Event Threat Detection detectors that you can configure with your own detection parameters. You can create an Event Threat Detection custom module through the Google Cloud console. Alternatively, you can create one by updating a custom module template and sending the custom module to Security Command Center through the Google Cloud CLI. For information about available templates, see Custom modules and templates.

Custom module templates are written in JSON and let you define detection parameters that control what events in log entries should trigger findings. For example, the built-in `Malware: Bad IP` detector checks Virtual Private Cloud Flow Logs for evidence of connections to known suspicious IP addresses. However, you can enable and modify the `Configurable Bad IP` custom module with a list of suspicious IP addresses that you maintain. If your logs indicate a connection to any of your supplied IP addresses, a finding is generated and written to Security Command Center.

Module templates also let you define the severity of threats and provide custom remediation steps to help your security teams fix issues.

With custom modules, you have more control over how Event Threat Detection detects threats and reports findings. Custom modules include your supplied parameters, but still utilize Event Threat Detection's proprietary detection logic and threat intelligence methods, such as identifying indicators of compromise (IoC). You can implement a broad set of threat models tailored to your organization's unique requirements.

Event Threat Detection custom modules run alongside the built-in detectors. Enabled modules run in real-time mode, which triggers scans whenever new logs are created.

## Custom modules and templates

The following table contains a list of supported custom module types, descriptions, required logs, and JSON module templates.

You need these JSON module templates if you want to use the gcloud CLI to create or update custom modules. To see a template, click the expand icon add_circle  next to its name. For information about using custom modules, see [Configure and manage custom modules](https://docs.cloud.google.com/security-command-center/docs/use-custom-modules-etd).

Finding category | Module type | Log source types | Description  
---|---|---|---  
Configurable bad IP | `CONFIGURABLE_BAD_IP` | [VPC flow logs](https://docs.cloud.google.com/vpc/docs/flow-logs)  
[Firewall Rules logs](https://docs.cloud.google.com/vpc/docs/firewall-rules-logging) | Detects a connection to a specified IP address  
Template: Configurable bad IP
    
    
    {
      "metadata": {
        "severity": "SEVERITY",
        "description": "DESCRIPTION",
        "recommendation": "RECOMMENDATION"
      },
      "ips": [
        "IP_ADDRESS_1",
        "IP_ADDRESS_2"
      ]
    }

Replace the following:

  * `SEVERITY`: The severity of findings to be produced by this module. The valid values are `LOW`, `MEDIUM`, `HIGH`, and `CRITICAL`.
  * `DESCRIPTION`: A description of the threat that the custom module detects. This description is used to populate the `explanation` property of each finding generated by this module.
  * `RECOMMENDATION`: An explanation of the recommended steps that security teams can take to resolve the detected issue. This explanation is used to populate the `nextSteps` property of each finding generated by this module.


  * `IP_ADDRESS_1`: A publicly-routable IPv4 or IPv6 address or CIDR block to watch for—for example, `192.0.2.1` or `192.0.2.0/24`.
  * `IP_ADDRESS_2`: Optional. A publicly-routable IPv4 or IPv6 address or CIDR block to watch for—for example, `192.0.2.1` or `192.0.2.0/24`.

  
Configurable bad domain | `CONFIGURABLE_BAD_DOMAIN` | [Cloud DNS logs](https://docs.cloud.google.com/dns/docs/monitoring) | Detects a connection to a specified domain name  
Template: Configurable bad domain
    
    
    {
      "metadata": {
        "severity": "SEVERITY",
        "description": "DESCRIPTION",
        "recommendation": "RECOMMENDATION"
      },
      "domains": [
        "DOMAIN_1","DOMAIN_2"
      ]
    }

Replace the following:

  * `SEVERITY`: The severity of findings to be produced by this module. The valid values are `LOW`, `MEDIUM`, `HIGH`, and `CRITICAL`.
  * `DESCRIPTION`: A description of the threat that the custom module detects. This description is used to populate the `explanation` property of each finding generated by this module.
  * `RECOMMENDATION`: An explanation of the recommended steps that security teams can take to resolve the detected issue. This explanation is used to populate the `nextSteps` property of each finding generated by this module.


  * `DOMAIN_1`: A domain name to watch for—for example, `example.com`. A value of `localhost` is not permitted. Unicode and Punycode domain names are normalized. For example, 例子.example and xn--fsqu00a.example are equivalent.
  * `DOMAIN_2`: Optional. A domain name to watch for—for example, `example.com`. A value of `localhost` is not permitted. Unicode and Punycode domain names are normalized. For example, 例子.example and xn--fsqu00a.example are equivalent.

  
Unexpected Compute Engine instance type | `CONFIGURABLE_ALLOWED_COMPUTE_ENGINE_INSTANCE_TYPE` | **Cloud Audit Logs:**  
[Admin Activity logs](https://docs.cloud.google.com/iam/docs/audit-logging) | Detects the creation of Compute Engine instances that do not match a specified instance type or configuration.  
Template: Unexpected Compute Engine instance type
    
    
    {
      "metadata": {
        "severity": "SEVERITY",
        "description": "DESCRIPTION",
        "recommendation": "RECOMMENDATION"
      },
      "instances": [
        {
          "series": "SERIES",
          "cpus": {
            "minimum": MINIMUM_NUMBER_OF_CPUS,
            "maximum": MAXIMUM_NUMBER_OF_CPUS
          },
          "ram_mb": {
            "minimum": MINIMUM_RAM_SIZE,
            "maximum": MAXIMUM_RAM_SIZE
          },
          "gpus": {
            "minimum": MINIMUM_NUMBER_OF_GPUS,
            "maximum": MAXIMUM_NUMBER_OF_GPUS
          },
          "projects": [
            "PROJECT_ID_1",
            "PROJECT_ID_2"
          ],
          "regions": [
            "REGION_1",
            "REGION_2"
          ]
        },
        {
          "series": " ... ",
          ...
          "regions": [ ... ]
        }
      ]
    }
    

Replace the following:

  * `SEVERITY`: The severity of findings to be produced by this module. The valid values are `LOW`, `MEDIUM`, `HIGH`, and `CRITICAL`.
  * `DESCRIPTION`: A description of the threat that the custom module detects. This description is used to populate the `explanation` property of each finding generated by this module.
  * `RECOMMENDATION`: An explanation of the recommended steps that security teams can take to resolve the detected issue. This explanation is used to populate the `nextSteps` property of each finding generated by this module.


  * `SERIES`: Optional. The Compute Engine machine series—for example, `C2`. If empty, the module permits all series. For more information, see [Machine families resource and comparison guide](https://docs.cloud.google.com/compute/docs/machine-resource).
  * `MINIMUM_NUMBER_OF_CPUS`: Optional. The minimum number of CPUs to allow. If not present, there is no minimum. Must not be negative.
  * `MAXIMUM_NUMBER_OF_CPUS`: Optional. The maximum number of CPUs to allow. If not present, there is no maximum. Must be greater than or equal to `minimum` and less than or equal to 1,000.
  * `MINIMUM_RAM_SIZE`: Optional. The minimum RAM size to allow, in megabytes. If not present, there is no minimum.
  * `MAXIMUM_RAM_SIZE`: Optional. The maximum RAM size to allow, in megabytes. If not present, there is no maximum. Must be greater than or equal to `minimum` and less than or equal to 10,000,000.
  * `MINIMUM_NUMBER_OF_GPUS`: Optional. The minimum number of GPUs to allow. If not present, there is no minimum. Must not be negative.
  * `MAXIMUM_NUMBER_OF_GPUS`: Optional. The maximum number of GPUs to allow. If not present, there is no maximum. Must be greater than or equal to `minimum` and less than or equal to 100.
  * `PROJECT_ID_1`: Optional. The ID of a project that you want to apply this module to—for example, `projects/example-project`. If empty or unset, the module is applied to instances created in all projects within the current scope.
  * `PROJECT_ID_2`: Optional. The ID of a project that you want to apply this module to—for example, `projects/example-project`.
  * `REGION_1`: Optional. A [region](https://docs.cloud.google.com/compute/docs/regions-zones) where you want to apply this module—for example, `us-central1`. If empty or unset, the module is applied to instances created in all regions.
  * `REGION_2`: Optional. A region where you want to apply this module—for example, `us-central1`.

  
Unexpected Compute Engine source image | `CONFIGURABLE_ALLOWED_COMPUTE_ENGINE_SOURCE_IMAGE` | **Cloud Audit Logs:**  
[Admin Activity logs](https://docs.cloud.google.com/iam/docs/audit-logging) | Detects the creation of a Compute Engine instance with an image or image family that does not match a specified list  
Template: Unexpected Compute Engine source image
    
    
    {
      "metadata": {
        "severity": "SEVERITY",
        "description": "DESCRIPTION",
        "recommendation": "RECOMMENDATION"
      },
      "patterns": [
        {
    
          "pattern": "PATTERN_1",
          "name": "NAME_1"
        },
        {
          "pattern": "PATTERN_2",
          "name": "NAME_2"
        }
      ]
    }

Replace the following:

  * `SEVERITY`: The severity of findings to be produced by this module. The valid values are `LOW`, `MEDIUM`, `HIGH`, and `CRITICAL`.
  * `DESCRIPTION`: A description of the threat that the custom module detects. This description is used to populate the `explanation` property of each finding generated by this module.
  * `RECOMMENDATION`: An explanation of the recommended steps that security teams can take to resolve the detected issue. This explanation is used to populate the `nextSteps` property of each finding generated by this module.


  * `PATTERN_1`: An [RE2](https://github.com/google/re2/wiki/Syntax) regular expression to check images against—for example, `debian-image-1`. If an image is used to create a Compute Engine instance and the name of that image isn't matched by any of the specified regular expressions, a finding is generated.
  * `NAME_1`: A descriptive name for this pattern—for example, `first-image`.
  * `PATTERN_2`: Optional. Another RE2 regular expression to check images against—for example, `debian-image-2`.
  * `NAME_2`: Optional. A descriptive name for the second pattern—for example, `second-image`.

  
Unexpected Compute Engine region | `CONFIGURABLE_ALLOWED_COMPUTE_ENGINE_REGION` | **Cloud Audit Logs:**  
[Admin Activity logs](https://docs.cloud.google.com/iam/docs/audit-logging) | Detects the creation of a Compute Engine instance in a region that is not in a specified list  
Template: Unexpected Compute Engine region
    
    
    {
      "metadata": {
        "severity": "SEVERITY",
        "description": "DESCRIPTION",
        "recommendation": "RECOMMENDATION"
      },
      "regions": [
        {
          "region": "REGION_1"
        },
        {
          "region": "REGION_2"
        }
      ]
    }

Replace the following:

  * `SEVERITY`: The severity of findings to be produced by this module. The valid values are `LOW`, `MEDIUM`, `HIGH`, and `CRITICAL`.
  * `DESCRIPTION`: A description of the threat that the custom module detects. This description is used to populate the `explanation` property of each finding generated by this module.
  * `RECOMMENDATION`: An explanation of the recommended steps that security teams can take to resolve the detected issue. This explanation is used to populate the `nextSteps` property of each finding generated by this module.


  * `REGION_1`: The [name of a region](https://docs.cloud.google.com/compute/docs/regions-zones) to permit—for example, `us-west1`. If a Compute Engine instance is created in a region that is not specified in the list, Event Threat Detection generates a finding. 
  * `REGION_2`: Optional. The name of a region to permit—for example, `us-central1`. If a Compute Engine instance is created in a region that is not specified in the list, Event Threat Detection generates a finding.

  
Breakglass account used | `CONFIGURABLE_BREAKGLASS_ACCOUNT_USED` | **Cloud Audit Logs:**  
[Admin Activity logs](https://docs.cloud.google.com/iam/docs/audit-logging)   
[Data Access logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access) (optional) | Detects the usage of an emergency access (_breakglass_) account  
Template: Breakglass account used
    
    
    {
      "metadata": {
        "severity": "SEVERITY",
        "description": "DESCRIPTION",
        "recommendation": "RECOMMENDATION"
      },
      "accounts": [
        "BREAKGLASS_ACCOUNT_1", "BREAKGLASS_ACCOUNT_2"
      ]
    }

Replace the following:

  * `SEVERITY`: The severity of findings to be produced by this module. The valid values are `LOW`, `MEDIUM`, `HIGH`, and `CRITICAL`.
  * `DESCRIPTION`: A description of the threat that the custom module detects. This description is used to populate the `explanation` property of each finding generated by this module.
  * `RECOMMENDATION`: An explanation of the recommended steps that security teams can take to resolve the detected issue. This explanation is used to populate the `nextSteps` property of each finding generated by this module.


  * `BREAKGLASS_ACCOUNT_1`: A breakglass account to watch for—for example, `test@example.com`. A finding is generated if this account is used for an action that is recorded in a Cloud Audit Logs entry.
  * `BREAKGLASS_ACCOUNT_2`: Optional. A breakglass account to watch for—for example, `test@example.com`. A finding is generated if this account is used for an action that is recorded in a Cloud Audit Logs entry.

  
Unexpected role grant | `CONFIGURABLE_UNEXPECTED_ROLE_GRANT` | **Cloud Audit Logs:**  
[Admin Activity logs](https://docs.cloud.google.com/iam/docs/audit-logging) | Detects when a specified role is granted to a user  
Template: Unexpected role grant
    
    
    {
      "metadata": {
        "severity": "SEVERITY",
        "description": "DESCRIPTION",
        "recommendation": "RECOMMENDATION"
      },
      "roles": ["ROLE_1", "ROLE_2"]
    }

Replace the following:

  * `SEVERITY`: The severity of findings to be produced by this module. The valid values are `LOW`, `MEDIUM`, `HIGH`, and `CRITICAL`.
  * `DESCRIPTION`: A description of the threat that the custom module detects. This description is used to populate the `explanation` property of each finding generated by this module.
  * `RECOMMENDATION`: An explanation of the recommended steps that security teams can take to resolve the detected issue. This explanation is used to populate the `nextSteps` property of each finding generated by this module.


  * `ROLE_1`: An [IAM role](https://docs.cloud.google.com/iam/docs/understanding-roles) to watch for—for example, `roles/owner`. A finding is generated if this role is granted.
  * `ROLE_2`: Optional. An IAM role to watch for—for example, `roles/editor`. A finding is generated if this role is granted.

  
Custom role with prohibited permission | `CONFIGURABLE_CUSTOM_ROLE_WITH_PROHIBITED_PERMISSION` | **Cloud Audit Logs:**  
[Admin Activity logs](https://docs.cloud.google.com/iam/docs/audit-logging) | Detects when a custom role with any of the specified IAM permissions is created or updated.  
Template: Custom role with prohibited permission
    
    
    {
      "metadata": {
        "severity": "SEVERITY",
        "description": "DESCRIPTION",
        "recommendation": "RECOMMENDATION"
      },
      "permissions": [
        "PERMISSION_1",
        "PERMISSION_2"
      ]
    }

Replace the following:

  * `SEVERITY`: The severity of findings to be produced by this module. The valid values are `LOW`, `MEDIUM`, `HIGH`, and `CRITICAL`.
  * `DESCRIPTION`: A description of the threat that the custom module detects. This description is used to populate the `explanation` property of each finding generated by this module.
  * `RECOMMENDATION`: An explanation of the recommended steps that security teams can take to resolve the detected issue. This explanation is used to populate the `nextSteps` property of each finding generated by this module.


  * `PERMISSION_1`: An [IAM permission](https://docs.cloud.google.com/iam/docs/permissions-reference) to watch for—for example, `storage.buckets.list`. Event Threat Detection generates a finding if a custom IAM role containing this permission is granted to a principal. 
  * `PERMISSION_2`: Optional. An IAM permission to watch for—for example, `storage.buckets.get`. Event Threat Detection generates a finding if a custom IAM role containing this permission is granted to a principal. 

  
Unexpected Cloud API Call | `CONFIGURABLE_UNEXPECTED_CLOUD_API_CALL` | **Cloud Audit Logs:**  
[Admin Activity logs](https://docs.cloud.google.com/iam/docs/audit-logging)   
[Data Access logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access) (optional) | Detects when a specified principal calls a specified method against a specified resource. A finding is generated only if all regular expressions are matched in a single log entry.  
Template: Unexpected Cloud API Call
    
    
    {
      "metadata": {
        "severity": "SEVERITY",
        "description": "DESCRIPTION",
        "recommendation": "RECOMMENDATION"
      },
      "caller_pattern": "CALLER_PATTERN",
      "method_pattern": "METHOD_PATTERN",
      "resource_pattern": "RESOURCE_PATTERN"
    }

Replace the following:

  * `SEVERITY`: The severity of findings to be produced by this module. The valid values are `LOW`, `MEDIUM`, `HIGH`, and `CRITICAL`.
  * `DESCRIPTION`: A description of the threat that the custom module detects. This description is used to populate the `explanation` property of each finding generated by this module.
  * `RECOMMENDATION`: An explanation of the recommended steps that security teams can take to resolve the detected issue. This explanation is used to populate the `nextSteps` property of each finding generated by this module.


  * `CALLER_PATTERN`: An [RE2](https://github.com/google/re2/wiki/Syntax) regular expression to check principals against. For example, `.*` matches any principal. 
  * `METHOD_PATTERN`: An RE2 regular expression to check methods against—for example, `^cloudsql\\.instances\\.export$`.
  * `RESOURCE_PATTERN`: An RE2 regular expression to check resources against—for example, `example-project`.

  
  
## Pricing and quota

This feature is free of charge to Security Command Center Premium customers.

Event Threat Detection custom modules are subject to quota limits.

The default quota limit for the creation of custom modules is 200.

API calls to custom module methods are also subject to quota limits. The following table shows the default quota limits for custom module API calls.

API call type | Limit  
---|---  
Get, List | 1,000 API calls per minute, per organization  
Create, Update, Delete | 60 API calls per minute, per organization  
  
## Module size limits

Each Event Threat Detection custom module has a size limit of 6 MB.

## Rate limits

The following rate limits apply:

  * 30 findings per custom module per hour.
  * 200 custom module findings per parent resource (organization or project) per hour. Each finding counts towards either an organization or project, depending on which level the source custom module was created in.



These limits can't be increased.

## What's next

  * Learn how to [create and manage custom modules](https://docs.cloud.google.com/security-command-center/docs/use-custom-modules-etd).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
