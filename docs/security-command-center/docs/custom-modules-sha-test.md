---
url: https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-test/
title: Test custom modules for Security Health Analytics \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:46:46.488398+00:00
---

# Test custom modules for Security Health Analytics  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-test/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Test custom modules for Security Health Analytics Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page explains how to test Security Health Analytics custom modules in the Google Cloud console by uploading a YAML file that contains test data.

## Before you begin

Before you can test custom modules, you need to satisfy the following prerequisites:

  * All of the general prerequisites that apply to using Security Health Analytics custom modules. For the full list of prerequisites, see [Using custom modules for Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-create#before_you_begin).
  * Your user account must be granted one or more Identity and Access Management (IAM) roles that allow you to not only work with Security Command Center and custom modules, but also includes the `securitycenter.securityhealthanalyticscustommodules.test` permission. For more about the permissions and roles you need to work with custom modules, see [Required IAM permissions](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-create#iam-for-custom-modules).
  * API calls to test custom modules are subject to a quota. For more information, see [Custom module quotas](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-overview#custom_module_quotas).



## Create test resources in a YAML file

To test a custom module, you define fake resource definitions, fake policy definitions, or both in a YAML file.

The definitions do not correspond to real resource or policy instances, but the definitions must conform to the schemas of the resource or policy types that are specified in your custom modules.

In your test definitions, the only properties that you need to specify are the properties that your custom modules evaluate. You don't need to include resource properties that the custom module doesn't reference.

To test your CEL expressions in the custom module, specify property values in the test file that cause the CEL expressions to resolve to `true`.

### Format of the test data

Start the file with `testData:` on the first line, followed by one or more `- asset` definitions.
    
    
    testData:
    - asset:
        resource: ARBITRARY_ASSET_NAME_1
        assetType: RESOURCE_TYPE_1
        resourceData:
          PROPERTIES_TO_TEST_1: PROPERTY_VALUE_1
            SUB_PROPERTY: SUB_PROPERTY_VALUE
          PROPERTIES_TO_TEST_2: PROPERTY_VALUE_2
    - asset:
        resource: ARBITRARY_ASSET_NAME_2
        assetType: RESOURCE_TYPE_2
        iamPolicyData:
          PROPERTIES_TO_TEST_3: PROPERTY_VALUE_3
          PROPERTIES_TO_TEST_4: PROPERTY_VALUE_4
    

Replace the following:

  * `ARBITRARY_ASSET_NAME_N`: An arbitrary value that displays in the test results when the test is successful.
  * `RESOURCE_TYPE_N`: The type of asset or resource that the custom module checks, specified as the domain name of the API's service endpoint and resource name—for example, `cloudkms.googleapis.com/CryptoKey`.
  * `PROPERTIES_TO_TEST_N`: The properties that are used in the detection logic of the custom module to trigger a finding.
  * `PROPERTY_VALUE_N`: A value of the property that triggers a finding.
  * `SUB_PROPERTY`: A sub-property or property of another resource that the target resource references in its resource definition.



### Example test definitions

This section contains an example of a test resource definition and a test policy definition. Although the two examples are shown as being defined in separate files, `asset` definitions for resources and policies can be combined in a single `testData` file.

#### Example resource definition

The following example of a test resource definition, tests a custom module that checks whether the `rotationPeriod` property of `CryptoKey` resources exceeds `2592000` seconds (30 days). The other properties in the definition are not used in the custom module, but still conform to the schema of the resource. For the full definition of the custom module that this example tests, see [Example custom module definition](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-code#example_custom_module_definition).
    
    
    testData:
    - asset:
        resource: THE CRYPTOKEY TEST WAS SUCCESSFUL!
        assetType: cloudkms.googleapis.com/CryptoKey
        resourceData:
          nextRotationTime:  '2020-02-05T12:00:55.192645Z'
          primary:
            state: 'ENABLED'
          purpose: 'ENCRYPT_DECRYPT'
          **rotationPeriod: '2592001s'**
    

#### Example policy definition

The following is an example of a test definition for an IAM policy:
    
    
    testData:
    - asset:
        resource: //cloudresourcemanager.googleapis.com/projects/fake-project
        assetType: cloudresourcemanager.googleapis.com/Project
        iamPolicyData:
          bindings:
          - role: "roles/viewer"
            members:
            - "serviceAccount:fake-service-account@compute-system.iam.gserviceaccount.com"
            - "user:fake-email-account"
    

## Test a custom module

You can test new custom modules or existing custom modules in the Google Cloud console.

To test a custom module, follow these steps:

  1. Go to the Security Health Analytics **Modules** page in Security Command Center settings.

[Go to Modules](https://console.cloud.google.com/security/command-center/config/services/security-health-analytics/modules)

  2. Open or create a custom module for testing:

     * To create a new custom module, click **Create module** and follow the instructions in [Create custom modules](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-create#create_module).
     * To open an existing custom module, click the edit (_edit_) icon under **Actions** on the right side of the row for the module you want to test.
  3. Select the **Test module** tab.

  4. Under **Upload the YAML file** , click **Browse** to upload a file that contains sample asset data. The test runs as soon as the YAML file is uploaded.

  5. Under **Test results preview** , check the results.

     * If there are syntax or other errors in your YAML file, a floating error message displays near the bottom of the browser page.
     * If the test is a success, the test returns the following information:

       * The display name of the custom module.
       * The arbitrary name that you specify on the `resource` property in the test data file.
       * The organization, folder, or project in which the custom module was, or will be, created.

Test results are not stored or written to Security Command Center.




## What's next

  * To work with custom modules, see [Using custom modules for Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-create)
  * To work with findings in the Google Cloud console, see [Work with findings](https://docs.cloud.google.com/security-command-center/docs/how-to-work-with-findings-in-the-dashboard)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
