---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Commitment.Type
title: Enum Commitment.Type (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:19.613317+00:00
---

# Enum Commitment.Type (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Commitment.Type

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum Commitment.Type (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 
    
    
    public enum Commitment.Type extends Enum<Commitment.Type> implements ProtocolMessageEnum

The type of commitment; specifies the machine series for which you want to commit to purchasing resources. The choice of machine series affects the discount rate and the eligible resource types.

The type must be one of the following:ACCELERATOR_OPTIMIZED, ACCELERATOR_OPTIMIZED_A3,ACCELERATOR_OPTIMIZED_A3_MEGA,COMPUTE_OPTIMIZED, COMPUTE_OPTIMIZED_C2D, COMPUTE_OPTIMIZED_C3, COMPUTE_OPTIMIZED_C3D,COMPUTE_OPTIMIZED_H3, GENERAL_PURPOSE,GENERAL_PURPOSE_C4, GENERAL_PURPOSE_E2,GENERAL_PURPOSE_N2, GENERAL_PURPOSE_N2D,GENERAL_PURPOSE_N4, GENERAL_PURPOSE_T2D,GRAPHICS_OPTIMIZED, GRAPHICS_OPTIMIZED_G4,GRAPHICS_OPTIMIZED_G4_VGPU,MEMORY_OPTIMIZED, MEMORY_OPTIMIZED_M3,MEMORY_OPTIMIZED_X4, STORAGE_OPTIMIZED_Z3,STORAGE_OPTIMIZED_Z4DS, STORAGE_OPTIMIZED_Z4DH,STORAGE_OPTIMIZED_Z4D4T,STORAGE_OPTIMIZED_Z4M. For example, type MEMORY_OPTIMIZED specifies a commitment that applies only to eligible resources of memory optimized M1 and M2 machine series. Type GENERAL_PURPOSE specifies a commitment that applies only to eligible resources of general purpose N1 machine series.

Protobuf enum `google.cloud.compute.v1.Commitment.Type`

## Implements

[ProtocolMessageEnum](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolMessageEnum.html)

## Inherited Members

[Enum.<T>valueOf(Class<T>,String)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#valueOf-java.lang.Class-java.lang.String-)

[Enum.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#clone--)

[Enum.compareTo(E)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#compareTo-E-)

[Enum.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#equals-java.lang.Object-)

[Enum.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#finalize--)

[Enum.getDeclaringClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#getDeclaringClass--)

[Enum.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#hashCode--)

[Enum.name()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#name--)

[Enum.ordinal()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#ordinal--)

[Enum.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#toString--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields   
  
---  
**Name** | **Description**  
`ACCELERATOR_OPTIMIZED` | `ACCELERATOR_OPTIMIZED = 280848403;`  
`ACCELERATOR_OPTIMIZED_A3` | `ACCELERATOR_OPTIMIZED_A3 = 158574526;`  
`ACCELERATOR_OPTIMIZED_A3_MEGA` | `ACCELERATOR_OPTIMIZED_A3_MEGA = 156517459;`  
`ACCELERATOR_OPTIMIZED_A3_MEGA_VALUE` | `ACCELERATOR_OPTIMIZED_A3_MEGA = 156517459;`  
`ACCELERATOR_OPTIMIZED_A3_ULTRA` | `ACCELERATOR_OPTIMIZED_A3_ULTRA = 27812811;`  
`ACCELERATOR_OPTIMIZED_A3_ULTRA_VALUE` | `ACCELERATOR_OPTIMIZED_A3_ULTRA = 27812811;`  
`ACCELERATOR_OPTIMIZED_A3_VALUE` | `ACCELERATOR_OPTIMIZED_A3 = 158574526;`  
`ACCELERATOR_OPTIMIZED_A4` | `ACCELERATOR_OPTIMIZED_A4 = 158574527;`  
`ACCELERATOR_OPTIMIZED_A4_VALUE` | `ACCELERATOR_OPTIMIZED_A4 = 158574527;`  
`ACCELERATOR_OPTIMIZED_VALUE` | `ACCELERATOR_OPTIMIZED = 280848403;`  
`COMPUTE_OPTIMIZED` | `COMPUTE_OPTIMIZED = 158349023;`  
`COMPUTE_OPTIMIZED_C2D` | `COMPUTE_OPTIMIZED_C2D = 383246453;`  
`COMPUTE_OPTIMIZED_C2D_VALUE` | `COMPUTE_OPTIMIZED_C2D = 383246453;`  
`COMPUTE_OPTIMIZED_C3` | `COMPUTE_OPTIMIZED_C3 = 428004784;`  
`COMPUTE_OPTIMIZED_C3D` | `COMPUTE_OPTIMIZED_C3D = 383246484;`  
`COMPUTE_OPTIMIZED_C3D_VALUE` | `COMPUTE_OPTIMIZED_C3D = 383246484;`  
`COMPUTE_OPTIMIZED_C3_VALUE` | `COMPUTE_OPTIMIZED_C3 = 428004784;`  
`COMPUTE_OPTIMIZED_H3` | `COMPUTE_OPTIMIZED_H3 = 428004939;`  
`COMPUTE_OPTIMIZED_H3_VALUE` | `COMPUTE_OPTIMIZED_H3 = 428004939;`  
`COMPUTE_OPTIMIZED_H4D` | `COMPUTE_OPTIMIZED_H4D = 383251320;`  
`COMPUTE_OPTIMIZED_H4D_VALUE` | `COMPUTE_OPTIMIZED_H4D = 383251320;`  
`COMPUTE_OPTIMIZED_VALUE` | `COMPUTE_OPTIMIZED = 158349023;`  
`GENERAL_PURPOSE` | `GENERAL_PURPOSE = 299793543;`  
`GENERAL_PURPOSE_C4` | `GENERAL_PURPOSE_C4 = 301911817;`  
`GENERAL_PURPOSE_C4A` | `GENERAL_PURPOSE_C4A = 232460888;`  
`GENERAL_PURPOSE_C4A_VALUE` | `GENERAL_PURPOSE_C4A = 232460888;`  
`GENERAL_PURPOSE_C4D` | `GENERAL_PURPOSE_C4D = 232460891;`  
`GENERAL_PURPOSE_C4D_VALUE` | `GENERAL_PURPOSE_C4D = 232460891;`  
`GENERAL_PURPOSE_C4_VALUE` | `GENERAL_PURPOSE_C4 = 301911817;`  
`GENERAL_PURPOSE_E2` | `GENERAL_PURPOSE_E2 = 301911877;`  
`GENERAL_PURPOSE_E2_VALUE` | `GENERAL_PURPOSE_E2 = 301911877;`  
`GENERAL_PURPOSE_N2` | `GENERAL_PURPOSE_N2 = 301912156;`  
`GENERAL_PURPOSE_N2D` | `GENERAL_PURPOSE_N2D = 232471400;`  
`GENERAL_PURPOSE_N2D_VALUE` | `GENERAL_PURPOSE_N2D = 232471400;`  
`GENERAL_PURPOSE_N2_VALUE` | `GENERAL_PURPOSE_N2 = 301912156;`  
`GENERAL_PURPOSE_N4` | `GENERAL_PURPOSE_N4 = 301912158;`  
`GENERAL_PURPOSE_N4A` | `GENERAL_PURPOSE_N4A = 232471459;`  
`GENERAL_PURPOSE_N4A_VALUE` | `GENERAL_PURPOSE_N4A = 232471459;`  
`GENERAL_PURPOSE_N4D` | `GENERAL_PURPOSE_N4D = 232471462;`  
`GENERAL_PURPOSE_N4D_VALUE` | `GENERAL_PURPOSE_N4D = 232471462;`  
`GENERAL_PURPOSE_N4_VALUE` | `GENERAL_PURPOSE_N4 = 301912158;`  
`GENERAL_PURPOSE_T2D` | `GENERAL_PURPOSE_T2D = 232477166;`  
`GENERAL_PURPOSE_T2D_VALUE` | `GENERAL_PURPOSE_T2D = 232477166;`  
`GENERAL_PURPOSE_VALUE` | `GENERAL_PURPOSE = 299793543;`  
`GRAPHICS_OPTIMIZED` | `GRAPHICS_OPTIMIZED = 68500563;`  
`GRAPHICS_OPTIMIZED_G4` | `GRAPHICS_OPTIMIZED_G4 = 54029369;`  
`GRAPHICS_OPTIMIZED_G4_VALUE` | `GRAPHICS_OPTIMIZED_G4 = 54029369;`  
`GRAPHICS_OPTIMIZED_G4_VGPU` | `GRAPHICS_OPTIMIZED_G4_VGPU = 298988732;`  
`GRAPHICS_OPTIMIZED_G4_VGPU_VALUE` | `GRAPHICS_OPTIMIZED_G4_VGPU = 298988732;`  
`GRAPHICS_OPTIMIZED_VALUE` | `GRAPHICS_OPTIMIZED = 68500563;`  
`MEMORY_OPTIMIZED` | `MEMORY_OPTIMIZED = 281753417;`  
`MEMORY_OPTIMIZED_M3` | `MEMORY_OPTIMIZED_M3 = 276301372;`  
`MEMORY_OPTIMIZED_M3_VALUE` | `MEMORY_OPTIMIZED_M3 = 276301372;`  
`MEMORY_OPTIMIZED_M4` | `MEMORY_OPTIMIZED_M4 = 276301373;`  
`MEMORY_OPTIMIZED_M4_6TB` | `MEMORY_OPTIMIZED_M4_6TB = 210543650;`  
`MEMORY_OPTIMIZED_M4_6TB_VALUE` | `MEMORY_OPTIMIZED_M4_6TB = 210543650;`  
`MEMORY_OPTIMIZED_M4_VALUE` | `MEMORY_OPTIMIZED_M4 = 276301373;`  
`MEMORY_OPTIMIZED_VALUE` | `MEMORY_OPTIMIZED = 281753417;`  
`MEMORY_OPTIMIZED_X4_1440_24T` |  CUD bucket for X4 machine with 1440 vCPUs and 24TB of memory. `MEMORY_OPTIMIZED_X4_1440_24T = 206669823;`  
`MEMORY_OPTIMIZED_X4_1440_24T_VALUE` |  CUD bucket for X4 machine with 1440 vCPUs and 24TB of memory. `MEMORY_OPTIMIZED_X4_1440_24T = 206669823;`  
`MEMORY_OPTIMIZED_X4_16TB` | `MEMORY_OPTIMIZED_X4_16TB = 183089120;`  
`MEMORY_OPTIMIZED_X4_16TB_VALUE` | `MEMORY_OPTIMIZED_X4_16TB = 183089120;`  
`MEMORY_OPTIMIZED_X4_1920_32T` |  CUD bucket for X4 machine with 1920 vCPUs and 32TB of memory. `MEMORY_OPTIMIZED_X4_1920_32T = 291963529;`  
`MEMORY_OPTIMIZED_X4_1920_32T_VALUE` |  CUD bucket for X4 machine with 1920 vCPUs and 32TB of memory. `MEMORY_OPTIMIZED_X4_1920_32T = 291963529;`  
`MEMORY_OPTIMIZED_X4_24TB` | `MEMORY_OPTIMIZED_X4_24TB = 183116989;`  
`MEMORY_OPTIMIZED_X4_24TB_VALUE` | `MEMORY_OPTIMIZED_X4_24TB = 183116989;`  
`MEMORY_OPTIMIZED_X4_32TB` | `MEMORY_OPTIMIZED_X4_32TB = 183144858;`  
`MEMORY_OPTIMIZED_X4_32TB_VALUE` | `MEMORY_OPTIMIZED_X4_32TB = 183144858;`  
`MEMORY_OPTIMIZED_X4_480_6T` |  CUD bucket for X4 machine with 480 vCPUs and 6TB of memory. `MEMORY_OPTIMIZED_X4_480_6T = 478547742;`  
`MEMORY_OPTIMIZED_X4_480_6T_VALUE` |  CUD bucket for X4 machine with 480 vCPUs and 6TB of memory. `MEMORY_OPTIMIZED_X4_480_6T = 478547742;`  
`MEMORY_OPTIMIZED_X4_480_8T` |  CUD bucket for X4 machine with 480 vCPUs and 8TB of memory. `MEMORY_OPTIMIZED_X4_480_8T = 478547804;`  
`MEMORY_OPTIMIZED_X4_480_8T_VALUE` |  CUD bucket for X4 machine with 480 vCPUs and 8TB of memory. `MEMORY_OPTIMIZED_X4_480_8T = 478547804;`  
`MEMORY_OPTIMIZED_X4_960_12T` |  CUD bucket for X4 machine with 960 vCPUs and 12TB of memory. `MEMORY_OPTIMIZED_X4_960_12T = 424752410;`  
`MEMORY_OPTIMIZED_X4_960_12T_VALUE` |  CUD bucket for X4 machine with 960 vCPUs and 12TB of memory. `MEMORY_OPTIMIZED_X4_960_12T = 424752410;`  
`MEMORY_OPTIMIZED_X4_960_16T` |  CUD bucket for X4 machine with 960 vCPUs and 16TB of memory. `MEMORY_OPTIMIZED_X4_960_16T = 424752534;`  
`MEMORY_OPTIMIZED_X4_960_16T_VALUE` |  CUD bucket for X4 machine with 960 vCPUs and 16TB of memory. `MEMORY_OPTIMIZED_X4_960_16T = 424752534;`  
`NETWORK_OPTIMIZED_C4N` |  CUD bucket for C4N (dual Diorite) machines. `NETWORK_OPTIMIZED_C4N = 147027572;`  
`NETWORK_OPTIMIZED_C4N_VALUE` |  CUD bucket for C4N (dual Diorite) machines. `NETWORK_OPTIMIZED_C4N = 147027572;`  
`NETWORK_OPTIMIZED_U4C` |  CUD bucket for NETWORK_OPTIMIZED_U4C machines. `NETWORK_OPTIMIZED_U4C = 147044859;`  
`NETWORK_OPTIMIZED_U4C_VALUE` |  CUD bucket for NETWORK_OPTIMIZED_U4C machines. `NETWORK_OPTIMIZED_U4C = 147044859;`  
`NETWORK_OPTIMIZED_U4P` |  CUD bucket for NETWORK_OPTIMIZED_U4P machines. `NETWORK_OPTIMIZED_U4P = 147044872;`  
`NETWORK_OPTIMIZED_U4P_VALUE` |  CUD bucket for NETWORK_OPTIMIZED_U4P machines. `NETWORK_OPTIMIZED_U4P = 147044872;`  
`NETWORK_OPTIMIZED_U4S` |  CUD bucket for NETWORK_OPTIMIZED_U4S machines. `NETWORK_OPTIMIZED_U4S = 147044875;`  
`NETWORK_OPTIMIZED_U4S_VALUE` |  CUD bucket for NETWORK_OPTIMIZED_U4S machines. `NETWORK_OPTIMIZED_U4S = 147044875;`  
`STORAGE_OPTIMIZED_Z3` | `STORAGE_OPTIMIZED_Z3 = 316796085;`  
`STORAGE_OPTIMIZED_Z3_VALUE` | `STORAGE_OPTIMIZED_Z3 = 316796085;`  
`STORAGE_OPTIMIZED_Z4D4T` |  CUD bucket for Z4D-4T machines. `STORAGE_OPTIMIZED_Z4D4T = 18503022;`  
`STORAGE_OPTIMIZED_Z4D4T_VALUE` |  CUD bucket for Z4D-4T machines. `STORAGE_OPTIMIZED_Z4D4T = 18503022;`  
`STORAGE_OPTIMIZED_Z4DH` |  CUD bucket for Z4DH machines. `STORAGE_OPTIMIZED_Z4DH = 35233722;`  
`STORAGE_OPTIMIZED_Z4DH_VALUE` |  CUD bucket for Z4DH machines. `STORAGE_OPTIMIZED_Z4DH = 35233722;`  
`STORAGE_OPTIMIZED_Z4DS` |  CUD bucket for Z4DS machines. `STORAGE_OPTIMIZED_Z4DS = 35233733;`  
`STORAGE_OPTIMIZED_Z4DS_VALUE` |  CUD bucket for Z4DS machines. `STORAGE_OPTIMIZED_Z4DS = 35233733;`  
`STORAGE_OPTIMIZED_Z4M` |  CUD bucket for Z4M (bare metal) machines. `STORAGE_OPTIMIZED_Z4M = 157002327;`  
`STORAGE_OPTIMIZED_Z4M_VALUE` |  CUD bucket for Z4M (bare metal) machines. `STORAGE_OPTIMIZED_Z4M = 157002327;`  
`TYPE_UNSPECIFIED` |  Note for internal users: When adding a new enum Type for v1, make sure to also add it in the comment for the `optional Type type` definition. This ensures that the public documentation displays the new enum Type. `TYPE_UNSPECIFIED = 437714322;`  
`TYPE_UNSPECIFIED_VALUE` |  Note for internal users: When adding a new enum Type for v1, make sure to also add it in the comment for the `optional Type type` definition. This ensures that the public documentation displays the new enum Type. `TYPE_UNSPECIFIED = 437714322;`  
`UNDEFINED_TYPE` |  A value indicating that the enum field is not set. `UNDEFINED_TYPE = 0;`  
`UNDEFINED_TYPE_VALUE` |  A value indicating that the enum field is not set. `UNDEFINED_TYPE = 0;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Commitment.Type#com_google_cloud_compute_v1_Commitment_Type_forNumber_int_) instead._  
`valueOf(String name)` |   
`values()` |   
  
## Methods   
  
---  
**Name** | **Description**  
`getDescriptorForType()` |   
`getNumber()` |   
`getValueDescriptor()` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
