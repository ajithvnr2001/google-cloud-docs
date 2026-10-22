---
url: https://docs.cloud.google.com/docs/terraform/policy-validation/create-terraform-constraints/
title: Create Terraform constraints \u00a0|\u00a0 Terraform on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:26.590525+00:00
---

# Create Terraform constraints  |  Terraform on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/terraform/policy-validation/create-terraform-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Terraform on Google Cloud ](https://docs.cloud.google.com/docs/terraform)
  * [ Guides ](https://docs.cloud.google.com/docs/terraform/terraform-overview)



Send feedback 

#  Create Terraform constraints Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Before you begin

  * [Create a policy library](https://docs.cloud.google.com/docs/terraform/policy-validation/create-policy-library).



## Constraint Framework

`gcloud beta terraform vet` uses [Constraint Framework](https://github.com/open-policy-agent/frameworks/tree/master/constraint#opa-constraint-framework) policies, which consist of _constraints_ and _constraint templates_. The difference between the two is as follows:

  * A constraint template is like a function declaration; it defines a rule in [Rego](https://www.openpolicyagent.org/docs/how-do-i-write-policies.html) and optionally takes input parameters.
  * A constraint is a file that references a constraint template and defines the input parameters to pass to it and the resources covered by the policy.



This allows you to avoid repetition. You can write a constraint template with a generic policy, then write any number of constraints that provide different input parameters or different resource matching rules.

## Create a constraint template

To create a constraint template, follow these steps:

  1. Collect sample data.
  2. Write [Rego](https://www.openpolicyagent.org/docs/how-do-i-write-policies.html).
  3. Test your Rego.
  4. Set up a constraint template skeleton.
  5. Inline your Rego.
  6. Set up a constraint.



### Collect sample data

In order to write a constraint template, you need to have sample data to operate on. Terraform-based constraints operate on **resource change data** , which comes from the `resource_changes` key of [Terraform plan JSON](https://www.terraform.io/docs/internals/json-format.html).

For example, your JSON might look like this:
    
    
    // tfplan.json
    {
      "format_version": "0.2",
      "terraform_version": "1.0.10",
      "resource_changes": [
        {
          "address": "google_compute_address.internal_with_subnet_and_address",
          "mode": "managed",
          "type": "google_compute_address",
          "name": "internal_with_subnet_and_address",
          "provider_name": "registry.terraform.io/hashicorp/google",
          "change": {
            "actions": [
              "create"
            ],
            "before": null,
            "after": {
              "address": "10.0.42.42",
              "address_type": "INTERNAL",
              "description": null,
              "name": "my-internal-address",
              "network": null,
              "prefix_length": null,
              "region": "us-central1",
              "timeouts": null
            },
            "after_unknown": {
              "creation_timestamp": true,
              "id": true,
              "network_tier": true,
              "project": true,
              "purpose": true,
              "self_link": true,
              "subnetwork": true,
              "users": true
            },
            "before_sensitive": false,
            "after_sensitive": {
              "users": []
            }
          }
        }
      ],
      // other data
    }
    

### Write Rego

After you have sample data, you can write the logic for your constraint template in [Rego](https://www.openpolicyagent.org/docs/how-do-i-write-policies.html). Your Rego must have a `violations` rule. The resource change being reviewed is available as `input.review`. Constraint parameters are available as `input.parameters`. For example, to require that `google_compute_address` resources have an allowed `address_type`, write:
    
    
    # validator/tf-compute-address-address-type-allowlist-constraint-v1.rego
    package templates.gcp.TFComputeAddressAddressTypeAllowlistConstraintV1
    
    violation[{
      "msg": message,
      "details": metadata,
    }] {
      resource := input.review
      resource.type == "google_compute_address"
    
      allowed_address_types := input.parameters.allowed_address_types
      count({resource.change.after.address_type} & allowed_address_types) >= 1
      message := sprintf(
        "Compute address %s has a disallowed address_type: %s",
        [resource.address, resource.change.after.address_type]
      )
      metadata := {"resource": resource.name}
    }
    

#### Name your constraint template

The previous example uses the name `TFComputeAddressAddressTypeAllowlistConstraintV1`. This is a unique identifier for each constraint template. We recommend following these naming guidelines:

  * General format: `TF{resource}{feature}Constraint{version}`. Use CamelCase. (In other words, capitalize each new word.)
  * For single-resource constraints, follow the [Terraform provider's](https://registry.terraform.io/providers/hashicorp/google/latest/docs) conventions for product naming. For example, for `google_tags_tag` the product name is `tags` even though the API name is `resourcemanager`.
  * If a template applies to more than one type of resource, omit the resource part and only include the feature (example: "TFAddressTypeAllowlistConstraintV1").
  * The version number does not follow semver form; it is just a single number. This effectively makes every version of a template an unique template.



We recommend using a name for your Rego file that matches the constraint template name, but using snake_case. In other words, convert the name to lowercase separate words with `_`. For the previous example, the recommended filename is `tf-compute-address-address-type-allowlist-constraint-v1.rego`

### Test your Rego

You can test your Rego manually with the [Rego Playground](https://play.openpolicyagent.org/). Make sure to use non-sensitive data.

We recommend writing [automated tests](https://www.openpolicyagent.org/docs/how-do-i-test-policies.html). Put your collected sample data in `validator/test/fixtures/<constraint filename>/resource_changes/data.json` and reference it in your test file like this:
    
    
    # validator/tf-compute-address-address-type-allowlist-constraint-v1-test.rego
    package templates.gcp.TFComputeAddressAddressTypeAllowlistConstraintV1
    
    import data.test.fixtures.tf-compute-address-address-type-allowlist-constraint-v1-test.resource_changes as resource_changes
    
    test_violation_with_disallowed_address_type {
      parameters := {
        "allowed_address_types": "EXTERNAL"
      }
      violations := violation with input.review as resource_changes[_]
        with input.parameters as parameters
      count(violations) == 1
    }
    

Place your Rego and your test in the `validator` folder in your policy library.

### Set up a constraint template skeleton

After you have a working and tested Rego rule, you must package it as a constraint template. Constraint Framework uses Kubernetes Custom Resource Definitions as the container for the policy Rego.

The constraint template also defines what parameters are allowed as inputs from constraints, using the [OpenAPI V3](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.0.md#schemaObject) schema.

Use the same name for the skeleton as you used for your Rego. In particular:

  * Use the same filename as for your Rego. Example: `tf-compute-address-address-type-allowlist-constraint-v1.yaml`
  * `spec.crd.spec.names.kind` must contain the template name
  * `metadata.name` must contain the template name, but lower-cased



Place the constraint template skeleton in `policies/templates`.

For example:
    
    
    # policies/templates/tf-compute-address-address-type-allowlist-constraint-v1.yaml
    apiVersion: templates.gatekeeper.sh/v1beta1
    kind: ConstraintTemplate
    metadata:
      name: tfcomputeaddressaddresstypeallowlistconstraintv1
    spec:
      crd:
        spec:
          names:
            kind: TFComputeAddressAddressTypeAllowlistConstraintV1
          validation:
            openAPIV3Schema:
              properties:
                allowed_address_types:
                  description: "A list of address_types allowed, for example: ['INTERNAL']"
                  type: array
                  items:
                    type: string
      targets:
        - target: validation.resourcechange.terraform.cloud.google.com
          rego: |
                #INLINE("validator/tf-compute-address-address-type-allowlist-constraint-v1.rego")
                #ENDINLINE
    

### Inline your Rego

At this point, following the previous example, your directory layout looks like this:
    
    
    | policy-library/
    |- validator/
    ||- tf-compute-address-address-type-allowlist-constraint-v1.rego
    ||- tf-compute-address-address-type-allowlist-constraint-v1-test.rego
    |- policies
    ||- templates
    |||- tf-compute-address-address-type-allowlist-constraint-v1.yaml
    

If you cloned the [Google-provided policy-library repository](https://github.com/GoogleCloudPlatform/policy-library), you can run `make build` to automatically update your constraint templates in `policies/templates` with the Rego defined in `validator`.

### Set up a constraint

Constraints contain three pieces of information that `gcloud beta terraform vet` needs to properly enforce and report violations:

  * `severity`: `low`, `medium`, or `high`
  * `match`: parameters for determining if a constraint applies to a particular resource. The following match parameters are supported: 
    * `addresses`: A list of resource addresses to include using glob-style matching
    * `excludedAddresses`: (Optional) A list of resource addresses to exclude using glob-style matching.
  * `parameters`: Values for the constraint template's input parameters.



Make sure that `kind` contains the constraint template name. We recommend setting `metadata.name` to a descriptive slug.

For example, to only allow `INTERNAL` address types using the previous example constraint template, write:
    
    
    # policies/constraints/tf_compute_address_internal_only.yaml
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: TFComputeAddressAddressTypeAllowlistConstraintV1
    metadata:
      name: tf_compute_address_internal_only
    spec:
      severity: high
      match:
        addresses:
        - "**"
      parameters:
        allowed_address_types:
        - "INTERNAL"
    

Matching examples:

**Address matcher** | **Description**  
---|---  
`module.**` | All resources in any module  
`module.my_module.**` | Everything in module `my_module`  
`**.google_compute_global_forwarding_rule.*` | All google_compute_global_forwarding_rule resources in any module  
`module.my_module.google_compute_global_forwarding_rule.*` | All google_compute_global_forwarding_rule resources in `my_module`  
  
If a resource address matches values in `addresses` and `excludedAddresses`, it is excluded.

## Limitations

Terraform plan data gives the best available representation of actual state after apply. However, in many cases, the state after apply might not be known because it is calculated on the server side.

Building CAI ancestry paths is part of the process when validating policies. It uses the default project provided to get around unknown project IDs. In the case where a default project is not provided, the ancestry path defaults to `organizations/unknown`.

You can disallow unknown ancestry by adding the following constraint:
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: GCPAlwaysViolatesConstraintV1
    metadata:
      name: disallow_unknown_ancestry
      annotations:
        description: |
          Unknown ancestry is not allowed; use --project=<project> to set a
          default ancestry
    spec:
      severity: high
      match:
        ancestries:
        - "organizations/unknown"
      parameters: {}
    

## Supported resources

You can create resource change constraints for any Terraform resource from any Terraform provider.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
