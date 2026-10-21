---
url: https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies/
title: OS policy and OS policy assignment \u00a0|\u00a0 VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:36:51.501736+00:00
---

# OS policy and OS policy assignment  |  VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  OS policy and OS policy assignment Stay organized with collections  Save and categorize content based on your preferences. 

An _OS policy_ is a file that contains the declarative configuration for OS resources such as packages, repositories, files, or custom resources defined by scripts. For more information, see the resource definition for [`OSPolicy`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments#OSPolicy).

An _OS policy assignment_ is an API resource that is used by VM Manager to apply OS policies to VMs. For more information, see the resource definition for [`OSPolicyAssignment`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments#OSPolicyAssignment).

## OS policy

An OS policy is a JSON or YAML file that has three sections:

  * **Mode**. The policy behavior. The following two modes are available:

    * `Validation`: for this mode, the policy checks to see if the resources are in the chosen state but doesn't take any action.
    * `Enforcement`: for this mode, the policy checks to see if the resources are in the chosen state and, if not, performs the necessary actions to bring them to that chosen state.

For both modes, VM Manager reports compliance for the OS policy and the associated resources.

  * **Resource groups**. The operating system name and version that the associated resource specifications apply to. For example, you can define a single policy to install or deploy an agent across different operating system distributions and versions.

  * **Resources**. The specifications needed for the VM to attain the selected configuration. You can specify a maximum of 10 resource IDs in each resource group. The following resource types are supported:

    * `pkg`: used for installing or removing Linux and Windows packages
    * `repository`: used for specifying which repository software packages can be installed from
    * `exec`: used to enable the running of an ad hoc shell (`/bin/sh`) or PowerShell script
    * `file`: used to manage files on the system

**Note:** Custom OS policy scripts and output files that you define using the `exec` resource don't use [customer-managed encryption keys (CMEKs)](https://docs.cloud.google.com/kms/docs/cmek). Make sure that you don't include any sensitive information in these scripts or output files. Alternatively, use a [Cloud Storage bucket](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy#gcs) to store the `exec` script and output file. See [Example 3](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies#example-3). Ensure that the service accounts attached to your VMs are granted the required [IAM permissions to upload objects to Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).



**Pro Tip:** For more information about the fields and parameters for an OS policy, see [Resource: OSPolicy](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments#ospolicy).

### Example OS policies

The following examples show how to create OS policies. You can upload these OS policies to the Google Cloud console when creating an OS policy assignment.

  * Example 1: installs a package.
  * Example 2: runs a script.
  * Example 3: runs a script that is stored in a Cloud Storage bucket and copies the output file to a Cloud Storage bucket.
  * Example 4: specifies a download repository and installs packages from that repository.
  * Example 5: configures CIS benchmark scanning on VMs running Container-Optimized OS (COS). For more information about using OS policy for CIS benchmark scanning, see [Automate enabling and checking of CIS compliance status](https://docs.cloud.google.com/container-optimized-os/docs/how-to/cis-compliance#using-os-policy).



For a full list of sample OS policies that you can apply in your environment, see the [GoogleCloudPlatform/osconfig](https://github.com/GoogleCloudPlatform/osconfig/tree/master/examples/OSPolicyAssignments/console) GitHub repository.

### Example 1

Create an OS policy that installs a Windows MSI downloaded from a Cloud Storage bucket.
    
    
    # An OS policy to install a Windows MSI downloaded from a Google Cloud Storage bucket.
    id: install-msi-policy
    mode: ENFORCEMENT
    resourceGroups:
      - resources:
          - id: install-msi
            pkg:
              desiredState: INSTALLED
              msi:
                source:
                  gcs:
                    bucket: my-bucket
                    object: my-app.msi
                    generation: 1619136883923956
    

### Example 2

Create an OS policy that verifies if the Apache web server is running on your Linux VMs.
    
    
    # An OS policy that ensures Apache web server is running on Linux OSes.
    id: apache-always-up-policy
    mode: ENFORCEMENT
    resourceGroups:
      - resources:
          id: ensure-apache-is-up
          exec:
            validate:
              interpreter: SHELL
              # If Apache web server is already running, return an exit code 100 to indicate
              # that exec resource is already in desired state. In this scenario,
              # the `enforce` step will not be run.
              # Otherwise return an exit code of 101 to indicate that exec resource is not in
              # desired state. In this scenario, the `enforce` step will be run.
              script: if systemctl is-active --quiet httpd; then exit 100; else exit 101; fi
            enforce:
              interpreter: SHELL
              # Start Apache web server and return an exit code of 100 to indicate that the
              # resource is now in its desired state.
              script: systemctl start httpd && exit 100
    

### Example 3

Create an OS policy that verifies if the Apache web server is running on your Linux VMs. In this example, the `apache-validate.sh` script is stored in a Cloud Storage bucket. To copy the output to a Cloud Storage bucket, the `apache-enforce.sh` script must include a command similar to the following:
    
    
          gcsutil cp my-exec-output-file gs://my-gcs-bucket
          
    
    
    # An OS policy that ensures Apache web server is running on Linux OSes.
    id: gcs-test-apache-always-up-policy
    mode: ENFORCEMENT
    resourceGroups:
      - resources:
          id: ensure-apache-is-up
          exec:
            validate:
              interpreter: SHELL
              # If Apache web server is already running, return an exit code 100 to indicate
              # that exec resource is already in desired state. In this scenario,
              # the enforce step will not be run.
              # Otherwise return an exit code of 101 to indicate that exec resource is not in
              # desired state. In this scenario, the enforce step will be run.
              file:
                gcs:
                  bucket: my-gcs-bucket
                  object: apache-validate.sh
                  generation: 1726747503303299
            enforce:
              interpreter: SHELL
              # Start Apache web server and return an exit code of 100 to indicate that the
              # resource is now in its desired state.
              file:
                gcs:
                  bucket: my-gcs-bucket
                  object: apache-enforce.sh
                  generation: 1726747503250884
    

### Example 4

Create an OS policy that installs Google Cloud Observability agents on CentOS VMs.
    
    
    id: cloudops-policy
    mode: ENFORCEMENT
    resourceGroups:
      - resources:
          - id: add-repo
            repository:
              yum:
                id: google-cloud-ops-agent
                displayName: Google Cloud Ops Agent Repository
                baseUrl: https://packages.cloud.google.com/yum/repos/google-cloud-ops-agent-el7-x86_64-all
                gpgKeys:
                  - https://packages.cloud.google.com/yum/doc/yum-key.gpg
                  - https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
          - id: install-pkg
            pkg:
              desiredState: INSTALLED
              yum:
                name: google-cloud-ops-agent
          - id: exec-script
            exec:
              validate:
                script: |-
                  if [[ $(rpm --query --queryformat '%{VERSION}
                  ' google-cloud-ops-agent) == '1.0.2' ]]; then exit 100; else exit 101; fi
                interpreter: SHELL
              enforce:
                script:
                  sudo yum remove -y google-cloud-ops-agent || true; sudo yum install
                  -y 'google-cloud-ops-agent-1.0.2*' && exit 100
                interpreter: SHELL
          - id: ensure-agent-running
            exec:
              validate:
                script:
                  if (ps aux | grep 'opt[/].*google-cloud-ops-agent.*bin/'); then exit
                  100; else exit 101; fi
                interpreter: SHELL
              enforce:
                script: sudo systemctl start google-cloud-ops-agent.target && exit 100
                interpreter: SHELL
    

### Example 5

Configures periodic CIS Level 1 scanning with the default period of once a day.
    
    
    # An OS policy to check CIS level 1 compliance once a day.
    id: ensure-cis-level1-compliance-once-a-day-policy
    mode: ENFORCEMENT
    resourceGroups:
      - resources:
          id: ensure-cis-level1-compliance-once-a-day
          exec:
            validate:
              interpreter: SHELL
              # If cis-compliance-scanner.service is active, return an exit code
              # 100 to indicate that the instance is in compliant state.
              # Otherwise, return an exit code of 101 to run `enforce` step.
              script: |-
                is_active=$(systemctl is-active cis-compliance-scanner.timer)
                result=$(systemctl show -p Result --value cis-compliance-scanner.service)
    
                if [ "$is_active" == "active" ] && [ "$result" == "success" ]; then
                  exit 100;
                else
                  exit 101;
                fi
            enforce:
              interpreter: SHELL
              # COS 97 images are by-default CIS Level 1 compliant and there is no
              # additional configuration needed. However, if certain changes
              # cause non-compliance because of the workload on the instance, this
              # section can be used to automate to make fixes. For example, the
              # workload might generate a file that does not comply with the
              # recommended file permissions.
              # Return an exit code of 100 to indicate that the desired changes
              # successfully applied.
              script: |-
                # optional <your code>
                # Check the compliance of the instance once a day.
                systemctl start cis-compliance-scanner.timer && exit 100
    

## OS policy assignment

An OS policy assignment has the following sections:

  * **OS Policies**. One or more OS policies that you want to apply to your VM. To download or create a policy, see [OS policies](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies).

**Note:** You can create a maximum of 20 OS policy assignments for each zone in a project. For more information, see [OS Config quotas](https://docs.cloud.google.com/compute/vm-manager/docs/os-config-quotas#allocation_quotas). To create more than 20 OS policy assignments in a zone, [request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).
  * **Target VMs**. A set of VMs within a single zone that you want to apply the policy to. Within a zone you can limit or restrict VMs by specifying the OS names and include or exclude labels. You can select a combination of the following options:

    * Zone: specifies the Google Cloud zone where you want to roll out the OS policy assignment.
    * OS name and version: specifies the short name and version of the target operating system that the OS policy applies to. For an example of how to target multiple operating systems, see Example 4.

To filter VMs based on the operating system, use any of the following short names in your OS policy YAML files:

Full name | Short name  
---|---  
CentOS | `centos`  
Container-Optimized OS (COS) | `cos`  
Debian | `debian`  
openSUSE Leap | `opensuse-leap`  
Oracle Linux | `ol`  
Red Hat Enterprise Linux (RHEL) | `rhel`  
Rocky Linux | `rocky`  
SUSE Linux Enterprise Server (SLES) | `sles`  
Ubuntu | `ubuntu`  
Windows Server | `windows`  
  
For a full list of operating systems and versions that support OS policies, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#vm-manager).

    * Include set: specifies the VMs that the OS policy applies to based on VM or system labels.
    * Exclude set: specifies the VMs that the OS policy should ignore based on VM or system labels.

For both include and exclude label sets, a single string label is accepted if it matches the naming convention used by the system. However, most labels are specified in `key:value` pairs. For more information about labels, see [Labeling resources](https://docs.cloud.google.com/compute/docs/labeling-resources).

For example, you can select all the Ubuntu VMs in your test environment, and exclude those that are running Google Kubernetes Engine, by specifying the following: 

    * OS short name: `ubuntu`
    * Include: `env:test`, `env:staging`
    * Exclude: `goog-gke-node`
  * **A rollout rate**. Specifies the pace at which to apply the OS policies to the VMs. The OS policies are rolled out gradually to let you track system health and make modifications if the updates cause regressions in your environment. A rollout plan has the following components:

    * Wave size (disruption budget): the fixed number or percentage of VMs that can experience a rollout at one time. This means that at any moment of the rollout only a specified number of VMs are targeted.
    * Wait time: the time between when the service applies policies to the VM and when a VM is removed from the disruption threshold. For example, a wait time of 15 minutes means that the rollout process must wait 15 minutes after applying the policies to a VM before it can remove the VM from the disruption threshold and the rollout can proceed. The wait time helps control the speed of a rollout and also lets you catch and resolve potential rollout issues early. Select a time that is long enough for you to monitor the status of your rollouts.

For example, if you set a target of 10 VMs, set the disruption threshold at 20%, and set a bake time of 15 minutes, then at any given time, only 2 VMs are scheduled to be updated. After each VM is updated, 15 minutes must pass before the VM is removed from the disruption threshold and another VM is added to the rollout.

For more information about rollouts, see [Rollouts](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/create-os-policy-assignment#rollouts).




**Pro Tip:** For more information about the fields and parameters for an OS policy assignment, see [Resource: OSPolicyAssignment](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments#resource:-ospolicyassignment).

### Example OS policy assignment

The following examples show how to create OS policy assignments. You can use these examples to create OS policy assignments from the Google Cloud CLI or the OS Config API.

  * Example 1: installs a package.
  * Example 2: runs a script.
  * Example 3: specifies a download repository and installs packages from that repository.
  * Example 4: an OS policy assignment that applies to multiple operating systems.



For a list of sample OS policy assignments that you can apply in your environment, see the [GoogleCloudPlatform/osconfig](https://github.com/GoogleCloudPlatform/osconfig/tree/master/examples/OSPolicyAssignments/gcloud) GitHub repository.

### Example 1

Create an OS policy assignment that installs a Windows MSI downloaded from a Cloud Storage bucket.
    
    
    # An OS policy assignment to install a Windows MSI downloaded from a Google Cloud Storage bucket
    # on all VMs running Windows Server OS.
    osPolicies:
      - id: install-msi-policy
        mode: ENFORCEMENT
        resourceGroups:
          - resources:
              - id: install-msi
                pkg:
                  desiredState: INSTALLED
                  msi:
                    source:
                      gcs:
                        bucket: my-bucket
                        object: my-app.msi
                        generation: 1619136883923956
    instanceFilter:
      inventories:
        - osShortName: windows
    rollout:
      disruptionBudget:
        fixed: 10
      minWaitDuration: 300s
    

### Example 2

Create an OS policy assignment that verifies if the Apache web server is running on all your Linux VMs.
    
    
    # An OS policy assignment that ensures Apache web server is running on Linux OSes.
    # The assignment is applied only to those VMs that have the label `type:webserver` assigned to them.
    osPolicies:
      - id: apache-always-up-policy
        mode: ENFORCEMENT
        resourceGroups:
          - resources:
              id: ensure-apache-is-up
              exec:
                validate:
                  interpreter: SHELL
                  # If Apache web server is already running, return an exit code 100 to indicate
                  # that exec resource is already in desired state. In this scenario,
                  # the `enforce` step will not be run.
                  # Otherwise return an exit code of 101 to indicate that exec resource is not in
                  # desired state. In this scenario, the `enforce` step will be run.
                  script: if systemctl is-active --quiet httpd; then exit 100; else exit 101; fi
                enforce:
                  interpreter: SHELL
                  # Start Apache web server and return an exit code of 100 to indicate that the
                  # resource is now in its desired state.
                  script: systemctl start httpd && exit 100
    instanceFilter:
      inclusionLabels:
        - labels:
            type: webserver
    rollout:
      disruptionBudget:
        fixed: 10
      minWaitDuration: 300s
    

### Example 3

Creates an OS policy assignment that installs Google Cloud Observability agents on CentOS VMs.
    
    
    # An OS policy assignment that ensures google-cloud-ops-agent is running on all Centos VMs in the project
    osPolicies:
      - id: cloudops-policy
        mode: ENFORCEMENT
        resourceGroups:
            resources:
              - id: add-repo
                repository:
                  yum:
                    id: google-cloud-ops-agent
                    displayName: Google Cloud Ops Agent Repository
                    baseUrl: https://packages.cloud.google.com/yum/repos/google-cloud-ops-agent-el7-x86_64-all
                    gpgKeys:
                      - https://packages.cloud.google.com/yum/doc/yum-key.gpg
                      - https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
              - id: install-pkg
                pkg:
                  desiredState: INSTALLED
                  yum:
                    name: google-cloud-ops-agent
              - id: exec-script
                exec:
                  validate:
                    script: |-
                      if [[ $(rpm --query --queryformat '%{VERSION}
                      ' google-cloud-ops-agent) == '1.0.2' ]]; then exit 100; else exit 101; fi
                    interpreter: SHELL
                  enforce:
                    script:
                      sudo yum remove -y google-cloud-ops-agent || true; sudo yum install
                      -y 'google-cloud-ops-agent-1.0.2*' && exit 100
                    interpreter: SHELL
              - id: ensure-agent-running
                exec:
                  validate:
                    script:
                      if (ps aux | grep 'opt[/].*google-cloud-ops-agent.*bin/'); then exit
                      100; else exit 101; fi
                    interpreter: SHELL
                  enforce:
                    script: sudo systemctl start google-cloud-ops-agent.target && exit 100
                    interpreter: SHELL
    instanceFilter:
      inventories:
        - osShortName: centos
    rollout:
      disruptionBudget:
        fixed: 10
      minWaitDuration: 300s
    

### Example 4

Creates an OS policy assignment that applies to multiple Linux and Windows operating systems.
    
    
    # An OS policy assignment that applies to multiple Linux and Windows operating systems.
    id: multi-os
    mode: VALIDATION
    resourceGroups:
      - inventoryFilters:
          - osShortName: debian
          - osShortName: centos
          - osShortName: ubuntu
          - osShortName: rhel
          - osShortName: rocky
          - osShortName: cos
          - osShortName: opensuse-leap
          - osShortName: ol
          - osShortName: sles
        resources:
          - id: linux
            exec:
              validate:
                interpreter: SHELL
                # Linux-specific script.
                # Exit code of 100 = resource is in the desired state
                script: |
                  exit 100
      - inventoryFilters:
          - osShortName: windows
        resources:
          - id: windows
            exec:
              validate:
                interpreter: POWERSHELL
                # Windows-specific script.
                # Exit code of 100 = resource is in the desired state
                script: |
                  exit 100
    

## What's next?

  * Learn more about [OS policies](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies).
  * [Create an OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/create-os-policy-assignment).
  * [Manage OS policies](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/manage-os-policy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
