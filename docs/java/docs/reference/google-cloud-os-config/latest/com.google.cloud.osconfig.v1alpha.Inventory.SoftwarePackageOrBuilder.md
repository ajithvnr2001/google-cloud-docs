---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.Inventory.SoftwarePackageOrBuilder
title: Interface Inventory.SoftwarePackageOrBuilder (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:49.196941+00:00
---

# Interface Inventory.SoftwarePackageOrBuilder (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.Inventory.SoftwarePackageOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Inventory.SoftwarePackageOrBuilder (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.6  2.4.3  2.3.2 
    
    
    public static interface Inventory.SoftwarePackageOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAptPackage()
    
    
    public abstract Inventory.VersionedPackage getAptPackage()

Details of an APT package. For details about the apt package manager, see <https://wiki.debian.org/Apt>.

`.google.cloud.osconfig.v1alpha.Inventory.VersionedPackage apt_package = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Inventory.VersionedPackage](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.Inventory.VersionedPackage)` | The aptPackage.  
  
### getAptPackageOrBuilder()
    
    
    public abstract Inventory.VersionedPackageOrBuilder getAptPackageOrBuilder()

Details of an APT package. For details about the apt package manager, see <https://wiki.debian.org/Apt>.

`.google.cloud.osconfig.v1alpha.Inventory.VersionedPackage apt_package = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Inventory.VersionedPackageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.Inventory.VersionedPackageOrBuilder)` |   
  
### getCosPackage()
    
    
    public abstract Inventory.VersionedPackage getCosPackage()

Details of a COS package.

`.google.cloud.osconfig.v1alpha.Inventory.VersionedPackage cos_package = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Inventory.VersionedPackage](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.Inventory.VersionedPackage)` | The cosPackage.  
  
### getCosPackageOrBuilder()
    
    
    public abstract Inventory.VersionedPackageOrBuilder getCosPackageOrBuilder()

Details of a COS package.

`.google.cloud.osconfig.v1alpha.Inventory.VersionedPackage cos_package = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Inventory.VersionedPackageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.Inventory.VersionedPackageOrBuilder)` |   
  
### getDetailsCase()
    
    
    public abstract Inventory.SoftwarePackage.DetailsCase getDetailsCase()

**Returns**  
---  
**Type** | **Description**  
`[Inventory.SoftwarePackage.DetailsCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.Inventory.SoftwarePackage.DetailsCase)` |   
  
### getGoogetPackage()
    
    
    public abstract Inventory.VersionedPackage getGoogetPackage()

Details of a Googet package. For details about the googet package manager, see <https://github.com/google/googet>.

`.google.cloud.osconfig.v1alpha.Inventory.VersionedPackage googet_package = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Inventory.VersionedPackage](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.Inventory.VersionedPackage)` | The googetPackage.  
  
### getGoogetPackageOrBuilder()
    
    
    public abstract Inventory.VersionedPackageOrBuilder getGoogetPackageOrBuilder()

Details of a Googet package. For details about the googet package manager, see <https://github.com/google/googet>.

`.google.cloud.osconfig.v1alpha.Inventory.VersionedPackage googet_package = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Inventory.VersionedPackageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.Inventory.VersionedPackageOrBuilder)` |   
  
### getQfePackage()
    
    
    public abstract Inventory.WindowsQuickFixEngineeringPackage getQfePackage()

Details of a Windows Quick Fix engineering package. See <https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/win32-quickfixengineering> for info in Windows Quick Fix Engineering.

` .google.cloud.osconfig.v1alpha.Inventory.WindowsQuickFixEngineeringPackage qfe_package = 7; `

**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsQuickFixEngineeringPackage](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.Inventory.WindowsQuickFixEngineeringPackage)` | The qfePackage.  
  
### getQfePackageOrBuilder()
    
    
    public abstract Inventory.WindowsQuickFixEngineeringPackageOrBuilder getQfePackageOrBuilder()

Details of a Windows Quick Fix engineering package. See <https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/win32-quickfixengineering> for info in Windows Quick Fix Engineering.

` .google.cloud.osconfig.v1alpha.Inventory.WindowsQuickFixEngineeringPackage qfe_package = 7; `

**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsQuickFixEngineeringPackageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.Inventory.WindowsQuickFixEngineeringPackageOrBuilder)` |   
  
### getWindowsApplication()
    
    
    public abstract Inventory.WindowsApplication getWindowsApplication()

Details of Windows Application.

`.google.cloud.osconfig.v1alpha.Inventory.WindowsApplication windows_application = 9; `

**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsApplication](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.Inventory.WindowsApplication)` | The windowsApplication.  
  
### getWindowsApplicationOrBuilder()
    
    
    public abstract Inventory.WindowsApplicationOrBuilder getWindowsApplicationOrBuilder()

Details of Windows Application.

`.google.cloud.osconfig.v1alpha.Inventory.WindowsApplication windows_application = 9; `

**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsApplicationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.Inventory.WindowsApplicationOrBuilder)` |   
  
### getWuaPackage()
    
    
    public abstract Inventory.WindowsUpdatePackage getWuaPackage()

Details of a Windows Update package. See <https://docs.microsoft.com/en-us/windows/win32/api/_wua/> for information about Windows Update.

`.google.cloud.osconfig.v1alpha.Inventory.WindowsUpdatePackage wua_package = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.Inventory.WindowsUpdatePackage)` | The wuaPackage.  
  
### getWuaPackageOrBuilder()
    
    
    public abstract Inventory.WindowsUpdatePackageOrBuilder getWuaPackageOrBuilder()

Details of a Windows Update package. See <https://docs.microsoft.com/en-us/windows/win32/api/_wua/> for information about Windows Update.

`.google.cloud.osconfig.v1alpha.Inventory.WindowsUpdatePackage wua_package = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.Inventory.WindowsUpdatePackageOrBuilder)` |   
  
### getYumPackage()
    
    
    public abstract Inventory.VersionedPackage getYumPackage()

Yum package info. For details about the yum package manager, see <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/ch-yum>.

`.google.cloud.osconfig.v1alpha.Inventory.VersionedPackage yum_package = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Inventory.VersionedPackage](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.Inventory.VersionedPackage)` | The yumPackage.  
  
### getYumPackageOrBuilder()
    
    
    public abstract Inventory.VersionedPackageOrBuilder getYumPackageOrBuilder()

Yum package info. For details about the yum package manager, see <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/ch-yum>.

`.google.cloud.osconfig.v1alpha.Inventory.VersionedPackage yum_package = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Inventory.VersionedPackageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.Inventory.VersionedPackageOrBuilder)` |   
  
### getZypperPackage()
    
    
    public abstract Inventory.VersionedPackage getZypperPackage()

Details of a Zypper package. For details about the Zypper package manager, see <https://en.opensuse.org/SDB:Zypper_manual>.

`.google.cloud.osconfig.v1alpha.Inventory.VersionedPackage zypper_package = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Inventory.VersionedPackage](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.Inventory.VersionedPackage)` | The zypperPackage.  
  
### getZypperPackageOrBuilder()
    
    
    public abstract Inventory.VersionedPackageOrBuilder getZypperPackageOrBuilder()

Details of a Zypper package. For details about the Zypper package manager, see <https://en.opensuse.org/SDB:Zypper_manual>.

`.google.cloud.osconfig.v1alpha.Inventory.VersionedPackage zypper_package = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Inventory.VersionedPackageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.Inventory.VersionedPackageOrBuilder)` |   
  
### getZypperPatch()
    
    
    public abstract Inventory.ZypperPatch getZypperPatch()

Details of a Zypper patch. For details about the Zypper package manager, see <https://en.opensuse.org/SDB:Zypper_manual>.

`.google.cloud.osconfig.v1alpha.Inventory.ZypperPatch zypper_patch = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Inventory.ZypperPatch](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.Inventory.ZypperPatch)` | The zypperPatch.  
  
### getZypperPatchOrBuilder()
    
    
    public abstract Inventory.ZypperPatchOrBuilder getZypperPatchOrBuilder()

Details of a Zypper patch. For details about the Zypper package manager, see <https://en.opensuse.org/SDB:Zypper_manual>.

`.google.cloud.osconfig.v1alpha.Inventory.ZypperPatch zypper_patch = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Inventory.ZypperPatchOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1alpha.Inventory.ZypperPatchOrBuilder)` |   
  
### hasAptPackage()
    
    
    public abstract boolean hasAptPackage()

Details of an APT package. For details about the apt package manager, see <https://wiki.debian.org/Apt>.

`.google.cloud.osconfig.v1alpha.Inventory.VersionedPackage apt_package = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the aptPackage field is set.  
  
### hasCosPackage()
    
    
    public abstract boolean hasCosPackage()

Details of a COS package.

`.google.cloud.osconfig.v1alpha.Inventory.VersionedPackage cos_package = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cosPackage field is set.  
  
### hasGoogetPackage()
    
    
    public abstract boolean hasGoogetPackage()

Details of a Googet package. For details about the googet package manager, see <https://github.com/google/googet>.

`.google.cloud.osconfig.v1alpha.Inventory.VersionedPackage googet_package = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the googetPackage field is set.  
  
### hasQfePackage()
    
    
    public abstract boolean hasQfePackage()

Details of a Windows Quick Fix engineering package. See <https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/win32-quickfixengineering> for info in Windows Quick Fix Engineering.

` .google.cloud.osconfig.v1alpha.Inventory.WindowsQuickFixEngineeringPackage qfe_package = 7; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the qfePackage field is set.  
  
### hasWindowsApplication()
    
    
    public abstract boolean hasWindowsApplication()

Details of Windows Application.

`.google.cloud.osconfig.v1alpha.Inventory.WindowsApplication windows_application = 9; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the windowsApplication field is set.  
  
### hasWuaPackage()
    
    
    public abstract boolean hasWuaPackage()

Details of a Windows Update package. See <https://docs.microsoft.com/en-us/windows/win32/api/_wua/> for information about Windows Update.

`.google.cloud.osconfig.v1alpha.Inventory.WindowsUpdatePackage wua_package = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the wuaPackage field is set.  
  
### hasYumPackage()
    
    
    public abstract boolean hasYumPackage()

Yum package info. For details about the yum package manager, see <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/ch-yum>.

`.google.cloud.osconfig.v1alpha.Inventory.VersionedPackage yum_package = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the yumPackage field is set.  
  
### hasZypperPackage()
    
    
    public abstract boolean hasZypperPackage()

Details of a Zypper package. For details about the Zypper package manager, see <https://en.opensuse.org/SDB:Zypper_manual>.

`.google.cloud.osconfig.v1alpha.Inventory.VersionedPackage zypper_package = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the zypperPackage field is set.  
  
### hasZypperPatch()
    
    
    public abstract boolean hasZypperPatch()

Details of a Zypper patch. For details about the Zypper package manager, see <https://en.opensuse.org/SDB:Zypper_manual>.

`.google.cloud.osconfig.v1alpha.Inventory.ZypperPatch zypper_patch = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the zypperPatch field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
