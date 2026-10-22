---
url: https://docs.cloud.google.com/docs/terraform/policy-validation/create-cai-constraints/
title: Create CAI constraints \u00a0|\u00a0 Terraform on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:52.977631+00:00
---

# Create CAI constraints  |  Terraform on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/terraform/policy-validation/create-cai-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Terraform on Google Cloud ](https://docs.cloud.google.com/docs/terraform)
  * [ Guides ](https://docs.cloud.google.com/docs/terraform/terraform-overview)



Send feedback 

#  Create CAI constraints Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Before you begin

  * [Create a policy library](https://docs.cloud.google.com/docs/terraform/policy-validation/create-policy-library).



## Constraint Framework

`gcloud beta terraform vet` uses [Constraint Framework](https://github.com/open-policy-agent/frameworks/tree/master/constraint#opa-constraint-framework) policies, which consist of _constraints_ and _constraint templates_. The difference between the two is as follows:

  * A constraint template is like a function declaration; it defines a rule in [Rego](https://www.openpolicyagent.org/docs/how-do-i-write-policies.html) and optionally takes input parameters.
  * A constraint is a file that references a constraint template and defines the input parameters to pass to it and the resources covered by the policy.



This allows you to avoid repetition. You can write a constraint template with a generic policy, then write any number of constraints that provide different input parameters or different resource matching rules.

## CAI Assets vs Terraform resources

Cloud Asset Inventory Assets are a standard Google data export format that is available [for many Google Cloud resources](https://docs.cloud.google.com/docs/cloud-asset-inventory/overview#supported_resource_types). CAI data is only usually available after a resource has been created or updated. However, by converting Terraform resource changes to CAI Asset data, `gcloud beta terraform vet` allows you to write a policy one time and use it both before apply and as an audit check with compatible tools.

### Compatible tools

_The following tools are not official Google products and are not supported._ However, they might be compatible with policies written for `gcloud beta terraform vet`:

  * [CFT Scorecard](https://github.com/GoogleCloudPlatform/cloud-foundation-toolkit/blob/master/cli/docs/scorecard.md)
  * [Forseti](https://opensource.google/projects/forsetisecurity)



## Create a constraint template

Before you develop your constraint template, verify that the Asset you want to write a policy for is supported by both [Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/supported-asset-types) and by `gcloud beta terraform vet`.

Creating a constraint template takes the following steps:

  1. Collect sample data.
  2. Write [Rego](https://www.openpolicyagent.org/docs/how-do-i-write-policies.html).
  3. Test your Rego.
  4. Set up a constraint template skeleton.
  5. Inline your Rego.
  6. Set up a constraint.



### Collect sample data

In order to write a constraint template, you need to have sample data to operate on. CAI-based constraints operate on **CAI Asset data**. Gather sample data by creating resources of the appropriate type and exporting those resources as JSON, as described in the [CAI quickstart](https://cloud.google.com/resource-manager/docs/cloud-asset-inventory/quickstart-cloud-asset-inventory).

Here is an example JSON export for a Compute Address:
    
    
    [
      {
        "name": "//compute.googleapis.com/projects/789/regions/us-central1/addresses/my-internal-address",
        "asset_type": "compute.googleapis.com/Address",
        "ancestors: [
          "organization/123",
          "folder/456",
          "project/789"
        ],
        "resource": {
          "version": "v1",
          "discovery_document_uri": "https://www.googleapis.com/discovery/v1/apis/compute/v1/rest",
          "discovery_name": "Address",
          "parent": "//cloudresourcemanager.googleapis.com/projects/789",
          "data": {
            "address": "10.0.42.42",
            "addressType": "INTERNAL",
            "name": "my-internal-address",
            "region": "projects/789/global/regions/us-central1"
          }
        }
      },
    ]
    

### Write Rego

After you have sample data, you can write the logic for your constraint template in [Rego](https://www.openpolicyagent.org/docs/how-do-i-write-policies.html). Your Rego must have a `violations` rule. The asset being reviewed is available as `input.review`. Constraint parameters are available as `input.parameters`. For example, to require that `compute.googleapis.com/Address` assets have an allowed `addressType`, write:
    
    
    # validator/gcp_compute_address_address_type_allowlist_constraint_v1.rego
    package templates.gcp.GCPComputeAddressAddressTypeAllowlistConstraintV1
    
    violation[{
      "msg": message,
      "details": metadata,
    }] {
      asset := input.review
      asset.asset_type == "compute.googleapis.com/Address"
    
      allowed_address_types := input.parameters.allowed_address_types
      count({asset.resource.data.addressType} & allowed_address_types) >= 1
      message := sprintf(
        "Compute address %s has a disallowed address_type: %s",
        [asset.name, asset.resource.data.addressType]
      )
      metadata := {"asset": asset.name}
    }
    

#### Name your constraint template

The previous example uses the name `GCPComputeAddressAddressTypeAllowlistConstraintV1`. This is a unique identifier for each constraint template. We recommend following these naming guidelines:

  * General format: `GCP{resource}{feature}Constraint{version}`. Use CamelCase. (In other words, capitalize each new word.)
  * For single-resource constraints, follow [gcloud](https://cloud.google.com/sdk/gcloud/) group names for resource naming. For example, use "compute" instead of "gce", "sql" instead of "cloud-sql", and "container-cluster" instead of "gke".
  * If a template applies to more than one type of resource, omit the resource part and only include the feature (example: "GCPAddressTypeAllowlistConstraintV1").
  * The version number does not follow semver form; it is just a single number. This effectively makes every version of a template an unique template.



We recommend using a name for your Rego file that matches the constraint template name, but using snake_case. In other words, convert the name to lowercase separate words with `_`. For the previous example, the recommended filename is `gcp_compute_address_address_type_allowlist_constraint_v1.rego`

### Test your Rego

You can test your Rego manually with the [Rego Playground](https://play.openpolicyagent.org/). Make sure to use non-sensitive data.

We recommend writing [automated tests](https://www.openpolicyagent.org/docs/how-do-i-test-policies.html). Put your collected sample data in `validator/test/fixtures/<constraint filename>/assets/data.json` and reference it in your test file like this:
    
    
    # validator/gcp_compute_address_address_type_allowlist_constraint_v1_test.rego
    package templates.gcp.GCPComputeAddressAddressTypeAllowlistConstraintV1
    
    import data.test.fixtures.gcp_compute_address_address_type_allowlist_constraint_v1_test.assets as assets
    
    test_violation_with_disallowed_address_type {
      parameters := {
        "allowed_address_types": "EXTERNAL"
      }
      violations := violation with input.review as assets[_]
        with input.parameters as parameters
      count(violations) == 1
    }
    

Place your Rego and your test in the `validator` folder in your policy library.

### Set up a constraint template skeleton

After you have a working and tested Rego rule, you must package it as a constraint template. Constraint Framework uses Kubernetes Custom Resource Definitions as the container for the policy Rego.

The constraint template also defines what parameters are allowed as inputs from constraints, using the [OpenAPI V3](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.0.md#schemaObject) schema.

Use the same name for the skeleton as you used for your Rego. In particular:

  * Use the same filename as for your Rego. Example: `gcp_compute_address_address_type_allowlist_constraint_v1.yaml`
  * `spec.crd.spec.names.kind` must contain the template name
  * `metadata.name` must contain the template name, but lower-cased



Place the constraint template skeleton in `policies/templates`.

For the example above:
    
    
    # policies/templates/gcp_compute_address_address_type_allowlist_constraint_v1.yaml
    apiVersion: templates.gatekeeper.sh/v1beta1
    kind: ConstraintTemplate
    metadata:
      name: gcpcomputeaddressaddresstypeallowlistconstraintv1
    spec:
      crd:
        spec:
          names:
            kind: GCPComputeAddressAddressTypeAllowlistConstraintV1
          validation:
            openAPIV3Schema:
              properties:
                allowed_address_types:
                  description: "A list of address_types allowed, for example: ['INTERNAL']"
                  type: array
                  items:
                    type: string
      targets:
        - target: validation.gcp.forsetisecurity.org
          rego: |
                #INLINE("validator/gcp_compute_address_address_type_allowlist_constraint_v1.rego")
                #ENDINLINE
    

### Inline your Rego

At this point, following the previous example, your directory layout looks like this:
    
    
    | policy-library/
    |- validator/
    ||- gcp_compute_address_address_type_allowlist_constraint_v1.rego
    ||- gcp_compute_address_address_type_allowlist_constraint_v1_test.rego
    |- policies
    ||- templates
    |||- gcp_compute_address_address_type_allowlist_constraint_v1.yaml
    

If you cloned the [Google-provided policy-library repository](https://github.com/GoogleCloudPlatform/policy-library), you can run `make build` to automatically update your constraint templates in `policies/templates` with the Rego defined in `validator`.

### Set up a constraint

Constraints contain three pieces of information that `gcloud beta terraform vet` needs to properly enforce and report violations:

  * `severity`: `low`, `medium`, or `high`
  * `match`: parameters for determining if a constraint applies to a particular resource. The following match parameters are supported: 
    * `ancestries`: A list of ancestry paths to include using glob-style matching
    * `excludedAncestries`: (Optional) A list of ancestry paths to exclude using glob-style matching.
  * `parameters`: Values for the constraint template's input parameters.



Make sure that `kind` contains the constraint template name. We recommend setting `metadata.name` to a descriptive slug.

For example, to only allow `INTERNAL` address types using the previous example constraint template, write:
    
    
    # policies/constraints/gcp_compute_address_internal_only.yaml
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: GCPComputeAddressAddressTypeAllowlistConstraintV1
    metadata:
      name: gcp_compute_address_internal_only
    spec:
      severity: high
      match:
        ancestries:
        - "**"
      parameters:
        allowed_address_types:
        - "INTERNAL"
    

Matching examples:

**Ancestry path matcher** | **Description**  
---|---  
organizations/** | All organizations  
organizations/123/**  | Everything in organization 123  
organizations/123/folders/**  | Everything in organization 123 that is under a folder  
organizations/123/folders/456  | Everything in folder 456 in organization 123  
organizations/123/folders/456/projects/789 | Everything in project 789 in folder 456 in organization 123  
  
If a resource address matches values in `ancestries` and `excludedAncestries`, it is excluded.

## Limitations

Terraform plan data gives the best available representation of actual state after apply. However, in many cases, the state after apply might not be known because it is calculated on the server side. In these cases, the data is not available in the converted CAI Assets either.

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
    

### Supported resources

If you want `gcloud beta terraform vet` to add support for a resource that is not on this list, open an [enhancement request](https://github.com/GoogleCloudPlatform/terraform-google-conversion/issues/new?assignees=&labels=enhancement&projects=&template=enhancement.md) and consider [contributing code](https://github.com/GoogleCloudPlatform/terraform-google-conversion/blob/main/docs/contributing/index.md).

The list of supported resources depends on which version of `gcloud beta terraform vet` is installed. The current list of supported resources follows:

Terraform resource | Cloud Asset Inventory Assets  
---|---  
google_access_context_manager_access_policy_iam_binding | accesscontextmanager.googleapis.com/AccessPolicy  
google_access_context_manager_access_policy_iam_member | accesscontextmanager.googleapis.com/AccessPolicy  
google_access_context_manager_access_policy_iam_policy | accesscontextmanager.googleapis.com/AccessPolicy  
google_access_context_manager_service_perimeter | accesscontextmanager.googleapis.com/ServicePerimeter  
google_apigee_environment_iam_binding | apigee.googleapis.com/Environment  
google_apigee_environment_iam_member | apigee.googleapis.com/Environment  
google_apigee_environment_iam_policy | apigee.googleapis.com/Environment  
google_bigquery_dataset | bigquery.googleapis.com/Dataset  
google_bigquery_dataset_iam_binding | bigquery.googleapis.com/Dataset  
google_bigquery_dataset_iam_member | bigquery.googleapis.com/Dataset  
google_bigquery_dataset_iam_policy | bigquery.googleapis.com/Dataset  
google_bigquery_table | bigquery.googleapis.com/Table  
google_bigquery_table_iam_binding | bigquery.googleapis.com/Table  
google_bigquery_table_iam_member | bigquery.googleapis.com/Table  
google_bigquery_table_iam_policy | bigquery.googleapis.com/Table  
google_bigtable_instance | bigtableadmin.googleapis.com/Cluster, bigtableadmin.googleapis.com/Instance  
google_binary_authorization_attestor_iam_binding | binaryauthorization.googleapis.com/Attestor  
google_binary_authorization_attestor_iam_member | binaryauthorization.googleapis.com/Attestor  
google_binary_authorization_attestor_iam_policy | binaryauthorization.googleapis.com/Attestor  
google_cloud_run_domain_mapping | run.googleapis.com/DomainMapping  
google_cloud_run_service | run.googleapis.com/Service  
google_cloud_run_service_iam_binding | run.googleapis.com/Service  
google_cloud_run_service_iam_member | run.googleapis.com/Service  
google_cloud_run_service_iam_policy | run.googleapis.com/Service  
google_cloudfunctions_function | cloudfunctions.googleapis.com/CloudFunction  
google_cloudfunctions_function_iam_binding | cloudfunctions.googleapis.com/CloudFunction  
google_cloudfunctions_function_iam_member | cloudfunctions.googleapis.com/CloudFunction  
google_cloudfunctions_function_iam_policy | cloudfunctions.googleapis.com/CloudFunction  
google_compute_address | compute.googleapis.com/Address  
google_compute_backend_service_iam_binding | compute.googleapis.com/BackendService  
google_compute_backend_service_iam_member | compute.googleapis.com/BackendService  
google_compute_backend_service_iam_policy | compute.googleapis.com/BackendService  
google_compute_disk | compute.googleapis.com/Disk  
google_compute_disk_iam_binding | compute.googleapis.com/Disk  
google_compute_disk_iam_member | compute.googleapis.com/Disk  
google_compute_disk_iam_policy | compute.googleapis.com/Disk  
google_compute_firewall | compute.googleapis.com/Firewall  
google_compute_forwarding_rule | compute.googleapis.com/ForwardingRule  
google_compute_global_address | compute.googleapis.com/GlobalAddress  
google_compute_global_forwarding_rule | compute.googleapis.com/GlobalForwardingRule  
google_compute_image_iam_binding | compute.googleapis.com/Image  
google_compute_image_iam_member | compute.googleapis.com/Image  
google_compute_image_iam_policy | compute.googleapis.com/Image  
google_compute_instance | compute.googleapis.com/Instance  
google_compute_instance_iam_binding | compute.googleapis.com/Instance  
google_compute_instance_iam_member | compute.googleapis.com/Instance  
google_compute_instance_iam_policy | compute.googleapis.com/Instance  
google_compute_network | compute.googleapis.com/Network  
google_compute_region_backend_service_iam_binding | compute.googleapis.com/RegionBackendService  
google_compute_region_backend_service_iam_member | compute.googleapis.com/RegionBackendService  
google_compute_region_backend_service_iam_policy | compute.googleapis.com/RegionBackendService  
google_compute_region_disk_iam_binding | compute.googleapis.com/RegionDisk  
google_compute_region_disk_iam_member | compute.googleapis.com/RegionDisk  
google_compute_region_disk_iam_policy | compute.googleapis.com/RegionDisk  
google_compute_security_policy | compute.googleapis.com/SecurityPolicy  
google_compute_snapshot | compute.googleapis.com/Snapshot  
google_compute_ssl_policy | compute.googleapis.com/SslPolicy  
google_compute_subnetwork | compute.googleapis.com/Subnetwork  
google_compute_subnetwork_iam_binding | compute.googleapis.com/Subnetwork  
google_compute_subnetwork_iam_member | compute.googleapis.com/Subnetwork  
google_compute_subnetwork_iam_policy | compute.googleapis.com/Subnetwork  
google_container_cluster | container.googleapis.com/Cluster  
google_container_node_pool | container.googleapis.com/NodePool  
google_data_catalog_entry_group_iam_binding | datacatalog.googleapis.com/EntryGroup  
google_data_catalog_entry_group_iam_member | datacatalog.googleapis.com/EntryGroup  
google_data_catalog_entry_group_iam_policy | datacatalog.googleapis.com/EntryGroup  
google_data_catalog_tag_template_iam_binding | datacatalog.googleapis.com/TagTemplate  
google_data_catalog_tag_template_iam_member | datacatalog.googleapis.com/TagTemplate  
google_data_catalog_tag_template_iam_policy | datacatalog.googleapis.com/TagTemplate  
google_dns_managed_zone | dns.googleapis.com/ManagedZone  
google_dns_policy | dns.googleapis.com/Policy  
google_endpoints_service_consumers_iam_binding | servicemanagement.googleapis.com/ServiceConsumers  
google_endpoints_service_consumers_iam_member | servicemanagement.googleapis.com/ServiceConsumers  
google_endpoints_service_consumers_iam_policy | servicemanagement.googleapis.com/ServiceConsumers  
google_endpoints_service_iam_binding | servicemanagement.googleapis.com/Service  
google_endpoints_service_iam_member | servicemanagement.googleapis.com/Service  
google_endpoints_service_iam_policy | servicemanagement.googleapis.com/Service  
google_filestore_instance | file.googleapis.com/Instance  
google_folder_iam_binding | cloudresourcemanager.googleapis.com/Folder  
google_folder_iam_member | cloudresourcemanager.googleapis.com/Folder  
google_folder_iam_policy | cloudresourcemanager.googleapis.com/Folder  
google_folder_organization_policy | cloudresourcemanager.googleapis.com/Folder  
google_healthcare_consent_store_iam_binding | healthcare.googleapis.com/ConsentStore  
google_healthcare_consent_store_iam_member | healthcare.googleapis.com/ConsentStore  
google_healthcare_consent_store_iam_policy | healthcare.googleapis.com/ConsentStore  
google_iap_tunnel_iam_binding | iap.googleapis.com/Tunnel  
google_iap_tunnel_iam_member | iap.googleapis.com/Tunnel  
google_iap_tunnel_iam_policy | iap.googleapis.com/Tunnel  
google_iap_tunnel_instance_iam_binding | iap.googleapis.com/TunnelInstance  
google_iap_tunnel_instance_iam_member | iap.googleapis.com/TunnelInstance  
google_iap_tunnel_instance_iam_policy | iap.googleapis.com/TunnelInstance  
google_iap_web_iam_binding | iap.googleapis.com/Web  
google_iap_web_iam_member | iap.googleapis.com/Web  
google_iap_web_iam_policy | iap.googleapis.com/Web  
google_kms_crypto_key | cloudkms.googleapis.com/CryptoKey  
google_kms_crypto_key_iam_binding | cloudkms.googleapis.com/CryptoKey  
google_kms_crypto_key_iam_member | cloudkms.googleapis.com/CryptoKey  
google_kms_crypto_key_iam_policy | cloudkms.googleapis.com/CryptoKey  
google_kms_key_ring | cloudkms.googleapis.com/KeyRing  
google_kms_key_ring_iam_binding | cloudkms.googleapis.com/KeyRing  
google_kms_key_ring_iam_member | cloudkms.googleapis.com/KeyRing  
google_kms_key_ring_iam_policy | cloudkms.googleapis.com/KeyRing  
google_monitoring_alert_policy | monitoring.googleapis.com/AlertPolicy  
google_monitoring_notification_channel | monitoring.googleapis.com/NotificationChannel  
google_notebooks_instance_iam_binding | notebooks.googleapis.com/Instance  
google_notebooks_instance_iam_member | notebooks.googleapis.com/Instance  
google_notebooks_instance_iam_policy | notebooks.googleapis.com/Instance  
google_notebooks_runtime_iam_binding | notebooks.googleapis.com/Runtime  
google_notebooks_runtime_iam_member | notebooks.googleapis.com/Runtime  
google_notebooks_runtime_iam_policy | notebooks.googleapis.com/Runtime  
google_organization_iam_binding | cloudresourcemanager.googleapis.com/Organization  
google_organization_iam_custom_role | iam.googleapis.com/Role  
google_organization_iam_member | cloudresourcemanager.googleapis.com/Organization  
google_organization_iam_policy | cloudresourcemanager.googleapis.com/Organization  
google_organization_policy | cloudresourcemanager.googleapis.com/Organization  
google_privateca_ca_pool_iam_binding | privateca.googleapis.com/CaPool  
google_privateca_ca_pool_iam_member | privateca.googleapis.com/CaPool  
google_privateca_ca_pool_iam_policy | privateca.googleapis.com/CaPool  
google_privateca_certificate_template_iam_binding | privateca.googleapis.com/CertificateTemplate  
google_privateca_certificate_template_iam_member | privateca.googleapis.com/CertificateTemplate  
google_privateca_certificate_template_iam_policy | privateca.googleapis.com/CertificateTemplate  
google_project | cloudbilling.googleapis.com/ProjectBillingInfo, cloudresourcemanager.googleapis.com/Project  
google_project_iam_binding | cloudresourcemanager.googleapis.com/Project  
google_project_iam_custom_role | iam.googleapis.com/Role  
google_project_iam_member | cloudresourcemanager.googleapis.com/Project  
google_project_iam_policy | cloudresourcemanager.googleapis.com/Project  
google_project_organization_policy | cloudresourcemanager.googleapis.com/Project  
google_project_service | serviceusage.googleapis.com/Service  
google_pubsub_lite_reservation | pubsublite.googleapis.com/Reservation  
google_pubsub_lite_subscription | pubsublite.googleapis.com/Subscription  
google_pubsub_lite_topic | pubsublite.googleapis.com/Topic  
google_pubsub_schema | pubsub.googleapis.com/Schema  
google_pubsub_subscription | pubsub.googleapis.com/Subscription  
google_pubsub_subscription_iam_binding | pubsub.googleapis.com/Subscription  
google_pubsub_subscription_iam_member | pubsub.googleapis.com/Subscription  
google_pubsub_subscription_iam_policy | pubsub.googleapis.com/Subscription  
google_pubsub_topic | pubsub.googleapis.com/Topic  
google_pubsub_topic_iam_binding | pubsub.googleapis.com/Topic  
google_pubsub_topic_iam_member | pubsub.googleapis.com/Topic  
google_pubsub_topic_iam_policy | pubsub.googleapis.com/Topic  
google_redis_instance | redis.googleapis.com/Instance  
google_secret_manager_secret_iam_binding | secretmanager.googleapis.com/Secret  
google_secret_manager_secret_iam_member | secretmanager.googleapis.com/Secret  
google_secret_manager_secret_iam_policy | secretmanager.googleapis.com/Secret  
google_spanner_database | spanner.googleapis.com/Database  
google_spanner_database_iam_binding | spanner.googleapis.com/Database  
google_spanner_database_iam_member | spanner.googleapis.com/Database  
google_spanner_database_iam_policy | spanner.googleapis.com/Database  
google_spanner_instance | spanner.googleapis.com/Instance  
google_spanner_instance_iam_binding | spanner.googleapis.com/Instance  
google_spanner_instance_iam_member | spanner.googleapis.com/Instance  
google_spanner_instance_iam_policy | spanner.googleapis.com/Instance  
google_sql_database | sqladmin.googleapis.com/Database  
google_sql_database_instance | sqladmin.googleapis.com/Instance  
google_storage_bucket | storage.googleapis.com/Bucket  
google_storage_bucket_iam_binding | storage.googleapis.com/Bucket  
google_storage_bucket_iam_member | storage.googleapis.com/Bucket  
google_storage_bucket_iam_policy | storage.googleapis.com/Bucket  
google_vpc_access_connector | vpcaccess.googleapis.com/Connector  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
