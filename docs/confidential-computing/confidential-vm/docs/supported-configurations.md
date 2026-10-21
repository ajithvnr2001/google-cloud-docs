---
url: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations/
title: Supported configurations \u00a0|\u00a0 Confidential VM \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:25.334511+00:00
---

# Supported configurations  |  Confidential VM  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Confidential VM ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview)



Send feedback 

#  Supported configurations Stay organized with collections  Save and categorize content based on your preferences. 

To create a Confidential VM instance, you need a virtual machine that has the following properties:

  * [A supported Compute Engine machine type, CPU, and zone](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#machine-type-cpu-zone)

  * [A supported operating system](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#operating-systems)




You can configure your own Confidential VM instance manually, or accept the suggested settings when you enable the Confidential VM service in the Google Cloud console.

## Limitations

The following limitations apply depending on how you've configured your Confidential VM instance.

###  All Confidential VM instances 

  * You must create a new VM instance to enable Confidential VM. Existing instances can't be converted to Confidential VM instances.

  * You can't attach [TPUs](https://docs.cloud.google.com/tpu/docs/intro-to-tpu) to Confidential VM instances.

  * Confidential VM instances require an NVMe interface for disks. SCSI isn't supported.

  * Only new disks can be formatted to XFS on Linux kernel versions earlier than 5.10. To format existing disks to XFS, you need kernel version 5.10 or later.

  * You can't attach more than 40 disks to a Confidential VM instance. You can request an exception through a [support channel](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/get-support), although instances with more than 40 disks might fail silently.

  * Boot time is proportional to the amount of memory assigned to an instance. You might notice longer boot times for Confidential VM instances with large amounts of memory.

  * Establishing SSH connections takes longer on Confidential VM instances than non-Confidential VM instances.

  * [Live migration](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/troubleshoot-live-migration) is supported on N2D and C3D machine types running AMD SEV.

  * Confidential VM instances might experience lower network bandwidth and higher latency compared to non-Confidential VM instances.

  * Confidential VM instances with Hyperdisk Throughput have a restricted maximum data transfer size (MDTS), which reduces performance. To minimize performance degradation, avoid read-ahead requests exceeding the MDTS limit by setting `read_ahead_kb` to `124` KiB when using buffered I/O.




###  AMD SEV 

  * Debian 12 doesn't have attestation support for AMD SEV due to the missing `/dev/sev-guest` package.

  * AMD SEV on C2D and N2D machine types has a maximum [vNIC queue count](https://docs.cloud.google.com/compute/docs/network-bandwidth#rx-tx) of `8`.




  * AMD SEV on the C4D and C3D machine type has the following limitations:

    * Confidential VM instances that use C4D and C3D machine types might experience lower network bandwidth than equivalent non-confidential VM instances, even with [per VM Tier_1 networking performance](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) enabled.

    * Bare metal instances aren't supported.

    * The `rhel-8-4-sap-ha` image tagged `SEV_CAPABLE` doesn't work with AMD SEV on C4D and C3D machines with more than 8 vCPUs. This image is missing a required [patch](https://kernel.googlesource.com/pub/scm/linux/kernel/git/torvalds/linux.git/+/e998879d4fb7991856916972168cf27c0d86ed12%5E%21/?pli=1) that increases the size of the SWIOTLB buffer for high networking queues.

    * Confidential VM instances with AMD SEV on C3D machine type don't support Hyperdisk Balanced and Hyperdisk Throughput. 




###  AMD SEV-SNP 

  * Debian 12 doesn't have attestation support for AMD SEV-SNP due to the missing `/dev/sev-guest` package.

  * AMD SEV-SNP on N2D machine types has a maximum [vNIC queue count](https://docs.cloud.google.com/compute/docs/network-bandwidth#rx-tx) of `8`.

  * VM instances don't support `kdump`. Instead, use the guest console logs.

  * Confidential VM instances with AMD SEV-SNP don't support [reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview).

  * Due to a guest kernel migration and security updates, Confidential VM instances with AMD SEV-SNP might have longer boot times and performance changes between August 2026 and November 2026.




###  Intel TDX 

  * Intel TDX supports up to 192 vCPUs.

  * [Local SSD](https://docs.cloud.google.com/compute/docs/machine-resource#lssd-types) is only supported on `c3-standard-*-lssd` machine types.

  * VM instances take longer to shut down compared to standard VM instances. This delay increases with VM memory size.

  * Only Balanced Persistent Disk volumes that use the NVMe interface are supported.

  * VM instances can't be provisioned on sole-tenant node groups.

  * Due to additional security constraints, the CPUID instruction might return limited or no CPU architecture details. This might impact the performance of workloads that depend on those CPUID values.

  * VM instances don't support `kdump`. Instead, use the guest console logs.

  * Guest images without the [TDX halt fixes](https://lore.kernel.org/lkml/20250228014416.3925664-1-vannapurve@google.com/) might experience extended halt durations, resulting in performance degradation. To avoid the performance degradation, verify that these patches are installed in your guest kernel build.

  * Confidential VM instances with Intel TDX don't support [reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview).




###  NVIDIA Confidential Computing 

  * These VM instances don't support the creation of clusters for multi-node workloads.

  * These VM instances don't support [Hyperdisk Extreme](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme).

  * VM instances running on the [A3 High machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms) with NVIDIA H100 GPUs don't support [reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview).

  * Machine type limitations apply. See the limitations for each machine type:

    * [A3 High](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-high-limitations)
    * [G4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-limitations)



## Machine types, CPUs, and zones

Confidential VM is supported on the following machine types and configurations. For information about the GPU quotas required to create instances with attached GPUs, see [Quotas](https://docs.cloud.google.com/confidential-computing/confidential-vm/quotas#gpu-quotas).

Machine type | CPU platform | Confidential Computing technology | Live migration support | GPU support  
---|---|---|---|---  
`a3-highgpu-1g` [ View machine type names](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-standard-vms) | 

  * Intel Sapphire Rapids

| 

  * Intel TDX [See limitations](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx#limitations)
  * NVIDIA [See limitations](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=nvidia-confidential-computing#limitations)

| Not supported | Supported  
C2D [ View machine type names](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#c2d_machine_types) | 

  * AMD EPYC Milan

| 

  * AMD SEV [See limitations](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev#limitations)

| Not supported | Not supported  
`c3-standard-*` [ View machine type names](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_machine_types) | 

  * Intel Sapphire Rapids

| 

  * Intel TDX [See limitations](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx#limitations)

| Not supported | Not supported  
`c3-standard-*-lssd` [ View machine type names](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3-standard_1) | 

  * Intel Sapphire Rapids

| 

  * Intel TDX [See limitations](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx#limitations)

| Not supported | Not supported  
C3D [ View machine type names](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3d_machine_types) | 

  * AMD EPYC Genoa

| 

  * AMD SEV [See limitations](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev#limitations)

| Supported | Not supported  
`c4-standard-*` [ View machine type names](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_machine_types) | 

  * Intel Granite Rapids

| 

  * Intel TDX [See limitations](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=intel-tdx#limitations)

| Not supported | Not supported  
C4D [ View machine type names](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_machine_types) | 

  * AMD EPYC Turin

| 

  * AMD SEV [See limitations](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev#limitations)

| Not supported | Not supported  
`g4-standard-48` [ View machine type names](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series) | 

  * AMD EPYC Turin

| 

  * AMD SEV [See limitations](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev#limitations)
  * NVIDIA [ See limitations](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=nvidia-confidential-computing#limitations)

| Not supported | Supported  
N2D [ View machine type names](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2d_machine_types) | 

  * AMD EPYC Milan

| 

  * AMD SEV on Milan [See limitations](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev#limitations)
  * AMD SEV-SNP on Milan [See limitations](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations?tab=amd-sev-snp#limitations)

| Supported on AMD SEV VM instances only | Not supported  
  
### View supported zones

You can view which zones support these machine types and Confidential Computing technology with one of the following methods.

###  AMD SEV 

###  Reference table 

To view which zones support SEV on Confidential VM, complete the following steps.

  1. Go to [**Available regions and zones**](https://docs.cloud.google.com/compute/docs/regions-zones#available).

  2. Click **Select a machine type** , and then select **N2D** , **C2D** , **C3D** , and **C4D**.

  3. Click **Select a CPU** , and then select **AMD EPYC Milan** , **AMD EPYC Genoa** , or **AMD EPYC Turin**.




###  gcloud 

To list the zones available in Google Cloud, run the following command:
    
    
    gcloud compute zones list \
        --format="value(NAME)"
    

To list the available CPU platforms for a specific zone, run the following command and check for AMD Milan, AMD Genoa, or AMD Turin support:
    
    
    gcloud compute zones describe ZONE_NAME \
        --format="value(availableCpuPlatforms)"
    

###  AMD SEV-SNP 

AMD SEV-SNP is supported in the following zones, on N2D machine type with AMD Milan CPU platforms:

  * asia-southeast1-a

  * asia-southeast1-b

  * asia-southeast1-c

  * europe-west2-b

  * europe-west2-c

  * europe-west3-a

  * europe-west3-b

  * europe-west3-c

  * europe-west4-a

  * europe-west4-b

  * europe-west4-c

  * us-central1-a

  * us-central1-b

  * us-central1-c




###  Intel TDX 

###  c3-standard-* 

Intel TDX is supported in the following zones, on `c3-standard-*` machine types.

  * asia-northeast1-b

  * asia-south1-b

  * asia-southeast1-a

  * asia-southeast1-b

  * asia-southeast1-c

  * europe-west3-a

  * europe-west3-b

  * europe-west4-a

  * europe-west4-b

  * europe-west4-c

  * europe-west9-a

  * europe-west9-b

  * us-central1-a

  * us-central1-b

  * us-central1-c

  * us-east1-b

  * us-east1-c

  * us-east4-a

  * us-east4-b

  * us-east4-c

  * us-east5-b

  * us-east5-c

  * us-west1-a

  * us-west1-b




###  c3-standard-*-lssd 

Intel TDX is supported on `c3-standard-*-lssd` machine types in the following zones:

  * asia-southeast1-a

  * asia-southeast1-b

  * europe-west4-a

  * europe-west4-b

  * southamerica-east1-a

  * us-central1-a

  * us-central1-b

  * us-east4-b

  * us-east4-c

  * us-east5-b

  * us-east5-c

  * us-west1-b




###  c4-standard-* 

Intel TDX is supported in the following zones, on `c4-standard-*` machine types:

  * asia-southeast1-a

  * asia-southeast1-b

  * asia-southeast1-c

  * europe-west1-b

  * europe-west3-a

  * europe-west3-b

  * europe-west4-a

  * europe-west4-b

  * us-central1-a

  * us-central1-b

  * us-central1-f

  * us-east4-a

  * us-east4-b

  * us-east4-c

  * us-west1-a




###  NVIDIA Confidential Computing 

###  A3 High machine type 

NVIDIA Confidential Computing is supported in the following zones, on Confidential VM instances with an attached GPU on the A3 High machine type:

  * europe-west4-c

  * us-central1-a

  * us-east5-a




###  G4 machine type 

NVIDIA Confidential Computing is supported in the following zones, on Confidential VM instances with an attached GPU on the G4 machine type:

  * asia-east1-a

  * asia-east1-b

  * asia-south1-c

  * asia-south2-a

  * asia-south2-c

  * asia-southeast1-a

  * asia-southeast1-b

  * asia-southeast1-c

  * asia-southeast2-b

  * asia-southeast2-c

  * europe-north1-a

  * europe-north1-b

  * europe-north1-c

  * europe-west1-c

  * europe-west2-b

  * europe-west2-c

  * europe-west4-a

  * europe-west4-ai1a

  * europe-west4-b

  * europe-west8-b

  * europe-west10-b

  * us-central1-d

  * us-central1-f

  * us-east1-b

  * us-east1-d

  * us-east4-b

  * us-east4-c

  * us-east5-a

  * us-east5-b

  * us-east5-c

  * us-south1-a

  * us-south1-b

  * us-west1-b

  * us-west1-c

  * us-west3-a

  * us-west4-a




## Operating systems

For the available Confidential VM operating system images, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details). Find your distribution of choice, and then click the **Security features** tab to check if Confidential VM is supported.

Alternatively, you can view supported operating system images with a `gcloud` command, or [create your own Linux image](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/create-custom-confidential-vm-images).

### View supported operating system images with gcloud

The operating system images you can use are determined by your Confidential Computing technology choice.

You can list the operating system images, their image families, and their versions that support AMD and Intel Confidential Computing technologies by running the following command:
    
    
    gcloud compute images list \
        --filter="guestOsFeatures[].type:(OS_FEATURE)"
    

Provide the following value:

`OS_FEATURE`: The type of Confidential Computing support you want. Accepted values are:

  * `SEV_CAPABLE`: Operating systems that support AMD SEV.

  * `SEV_LIVE_MIGRATABLE_V2`: Operating systems that support AMD SEV and live migration.

  * `SEV_SNP_CAPABLE`: Operating systems that support AMD SEV-SNP isolation and attestation.

  * `TDX_CAPABLE`: Operating systems that support Intel TDX isolation and attestation.




To limit the results to a specific image family, project, or other text provided in the previous command's response, use an `AND` operator, and replace STRING with a partial text match, similar to the following example:
    
    
    gcloud compute images list \
        --filter="guestOsFeatures[].type:(OS_FEATURE) AND STRING"
    

To view details about a specific image, run the following command using details from the responses of the previous commands:
    
    
    gcloud compute images describe IMAGE_NAME \
        --project=IMAGE_PROJECT
    

### Supported images for a Confidential VM instance with GPU

For Confidential VM instances with attached NVIDIA GPUs, we recommend using the following operating system image families based on the machine type:

  * **A3 High machine type** :

    * `ubuntu-2204-lts`

    * `cos-tdx-113-lts`

While other images might be tagged as `TDX_CAPABLE`, we don't provide official support for them when used with GPUs.

  * **G4 machine type** :

    * `ubuntu-2404-lts-amd64`

    * `cos-125-lts`




### Supported images for C3 with Local SSD

For Confidential VM instances using Intel TDX on `c3-standard-*-lssd` machine types, the following operating system image families are supported:

  * `cos-117-lts`

  * `cos-121-lts`




## What's next

  * Learn how to [create a Confidential VM instance](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/create-a-confidential-vm-instance).

  * Learn how to [create a Confidential VM instance with GPU](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/create-a-confidential-vm-instance-with-gpu).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
