---
url: https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core/
title: Set the number of threads per core \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:05:21.562144+00:00
---

# Set the number of threads per core  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Set the number of threads per core Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

Simultaneous multithreading (SMT), which is known on Intel processors as Hyper-Threading Technology (HTT), lets a CPU core run as two hardware multithreads. On Compute Engine, each virtual CPU (vCPU) is implemented as a single hardware multithread, and two vCPUs share each physical CPU core by default.

Compute Engine lets you manually set the value for the number of threads per core. For example, workloads with the following concerns might benefit from disabling SMT (setting the number of threads per core to 1):

  * **Performance:** Reducing the number of threads that can run on each physical CPU core can help improve the performance of compute-bound workloads. This is beneficial for highly parallel high performance computing (HPC) applications and workloads that perform many floating-point calculations.

  * **Security:** If a VM runs untrusted code, reducing the number of threads per core can help mitigate CPU vulnerabilities such as [Microarchitectural Data Sampling](https://www.intel.com/content/www/us/en/developer/articles/technical/software-security-guidance/technical-documentation/intel-analysis-microarchitectural-data-sampling.html).

  * **Licensing:** Some licensing agreements have requirements related to the number of vCPUs that you consume. Reducing the number of threads per core from 2 to 1 might reduce your licensing costs. For more information, consult your licensing agreement.




For many general computing tasks or tasks that require lots of I/O, SMT can increase application throughput significantly. For compute-bound jobs in which both virtual cores are compute-bound, SMT can hinder overall application performance and can add unpredictable variance to jobs. In this case, turning off SMT allows more predictable performance and can decrease job times.

**Important:** Disabling SMT changes the way cores are counted and may increase the cost per core. Although cost per core is a common metric for on-premises hardware, a more appropriate metric for the cloud is cost per workload, or cost per job. For compute-bound jobs, you pay for what you use. Turning off SMT can reduce the overall runtime, which can reduce the overall cost of the job. We recommend that you benchmark your application and use this feature where it's beneficial.

## Limitations

  * You cannot set the number of threads per core on VMs for the following machine types:

    * [All C4A machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_machine_types)
    * [All H4D machine types](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_machine_types)
    * [All H3 machine types](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h3_machine_types)
    * [All N4A machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_machine_types)
    * [All Tau T2A machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machine_types)
    * [All Tau T2D machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2d_machine_types)
    * Machine types that have fewer than 2 vCPUs, for example, `n1-standard-1`
    * [Shared-core](https://docs.cloud.google.com/compute/docs/general-purpose-machines#sharedcore) machine types, such as `e2-small`.
  * For [bare metal instances](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances), the number of hyperthreads you have access to is equivalent to the number of hyperthreads on the machine.




## Known issues

In the Google Cloud console, when the number of threads per core is set to 1, the CPU utilization metric scales up to a maximum of 50%. This is a known visualization error. The actual CPU utilization is double what is shown.

## Pricing

You are billed for the number of vCPUs defined by a VM's machine type, not the number of threads that run on each core. For example, the `n2-standard-8` machine type can run up to 8 vCPUs, which is 2 vCPUs for each of the 4 physical CPU cores. If, with the `n2-standard-8` machine type, you decide to only run 1 thread per core—effectively 4 vCPUs—you are still billed for 8 vCPUs. For more information about how you are billed for VMs, see [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing).

## Change the number of threads per core during VM creation

To change the number of threads per core during VM creation, use the Google Cloud console, the gcloud CLI, or the Compute Engine API.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions):

  * All permissions required to [create a new VM](https://docs.cloud.google.com/compute/docs/instances/create-start-instance)



###  Console 

To change the number of threads per core during VM creation, use the following Google Cloud console procedure:

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Name** field, enter a name for the VM.

  3. Choose a **Region** and a **Zone** for the VM.

  4. Choose a **Machine family** and a supported **Machine type**.

  5. Click **Advanced configurations** to expand the section.

  6. In **vCPUs to core ratio** , choose the number of threads per core.

  7. Finish configuring other settings for the VM and click **Create**.




###  gcloud 

To change the number of threads per core during VM creation, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).

Before using any of the command data below, make the following replacements: 

  * VM_NAME: the name for the new VM.
  * ZONE: the zone for the new VM.
  * MACHINE_TYPE: the machine type for the new VM. Must be a machine type with 2 or more vCPUs.
  * THREADS_PER_CORE: the number of threads per physical core. Set to either `2` or `1`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud compute instances create VM_NAME \
        --zone=ZONE \
        --machine-type=MACHINE_TYPE \
        --threads-per-core=THREADS_PER_CORE

#### Windows (PowerShell)
    
    
    gcloud compute instances create VM_NAME `
        --zone=ZONE `
        --machine-type=MACHINE_TYPE `
        --threads-per-core=THREADS_PER_CORE

#### Windows (cmd.exe)
    
    
    gcloud compute instances create VM_NAME ^
        --zone=ZONE ^
        --machine-type=MACHINE_TYPE ^
        --threads-per-core=THREADS_PER_CORE

You should receive a response similar to the following:
    
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME].
    NAME: VM_NAME
    ZONE: ZONE
    MACHINE_TYPE: MACHINE_TYPE
    PREEMPTIBLE:
    INTERNAL_IP: EXTERNAL_IP
    EXTERNAL_IP: INTERNAL_IP
    STATUS: RUNNING
    

###  REST 

To change the number of threads per core during VM creation, use the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) with the `threadsPerCore` field.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID.
  * ZONE: the zone for the new VM.
  * MACHINE_TYPE: the machine type for the new VM. Must be a machine type with 2 or more vCPUs.
  * VM_NAME: the name for the new VM.
  * THREADS_PER_CORE: the number of threads per physical core. Set to either `2` or `1`.



HTTP method and URL: 
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances

Request JSON body: 
    
    
    {
      "machineType": "projects/PROJECT_ID/zones/ZONE/machineTypes/MACHINE_TYPE",
      "name": "VM_NAME",
      "advancedMachineFeatures": {
        "threadsPerCore": THREADS_PER_CORE
      },
      "disks": [
        {
          "type": "PERSISTENT",
          "boot": true,
          "initializeParams": {
            "sourceImage": "projects/debian-cloud/global/images/family/debian-13"
          }
        }
      ],
      "networkInterfaces": [
        {
          "network": "global/networks/default"
        }
      ]
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances"

#### PowerShell (Windows)

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "compute#operation",
      "id": "7334609091572405391",
      "name": "operation-1663806045894-5e939085735d8-7499db32-c12fcc03",
      "zone": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE",
      "operationType": "insert",
      "targetLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME",
      "targetId": "1226375378512516273",
      "status": "RUNNING",
      "user": "EMAIL_ADDRESS",
      "progress": 0,
      "insertTime": "2022-09-21T17:20:48.751-07:00",
      "startTime": "2022-09-21T17:20:48.751-07:00",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/operations/operation-1663806045894-5e939085735d8-7499db32-c12fcc03"
    }
    

## Change the number of threads per core on a VM

To change the number of threads per core on a VM, use the Google Cloud console, the gcloud CLI, or the Compute Engine API.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions):

  * `compute.instances.get` on the project 
  * `compute.instances.update` on the project 



###  Console 

To change the number of threads per core on an existing VM, use the following Google Cloud console procedure:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the **Name** of the VM.

  3. Click stop **Stop** to stop the VM. If there is no **Stop** option, click more_vert **More actions >** stop **Stop**.

  4. Click **Edit**.

  5. Click **Advanced configurations** to expand the section.

  6. In the **vCPUs to core ratio** drop-down list, choose the number of threads per core.

  7. Click **Save**.




###  gcloud 

To change the number of threads per core on an existing VM, do the following:

  1. Export the properties of the VM by using the following [`gcloud compute instances export` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/export):
         
         gcloud compute instances export VM_NAME \
             --destination=YAML_FILE_PATH \
             --zone=ZONE
         

Replace the following:

     * `VM_NAME`: the name of the VM from which to export properties

     * `YAML_FILE_PATH`: the path and filename of a YAML file in which to save the exported configuration data

     * `ZONE`: the zone that contains the VM

  2. In the VM configuration file that was saved in FILE_PATH, update the value for `threadsPerCore`. If the value is not in the file, add the following:
         
         advancedMachineFeatures:
           threadsPerCore: THREADS_PER_CORE
         

**Tip:** To avoid getting an error such as `"ERROR: (gcloud.compute.instances.update-from-file) Cannot parse YAML: [Expected type  for field value, found True (type )]"`, add quotes (`' '`) around any label values of `yes` or `no` in the exported instance configuration file. This indicates the values are strings, not Boolean values.
  3. Update the VM with the new count of threads per core by using the following [`gcloud compute instances update-from-file` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update-from-file):
         
         gcloud compute instances update-from-file VM_NAME \
             --source=FILE_PATH \
             --most-disruptive-allowed-action=RESTART \
             --zone=ZONE
         

Replace the following:

     * `VM_NAME`: the name of the VM to update

     * `FILE_PATH`: the path to the updated VM configuration file

     * `ZONE`: the zone that contains the VM to update




###  REST 

To change the number of threads per core on an existing VM, use the following [`instances.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/update):
    
    
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME?most_disruptive_allowed_action=RESTART
    
    {
      ...
      "advanced_machine_features": {
        ...
        "threadsPerCore": "THREADS_PER_CORE"
      },
      ...
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project

  * `ZONE`: the zone that contains the VM

  * `VM_NAME`: the name of the VM from which to export properties

  * `THREADS_PER_CORE`: the number of threads per core




## View the number of threads per core

To view the number of threads per core, use the procedure that corresponds to the OS that is running on the VM.

###  Linux 

To view the number of threads per core on Linux-based VMs, use the following procedure:

  1. [Connect to the Linux VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).

  2. Run the `lscpu` command.
         
         lscpu
         

  3. Review the output to view the number of threads per core.

In the following sample output from an `n2-standard-16` machine, the value for the number of threads per core is `1` as shown in the `Thread(s) per core` line.
         
         ...
         CPU(s):                          8
         On-line CPU(s) list:             0-7
         Thread(s) per core:              1
         Core(s) per socket:              8
         Socket(s):                       1
         NUMA node(s):                    1
         Vendor ID:                       GenuineIntel
         CPU family:                      6
         Model:                           85
         Model name:                      Intel(R) Xeon(R) CPU @ 2.80GHz
         ...
         




###  Windows 

To view the number of threads per core on Windows-based VMs, use the following procedure:

  1. [Connect to the Windows VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).

  2. Launch Powershell.

  3. Run the following command.
         
         Get-WmiObject -Class Win32_processor | Select-Object NumberOfCores, @{Name="Thread(s) per core";Expression={$_.NumberOfLogicalProcessors/$_.NumberOfCores}}
         

  4. Review the output to view the number of threads per core.

In the following sample output from an `n2-standard-16` machine, the value for the number of threads per core is `1` as shown in the `Thread(s) per core` column.
         
         NumberOfCores Thread(s) per core
         ------------- ------------------
                     8                  1
         




## What's next

  * Learn about the [operating systems that you can run on Compute Engine VMs](https://docs.cloud.google.com/compute/docs/images/os-details).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
