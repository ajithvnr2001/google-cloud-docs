---
url: https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1alpha.types.InstanceOSPoliciesCompliance
title: Class InstanceOSPoliciesCompliance (1.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:15.364324+00:00
---

# Class InstanceOSPoliciesCompliance (1.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1alpha.types.InstanceOSPoliciesCompliance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class InstanceOSPoliciesCompliance (1.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.26.0 (latest)  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.2  1.19.0  1.18.1  1.17.5  1.16.0  1.15.3  1.14.1  1.13.0  1.12.4  1.11.2  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.2  1.4.0  1.3.2  1.2.0  1.1.0  1.0.0  0.1.2 
    
    
    InstanceOSPoliciesCompliance(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

This API resource represents the OS policies compliance data for a Compute Engine virtual machine (VM) instance at a given point in time.

A Compute Engine VM can have multiple OS policy assignments, and each assignment can have multiple OS policies. As a result, multiple OS policies could be applied to a single VM.

You can use this API resource to determine both the compliance state of your VM as well as the compliance state of an individual OS policy.

For more information, see `View compliance <https://cloud.google.com/compute/docs/os-configuration-management/view-compliance>`__.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Output only. The `InstanceOSPoliciesCompliance` API resource name. Format: `projects/{project_number}/locations/{location}/instanceOSPoliciesCompliances/{instance_id}`  
`instance` |  `str`   
Output only. The Compute Engine VM instance name.   
`state` |  `[google.cloud.osconfig_v1alpha.types.OSPolicyComplianceState](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1alpha.types.OSPolicyComplianceState)`   
Output only. Compliance state of the VM.   
`detailed_state` |  `str`   
Output only. Detailed compliance state of the VM. This field is populated only when compliance state is `UNKNOWN`. It may contain one of the following values: \- `no-compliance-data`: Compliance data is not available for this VM. \- `no-agent-detected`: OS Config agent is not detected for this VM. \- `config-not-supported-by-agent`: The version of the OS Config agent running on this VM does not support configuration management. \- `inactive`: VM is not running. \- `internal-service-errors`: There were internal service errors encountered while enforcing compliance. \- `agent-errors`: OS config agent encountered errors while enforcing compliance.   
`detailed_state_reason` |  `str`   
Output only. The reason for the `detailed_state` of the VM (if any).   
`os_policy_compliances` |  `MutableSequence[[google.cloud.osconfig_v1alpha.types.InstanceOSPoliciesCompliance.OSPolicyCompliance](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1alpha.types.InstanceOSPoliciesCompliance.OSPolicyCompliance)]`   
Output only. Compliance data for each `OSPolicy` that is applied to the VM.   
`last_compliance_check_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Timestamp of the last compliance check for the VM.   
`last_compliance_run_id` |  `str`   
Output only. Unique identifier for the last compliance run. This id will be logged by the OS config agent during a compliance run and can be used for debugging and tracing purpose.   
  
## Classes 

### OSPolicyCompliance
    
    
    OSPolicyCompliance(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Compliance data for an OS policy

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
