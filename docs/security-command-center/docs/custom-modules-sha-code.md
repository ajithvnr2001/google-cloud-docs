---
url: https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-code/
title: Code a custom module for Security Health Analytics \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:46:30.468372+00:00
---

# Code a custom module for Security Health Analytics  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-code/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Code a custom module for Security Health Analytics Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page explains how to code a custom module definition by using the [Common Expression Language (CEL)](https://opensource.google/projects/cel) and [YAML](https://yaml.org/spec/).

Use the Google Cloud CLI to upload your custom module definitions to Security Health Analytics.

In the YAML file, a custom module definition consists of a structured set of properties that you use to define the following elements of a Security Health Analytics custom module:

  * The resources to scan.
  * The detection logic to use.
  * The information to provide to your security teams so that they can quickly understand, triage, and resolve the detected issue.



The specific required and optional properties that make up a YAML definition are covered in Coding steps.

## Avoid creating redundant detectors

To control finding volume, avoid creating and running modules that contain redundant functionality.

For example, if you create a custom module that checks for encryption keys that are not rotated after 30 days, consider disabling the built-in Security Health Analytics detector `KMS_KEY_NOT_ROTATED`, because its check, which uses a value of 90 days, would be superfluous.

For more information on disabling detectors, see [Enable and disable detectors](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics#enable_and_disable_detectors).

## Coding steps

You code the definition of a custom module for Security Health Analytics as a series of YAML properties, some of which contain CEL expressions.

To code a custom definition module, follow these steps:

  1. Create a text file with the `yaml` filename extension.

  2. In the text file, create a `resource_selector` property and specify one to five resource types for the custom module to scan. A resource type cannot be specified more than once in a custom module definition. For example:
         
         resource_selector:
          resource_types:
          ‐ cloudkms.googleapis.com/CryptoKey

The resource types that you specify must be supported by Security Command Center. For a list of supported resource types, see [Supported resource types](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-overview#sha-custom-module-asset-support).

  3. Create a `predicate` property and specify one or more CEL expressions that check properties of the resource types to be scanned. Any properties the you reference in the CEL expressions must exist in the Google Cloud API definition of each resource type that you specify under `resource_selector`. To trigger a finding, the expression must resolve to `TRUE`. For example, in the following expression, only `rotationPeriod` values greater than `2592000s` trigger a finding.
         
         predicate:
          expression: resource.rotationPeriod > duration("2592000s")

For help writing CEL expressions, see the following resources:

     * [Supported resource types](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-overview#supported-resource-types). Click on each resource to see the properties that you can use in your CEL expressions.
     * Writing CEL expressions.
     * Referencing resource and policy properties in custom modules.
  4. Create a `description` property that explains the vulnerability or misconfiguration that the custom module detects. This explanation appears in each finding instance to help investigators understand the detected issue. The text must be enclosed in quotation marks. For example:
         
         description: "The rotation period of
          the identified cryptokey resource exceeds 30 days, the
          maximum rotation period that our security guidelines allow."

  5. Create a `recommendation` property that explains how to fix the detected issue. The gcloud CLI requires an escape character before certain characters, such as quotation marks. The following example shows the use of the backslash to escape each set of quotation marks:
         
         recommendation: "To fix this issue go to
           https://console.cloud.google.com/security/kms. Click the key-ring that
           contains the key. Click the key. Click \"Edit rotation period\". Then
           set the rotation period to at most 30 days."
         

If you create or update a custom module by using the Google Cloud console, escape characters are not required.

  6. Create a `severity` property and specify the default severity for the findings that are created by this module. Commonly used values for the `severity` property are `LOW`, `MEDIUM`, `HIGH`, and `CRITICAL`. For example,
         
         severity: MEDIUM

  7. Optionally, create a `custom_output` property and specify additional information to return with each finding. Specify the information to return as one or more name-value pairs. You can return either the value of a property of the scanned resource or a literal string. Properties must be specified as `resource.PROPERTY_NAME`. Literal strings must be enclosed in quotation marks. The following example shows a `custom_output` definition that returns both a property value, the value of `rotationPeriod` in the scanned `CryptoKey` resource, and a text string, `"Excessive rotation period for CryptoKey"`:
         
         custom_output:
            properties:
              - name: duration
                value_expression:
                  expression: resource.rotationPeriod
              - name: note
                value_expression:
                  expression: "'Excessive rotation period for CryptoKey'"
         

  8. Save the file to a location that your gcloud CLI can access.

  9. Upload the definition to Security Health Analytics with the following command:
         
         gcloud scc custom-modules sha create \
              --organization=organizations/ORGANIZATION_ID \
              --display-name="MODULE_DISPLAY_NAME" \
              --enablement-state="ENABLED" \
              --custom-config-from-file=DEFINITION_FILE_NAME.yaml
         

Replace the following values:

     * `ORGANIZATION_ID` with the ID of the parent organization of the custom module or replace the `--organization` flag with either `--folders` or `--project` and specify the ID of the parent folder or project.
     * `MODULE_DISPLAY_NAME` with a name to display as the finding category when the custom module returns findings. The name must be between 1 and 128 characters, start with a lowercase letter, and contain alphanumeric characters or underscores only.
     * `DEFINITION_FILE_NAME` with the path and file name of the YAML file that contains the definition of the custom module.

For more information about working with Security Health Analytics custom modules, see [Using custom modules for Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-create).




### Scan latencies for new custom modules

Creating a custom module does not trigger a new scan.

Security Health Analytics doesn't start using a new custom module until either of the following:

  * The first batch scan after you create the custom module. Depending on when you create a custom module in your batch-scan schedule, you might have to wait up to 24 hours before Security Health Analytics starts using the custom module.
  * A change to a target resource triggers a real-time scan.



### Example custom module definition

The following example shows a completed custom module definition that triggers a finding if the value of the `rotationPeriod` property of a `cloudkms.googleapis.com/CryptoKey` resource is greater than 2,592,000 seconds (30 days). The example returns two optional values in the `custom_output` section: the value of `resource.rotationPeriod` and a note as a text string.

In the example, note the following elements:

  * The type of asset or resource to check is listed in the `resource_selector` section under `resource_types`.
  * The check that the module performs on the resources, its _detection logic_ , is defined in the `predicate` section preceded by `expression`.
  * Two custom source properties, `duration` and `violation`, are defined in the `custom_output` section.
  * The explanation of the issue that was detected is specified in the `description` property.
  * The guidance for remediating the detected issue is specified on the `recommendation` property. Because quotation marks appear in the guidance, a backslash escape character is required before each quotation mark.


    
    
    severity: HIGH
    description: "Regular key rotation helps provide protection against
    compromised keys, and limits the number of encrypted messages available
    to cryptanalysis for a specific key version."
    recommendation: "To fix this issue go to
    https://console.cloud.google.com/security/kms. Click the key-ring that
    contains the key. Click the key. Click \"Edit rotation period\". Then
    set the rotation period to at most 30 days."
    resource_selector:
      resource_types:
      - cloudkms.googleapis.com/CryptoKey
    predicate:
      expression: resource.rotationPeriod > duration("2592000s")
    custom_output:
      properties:
        - name: duration
          value_expression:
            expression: resource.rotationPeriod
        - name: violation
          value_expression:
            expression:
              "'Excessive rotation period for CryptoKey'"
    

## Referencing resource and policy properties in custom modules

Regardless of which method you use to create a custom module—by using the Google Cloud console or by writing the definition yourself—you need to be able to look up the properties that you can evaluate in the custom module. You also need to know how to reference those properties in a custom module definition.

### Find the properties of a resource or policy

The properties of a Google Cloud resource are defined in the API definition of the resource. You can find this definition by clicking the resource name on [Supported resource types](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-overview#sha-custom-module-asset-support).

You can find the properties of a policy in the IAM API reference documentation. For properties of a policy, see [Policy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy).

### Reference a resource property in a custom module definition

When you create a custom module, all direct references to the property of a scanned resource must begin with `resource`, followed by any parent properties and finally the target property. The properties are separated by a period, using a JSON-style dot notation.

The following are examples of resource properties and how they can be retrieved:

  * `resourceName`: stores the full name of a resource in Cloud Asset Inventory, for example, `//cloudresourcemanager.googleapis.com/projects/296605646631`.
  * `resource.rotationPeriod`: where `rotationPeriod` is a property of `resource`.
  * `resource.metadata.name`: where `name` is a sub-property of `metadata`, which is a sub-property of `resource`.



#### Reference IAM policy properties

You can create CEL expressions that evaluate the IAM policy of a resource by referencing the resource's IAM policy properties. The only properties available are bindings and roles within bindings.

When referencing IAM policy properties, `policy` is the top-level property.

The following are examples of IAM policy properties and how they can be retrieved:

  * `policy.bindings`, where `bindings` is a property of `policy`.
  * `policy.version`, where `version` is a property of `policy`.



For more examples, see Example CEL expressions.

For information about the properties of a policy, see [Policy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy).

## Writing CEL expressions

When you create a custom module, you use CEL expressions to evaluate the properties of the scanned resource. Optionally, you can also use CEL expressions to define custom `name`-`value` pairs that return additional information with your findings.

Whether you are creating a custom module in the Google Cloud console or writing your custom module definition yourself in a YAML file, the CEL expressions you define are the same.

### CEL expressions for detection logic

You code the detection logic of a custom module by using CEL expressions with standard CEL operators to evaluate the properties of the scanned resources.

Your expressions can be simple checks of a single value or more complex compound expressions that check multiple values or conditions. Either way, the expression must resolve to a boolean `true` to trigger a finding.

If you are creating a custom module in the Google Cloud console, you write these expressions in the **Expression editor** on the **Configure module** page.

If you are coding a custom module in a YAML file, you add these expressions under the `predicate` property.

Regardless of whether you are using the Google Cloud console or a YAML file, CEL expressions that evaluate resource properties, must conform to the following rules:

  * The properties that you specify in a CEL expression must be properties of the scanned resource, as defined in the API definition of the resource type.
  * If a custom module evaluates multiple resource types, the properties that you specify in the CEL expressions must be common to each resource type the custom module evaluates.

For example, if you define a custom module called `invalid_cryptokey` that checks two resource types: `cloudkms.googleapis.com/CryptoKey` and `cloudkms.googleapis.com/CryptoKeyVersion`, you could write the following expression, because both the `CryptoKey` and `CryptoKeyVersion` resource types include the `name` property:
        
        predicate:
        resource.name.matches("projects/project1/locations/us-central1/keyRings/keyring1/cryptoKeys/.*")

However, you can't specify the following expression in the `invalid_cryptokey` custom module because the `importTime` and `rotationPeriod` properties that the expression evaluates are not shared by both resource types:
        
        predicate:
        resource.importTime >= timestamp("2022-10-02T15:01:23Z") || resource.rotationPeriod > duration("2592000s")

  * All enums in a CEL expression must be represented as strings. For example, the following is a valid expression for the `cloudkms.googleapis.com/CryptoKeyVersion` resource type:
        
        resource.state = "PENDING_GENERATION"

  * The result of the CEL expressions that you define in the `predicate` property must be a Boolean. A finding is triggered only if the result is `true`.




For more information about CEL, see the following:

  * [The CEL spec](https://github.com/google/cel-spec)
  * [The CEL language definition](https://github.com/google/cel-spec/blob/master/doc/langdef.md)



#### Example CEL expressions

The following table lists some CEL expressions that can be used to evaluate resource properties. You can use these both in the Google Cloud console and in YAML custom module definitions.

**Resource type** | **Explanation** | **CEL expression**  
---|---|---  
Any resource with an IAM policy | IAM policy check to identify members from outside domain | `!policy.bindings.all(binding, binding.members.all(m ,!m.endsWith('@gmail.com')))`  
`cloudkms.googleapis.com/CryptoKey` | Cloud KMS key rotation period check | `has(resource.rotationPeriod) && resource.rotationPeriod > duration('60h')`  
Multiple resource types with a single policy | Check if the resource name starts with `dev` or `devAccess` based on resource type | `(resource.type == 'compute.googleapis.com/Disk' && resource.name.startsWith('projects/PROJECT_ID/regions/ REGION/disks/devAccess')) || (resource.type == 'compute.googleapis.com/Instance ' && resource.name.startsWith('projects/PROJECT_ID/zones/REGION/instances/dev-'))`  
`compute.googleapis.com/Network` | Virtual Private Cloud peering rule to match network peers | `resource.selfLink.matches('https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/default') || resource.peerings.exists(p, p.network.matches('https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/shared$'))`  
`cloudfunctions.googleapis.com/CloudFunction` | Only allow internal ingress traffic for Cloud Run function  | `has(resource.ingressSettings) && resource.ingressSettings.matches('ALLOW_INTERNAL_ONLY')`  
`compute.googleapis.com/Instance` | Resource name matches pattern | `resource.name.matches('^gcp-vm-(linux|windows)-v\\d+$')`  
`serviceusage.googleapis.com/Service` | Only allow storage-related APIs to be enabled  | `resource.state == 'ENABLED' && !( resource.name.matches('storage-api.googleapis.com') || resource.name.matches('bigquery-json.googleapis.com') || resource.name.matches('bigquery.googleapis.com') || resource.name.matches('sql-component.googleapis.com') || resource.name.matches('spanner.googleapis.com'))`  
`sqladmin.googleapis.com/Instance` | Only allowlisted public IPs are allowed  | `(resource.instanceType == 'CLOUD_SQL_INSTANCE' && resource.backendType == 'SECOND_GEN' && resource.settings.ipConfiguration.ipv4Enabled ) && !(resource.ipAddresses.all(ip, ip.type != 'PRIMARY' || ip.ipAddress.matches('IP_ADDRESS'))))`  
`dataproc.googleapis.com/Cluster` | Check if project IDs in a Managed Service for Apache Spark cluster contain the substrings testing or development | `has(resource.projectId) && resource.projectId.contains('testing') || resource.projectId.contains('development')`  
  
### CEL expressions for custom finding properties

Optionally, to return additional information with each finding that can be used in finding queries, you can define up to ten custom properties to return with the findings that are generated by your custom modules.

The custom properties appear in the source properties of the finding in the its JSON and under the **Source properties** tab of the finding details in Google Cloud console.

You define custom properties as `name`-`value` pairs.

If you are creating a custom module in the Google Cloud console, you define the `name`-`value` pairs in the **Custom finding properties** section on the **Define finding details** page.

If you are coding a custom module in a YAML file, you list the `name`-`value` pairs as `properties` under the `custom_output` property.

Regardless of whether you are using the Google Cloud console or a YAML file, the following rules apply:

  * Specify `name` as a text string without quotation marks.
  * Specify `value` as one of the following:

    * To return the value of a property, specify the property in the following format:

`RESOURCE_TYPE.PROPERTY.PROPERTY_TO_RETURN`

In the example:

    * `RESOURCE_TYPE` can be either `resource` or `policy`.
    * `PROPERTY` one or more parent properties of the property that contains the value to return.
    * `PROPERTY_TO_RETURN` is the property that contains the value to return.

    * To return a text string, enclose the string in quotation marks.




The following example shows two `name`-`value` pairs properly defined under `custom_output` in a YAML file:
    
    
    custom_output:
      properties:
        - name: duration
          value_expression:
            expression: resource.name
        - name: property_with_text
          value_expression:
            expression: "'Note content'"

## What's next

To test, submit, view, and update custom modules, see the following pages:

  * To test custom modules, see [Test custom modules for Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-test).
  * To upload, view, and update custom modules, see [Creating and managing custom modules for Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-create).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
