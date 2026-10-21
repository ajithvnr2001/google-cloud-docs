---
url: https://docs.cloud.google.com/workload-manager/docs/evaluate/custom-rules/rego-custom-rules/
title: Write custom rules using Rego \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:07:04.849030+00:00
---

# Write custom rules using Rego  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/evaluate/custom-rules/rego-custom-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Write custom rules using Rego Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to write custom rules using the [Rego policy language](https://www.openpolicyagent.org/docs/latest/policy-language/). You can use these rules in Workload Manager to evaluate your workloads against the best practices defined for your organization.

For more information, see [About custom rules in Workload Manager](https://docs.cloud.google.com/workload-manager/docs/evaluate/custom-rules/about-custom-rules).

## Before you begin

  * Be familiar with [Rego policy language](https://www.openpolicyagent.org/docs/latest/policy-language/).



## Write custom rules using Rego

Google provides a sample GitHub repository with a set of predefined rules that you can use to evaluate your workloads. These samples cover multiple use cases. Select rules from the repository or create a rule (`.rego`) file that describes your evaluation requirements.

A custom rule has the following sections:

  * **Metadata**. The following fields define the rule metadata:

    * `DETAILS`: a short description for the rule.
    * `SEVERITY`: a user-defined value that defines the severity of violation of the rule. For example, `HIGH`, `CRITICAL`, `MEDIUM`, or `LOW`.
    * `ASSET_TYPE`: one of the supported assets. See [Supported data sources](https://docs.cloud.google.com/workload-manager/docs/evaluate/custom-rules/about-custom-rules#supported-data-sources).
    * `TAGS`: one or more tags for the rule. These tags help filter the rules.
  * **Package declaration**. For example, `templates.google.compute.instance.label`.

  * **Import statements**. For example, `data.validator.google.lib as lib`.

  * **Rule definitions**. a set of instructions that defines the rule.




### Example rules

The following sample rules are available in the [GoogleCloudPlatform/workload-manager](https://github.com/GoogleCloudPlatform/workload-manager) GitHub repository. You can upload these rules as they are to your Cloud Storage bucket and use it to run your evaluations. Alternatively, modify the rules as per your organization policies and then upload the files to a Cloud Storage bucket.

  * Example 1: ensures that there is at least one label for your VMs.
  * Example 2: ensures that your workload does not use the Compute Engine default service account.
  * Example 3: ensures that VMs in your workload don't use an external IP address.



For a full list of sample rules that you can use in Workload Manager, see the [GoogleCloudPlatform/workload-manager](https://github.com/GoogleCloudPlatform/workload-manager) GitHub repository.

### Example 1

Ensures that there is at least one tag for the Compute Engine resources.
    
    
    # Copyright 2024 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    ########################################################################
    # DETAILS:  MUST have atleast one tag
    # SEVERITY: Medium
    # ASSET_TYPE: compute.googleapis.com/Instance
    # TAGS: Tags, Cost, Management, Compute Engine
    ########################################################################
    
    package google.compute.instance.tags
    
    import data.validator.google.lib as lib
    import data.validator.google.lib.parameters as gparam
    import future.keywords
    
    asset := input.asset
    
    params:= lib.get_default(gparam.global_parameters,"compute",{})
    
    deny [{"msg": message, "details": metadata}] {
    
    	# Check if resource is in exempt list
    	exempt_list := lib.get_default(params, "exemptions", [])
    	exempt := {asset.name} & {ex | ex := exempt_list[_]}
    	not count(exempt) != 0
    
    	tags := lib.get_default(asset.resource.data, "tags", {"items": []})
    	count(tags.items) == 0
    
    	message:="Compute resource is missing tags. Ensure appropriate tags are applied."
    
    	metadata:={"name": asset.name}
    }
    

### Example 2

Ensures that your workload does not use the Compute Engine default service account
    
    
    # Copyright 2024 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    ########################################################################
    # DETAILS:  MUST NOT use default service account
    # SEVERITY: Medium
    # ASSET_TYPE: compute.googleapis.com/Instance
    # TAGS: Defaults, Management, Compute Engine
    ########################################################################
    
    package google.compute.defaultserviceAccount
    
    import data.validator.google.lib as lib
    import data.validator.google.lib.parameters as gparam
    import future.keywords
    
    asset := input.asset
    
    input_enriched := object.union({"resource": {"data": {"serviceAccounts": []}}}, asset)
    
    params := lib.get_default(gparam.global_parameters, "compute", {})
    
    deny[{
    	"msg": "Disallowed default service account",
    	"details": {"name": asset.name},
    }] {
    
    	account = input_enriched.resource.data.serviceAccounts[_]
    	endswith(account.email, params.default_sa)
    }
    

### Example 3

Ensures that VMs in your workload don't use an external IP address.
    
    
    # Copyright 2024 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    ########################################################################
    # DETAILS:  Ensure VMs dont have External IP
    # SEVERITY: High
    # ASSET_TYPE: compute.googleapis.com/Instance
    # TAGS: Security, Network, Compute Engine, External IP, VM, Virtual Machine
    ########################################################################
    
    package google.compute.instance.approved.external.ip
    
    import data.validator.google.lib as lib
    import data.validator.google.lib.parameters as gparam
    import future.keywords
    
    asset := input.asset
    
    params := lib.get_default(gparam.global_parameters, "compute", {})
    
    deny [{"msg": message, "details": metadata}] {
    
    	# Check if resource is in exempt list
    	exempt_list := lib.get_default(params, "exemptions", [])
    	exempt := {asset.name} & {ex | ex := exempt_list[_]}
    	not count(exempt) != 0
    
    	# Find network access config block w/ external IP
    	instance := asset.resource.data
    	access_config := instance.networkInterfaces[_].accessConfigs
    	count(access_config) > 0
    
    	message := sprintf("%v : VM Instance has external IP. current config: %v",[asset.name, access_config])
    	metadata := {"name": asset.name}
    }
    

## Upload the rule to a Cloud Storage bucket

After you create the `.rego` file, [upload it a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/uploading-objects). The top level of your Cloud Storage bucket must include the `/lib` and `/rules` folders:

  * `lib`
    * `parameters.rego`
    * `utils.rego`
  * `/rules`
    * `rule_name1.rego`
    * `rule_name2.rego`



## What's next

  * Learn more [about workload evaluations](https://docs.cloud.google.com/workload-manager/docs/about-evaluations).
  * Learn how to [create and run an evaluation](https://docs.cloud.google.com/workload-manager/docs/create-evaluation).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
