---
url: https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1alpha.types.OSPolicy.Resource
title: Class Resource (1.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:38.264156+00:00
---

# Class Resource (1.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1alpha.types.OSPolicy.Resource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Resource (1.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.26.0 (latest)  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.2  1.19.0  1.18.1  1.17.5  1.16.0  1.15.3  1.14.1  1.13.0  1.12.4  1.11.2  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.2  1.4.0  1.3.2  1.2.0  1.1.0  1.0.0  0.1.2 
    
    
    Resource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An OS policy resource is used to define the desired state configuration and provides a specific functionality like installing/removing packages, executing a script etc.

The system ensures that resources are always in their desired state by taking necessary actions if they have drifted from their desired state.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`id` |  `str`   
Required. The id of the resource with the following restrictions: \- Must contain only lowercase letters, numbers, and hyphens. \- Must start with a letter. \- Must be between 1-63 characters. \- Must end with a number or a letter. \- Must be unique within the OS policy.   
`pkg` |  `[google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.PackageResource](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.PackageResource)`   
Package resource This field is a member of `oneof`_ `resource_type`.   
`repository` |  `[google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.RepositoryResource](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.RepositoryResource)`   
Package repository resource This field is a member of `oneof`_ `resource_type`.   
`exec_` |  `[google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.ExecResource](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.ExecResource)`   
Exec resource This field is a member of `oneof`_ `resource_type`.   
`file` |  `[google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.FileResource](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1alpha.types.OSPolicy.Resource.FileResource)`   
File resource This field is a member of `oneof`_ `resource_type`.   
  
## Classes 

### ExecResource
    
    
    ExecResource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A resource that allows executing scripts on the VM.

The `ExecResource` has 2 stages: `validate` and `enforce` and both stages accept a script as an argument to execute.

When the `ExecResource` is applied by the agent, it first executes the script in the `validate` stage. The `validate` stage can signal that the `ExecResource` is already in the desired state by returning an exit code of `100`. If the `ExecResource` is not in the desired state, it should return an exit code of `101`. Any other exit code returned by this stage is considered an error.

If the `ExecResource` is not in the desired state based on the exit code from the `validate` stage, the agent proceeds to execute the script from the `enforce` stage. If the `ExecResource` is already in the desired state, the `enforce` stage will not be run. Similar to `validate` stage, the `enforce` stage should return an exit code of `100` to indicate that the resource in now in its desired state. Any other exit code is considered an error.

NOTE: An exit code of `100` was chosen over `0` (and `101` vs `1`) to have an explicit indicator of `in desired state`, `not in desired state` and errors. Because, for example, Powershell will always return an exit code of `0` unless an `exit` statement is provided in the script. So, for reasons of consistency and being explicit, exit codes `100` and `101` were chosen.

### File
    
    
    File(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A remote or local file.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### FileResource
    
    
    FileResource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A resource that manages the state of a file.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### PackageResource
    
    
    PackageResource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A resource that manages a system package.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### RepositoryResource
    
    
    RepositoryResource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A resource that manages a package repository.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
