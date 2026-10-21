---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/assured/workloads/create/
title: gcloud alpha assured workloads create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:45:44.138664+00:00
---

# gcloud alpha assured workloads create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/assured/workloads/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha assured workloads create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha assured workloads create - create a new Assured Workloads environment 
SYNOPSIS
    

`gcloud alpha assured workloads create` [[`WORKLOAD_ID`] `--external-identifier`=`EXTERNAL_IDENTIFIER` | `--workload-id`=`FLAG_WORKLOAD_ID`] `--location`=`LOCATION` `--organization`=`ORGANIZATION` [`--async`] [`--version`=`VERSION`; default="v1"] [`--billing-account`=`BILLING_ACCOUNT` `--compliance-regime`=`COMPLIANCE_REGIME` `--display-name`=`DISPLAY_NAME` `--enable-sovereign-controls`=`ENABLE_SOVEREIGN_CONTROLS` `--labels`=[`KEY`=`VALUE`,…] `--next-rotation-time`=`NEXT_ROTATION_TIME` `--partner`=`PARTNER` `--partner-permissions`=[`KEY`=`VALUE`,…] `--partner-services-billing-account`=`PARTNER_SERVICES_BILLING_ACCOUNT` `--provisioned-resources-parent`=`PROVISIONED_RESOURCES_PARENT` `--resource-settings`=[`KEY`=`VALUE`,…] `--rotation-period`=`ROTATION_PERIOD`] [`--cmek-dedicated-project-config`=[`PROPERTY`=`VALUE`,…] `--cmek-key-ring`=`CMEK_KEY_RING` `--description`=`DESCRIPTION` `--framework`=`FRAMEWORK` `--framework-major-revision`=`FRAMEWORK_MAJOR_REVISION` `--cloud-control-config`=[`PROPERTY`=`VALUE`,…] | `--cloud-control-configs-from-file`=`CLOUD_CONTROL_CONFIGS_FROM_FILE` `--new-folder-config`=[`PROPERTY`=`VALUE`,…] | `--new-project-config`=[`PROPERTY`=`VALUE`,…] | `--target-folder`=`TARGET_FOLDER` | `--target-project`=`TARGET_PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new Assured Workloads environment. 
EXAMPLES
     The following example command creates a new Assured Workloads environment with these properties: 

  * belonging to an organization with ID 123 
  * located in the `us-central1` region 
  * display name `Test-Workload`
  * compliance regime `FEDRAMP_MODERATE`
  * billing account `billingAccounts/456`
  * first key rotation set for 10:15am on the December 30, 2020 
  * key rotation interval set for every 48 hours 
  * with the label: key = `LabelKey1`, value = `LabelValue1`
  * with the label: key = `LabelKey2`, value = `LabelValue2`
  * provisioned resources parent `folders/789`
  * with custom project ID `my-custom-id` for consumer project 
  * with external identifier for the workload of `external-id`


    
    
    gcloud alpha assured workloads create --organization=123 --location=us-central1 --display-name=Test-Workload --compliance-regime=FEDRAMP_MODERATE --billing-account=billingAccounts/456 --next-rotation-time=2020-12-30T10:15:00.00Z --rotation-period=172800s --labels=LabelKey1=LabelValue1,LabelKey2=LabelValue2 --provisioned-resources-parent=folders/789 --resource-settings=consumer-project-id=my-custom-id --external-identifier=external-id

The following example command creates a new Partner Assured Workloads, with the following properties: 

  * belonging to an organization with ID 123 
  * located in the `me-central2` region 
  * display name `Test-Workload`
  * partner `CNTXT`
  * partner services billing account `billingAccounts/789`
  * billing account `billingAccounts/456`
  * data logs viewer partner permission enabled 
  * first key rotation set for 10:15am on the December 30, 2020 
  * key rotation interval set for every 48 hours 
  * with the label: key = `LabelKey1`, value = `LabelValue1`
  * with the label: key = `LabelKey2`, value = `LabelValue2`
  * provisioned resources parent `folders/789`
  * with custom project ID `my-custom-id` for consumer project 
  * with external identifier for the workload of `external-id`


    
    
    gcloud alpha assured workloads create --organization=123 --location=me-central2 --display-name=Test-Workload --compliance-regime=ASSURED_WORKLOADS_FOR_PARTNERS --partner=SOVEREIGN_CONTROLS_BY_CNTXT --partner-services-billing-account=billingAccounts/01BF3F-2C6DE5-30C607 --partner-permissions=data-logs-viewer=true --billing-account=billingAccounts/456 --next-rotation-time=2020-12-30T10:15:00.00Z --rotation-period=172800s --labels=LabelKey1=LabelValue1,LabelKey2=LabelValue2 --provisioned-resources-parent=folders/789 --resource-settings=consumer-project-id=my-custom-id --external-identifier=external-id

The following example command creates a new Assured Workloads environment onboarding an existing project (V2): 

  * belonging to an organization with ID 123 
  * located in the `us-central1` region 
  * description `My Workload`
  * onboarding existing project `projects/456`
  * compliance framework `fedramp-moderate`
  * control configuration specified from file `controls.yaml`


    
    
    gcloud alpha assured workloads create my-workload --organization=123 --location=us-central1 --description="My Workload" --target-project=projects/456 --framework=fedramp-moderate --cloud-control-configs-from-file=controls.yaml --version=v2

The following example command creates a new Assured Workloads environment provisioning a new project with CMEK (V2): 

  * belonging to an organization with ID 123 
  * located in the `us-central1` region 
  * description `CMEK Workload`
  * provisioning a new project with ID `custom-id` and billing account `billingAccounts/456`
  * compliance framework `il4`
  * KMS key ring `projects/kms-p/locations/us-central1/keyRings/r1`
  * control configuration specified from file `controls.yaml`


    
    
    gcloud alpha assured workloads create --organization=123 --location=us-central1 --description="CMEK Workload" --new-project-config=project_id=custom-id,billing_account=billingAccounts/456 --framework=il4 --cmek-key-ring=projects/kms-p/locations/us-central1/keyRings/r1 --cloud-control-configs-from-file=controls.yaml --version=v2

POSITIONAL ARGUMENTS
    

At most one of these can be specified: 

[`WORKLOAD_ID`]
     User-assigned unique identifier for the workload. If omitted, generated by the server. 
`--external-identifier`=`EXTERNAL_IDENTIFIER`
     The external identifier of the Assured Workloads environment. 
`--workload-id`=`FLAG_WORKLOAD_ID`
     User-assigned unique identifier for the workload. 
REQUIRED FLAGS
    

`--location`=`LOCATION`
     The location of the Assured Workloads environment. For a current list of supported LOCATION values, see [Assured Workloads locations](https://cloud.google.com/assured-workloads/docs/locations). 
`--organization`=`ORGANIZATION`
     The parent organization of the Assured Workloads environment, provided as an organization ID. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--version`=`VERSION`; default="v1"
     Assured Workloads API version to use. Options are v1 and v2. Defaults to v1. `VERSION` must be one of: `v1`, `v2`. 
V1 CREATION FLAGS
    

`--billing-account`=`BILLING_ACCOUNT`
     The billing account of the new Assured Workloads environment, for example, billingAccounts/0000AA-AAA00A-A0A0A0 (V1). 
`--compliance-regime`=`COMPLIANCE_REGIME`
     The compliance regime of the new Assured Workloads environment (V1). `COMPLIANCE_REGIME` must be one of: `assured-workloads-for-partners`, `au-regions-and-us-support`, `australia-data-boundary-and-support`, `ca-protected-b`, `ca-regions-and-support`, `canada-controlled-goods`, `canada-data-boundary-and-support`, `cjis`, `data-boundary-for-canada-controlled-goods`, `data-boundary-for-canada-protected-b`, `data-boundary-for-cjis`, `data-boundary-for-fedramp-high`, `data-boundary-for-fedramp-moderate`, `data-boundary-for-il2`, `data-boundary-for-il4`, `data-boundary-for-il5`, `data-boundary-for-irs-publication-1075`, `data-boundary-for-itar`, `eu-data-boundary-and-support`, `eu-regions-and-support`, `fedramp-high`, `fedramp-moderate`, `healthcare-and-life-sciences-controls`, `healthcare-and-life-sciences-controls-us-support`, `hipaa`, `hitrust`, `il2`, `il4`, `il5`, `irs-1075`, `isr-regions`, `isr-regions-and-support`, `israel-data-boundary-and-support`, `itar`, `japan-data-boundary`, `jp-regions-and-support`, `ksa-data-boundary-with-access-justifications`, `ksa-regions-and-support-with-sovereignty-controls`, `regional-controls`, `regional-data-boundary`, `switzerland-data-boundary-with-access-justifications`, `us-data-boundary-and-support`, `us-data-boundary-for-healthcare-and-life-sciences`, `us-data-boundary-for-healthcare-and-life-sciences-with-support`, `us-regional-access`. 
`--display-name`=`DISPLAY_NAME`
     The display name of the new Assured Workloads environment (V1). 
`--enable-sovereign-controls`=`ENABLE_SOVEREIGN_CONTROLS`
     If true, enable sovereign controls for the new Assured Workloads environment, currently only supported by EU_REGIONS_AND_SUPPORT 
`--labels`=[`KEY`=`VALUE`,…]
     The labels of the new Assured Workloads environment, for example, LabelKey1=LabelValue1,LabelKey2=LabelValue2 
`--next-rotation-time`=`NEXT_ROTATION_TIME`
     The next rotation time of the KMS settings of new Assured Workloads environment, for example, 2020-12-30T10:15:30.00Z 
`--partner`=`PARTNER`
     The partner choice when creating a workload managed by local trusted partners. `PARTNER` must be one of: `local-controls-by-s3ns`, `sovereign-controls-by-cntxt`, `sovereign-controls-by-cntxt-no-ekm`, `sovereign-controls-by-psn`, `sovereign-controls-by-sia-minsait`, `sovereign-controls-by-t-systems`, `spain-data-boundary-by-telefonica`. 
`--partner-permissions`=[`KEY`=`VALUE`,…]
     The partner permissions for the partner regime, for example, data-logs-viewer=true/false 
`--partner-services-billing-account`=`PARTNER_SERVICES_BILLING_ACCOUNT`
     Billing account necessary for purchasing services from Sovereign Partners. This field is required for creating SIA/PSN/CNTXT partner workloads. The caller should have 'billing.resourceAssociations.create' IAM permission on this billing-account. The format of this string is billingAccounts/AAAAAA-BBBBBB-CCCCCC 
`--provisioned-resources-parent`=`PROVISIONED_RESOURCES_PARENT`
     The parent of the provisioned projects, for example, folders/{FOLDER_ID} 
`--resource-settings`=[`KEY`=`VALUE`,…]
     A comma-separated, key=value map of custom resource settings such as custom project ids, for example: consumer-project-id={CONSUMER_PROJECT_ID} Note: Currently only encryption-keys-project-id, encryption-keys-project-name and keyring-id are supported. The encryption-keys-project-id, encryption-keys-project-name and keyring-id settings can be specified only if KMS settings are provided 
`--rotation-period`=`ROTATION_PERIOD`
     The rotation period of the KMS settings of the new Assured Workloads environment, for example, 172800s 
V2 CREATION FLAGS
    

`--cmek-dedicated-project-config`=[`PROPERTY`=`VALUE`,…]
     Dedicated KMS project configuration (valid only with folder targets). 
`--cmek-key-ring`=`CMEK_KEY_RING`
     KMS Key Ring resource path for Customer-Managed Encryption Keys (V2). 
`--description`=`DESCRIPTION`
     User-friendly description for the workload (V2). 
`--framework`=`FRAMEWORK`
     Compliance framework resource name or ID, for example, fedramp-moderate (V2). 
`--framework-major-revision`=`FRAMEWORK_MAJOR_REVISION`
     Major revision ID of the compliance framework (V2). 
At most one of these can be specified: 

`--cloud-control-config`=[`PROPERTY`=`VALUE`,…]
     Repeated inline control configuration (V2). 
`--cloud-control-configs-from-file`=`CLOUD_CONTROL_CONFIGS_FROM_FILE`
     Path to JSON/YAML file specifying multiple control configurations (V2). 
At most one of these can be specified: 

`--new-folder-config`=[`PROPERTY`=`VALUE`,…]
     JSON/YAML specification for provisioning a new folder (V2). 
`--new-project-config`=[`PROPERTY`=`VALUE`,…]
     JSON/YAML specification for provisioning a new project (V2). 
`--target-folder`=`TARGET_FOLDER`
     Existing Folder ID to onboard into Assured Workloads (V2). 
`--target-project`=`TARGET_PROJECT`
     Existing Project ID or project number to onboard into Assured Workloads (V2). 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud assured workloads create](https://docs.cloud.google.com/sdk/gcloud/reference/assured/workloads/create)
    
    
    [gcloud beta assured workloads create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/assured/workloads/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
