---
url: https://docs.cloud.google.com/deployment-manager/docs/migrations/storage-buckets-setiampolicy/
title: Replacing the setIamPolicy Action with a supported resource type \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:46:58.771599+00:00
---

# Replacing the setIamPolicy Action with a supported resource type  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/migrations/storage-buckets-setiampolicy/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Replacing the setIamPolicy Action with a supported resource type Stay organized with collections  Save and categorize content based on your preferences. 

The [Actions feature](https://docs.cloud.google.com/deployment-manager/docs/migrations/actions) is an alpha feature that expands the range of API methods that Deployment Manager can call. Because this feature is unsupported, we recommend that you [migrate your existing usage](https://docs.cloud.google.com/deployment-manager/docs/migrations/actions#migrating) of Actions to supported alternatives. The commonly-used Action `storage.buckets.setIamPolicy` corresponds to an existing Deployment Manager resource type, `virtual.buckets.iamMemberBinding`, which you can use to replace it.

# Migrating your deployment from `storage.buckets.setIamPolicy` to `virtual.buckets.iamMemberBinding`

The `virtual.buckets.iamMemberBinding` resource is a virtual resource that represents an Identity and Access Management (IAM) policy binding. Its full type is `gcp-types/storage-v1:virtual.buckets.iamMemberBinding`.

`virtual.buckets.iamMemberBinding` has a custom implementation of the create, read, update, and delete (CRUD) operations from the Deployment Manager backend. It calls a similar method to the method called by the Action `storage.buckets.setIamPolicy`, but it is modeled as a normal resource instead of an Action, and it follows the same lifecycle as a normal resource type.

To migrate your deployment, replace your usage of the Action `storage.buckets.setIamPolicy` with the resource `virtual.buckets.iamMemberBinding` in all of your deployment configuration files. If you have multiple bindings, you might need multiple resources to implement the same logic across them. The virtual type doesn't replace any existing bindings on a resource, but patches the new ones in.

## Usage examples for migrating manually

To complete the migration manually, refer to the following usage examples. In certain cases, such as the application of multiple IAM bindings, you might need to add `metadata.dependsOn` or references to other resources to the `iamMemberBinding` resource to avoid situations such as race conditions.

### YAML + Jinja

The following is an example of how the `setIamPolicy` Action is used in a YAML configuration file. This approach is unsupported, and should be replaced with usage of the `iamMemberBinding` virtual resource:
    
    
    - name: patch-iam-policy
      action: gcp-types/storage-v1:storage.buckets.setIamPolicy
      properties:
        bucket:
        policy: # existing policy, e.g. from a getIamPolicyAction
        gcpIamPolicyPatch:
          add:
    

The following sample shows the recommended usage of the `iamMemberBinding` virtual resource in a YAML and Jinja template:
    
    
    {% set BUCKETNAME = "bucket-" + env["deployment"] %}
    
    resources:
    - type: gcp-types/storage-v1:buckets
      name: {{ BUCKETNAME }}
      properties:
      location: US
        storageClass: STANDARD
    - type: gcp-types/storage-v1:virtual.buckets.iamMemberBinding
      name: test-bucket-iam
      properties:
        bucket: $(ref.{{ BUCKETNAME }}.name)
        member: projectEditor:{{ env["project"] }}
        role: roles/storage.admin
    

### Python

The following is an example of how the `setIamPolicy` Action is used in a Python template. This approach is unsupported, and should be replaced with usage of the `iamMemberBinding` virtual resource:
    
    
    resources.append({
            'name': 'add-iam-policy',
            'action': 'gcp-types/storage-v1:storage.buckets.setIamPolicy',
            'properties': {
                'bucket': gcs_bucket,
                'userProject': project,
                'policy': '$(ref.get-iam-policy)',
                'gcpIamPolicyPatch': {
                    'add': [{
                        'roles':
                            'roles/storage.objectViewer',
                        'members': [
                            'serviceAccount:$(ref.%s.serviceAccount)' % tpu_name
                        ]
                    }]
                }
            }
        })

The following sample shows the recommended usage of the `iamMemberBinding` virtual resource in a Python template:
    
    
    iam_policy_resource = {
        'name': policy_name,
        'type': 'gcp-types/storage-v1:virtual.buckets.iamMemberBinding',
        'properties':
            {
               'bucket': '$(ref.{}.name)'.format(context.env['name']),
               'role': role['role'],
               'member': member,
             }
    }

You can find additional samples related to the [`gcs-bucket.py` template](https://github.com/GoogleCloudPlatform/cloud-foundation-toolkit/tree/master/dm/templates/gcs_bucket) in the [`cloud-foundation-toolkit` repository](https://github.com/GoogleCloudPlatform/cloud-foundation-toolkit) on GitHub. For a detailed demonstration of the process of converting the `gcs-bucket.py` template from using the Action `setIamPolicy` to using the virtual resource `iamMemberBinding`, refer to the [example conversion](https://github.com/GoogleCloudPlatform/cloud-foundation-toolkit/pull/453/files). You can also find [usage examples](https://github.com/GoogleCloudPlatform/cloud-foundation-toolkit/tree/master/dm/templates/gcs_bucket/examples) of the converted template.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
