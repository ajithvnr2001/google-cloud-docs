---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/osconfig/osconfigospolicyassignment/
title: OSConfigOSPolicyAssignment \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:49.483736+00:00
---

# OSConfigOSPolicyAssignment  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/osconfig/osconfigospolicyassignment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# OSConfigOSPolicyAssignment

**Property** | **Value**  
---|---  
Google Cloud Service Name | OS Config  
Google Cloud Service Documentation | [/compute/docs/osconfig/rest/](https://docs.cloud.google.com/compute/docs/osconfig/rest)  
Google Cloud REST Resource Name | v1.projects.locations.osPolicyAssignments  
Google Cloud REST Resource Documentation | [/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments)  
Config Connector Resource Short Names | gcposconfigospolicyassignment  
gcposconfigospolicyassignments  
osconfigospolicyassignment  
Config Connector Service Name | osconfig.googleapis.com  
Config Connector Resource Fully Qualified Name | osconfigospolicyassignments.osconfig.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Spec

#### Schema
    
    
    description: string
    instanceFilter:
      all: boolean
      exclusionLabels:
      - labels:
          string: string
      inclusionLabels:
      - labels:
          string: string
      inventories:
      - osShortName: string
        osVersion: string
    location: string
    osPolicies:
    - allowNoResourceGroupMatch: boolean
      description: string
      id: string
      mode: string
      resourceGroups:
      - inventoryFilters:
        - osShortName: string
          osVersion: string
        resources:
        - exec:
            enforce:
              args:
              - string
              file:
                allowInsecure: boolean
                gcs:
                  bucket: string
                  generation: integer
                  object: string
                localPath: string
                remote:
                  sha256Checksum: string
                  uri: string
              interpreter: string
              outputFilePath: string
              script: string
            validate:
              args:
              - string
              file:
                allowInsecure: boolean
                gcs:
                  bucket: string
                  generation: integer
                  object: string
                localPath: string
                remote:
                  sha256Checksum: string
                  uri: string
              interpreter: string
              outputFilePath: string
              script: string
          file:
            content: string
            file:
              allowInsecure: boolean
              gcs:
                bucket: string
                generation: integer
                object: string
              localPath: string
              remote:
                sha256Checksum: string
                uri: string
            path: string
            permissions: string
            state: string
          id: string
          pkg:
            apt:
              name: string
            deb:
              pullDeps: boolean
              source:
                allowInsecure: boolean
                gcs:
                  bucket: string
                  generation: integer
                  object: string
                localPath: string
                remote:
                  sha256Checksum: string
                  uri: string
            desiredState: string
            googet:
              name: string
            msi:
              properties:
              - string
              source:
                allowInsecure: boolean
                gcs:
                  bucket: string
                  generation: integer
                  object: string
                localPath: string
                remote:
                  sha256Checksum: string
                  uri: string
            rpm:
              pullDeps: boolean
              source:
                allowInsecure: boolean
                gcs:
                  bucket: string
                  generation: integer
                  object: string
                localPath: string
                remote:
                  sha256Checksum: string
                  uri: string
            yum:
              name: string
            zypper:
              name: string
          repository:
            apt:
              archiveType: string
              components:
              - string
              distribution: string
              gpgKey: string
              uri: string
            goo:
              name: string
              url: string
            yum:
              baseUrl: string
              displayName: string
              gpgKeys:
              - string
              id: string
            zypper:
              baseUrl: string
              displayName: string
              gpgKeys:
              - string
              id: string
    projectRef:
      external: string
      name: string
      namespace: string
    resourceID: string
    rollout:
      disruptionBudget:
        fixed: integer
        percent: integer
      minWaitDuration: string
    skipAwaitRollout: boolean
    

Fields  
---  
`description` _Optional_ |  `string` OS policy assignment description. Length of the description is limited to 1024 characters.  
`instanceFilter` _Required_ |  `object` Required. Filter to select VMs.  
`instanceFilter.all` _Optional_ |  `boolean` Target all VMs in the project. If true, no other criteria is permitted.  
`instanceFilter.exclusionLabels` _Optional_ |  `list (object)` List of label sets used for VM exclusion. If the list has more than one label set, the VM is excluded if any of the label sets are applicable for the VM.  
`instanceFilter.exclusionLabels[]` _Optional_ |  `object`  
`instanceFilter.exclusionLabels[].labels` _Optional_ |  `map (key: string, value: string)` Labels are identified by key/value pairs in this map. A VM should contain all the key/value pairs specified in this map to be selected.  
`instanceFilter.inclusionLabels` _Optional_ |  `list (object)` List of label sets used for VM inclusion. If the list has more than one `LabelSet`, the VM is included if any of the label sets are applicable for the VM.  
`instanceFilter.inclusionLabels[]` _Optional_ |  `object`  
`instanceFilter.inclusionLabels[].labels` _Optional_ |  `map (key: string, value: string)` Labels are identified by key/value pairs in this map. A VM should contain all the key/value pairs specified in this map to be selected.  
`instanceFilter.inventories` _Optional_ |  `list (object)` List of inventories to select VMs. A VM is selected if its inventory data matches at least one of the following inventories.  
`instanceFilter.inventories[]` _Optional_ |  `object`  
`instanceFilter.inventories[].osShortName` _Required*_ |  `string` Required. The OS short name  
`instanceFilter.inventories[].osVersion` _Optional_ |  `string` The OS version Prefix matches are supported if asterisk(*) is provided as the last character. For example, to match all versions with a major version of `7`, specify the following value for this field `7.*` An empty string matches all OS versions.  
`location` _Required_ |  `string` Immutable. The location for the resource  
`osPolicies` _Required_ |  `list (object)` Required. List of OS policies to be applied to the VMs.  
`osPolicies[]` _Required_ |  `object`  
`osPolicies[].allowNoResourceGroupMatch` _Optional_ |  `boolean` This flag determines the OS policy compliance status when none of the resource groups within the policy are applicable for a VM. Set this value to `true` if the policy needs to be reported as compliant even if the policy has nothing to validate or enforce.  
`osPolicies[].description` _Optional_ |  `string` Policy description. Length of the description is limited to 1024 characters.  
`osPolicies[].id` _Required_ |  `string` Required. The id of the OS policy with the following restrictions: * Must contain only lowercase letters, numbers, and hyphens. * Must start with a letter. * Must be between 1-63 characters. * Must end with a number or a letter. * Must be unique within the assignment.  
`osPolicies[].mode` _Required_ |  `string` Required. Policy mode Possible values: MODE_UNSPECIFIED, VALIDATION, ENFORCEMENT  
`osPolicies[].resourceGroups` _Required_ |  `list (object)` Required. List of resource groups for the policy. For a particular VM, resource groups are evaluated in the order specified and the first resource group that is applicable is selected and the rest are ignored. If none of the resource groups are applicable for a VM, the VM is considered to be non-compliant w.r.t this policy. This behavior can be toggled by the flag `allow_no_resource_group_match`  
`osPolicies[].resourceGroups[]` _Required_ |  `object`  
`osPolicies[].resourceGroups[].inventoryFilters` _Optional_ |  `list (object)` List of inventory filters for the resource group. The resources in this resource group are applied to the target VM if it satisfies at least one of the following inventory filters. For example, to apply this resource group to VMs running either `RHEL` or `CentOS` operating systems, specify 2 items for the list with following values: inventory_filters[0].os_short_name='rhel' and inventory_filters[1].os_short_name='centos' If the list is empty, this resource group will be applied to the target VM unconditionally.  
`osPolicies[].resourceGroups[].inventoryFilters[]` _Optional_ |  `object`  
`osPolicies[].resourceGroups[].inventoryFilters[].osShortName` _Required*_ |  `string` Required. The OS short name  
`osPolicies[].resourceGroups[].inventoryFilters[].osVersion` _Optional_ |  `string` The OS version Prefix matches are supported if asterisk(*) is provided as the last character. For example, to match all versions with a major version of `7`, specify the following value for this field `7.*` An empty string matches all OS versions.  
`osPolicies[].resourceGroups[].resources` _Required_ |  `list (object)` Required. List of resources configured for this resource group. The resources are executed in the exact order specified here.  
`osPolicies[].resourceGroups[].resources[]` _Required_ |  `object`  
`osPolicies[].resourceGroups[].resources[].exec` _Optional_ |  `object` Exec resource  
`osPolicies[].resourceGroups[].resources[].exec.enforce` _Optional_ |  `object` What to run to bring this resource into the desired state. An exit code of 100 indicates "success", any other exit code indicates a failure running enforce.  
`osPolicies[].resourceGroups[].resources[].exec.enforce.args` _Optional_ |  `list (string)` Optional arguments to pass to the source during execution.  
`osPolicies[].resourceGroups[].resources[].exec.enforce.args[]` _Optional_ |  `string`  
`osPolicies[].resourceGroups[].resources[].exec.enforce.file` _Optional_ |  `object` A remote or local file.  
`osPolicies[].resourceGroups[].resources[].exec.enforce.file.allowInsecure` _Optional_ |  `boolean` Defaults to false. When false, files are subject to validations based on the file type: Remote: A checksum must be specified. Cloud Storage: An object generation number must be specified.  
`osPolicies[].resourceGroups[].resources[].exec.enforce.file.gcs` _Optional_ |  `object` A Cloud Storage object.  
`osPolicies[].resourceGroups[].resources[].exec.enforce.file.gcs.bucket` _Required*_ |  `string` Required. Bucket of the Cloud Storage object.  
`osPolicies[].resourceGroups[].resources[].exec.enforce.file.gcs.generation` _Optional_ |  `integer` Generation number of the Cloud Storage object.  
`osPolicies[].resourceGroups[].resources[].exec.enforce.file.gcs.object` _Required*_ |  `string` Required. Name of the Cloud Storage object.  
`osPolicies[].resourceGroups[].resources[].exec.enforce.file.localPath` _Optional_ |  `string` A local path within the VM to use.  
`osPolicies[].resourceGroups[].resources[].exec.enforce.file.remote` _Optional_ |  `object` A generic remote file.  
`osPolicies[].resourceGroups[].resources[].exec.enforce.file.remote.sha256Checksum` _Optional_ |  `string` SHA256 checksum of the remote file.  
`osPolicies[].resourceGroups[].resources[].exec.enforce.file.remote.uri` _Required*_ |  `string` Required. URI from which to fetch the object. It should contain both the protocol and path following the format `{protocol}://{location}`.  
`osPolicies[].resourceGroups[].resources[].exec.enforce.interpreter` _Required*_ |  `string` Required. The script interpreter to use. Possible values: INTERPRETER_UNSPECIFIED, NONE, SHELL, POWERSHELL  
`osPolicies[].resourceGroups[].resources[].exec.enforce.outputFilePath` _Optional_ |  `string` Only recorded for enforce Exec. Path to an output file (that is created by this Exec) whose content will be recorded in OSPolicyResourceCompliance after a successful run. Absence or failure to read this file will result in this ExecResource being non-compliant. Output file size is limited to 100K bytes.  
`osPolicies[].resourceGroups[].resources[].exec.enforce.script` _Optional_ |  `string` An inline script. The size of the script is limited to 1024 characters.  
`osPolicies[].resourceGroups[].resources[].exec.validate` _Required*_ |  `object` Required. What to run to validate this resource is in the desired state. An exit code of 100 indicates "in desired state", and exit code of 101 indicates "not in desired state". Any other exit code indicates a failure running validate.  
`osPolicies[].resourceGroups[].resources[].exec.validate.args` _Optional_ |  `list (string)` Optional arguments to pass to the source during execution.  
`osPolicies[].resourceGroups[].resources[].exec.validate.args[]` _Optional_ |  `string`  
`osPolicies[].resourceGroups[].resources[].exec.validate.file` _Optional_ |  `object` A remote or local file.  
`osPolicies[].resourceGroups[].resources[].exec.validate.file.allowInsecure` _Optional_ |  `boolean` Defaults to false. When false, files are subject to validations based on the file type: Remote: A checksum must be specified. Cloud Storage: An object generation number must be specified.  
`osPolicies[].resourceGroups[].resources[].exec.validate.file.gcs` _Optional_ |  `object` A Cloud Storage object.  
`osPolicies[].resourceGroups[].resources[].exec.validate.file.gcs.bucket` _Required*_ |  `string` Required. Bucket of the Cloud Storage object.  
`osPolicies[].resourceGroups[].resources[].exec.validate.file.gcs.generation` _Optional_ |  `integer` Generation number of the Cloud Storage object.  
`osPolicies[].resourceGroups[].resources[].exec.validate.file.gcs.object` _Required*_ |  `string` Required. Name of the Cloud Storage object.  
`osPolicies[].resourceGroups[].resources[].exec.validate.file.localPath` _Optional_ |  `string` A local path within the VM to use.  
`osPolicies[].resourceGroups[].resources[].exec.validate.file.remote` _Optional_ |  `object` A generic remote file.  
`osPolicies[].resourceGroups[].resources[].exec.validate.file.remote.sha256Checksum` _Optional_ |  `string` SHA256 checksum of the remote file.  
`osPolicies[].resourceGroups[].resources[].exec.validate.file.remote.uri` _Required*_ |  `string` Required. URI from which to fetch the object. It should contain both the protocol and path following the format `{protocol}://{location}`.  
`osPolicies[].resourceGroups[].resources[].exec.validate.interpreter` _Required*_ |  `string` Required. The script interpreter to use. Possible values: INTERPRETER_UNSPECIFIED, NONE, SHELL, POWERSHELL  
`osPolicies[].resourceGroups[].resources[].exec.validate.outputFilePath` _Optional_ |  `string` Only recorded for enforce Exec. Path to an output file (that is created by this Exec) whose content will be recorded in OSPolicyResourceCompliance after a successful run. Absence or failure to read this file will result in this ExecResource being non-compliant. Output file size is limited to 100K bytes.  
`osPolicies[].resourceGroups[].resources[].exec.validate.script` _Optional_ |  `string` An inline script. The size of the script is limited to 1024 characters.  
`osPolicies[].resourceGroups[].resources[].file` _Optional_ |  `object` File resource  
`osPolicies[].resourceGroups[].resources[].file.content` _Optional_ |  `string` A a file with this content. The size of the content is limited to 1024 characters.  
`osPolicies[].resourceGroups[].resources[].file.file` _Optional_ |  `object` A remote or local source.  
`osPolicies[].resourceGroups[].resources[].file.file.allowInsecure` _Optional_ |  `boolean` Defaults to false. When false, files are subject to validations based on the file type: Remote: A checksum must be specified. Cloud Storage: An object generation number must be specified.  
`osPolicies[].resourceGroups[].resources[].file.file.gcs` _Optional_ |  `object` A Cloud Storage object.  
`osPolicies[].resourceGroups[].resources[].file.file.gcs.bucket` _Required*_ |  `string` Required. Bucket of the Cloud Storage object.  
`osPolicies[].resourceGroups[].resources[].file.file.gcs.generation` _Optional_ |  `integer` Generation number of the Cloud Storage object.  
`osPolicies[].resourceGroups[].resources[].file.file.gcs.object` _Required*_ |  `string` Required. Name of the Cloud Storage object.  
`osPolicies[].resourceGroups[].resources[].file.file.localPath` _Optional_ |  `string` A local path within the VM to use.  
`osPolicies[].resourceGroups[].resources[].file.file.remote` _Optional_ |  `object` A generic remote file.  
`osPolicies[].resourceGroups[].resources[].file.file.remote.sha256Checksum` _Optional_ |  `string` SHA256 checksum of the remote file.  
`osPolicies[].resourceGroups[].resources[].file.file.remote.uri` _Required*_ |  `string` Required. URI from which to fetch the object. It should contain both the protocol and path following the format `{protocol}://{location}`.  
`osPolicies[].resourceGroups[].resources[].file.path` _Required*_ |  `string` Required. The absolute path of the file within the VM.  
`osPolicies[].resourceGroups[].resources[].file.permissions` _Optional_ |  `string` Consists of three octal digits which represent, in order, the permissions of the owner, group, and other users for the file (similarly to the numeric mode used in the linux chmod utility). Each digit represents a three bit number with the 4 bit corresponding to the read permissions, the 2 bit corresponds to the write bit, and the one bit corresponds to the execute permission. Default behavior is 755. Below are some examples of permissions and their associated values: read, write, and execute: 7 read and execute: 5 read and write: 6 read only: 4  
`osPolicies[].resourceGroups[].resources[].file.state` _Required*_ |  `string` Required. Desired state of the file. Possible values: OS_POLICY_COMPLIANCE_STATE_UNSPECIFIED, COMPLIANT, NON_COMPLIANT, UNKNOWN, NO_OS_POLICIES_APPLICABLE  
`osPolicies[].resourceGroups[].resources[].id` _Required_ |  `string` Required. The id of the resource with the following restrictions: * Must contain only lowercase letters, numbers, and hyphens. * Must start with a letter. * Must be between 1-63 characters. * Must end with a number or a letter. * Must be unique within the OS policy.  
`osPolicies[].resourceGroups[].resources[].pkg` _Optional_ |  `object` Package resource  
`osPolicies[].resourceGroups[].resources[].pkg.apt` _Optional_ |  `object` A package managed by Apt.  
`osPolicies[].resourceGroups[].resources[].pkg.apt.name` _Required*_ |  `string` Required. Package name.  
`osPolicies[].resourceGroups[].resources[].pkg.deb` _Optional_ |  `object` A deb package file.  
`osPolicies[].resourceGroups[].resources[].pkg.deb.pullDeps` _Optional_ |  `boolean` Whether dependencies should also be installed. - install when false: `dpkg -i package` - install when true: `apt-get update && apt-get -y install package.deb`  
`osPolicies[].resourceGroups[].resources[].pkg.deb.source` _Required*_ |  `object` Required. A deb package.  
`osPolicies[].resourceGroups[].resources[].pkg.deb.source.allowInsecure` _Optional_ |  `boolean` Defaults to false. When false, files are subject to validations based on the file type: Remote: A checksum must be specified. Cloud Storage: An object generation number must be specified.  
`osPolicies[].resourceGroups[].resources[].pkg.deb.source.gcs` _Optional_ |  `object` A Cloud Storage object.  
`osPolicies[].resourceGroups[].resources[].pkg.deb.source.gcs.bucket` _Required*_ |  `string` Required. Bucket of the Cloud Storage object.  
`osPolicies[].resourceGroups[].resources[].pkg.deb.source.gcs.generation` _Optional_ |  `integer` Generation number of the Cloud Storage object.  
`osPolicies[].resourceGroups[].resources[].pkg.deb.source.gcs.object` _Required*_ |  `string` Required. Name of the Cloud Storage object.  
`osPolicies[].resourceGroups[].resources[].pkg.deb.source.localPath` _Optional_ |  `string` A local path within the VM to use.  
`osPolicies[].resourceGroups[].resources[].pkg.deb.source.remote` _Optional_ |  `object` A generic remote file.  
`osPolicies[].resourceGroups[].resources[].pkg.deb.source.remote.sha256Checksum` _Optional_ |  `string` SHA256 checksum of the remote file.  
`osPolicies[].resourceGroups[].resources[].pkg.deb.source.remote.uri` _Required*_ |  `string` Required. URI from which to fetch the object. It should contain both the protocol and path following the format `{protocol}://{location}`.  
`osPolicies[].resourceGroups[].resources[].pkg.desiredState` _Required*_ |  `string` Required. The desired state the agent should maintain for this package. Possible values: DESIRED_STATE_UNSPECIFIED, INSTALLED, REMOVED  
`osPolicies[].resourceGroups[].resources[].pkg.googet` _Optional_ |  `object` A package managed by GooGet.  
`osPolicies[].resourceGroups[].resources[].pkg.googet.name` _Required*_ |  `string` Required. Package name.  
`osPolicies[].resourceGroups[].resources[].pkg.msi` _Optional_ |  `object` An MSI package.  
`osPolicies[].resourceGroups[].resources[].pkg.msi.properties` _Optional_ |  `list (string)` Additional properties to use during installation. This should be in the format of Property=Setting. Appended to the defaults of `ACTION=INSTALL REBOOT=ReallySuppress`.  
`osPolicies[].resourceGroups[].resources[].pkg.msi.properties[]` _Optional_ |  `string`  
`osPolicies[].resourceGroups[].resources[].pkg.msi.source` _Required*_ |  `object` Required. The MSI package.  
`osPolicies[].resourceGroups[].resources[].pkg.msi.source.allowInsecure` _Optional_ |  `boolean` Defaults to false. When false, files are subject to validations based on the file type: Remote: A checksum must be specified. Cloud Storage: An object generation number must be specified.  
`osPolicies[].resourceGroups[].resources[].pkg.msi.source.gcs` _Optional_ |  `object` A Cloud Storage object.  
`osPolicies[].resourceGroups[].resources[].pkg.msi.source.gcs.bucket` _Required*_ |  `string` Required. Bucket of the Cloud Storage object.  
`osPolicies[].resourceGroups[].resources[].pkg.msi.source.gcs.generation` _Optional_ |  `integer` Generation number of the Cloud Storage object.  
`osPolicies[].resourceGroups[].resources[].pkg.msi.source.gcs.object` _Required*_ |  `string` Required. Name of the Cloud Storage object.  
`osPolicies[].resourceGroups[].resources[].pkg.msi.source.localPath` _Optional_ |  `string` A local path within the VM to use.  
`osPolicies[].resourceGroups[].resources[].pkg.msi.source.remote` _Optional_ |  `object` A generic remote file.  
`osPolicies[].resourceGroups[].resources[].pkg.msi.source.remote.sha256Checksum` _Optional_ |  `string` SHA256 checksum of the remote file.  
`osPolicies[].resourceGroups[].resources[].pkg.msi.source.remote.uri` _Required*_ |  `string` Required. URI from which to fetch the object. It should contain both the protocol and path following the format `{protocol}://{location}`.  
`osPolicies[].resourceGroups[].resources[].pkg.rpm` _Optional_ |  `object` An rpm package file.  
`osPolicies[].resourceGroups[].resources[].pkg.rpm.pullDeps` _Optional_ |  `boolean` Whether dependencies should also be installed. - install when false: `rpm --upgrade --replacepkgs package.rpm` - install when true: `yum -y install package.rpm` or `zypper -y install package.rpm`  
`osPolicies[].resourceGroups[].resources[].pkg.rpm.source` _Required*_ |  `object` Required. An rpm package.  
`osPolicies[].resourceGroups[].resources[].pkg.rpm.source.allowInsecure` _Optional_ |  `boolean` Defaults to false. When false, files are subject to validations based on the file type: Remote: A checksum must be specified. Cloud Storage: An object generation number must be specified.  
`osPolicies[].resourceGroups[].resources[].pkg.rpm.source.gcs` _Optional_ |  `object` A Cloud Storage object.  
`osPolicies[].resourceGroups[].resources[].pkg.rpm.source.gcs.bucket` _Required*_ |  `string` Required. Bucket of the Cloud Storage object.  
`osPolicies[].resourceGroups[].resources[].pkg.rpm.source.gcs.generation` _Optional_ |  `integer` Generation number of the Cloud Storage object.  
`osPolicies[].resourceGroups[].resources[].pkg.rpm.source.gcs.object` _Required*_ |  `string` Required. Name of the Cloud Storage object.  
`osPolicies[].resourceGroups[].resources[].pkg.rpm.source.localPath` _Optional_ |  `string` A local path within the VM to use.  
`osPolicies[].resourceGroups[].resources[].pkg.rpm.source.remote` _Optional_ |  `object` A generic remote file.  
`osPolicies[].resourceGroups[].resources[].pkg.rpm.source.remote.sha256Checksum` _Optional_ |  `string` SHA256 checksum of the remote file.  
`osPolicies[].resourceGroups[].resources[].pkg.rpm.source.remote.uri` _Required*_ |  `string` Required. URI from which to fetch the object. It should contain both the protocol and path following the format `{protocol}://{location}`.  
`osPolicies[].resourceGroups[].resources[].pkg.yum` _Optional_ |  `object` A package managed by YUM.  
`osPolicies[].resourceGroups[].resources[].pkg.yum.name` _Required*_ |  `string` Required. Package name.  
`osPolicies[].resourceGroups[].resources[].pkg.zypper` _Optional_ |  `object` A package managed by Zypper.  
`osPolicies[].resourceGroups[].resources[].pkg.zypper.name` _Required*_ |  `string` Required. Package name.  
`osPolicies[].resourceGroups[].resources[].repository` _Optional_ |  `object` Package repository resource  
`osPolicies[].resourceGroups[].resources[].repository.apt` _Optional_ |  `object` An Apt Repository.  
`osPolicies[].resourceGroups[].resources[].repository.apt.archiveType` _Required*_ |  `string` Required. Type of archive files in this repository. Possible values: ARCHIVE_TYPE_UNSPECIFIED, DEB, DEB_SRC  
`osPolicies[].resourceGroups[].resources[].repository.apt.components` _Required*_ |  `list (string)` Required. List of components for this repository. Must contain at least one item.  
`osPolicies[].resourceGroups[].resources[].repository.apt.components[]` _Required*_ |  `string`  
`osPolicies[].resourceGroups[].resources[].repository.apt.distribution` _Required*_ |  `string` Required. Distribution of this repository.  
`osPolicies[].resourceGroups[].resources[].repository.apt.gpgKey` _Optional_ |  `string` URI of the key file for this repository. The agent maintains a keyring at `/etc/apt/trusted.gpg.d/osconfig_agent_managed.gpg`.  
`osPolicies[].resourceGroups[].resources[].repository.apt.uri` _Required*_ |  `string` Required. URI for this repository.  
`osPolicies[].resourceGroups[].resources[].repository.goo` _Optional_ |  `object` A Goo Repository.  
`osPolicies[].resourceGroups[].resources[].repository.goo.name` _Required*_ |  `string` Required. The name of the repository.  
`osPolicies[].resourceGroups[].resources[].repository.goo.url` _Required*_ |  `string` Required. The url of the repository.  
`osPolicies[].resourceGroups[].resources[].repository.yum` _Optional_ |  `object` A Yum Repository.  
`osPolicies[].resourceGroups[].resources[].repository.yum.baseUrl` _Required*_ |  `string` Required. The location of the repository directory.  
`osPolicies[].resourceGroups[].resources[].repository.yum.displayName` _Optional_ |  `string` The display name of the repository.  
`osPolicies[].resourceGroups[].resources[].repository.yum.gpgKeys` _Optional_ |  `list (string)` URIs of GPG keys.  
`osPolicies[].resourceGroups[].resources[].repository.yum.gpgKeys[]` _Optional_ |  `string`  
`osPolicies[].resourceGroups[].resources[].repository.yum.id` _Required*_ |  `string` Required. A one word, unique name for this repository. This is the `repo id` in the yum config file and also the `display_name` if `display_name` is omitted. This id is also used as the unique identifier when checking for resource conflicts.  
`osPolicies[].resourceGroups[].resources[].repository.zypper` _Optional_ |  `object` A Zypper Repository.  
`osPolicies[].resourceGroups[].resources[].repository.zypper.baseUrl` _Required*_ |  `string` Required. The location of the repository directory.  
`osPolicies[].resourceGroups[].resources[].repository.zypper.displayName` _Optional_ |  `string` The display name of the repository.  
`osPolicies[].resourceGroups[].resources[].repository.zypper.gpgKeys` _Optional_ |  `list (string)` URIs of GPG keys.  
`osPolicies[].resourceGroups[].resources[].repository.zypper.gpgKeys[]` _Optional_ |  `string`  
`osPolicies[].resourceGroups[].resources[].repository.zypper.id` _Required*_ |  `string` Required. A one word, unique name for this repository. This is the `repo id` in the zypper config file and also the `display_name` if `display_name` is omitted. This id is also used as the unique identifier when checking for GuestPolicy conflicts.  
`projectRef` _Required_ |  `object` Immutable. The Project that this resource belongs to.  
`projectRef.external` _Optional_ |  `string` The project for the resource Allowed value: The Google Cloud resource name of a `Project` resource (format: `projects/{{name}}`).  
`projectRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`projectRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`resourceID` _Optional_ |  `string` Immutable. Optional. The name of the resource. Used for creation and acquisition. When unset, the value of `metadata.name` is used as the default.  
`rollout` _Required_ |  `object` Required. Rollout to deploy the OS policy assignment. A rollout is triggered in the following situations: 1) OSPolicyAssignment is created. 2) OSPolicyAssignment is updated and the update contains changes to one of the following fields: - instance_filter - os_policies 3) OSPolicyAssignment is deleted.  
`rollout.disruptionBudget` _Required_ |  `object` Required. The maximum number (or percentage) of VMs per zone to disrupt at any given moment.  
`rollout.disruptionBudget.fixed` _Optional_ |  `integer` Specifies a fixed value.  
`rollout.disruptionBudget.percent` _Optional_ |  `integer` Specifies the relative value defined as a percentage, which will be multiplied by a reference value.  
`rollout.minWaitDuration` _Required_ |  `string` Required. This determines the minimum duration of time to wait after the configuration changes are applied through the current rollout. A VM continues to count towards the `disruption_budget` at least until this duration of time has passed after configuration changes are applied.  
`skipAwaitRollout` _Optional_ |  `boolean` Set to true to skip awaiting rollout during resource creation and update.  
  
* Field is required when parent field is specified

### Status

#### Schema
    
    
    baseline: boolean
    conditions:
    - lastTransitionTime: string
      message: string
      reason: string
      status: string
      type: string
    deleted: boolean
    etag: string
    observedGeneration: integer
    reconciling: boolean
    revisionCreateTime: string
    revisionId: string
    rolloutState: string
    uid: string
    

Fields  
---  
`baseline` |  `boolean` Output only. Indicates that this revision has been successfully rolled out in this zone and new VMs will be assigned OS policies from this revision. For a given OS policy assignment, there is only one revision with a value of `true` for this field.  
`conditions` |  `list (object)` Conditions represent the latest available observations of the object's current state.  
`conditions[]` |  `object`  
`conditions[].lastTransitionTime` |  `string` Last time the condition transitioned from one status to another.  
`conditions[].message` |  `string` Human-readable message indicating details about last transition.  
`conditions[].reason` |  `string` Unique, one-word, CamelCase reason for the condition's last transition.  
`conditions[].status` |  `string` Status is the status of the condition. Can be True, False, Unknown.  
`conditions[].type` |  `string` Type is the type of the condition.  
`deleted` |  `boolean` Output only. Indicates that this revision deletes the OS policy assignment.  
`etag` |  `string` The etag for this OS policy assignment. If this is provided on update, it must match the server's etag.  
`observedGeneration` |  `integer` ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.  
`reconciling` |  `boolean` Output only. Indicates that reconciliation is in progress for the revision. This value is `true` when the `rollout_state` is one of: * IN_PROGRESS * CANCELLING  
`revisionCreateTime` |  `string` Output only. The timestamp that the revision was created.  
`revisionId` |  `string` Output only. The assignment revision ID A new revision is committed whenever a rollout is triggered for an OS policy assignment  
`rolloutState` |  `string` Output only. OS policy assignment rollout state Possible values: ROLLOUT_STATE_UNSPECIFIED, IN_PROGRESS, CANCELLING, CANCELLED, SUCCEEDED  
`uid` |  `string` Output only. Server generated unique id for the OS policy assignment resource.  
  
## Sample YAML(s)

### Fixed Os Policy Assignment
    
    
    # Copyright 2021 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    apiVersion: osconfig.cnrm.cloud.google.com/v1beta1
    kind: OSConfigOSPolicyAssignment
    metadata:
      name: osconfigospolicyassignment-sample-fixedospolicyassignment
    spec:
      projectRef:
         # Replace ${PROJECT_ID?} with your project ID
         external: "projects/${PROJECT_ID?}"
      location: "us-west2-a"
      description: "A test os policy assignment"
      osPolicies:
      - id: "policy"
        description: "A test os policy"
        mode: "VALIDATION"
        resourceGroups:
        - inventoryFilters:
          - osShortName: "centos"
            osVersion: "8.*"
          resources:
          - id: "apt"
            pkg:
              desiredState: "INSTALLED"
              apt:
                name: "bazel"
          - id: "deb1"
            pkg:
              desiredState: "INSTALLED"
              deb:
                source:
                  localPath: "$HOME/package.deb"
          - id: "deb2"
            pkg:
              desiredState: "INSTALLED"
              deb:
                pullDeps: true
                source:
                  allowInsecure: true
                  remote:
                    uri: "ftp.us.debian.org/debian/package.deb"
                    sha256Checksum: "3bbfd1043cd7afdb78cf9afec36c0c5370d2fea98166537b4e67f3816f256025"
          - id: "deb3"
            pkg:
              desiredState: "INSTALLED"
              deb:
                pullDeps: true
                source:
                  gcs:
                    bucket: "test-bucket"
                    object: "test-object"
                    generation: 1
          - id: "yum"
            pkg:
              desiredState: "INSTALLED"
              yum:
                name: "gstreamer-plugins-base-devel.x86_64"
          - id: "zypper"
            pkg:
              desiredState: "INSTALLED"
              zypper:
                name: "gcc"
          - id: "rpm1"
            pkg:
              desiredState: "INSTALLED"
              rpm:
                pullDeps: true
                source:
                  localPath: "$HOME/package.rpm"
          - id: "rpm2"
            pkg:
              desiredState: "INSTALLED"
              rpm:
                source:
                  allowInsecure: true
                  remote:
                    uri: "https://mirror.jaleco.com/centos/8.3.2011/BaseOS/x86_64/os/Packages/efi-filesystem-3-2.el8.noarch.rpm"
                    sha256Checksum: "3bbfd1043cd7afdb78cf9afec36c0c5370d2fea98166537b4e67f3816f256025"
          - id: "rpm3"
            pkg:
              desiredState: "INSTALLED"
              rpm:
                source:
                  gcs:
                    bucket: "test-bucket"
                    object: "test-object"
                    generation: 1
        - resources:
          - id: "apt-to-deb"
            pkg:
              desiredState: "INSTALLED"
              apt:
                name: "bazel"
          - id: "deb-local-path-to-gcs"
            pkg:
              desiredState: "INSTALLED"
              deb:
                source:
                  localPath: "$HOME/package.deb"
          - id: "googet"
            pkg:
              desiredState: "INSTALLED"
              googet:
                name: "gcc"
          - id: "msi1"
            pkg:
              desiredState: "INSTALLED"
              msi:
                source:
                  localPath: "$HOME/package.msi"
                properties:
                - "REBOOT=ReallySuppress"
          - id: "msi2"
            pkg:
              desiredState: "INSTALLED"
              msi:
                source:
                  allowInsecure: true
                  remote:
                    uri: "https://remote.uri.com/package.msi"
                    sha256Checksum: "3bbfd1043cd7afdb78cf9afec36c0c5370d2fea98166537b4e67f3816f256025"
          - id: "msi3"
            pkg:
              desiredState: "INSTALLED"
              msi:
                source:
                  gcs:
                    bucket: "test-bucket"
                    object: "test-object"
                    generation: 1
        allowNoResourceGroupMatch: false
      instanceFilter:
        all: false
        inclusionLabels:
        - labels:
            label-one: "value-one"
        exclusionLabels:
        - labels:
            label-two: "value-two"
        inventories:
        - osShortName: "centos"
          osVersion: "8.*"
      rollout:
        disruptionBudget:
          fixed: 1
        minWaitDuration: "3.5s"
    

### Percent Os Policy Assignment
    
    
    # Copyright 2021 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    apiVersion: osconfig.cnrm.cloud.google.com/v1beta1
    kind: OSConfigOSPolicyAssignment
    metadata:
      name: osconfigospolicyassignment-sample-percentospolicyassignment
    spec:
      projectRef:
         # Replace ${PROJECT_ID?} with your project ID
         external: "projects/${PROJECT_ID?}"
      location: "us-west2-a"
      description: "A test os policy assignment"
      osPolicies:
      - id: "policy"
        mode: "VALIDATION"
        resourceGroups:
        - resources:
          - id: "apt-to-yum"
            repository:
              apt:
                archiveType: "DEB"
                uri: "https://atl.mirrors.clouvider.net/debian"
                distribution: "debian"
                components:
                - "doc"
                gpgKey: ".gnupg/pubring.kbx"
          - id: "yum"
            repository:
              yum:
                id: "yum"
                displayName: "yum"
                baseUrl: "http://centos.s.uw.edu/centos/"
                gpgKeys:
                - "RPM-GPG-KEY-CentOS-7"
          - id: "zypper"
            repository:
              zypper:
                id: "zypper"
                displayName: "zypper"
                baseUrl: "http://mirror.dal10.us.leaseweb.net/opensuse"
                gpgKeys:
                - "sample-key-uri"
          - id: "goo"
            repository:
              goo:
                name: "goo"
                url: "https://foo.com/googet/bar"
          - id: "exec1"
            exec:
              validate:
                args:
                - "arg1"
                interpreter: "SHELL"
                outputFilePath: "$HOME/out"
                file:
                  localPath: "$HOME/script.sh"
              enforce:
                args:
                - "arg1"
                interpreter: "SHELL"
                outputFilePath: "$HOME/out"
                file:
                  allowInsecure: true
                  remote:
                    uri: "https://www.example.com/script.sh"
                    sha256Checksum: "c7938fed83afdccbb0e86a2a2e4cad7d5035012ca3214b4a61268393635c3063"
          - id: "exec2"
            exec:
              validate:
                args:
                - "arg1"
                interpreter: "SHELL"
                outputFilePath: "$HOME/out"
                file:
                  allowInsecure: true
                  remote:
                    uri: "https://www.example.com/script.sh"
                    sha256Checksum: "c7938fed83afdccbb0e86a2a2e4cad7d5035012ca3214b4a61268393635c3063"
              enforce:
                args:
                - "arg1"
                interpreter: "SHELL"
                outputFilePath: "$HOME/out"
                file:
                  localPath: "$HOME/script.sh"
          - id: "exec3"
            exec:
              validate:
                interpreter: "SHELL"
                outputFilePath: "$HOME/out"
                file:
                  allowInsecure: true
                  gcs:
                    bucket: "test-bucket"
                    object: "test-object"
                    generation: 1
              enforce:
                interpreter: "SHELL"
                outputFilePath: "$HOME/out"
                script: "pwd"
          - id: "exec4"
            exec:
              validate:
                interpreter: "SHELL"
                outputFilePath: "$HOME/out"
                script: "pwd"
              enforce:
                interpreter: "SHELL"
                outputFilePath: "$HOME/out"
                file:
                  allowInsecure: true
                  gcs:
                    bucket: "test-bucket"
                    object: "test-object"
                    generation: 1
          - id: "file1"
            file:
              path: "$HOME/file"
              state: "PRESENT"
              file:
                localPath: "$HOME/file"
        - resources:
          - id: "file2"
            file:
              path: "$HOME/file"
              state: "PRESENT"
              permissions: "755"
              file:
                allowInsecure: true
                remote:
                  uri: "https://www.example.com/file"
                  sha256Checksum: "c7938fed83afdccbb0e86a2a2e4cad7d5035012ca3214b4a61268393635c3063"
          - id: "file3"
            file:
              path: "$HOME/file"
              state: "PRESENT"
              file:
                gcs:
                  bucket: "test-bucket"
                  object: "test-object"
                  generation: 1
          - id: "file4"
            file:
              path: "$HOME/file"
              state: "PRESENT"
              content: "sample-content"
      instanceFilter:
        all: true
      rollout:
        disruptionBudget:
          percent: 1
        minWaitDuration: "3.5s"
    

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
