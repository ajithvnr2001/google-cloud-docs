---
url: https://docs.cloud.google.com/vmware-engine/docs/security-bulletins/
title: Security bulletins \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:06.948328+00:00
---

# Security bulletins  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/security-bulletins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Support ](https://docs.cloud.google.com/vmware-engine/docs/support)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Security bulletins

From time to time, we might release security bulletins related to Google Cloud VMware Engine. All security bulletins for VMware Engine are described here.

[ Use this XML feed to subscribe to security bulletins for this page. ![Subscribe](https://docs.cloud.google.com/static/docs/images/feed-icon.png)](https://cloud.google.com/feeds/google-cloud-vmware-engine-security-bulletins.xml)

## GCP-2026-050

**Published:** 2026-07-29

### Description

Description | Severity | Notes  
---|---|---  
Per advisory VMSA-2026-0006, multiple vulnerabilities in VMware ESXi, and vCenter were privately reported to Broadcom. We are in the process of applying the necessary patches supplied by Broadcom. There are no known workarounds for these reported vulnerabilities. Once patched, your VMware Engine deployments should be running vCenter and ESXi 8.0 U3k.

#### What should I do?

Google recommends customers to monitor their workloads on VMware Engine for any unusual activities. | Critical | 

  * [VMSA-2026-0006](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017)
  * CVE-2026-59309
  * CVE-2026-59310
  * CVE-2026-47876
  * CVE-2026-41703
  * CVE-2026-41709

  
  
## GCP-2026-029

**Published:** 2026-05-07

### Description

Description | Severity | Notes  
---|---|---  
Microsoft is updating the Secure Boot certificates originally issued in 2011 to ensure Windows devices continue to verify trusted boot software. These older certificates begin expiring in June 2026. Devices that haven't received the newer 2023 certificates will continue to start and operate normally, and standard Windows updates will continue to install. However, these devices will no longer be able to receive new security protections for the early boot process, including updates to Windows Boot Manager, Secure Boot databases, revocation lists, or mitigations for newly discovered boot-level vulnerabilities. Also, Secure Boot certificate expirations starting in June 2026 affect Linux systems that use Secure Boot.

#### What should I do?

Google recommends that customers update their Windows VMs by taking appropriate actions as recommended by Microsoft. Distributions like Ubuntu, Red Hat, and Fedora are already working to provide updated packages signed with the new 2023 key. Refer also to the [Broadcom documentation](https://knowledge.broadcom.com/external/article/423893/secure-boot-certificate-expirations-and.html) to resolve errors and warnings in VMware virtual machines as Secure Boot certificates approach expiration. After June 2026, systems lacking the 2023 certificate updates may experience failures during new operating system installations or while updating the existing bootloader firmware. | Informational |  [Broadcom KB 423893](https://knowledge.broadcom.com/external/article/423893/secure-boot-certificate-expirations-and.html)  
  
## GCP-2026-028

**Published:** 2026-05-05

**Updated:** 2026-05-27

### Description

Description | Severity | Notes  
---|---|---  
[CVE-2026-31431](https://knowledge.broadcom.com/external/article?articleNumber=439189), also known as "Copy Fail," is a high-severity local privilege escalation (LPE) vulnerability in the Linux kernel that allows an unprivileged user to gain root access. Disclosed in late April 2026, it stems from a logic flaw in the kernel's cryptographic subsystem (algif_aead) introduced in 2017.

#### What should I do?

Google recommends that customers protect their Linux Guest VMs by updating the kernel on all Linux VMs. Major distributions have released or are rolling out fixes. | High |  [CVE-2026-31431](https://knowledge.broadcom.com/external/article?articleNumber=439189)  
  
## GCP-2025-054

**Published:** 2025-10-14

### Description

Description | Severity | Notes  
---|---|---  
Per VMware security advisory [VMSA-2025-0015](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/36149), multiple vulnerabilities in VMware Aria Operations and VMware Tools were privately reported to Broadcom. Patches are available to remediate these vulnerabilities in affected Broadcom products. **What should I do?** We recommend upgrading to VMware Aria Automation 8.18.5 and VMware Tools 13.0.5. | Important | 

  * [VMSA-2025-0015](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/36149)
  * [CVE-2025-41244](https://nvd.nist.gov/vuln/detail/CVE-2025-41244)
  * [CVE-2025-41245](https://nvd.nist.gov/vuln/detail/CVE-2025-41245)
  * [CVE-2025-41246](https://nvd.nist.gov/vuln/detail/CVE-2025-41246)

  
  
## GCP-2025-040

**Published:** 2025-07-15

### Description

Description | Severity | Notes  
---|---|---  
Per advisory VMSA-2025-0013, multiple vulnerabilities in VMware ESXi were privately reported to Broadcom. We've either already patched these vulnerabilities or are in the process of applying the necessary patches supplied by Broadcom. There are no known workarounds for these reported vulnerabilities. Once patched, your VMware Engine deployments should be running ESXi 7.0U3w or ESXi 8.0U3f or greater.

#### What should I do?

Google recommends customers to monitor their workloads on VMware Engine for any unusual activities. | Medium to Critical | 

  * [VMSA-2025-0013](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/35877)
  * [CVE-2025-41236](https://nvd.nist.gov/vuln/detail/CVE-2025-41236)
  * [CVE-2025-41237](https://nvd.nist.gov/vuln/detail/CVE-2025-41237)
  * [CVE-2025-41238](https://nvd.nist.gov/vuln/detail/CVE-2025-41238)
  * [CVE-2025-41239](https://nvd.nist.gov/vuln/detail/CVE-2025-41239)

  
  
## GCP-2025-030

**Published:** 2025-05-23

Description | Severity | Notes  
---|---|---  
Per VMware security advisory [VMSA-2024-0017](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/24598), an SQL-injection vulnerability in VMware Aria Automation was privately reported to VMware. Patches are available to remediate this vulnerability in affected VMware products.

#### What should I do?

We recommend upgrading to VMware Aria Automation KB325790.  | Important | 

  * [VMSA-2024-0017](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/24598)
  * [CVE-2024-22280](https://nvd.nist.gov/vuln/detail/CVE-2024-22280)

  
  
## GCP-2025-029

**Published:** 2025-05-23

Description | Severity | Notes  
---|---|---  
Per VMware security advisory [VMSA-2025-0006](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/25541), a local privilege escalation vulnerability in VMware Aria Operations was responsibly reported to VMware. Patches are available to remediate this vulnerability in affected VMware products.

#### What should I do?

We recommend upgrading to VMware Aria Operations 8.18 HF5.  | Important | 

  * [VMSA-2025-0006](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/25541)
  * [CVE-2025-22231](https://nvd.nist.gov/vuln/detail/CVE-2025-22231)

  
  
## GCP-2025-028

**Published:** 2025-05-23

Description | Severity | Notes  
---|---|---  
Per VMware security advisory [VMSA-2025-0003](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/25329), multiple vulnerabilities in VMware Aria Operations for logs and VMware Aria Operations were privately reported to VMware. Patches are available to remediate this vulnerability in affected VMware products.

#### What should I do?

We recommend upgrading to VMware Aria Operations for Logs 8.18.3 and VMware Aria Operations to 8.18.3.  | Important | 

  * [VMSA-2025-0003](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/25329)
  * [CVE-2025-22218](https://nvd.nist.gov/vuln/detail/CVE-2025-22218)
  * [CVE-2025-22219](https://nvd.nist.gov/vuln/detail/CVE-2025-22219)
  * [CVE-2025-22220](https://nvd.nist.gov/vuln/detail/CVE-2025-22220)
  * [CVE-2025-22221](https://nvd.nist.gov/vuln/detail/CVE-2025-22221)
  * [CVE-2025-22222](https://nvd.nist.gov/vuln/detail/CVE-2025-22222)

  
  
## GCP-2025-026

**Published:** 2025-05-15

Description | Severity | Notes  
---|---|---  
Per VMware security advisory [VMSA-2025-0008](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/25711), a DOM based Cross-Site Scripting (XSS) vulnerability in VMware Aria Automation was privately reported to VMware. Patches are available to remediate this vulnerability in affected VMware products.

#### What should I do?

We recommend upgrading to VMware Aria Automation 8.18.1 patch 2.  | Important | 

  * [VMSA-2025-0008](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/25711)
  * [CVE-2025-22249](https://nvd.nist.gov/vuln/detail/CVE-2025-22249)

  
  
## GCP-2025-011

**Published:** 2025-03-06

Description | Severity | Notes  
---|---|---  
VMware disclosed multiple vulnerabilities in [VMSA-2025-0004](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/25390?utm_campaign=VCF_FY25_VCF_Security-Alert-VMSA-2025-0004_MKT_EM_2938&utm_content=VCF_FY25_VCF_Security-Alert_2938_VMSA-2025-0004_MKT_TRANS_EM_5308&utm_medium=email&utm_source=eloqua) that impact ESXi components deployed in customer environments.

#### VMware Engine impact

Your private clouds are either already patched or are in the process of being updated to address the security vulnerability. As part of the VMware Engine service, all customers get dedicated bare metal hosts with local attached disks that are physically isolated from other hardware. This means that the vulnerability is scoped to guest VMs within your specific private cloud only. Your private clouds will be updated to 7.0u3s Build number 24534642. This is equivalent to 7.0U3s: Build number 24585291.

#### What should I do?

Follow instructions from Broadcom and your security vendors regarding this vulnerability.  | Critical | 

  * [VMSA-2025-0004](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/25390?utm_campaign=VCF_FY25_VCF_Security-Alert-VMSA-2025-0004_MKT_EM_2938&utm_content=VCF_FY25_VCF_Security-Alert_2938_VMSA-2025-0004_MKT_TRANS_EM_5308&utm_medium=email&utm_source=eloqua)
  * [CVE-2025-22224](https://nvd.nist.gov/vuln/detail/CVE-2025-22224)
  * [CVE-2025-22225](https://nvd.nist.gov/vuln/detail/CVE-2025-22225)
  * [CVE-2025-22226](https://nvd.nist.gov/vuln/detail/CVE-2025-22226)

  
  
## GCP-2025-004

**Published:** 2025-01-16

Description | Severity | Notes  
---|---|---  
Per VMware security advisory VMSA-2025-0001, a server-side request forgery (SSRF) vulnerability in VMware Aria Automation was responsibly reported to VMware. Patches are available to remediate this vulnerability in affected VMware products.

#### What should I do?

We recommend upgrading to VMware Aria Automation 8.18.2 HF.  | Medium | 

  * [VMSA-2025-0001](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/25312)
  * [CVE-2025-22215](https://nvd.nist.gov/vuln/detail/CVE-2025-22215)

  
  
## GCP-2024-064

**Published:** 2024-12-10

Description | Severity | Notes  
---|---|---  
Per VMware security advisory VMSA-2024-0022, multiple vulnerabilities in VMware Aria Operations were responsibly reported to VMware. Updates are available to remediate these vulnerabilities in the affected VMware product.

#### What should I do?

We recommend upgrading to VMware Aria Operations 8.18.2.  | Important | 

  * [VMSA-2024-0022](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/25199)
  * [CVE-2024-38830](https://nvd.nist.gov/vuln/detail/CVE-2024-38830)
  * [CVE-2024-38831](https://nvd.nist.gov/vuln/detail/CVE-2024-38831)
  * [CVE-2024-38832](https://nvd.nist.gov/vuln/detail/CVE-2024-38832)
  * [CVE-2024-38833](https://nvd.nist.gov/vuln/detail/CVE-2024-38833)
  * [CVE-2024-38834](https://nvd.nist.gov/vuln/detail/CVE-2024-38834)

  
  
## GCP-2024-060

**Published:** 2024-10-17

Description | Severity | Notes  
---|---|---  
Per VMware security advisory VMSA-2024-0020, multiple vulnerabilities in VMware NSX were responsibly reported to VMware. The version NSX-T running on your VMware Engine environment is not impacted by CVE-2024-38815, CVE-2024-38818, or CVE-2024-38817.

#### What should I do?

Because VMware Engine clusters are not affected by this vulnerability, no further action is required. | Medium | 

  * [VMSA-2024-0020](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/25047)
  * [CVE-2024-38815](https://nvd.nist.gov/vuln/detail/CVE-2024-38215)
  * [CVE-2024-38817](https://nvd.nist.gov/vuln/detail/CVE-2024-38217)
  * [CVE-2024-38818](https://nvd.nist.gov/vuln/detail/CVE-2024-38218)

  
  
## GCP-2024-059

**Published:** 2024-10-16

Description | Severity | Notes  
---|---|---  
Per VMware security advisory VMSA-2024-0021, an authenticated SQL injection vulnerability in VMware HCX was privately reported to VMware. We have applied the mitigation approved by VMware to address this vulnerability. This fix addresses a security vulnerability described in CVE-2024-38814. The image versions running in your VMware Engine private cloud don't reflect any change at this time to indicate the changes applied. Appropriate mitigations have been installed and your environment is secured from this vulnerability.

#### What should I do?

We recommend upgrading to VMware HCX version 4.9.2. | High | 

  * [VMSA-2024-0021](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/25019)
  * [CVE-2024-38814](https://nvd.nist.gov/vuln/detail/CVE-2024-38214)

  
  
## GCP-2024-051

**Published:** 2024-09-18

Description | Severity | Notes  
---|---|---  
VMware disclosed multiple vulnerabilities in [VMSA-2024-0019](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/24968) that impact vCenter components deployed in customer environments. 

#### VMware Engine impact

  * Google has already disabled any potential exploit of this vulnerability. For example, Google has blocked the ports through which this vulnerability could be exploited. 
  * In addition, Google ensures all future deployments of vCenter are not exposed to this vulnerability. 



#### What should I do?

No further action is required at this time.  | Critical | 

  * [CVE-2024-38812](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38812)
  * [CVE-2024-38813](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-38813)

  
  
## GCP-2024-040

**Published:** 2024-07-01

Description | Severity | Notes  
---|---|---  
A vulnerability CVE-2024-6387 was discovered in OpenSSH server (sshd). This vulnerability is exploitable remotely on glibc-based linux systems: an unauthenticated remote code execution as root, because it affects sshd's privileged code, which is not sandboxed and runs with full privileges.   
  
At the time of publication, exploitation is believed to be difficult–requiring winning a race condition, which is hard to successfully exploit and may take several hours per machine being attacked. We are not aware of any exploitation attempts. 

#### What should I do?

  1. Apply updates from Linux distributions to your workloads as they become available. Please refer to guidance from Linux distributions. 
  2. If updating is not possible, consider turning OpenSSH off until it can be patched. 
  3. If OpenSSH needs to be left on, you can also execute a configuration update which eliminates the race case condition for the exploit. This is a runtime mitigation. To apply the changes in the sshd config, this script will restart the sshd service. 
         
         #!/bin/bash
         set -e
         
         SSHD_CONFIG_FILE=/etc/ssh/sshd_config
         # -c: count the matches
         # -q: don't print to console
         # -i: sshd_config keywords are case insensitive.
         if [[ "$(grep -ci '^LoginGraceTime' $SSHD_CONFIG_FILE)" -eq 0 ]]; then
             echo "LoginGraceTime 0" >> "$SSHD_CONFIG_FILE"
             echo "Set the LoginGraceTime to 0 in $SSHD_CONFIG_FILE"
         else
             sed -i 's/^LoginGraceTime.*$/LoginGraceTime 0/' /etc/ssh/sshd_config
             echo "Changed the LoginGraceTime to 0 in $SSHD_CONFIG_FILE"
         fi
         # Restart the sshd service to apply the new config.
         systemctl restart sshd
                   

  4. Finally, monitor for any unusual network activity involving SSH servers. 

| Critical | 

  * [CVE-2024-6387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6387)
  * [Broadcom VMware Cloud Foundation Response](https://knowledge.broadcom.com/external/article?articleNumber=371126)

  
  
## GCP-2024-037

**Published:** 2024-06-18

Description | Severity | Notes  
---|---|---  
VMware disclosed multiple vulnerabilities in [VMSA-2024-0012](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/24453) that impact vCenter components deployed in customer environments. 

#### VMware Engine impact

  * The vulnerability can be exploited by accessing specific ports in vCenter Server. Google has already blocked the vulnerable ports on vCenter server, which prevents any potential exploits of this vulnerability. 
  * In addition, Google ensures all future deployments of vCenter are not exposed to this vulnerability. 



#### What should I do?

No further action is required at this time.  | Critical | 

  * [CVE-2024-37079](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37079)
  * [CVE-2024-37080](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37080)
  * [CVE-2024-37081](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37081)

  
  
## GCP-2024-016

**Published:** 2024-03-05

Description | Severity | Notes  
---|---|---  
VMware disclosed multiple vulnerabilities in [VMSA-2024-0006](https://www.vmware.com/security/advisories/VMSA-2024-0006.html) that impact ESXi components deployed in customer environments. 

#### VMware Engine impact

Your private clouds have been updated to address the security vulnerability. 

#### What should I do?

No action is needed on your part.  | Critical | 

  * [VMSA-2024-0006](https://www.vmware.com/security/advisories/VMSA-2024-0006.html)
  * [CVE-2024-22252](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-22252)
  * [CVE-2024-22253](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-22253)
  * [CVE-2024-22254](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-22254)
  * [CVE-2024-22255](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-22255)

  
  
## GCP-2023-034

**Published:** 2023-10-25

**Updated:** 2023-10-27

Description | Severity | Notes  
---|---|---  
VMware disclosed multiple vulnerabilities in [VMSA-2023-0023](https://www.vmware.com/security/advisories/VMSA-2023-0023.html) that impact vCenter components deployed in customer environments.

#### VMware Engine impact

  * The vulnerability can be exploited by accessing specific ports in vCenter Server. These ports are not exposed to the public internet.
  * If your vCenter ports 2012/tcp, 2014/tcp, and 2020/tcp are not accessible by untrusted systems, then you are not exposed to this vulnerability.
  * Google has already blocked the vulnerable ports on vCenter server, preventing any potential exploit of this vulnerability.
  * In addition, Google will ensure all future deployments of vCenter server are not exposed to this vulnerability.
  * At the time of the bulletin, VMware is not aware of any exploitation "in the wild". For more details please refer to the [VMware documentation](https://core.vmware.com/resource/vmsa-2023-0023-questions-answers#are-the-vulnerabilities-disclosed-being-exploited-in-the-wild) for more information.



#### What should I do?

No further action is required at this time. | Critical | 

  * [CVE-2023-34048, CVE-2023-34056](https://www.vmware.com/security/advisories/VMSA-2023-0023.html)

  
  
## GCP-2023-027

**Published:** 2023-09-11 Description | Severity | Notes  
---|---|---  
VMware vCenter Server updates address multiple memory corruption vulnerabilities (CVE-2023-20892, CVE-2023-20893, CVE-2023-20894, CVE-2023-20895, CVE-2023-20896)

#### VMware Engine impact

VMware vCenter Server (vCenter Server) and VMware Cloud Foundation (Cloud Foundation).

#### What should I do?

Customers are not impacted and no action needs to be taken. | Medium | 

  * [CVE-2023-20893](https://www.vmware.com/security/advisories/VMSA-2023-0014.html)

  
  
## GCP-2023-025

**Published:** 2023-08-08 Description | Severity | Notes  
---|---|---  
Intel recently announced [Intel Security Advisory INTEL-SA-00828](https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00828.html) impacting some of their processor families. You are encouraged to assess your risks based on the advisory.

#### VMware Engine impact

Our fleet utilizes the impacted processor families. In our deployment, the entire server is dedicated to one customer. Hence, our deployment model doesn't add any additional risk to your assessment of this vulnerability. We are working with our partners to obtain necessary patches and will be deploying these patches on priority across the fleet using the standard upgrade process in the next several weeks.

#### What should I do?

No action is needed on your part, we are working on upgrading all the impacted systems. | High | 

  * [CVE-2022-40982](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-40982)

  
  
## GCP-2021-023

**Published:** 2021-09-21 Description | Severity | Notes  
---|---|---  
Per VMware security advisory VMSA-2021-0020, VMware received reports of multiple vulnerabilities in vCenter. VMware has made updates available to remediate these vulnerabilities in affected VMware products. We have already applied the patches provided by VMware for the vSphere stack to Google Cloud VMware Engine per the VMware security advisory. This update addresses the security vulnerabilities described in CVE-2021-22005, CVE-2021-22006, CVE-2021-22007, CVE-2021-22008, and CVE-2021-22010. Other non-critical security issues will be addressed in the upcoming VMware stack upgrade (per the advance notice sent in July, more details will be provided soon on the specific timeline of the upgrade).

#### VMware Engine impact

Based on our investigations, no customers were found to be impacted.

#### What should I do?

Because VMware Engine clusters are not affected by this vulnerability, no further action is required. | Critical | 

  * [VMSA-2021-0020](https://www.vmware.com/security/advisories/VMSA-2021-0020.html)
  * [CVE-2021-22005](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22005)
  * [CVE-2021-22006](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22006)
  * [CVE-2021-22007](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22007)
  * [CVE-2021-22008](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22008)
  * [CVE-2021-22010](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-22010)

  
  
## GCP-2021-010

**Published:** 2021-05-25 Description | Severity | Notes  
---|---|---  
Per VMware security advisory VMSA-2021-0010, remote code execution and authentication bypass vulnerabilities in vSphere Client (HTML5) were privately reported to VMware. VMware has made updates available to remediate these vulnerabilities in affected VMware products. We have applied the patches provided by VMware for the vSphere stack per the VMware security advisory. This update addresses security vulnerabilities described in CVE-2021-21985 and CVE-2021-21986. The image versions running in your VMware Engine private cloud don't reflect any change at this time to indicate the patches applied. Please rest assured that appropriate patches have been installed and your environment is secured from these vulnerabilities.

#### VMware Engine impact

Based on our investigations, no customers were found to be impacted.

#### What should I do?

Because VMware Engine clusters are not affected by this vulnerability, no further action is required. | Critical | 

  * [VMSA-2021-0010](https://www.vmware.com/security/advisories/VMSA-2021-0010.html)
  * [CVE-2021-21985](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-21985)
  * [CVE-2021-21986](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-21986)

  
  
## GCP-2021-002

**Published:** 2021-03-05 Description | Severity | Notes  
---|---|---  
Per VMware security advisory VMSA-2021-0002, VMware received reports of multiple vulnerabilities in VMware ESXi and vSphere Client (HTML5). VMware has made updates available to remediate these vulnerabilities in affected VMware products. We have applied the officially documented workarounds for the vSphere stack per the VMware security advisory. This update addresses security vulnerabilities described in CVE-2021-21972, CVE-2021-21973, and CVE-2021-21974.

#### VMware Engine impact

Based on our investigations, no customers were found to be impacted.

#### What should I do?

We recommend upgrading to the latest version of HCX. | Critical | 

  * [VMSA-2021-0002](https://www.vmware.com/security/advisories/VMSA-2021-0002.html)
  * [CVE-2021-21972](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-21972)
  * [CVE-2021-21973](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-21973)
  * [CVE-2021-21974](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-21974)

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
