---
url: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/security-bulletins/
title: Security bulletins \u00a0|\u00a0 Confidential VM \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:53.495504+00:00
---

# Security bulletins  |  Confidential VM  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/security-bulletins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Confidential VM ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs)
  * [ Resources ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/get-support)



Send feedback 

#  Security bulletins Stay organized with collections  Save and categorize content based on your preferences. 

The following describes all security bulletins related to Confidential VM.

## GCP-2026-053

**Published:** 2026-08-11

### Description

Description | Severity | Notes  
---|---|---  
Google is aware of several security vulnerabilities affecting Intel® Trust Domain Extensions (TDX) firmware that can compromise confidential guest integrity. These vulnerabilities could allow a privileged host adversary to bypass attestation checks, access restricted registers, or decrypt normally protected guest memory. **What Google products are affected?** All Confidential VM instances relying on Intel TDX technology. **What should I do?** Google has proactively applied these firmware upgrades to our server fleet to mitigate these vulnerabilities. No action is required for customers that did not receive a separate direct advisory to upgrade.  For more information, see Intel's PSIRT technical advisories: [INTEL-TA-01404](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-01404.html), [INTEL-TA-01428](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-01428.html), [INTEL-TA-01419](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-01419.html), [INTEL-TA-01439](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-01439.html), [INTEL-TA-01442](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-01442.html), [INTEL-TA-01436](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-01436.html).  | High | 

  * [CVE-2025-31938](https://nvd.nist.gov/vuln/detail/CVE-2025-31938)
  * [CVE-2025-35973](https://nvd.nist.gov/vuln/detail/CVE-2025-35973)
  * [CVE-2025-31356](https://nvd.nist.gov/vuln/detail/CVE-2025-31356)
  * [CVE-2026-20898](https://nvd.nist.gov/vuln/detail/CVE-2026-20898)
  * [CVE-2026-20713](https://nvd.nist.gov/vuln/detail/CVE-2026-20713)
  * [CVE-2026-20901](https://nvd.nist.gov/vuln/detail/CVE-2026-20901)
  * [CVE-2026-20885](https://nvd.nist.gov/vuln/detail/CVE-2026-20885)
  * [CVE-2026-20705](https://nvd.nist.gov/vuln/detail/CVE-2026-20705)
  * [CVE-2026-20775](https://nvd.nist.gov/vuln/detail/CVE-2026-20775)

  
  
## GCP-2026-021

**Published:** 2026-04-14

### Description

Description | Severity | Notes  
---|---|---  
AMD reported a vulnerability in its firmware that could have allowed a malicious hypervisor to direct the IOMMU to write into the guest memory of AMD SEV-SNP enabled instances, compromising guest data integrity. Google rolled out a mitigation to vulnerable Confidential VM instances with AMD SEV-SNP enabled. 

#### What should I do?

No customer action is needed. The mitigation has already been applied to Confidential VM instances with AMD SEV-SNP enabled.  For more information, see AMD advisory [ AMD-SB-3016](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-3016.html).  | Medium |  [CVE-2023-20585](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20585)  
  
## GCP-2026-019

**Published:** 2026-04-14

### Description

Description | Severity | Notes  
---|---|---  
Researchers discovered a vulnerability in AMD firmware that could allow a malicious hypervisor to alter BIOS settings and Memory Mapped I/O (MMIO) routing configurations, compromising the confidentiality and integrity of Confidential VMs with AMD SEV-SNP guests. Google implemented the mitigation that prevents this issue.

#### What should I do?

No customer action is needed. Mitigations have already been applied to Confidential VM instances with AMD SEV-SNP.

#### What vulnerabilities are being addressed?

For more information, see AMD advisory [AMD-SB-3034](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-3034.html). | Medium |  [CVE-2025-54510](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-54510)  
  
## GCP-2026-008

**Published:** 2026-02-10

### Description

Description | Severity | Notes  
---|---|---  
A set of security vulnerabilities affect Intel® TDX firmware. These vulnerabilities encompass various flaws, including race conditions (CVE-2025-30513, CVE-2025-31944), out-of-bounds reads (CVE-2025-32007, CVE-2025-27940), use of an uninitialized variable (CVE-2025-32467), and exposure of sensitive information during transient execution (CVE-2025-27572). Collectively, these issues may allow information disclosure, escalation of privilege, or denial of service. Exploitation generally requires privileged user access on the system. 

#### What should I do?

No customer action is required. All relevant fixes have been applied to the Google server fleet. For more information, see Intel's PSIRT technical advisory [INTEL-TA-01397](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-01397.html).  | High | 

  * [CVE-2025-30513](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30513)
  * [CVE-2025-31944](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-31944)
  * [CVE-2025-32007](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-32007)
  * [CVE-2025-32467](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-32467)
  * [CVE-2025-27572](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-27572)
  * [CVE-2025-27940](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-27940)

  
  
## GCP-2025-058

**Published:** 2025-10-20

### Description

Description | Severity | Notes  
---|---|---  
[ A flaw has been discovered in the RDSEED instruction](https://lore.kernel.org/lkml/20251016182107.3496116-1-gourry@gourry.net/) in AMD Zen 5 processors (Turin). This instruction is used to generate cryptographic random numbers. Under certain system load conditions, the 16- and 32-bit versions of RDSEED can silently fail, which could compromise applications relying on random number generation. Customers using the 64-bit version of RDSEED are unaffected. 

#### What should I do?

AMD is investigating the vulnerability. It's important to note that the 64-bit Linux kernel uses the safe 64-bit version of the RDSEED instruction, and that feeds the random numbers obtained from `/dev/[u]random`. Those random numbers are not impacted by this vulnerability.  If you have application code that synthesizes random numbers itself using the RDSEED instruction, be aware that the 16-bit and 32-bit versions of the instruction are insecure. The 64-bit version of the instruction is safe. 

#### What vulnerabilites are being addressed?

This vulnerability allows an attacker to cause RDSEED to silently fail, potentially compromising random number generation in applications.  | High |  [CVE-2025-62626](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-62626)  
  
## GCP-2025-007

**Published** : 2025-02-03

Description | Severity | Notes  
---|---|---  
Google has discovered a vulnerability in AMD Zen-based CPUs that affects Confidential VM instances with AMD SEV-SNP enabled. This vulnerability allows attackers with root access in a physical machine to compromise the confidentiality and integrity of the Confidential VM instance.  Google has applied fixes to the affected assets, including Google Cloud, to ensure customers are protected. At this time, no evidence of exploitation has been found or reported to Google.  **What should I do?** No customer action is required. Customers who want to verify the fix can check the Trusted Computing Base (TCB) version in the attestation report from their Confidential VM instance with AMD SEV-SNP. The minimum versions that mitigate this vulnerability are as follows: 
    
    
    SNP TCB SVN: 0x18 0d24
    tcb_version {
      psp_bootloader_version: 4
      snp_firmware_version: 24 (0x18)
      microcode_version: 219
    }

For more information, see AMD security bulletin [ AMD-SB-3019](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-3019.html). | High |  [ CVE-2024-56161](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-56161)  
  
## GCP-2024-046

**Published** : 2024-08-05

Description | Severity | Notes  
---|---|---  
AMD has notified Google about 3 new (2 medium risk, 1 high risk) firmware vulnerabilities affecting SEV-SNP in AMD EPYC 3rd generation (Milan) and 4th generation (Genoa) CPUs.  Google has applied fixes to the affected assets, including Google Cloud, to ensure customers are protected. At this time, no evidence of exploitation has been found or reported to Google.  **What should I do?** No customer action is required. Fixes have already been applied to the Google server fleet.  For more information, see AMD security advisory [ AMD-SN-3011](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-3011.html).  | Medium–High |  [ CVE-2023-31355](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31355) [ CVE-2024-21978](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21978) [ CVE-2024-21980](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21980)  
  
## GCP-2024-009

**Published** : 2024-02-13

Description | Severity | Notes  
---|---|---  
On February 13, 2024, AMD disclosed two vulnerabilities affecting SEV-SNP on EPYC CPUs based on third generation "Milan" and fourth generation "Genoa" Zen cores. The vulnerabilities allow privileged attackers to access stale data from guests or cause a loss of guest integrity.  Google has applied fixes to affected assets, including Google Cloud, to ensure customers are protected. At this time, no evidence of exploitation has been found or reported to Google.  **What should I do?** No customer action is required. Fixes have already been applied to the Google server fleet for Google Cloud, including Compute Engine.  For more information, see AMD security advisory [ AMD-SN-3007](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-3007.html).  | Medium |  [ CVE-2023-31346](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31346) [ CVE-2023-31347](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-31347)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
