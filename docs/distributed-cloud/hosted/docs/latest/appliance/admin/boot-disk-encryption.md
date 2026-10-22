---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/boot-disk-encryption/
title: Boot disk encryption \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:45.251998+00:00
---

# Boot disk encryption  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/boot-disk-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Boot disk encryption Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped appliance uses Linux Unified Key Setup (LUKS) based disk encryption with YubiKeys.

For each GDC air-gapped appliance, three or more YubiKeys are shipped separately to the customer. The YubiKeys are FIPS 140-2 certified. For more information on the YubiKey model, see <https://www.yubico.com/product/yubikey-5-nano-fips/>.

The USB ports on each server blade of the device are enabled with USB dongles. The YubiKeys are inserted into the server machines as part of the device setup. Each YubiKey is bound to a blade during the bootstrap process and cannot be used with another blade. The keys cannot be used interchangeably.

**Warning:** Store all YubiKeys in a secure location and remove them whenever the appliance is not in operation. Because YubiKeys can decrypt local drives at any stage of the GDC air-gapped appliance lifecycle, leaving them unattended in an inactive device creates a security vulnerability.

The YubiKey only needs to be inserted during the boot process. If you remove the YubiKey after the boot process, it doesn't affect the operation of the appliance. If you remove the YubiKey, it must be reinserted in the same node before the next boot. Ensure that the YubiKeys are transferred separately from the appliance to protect against server theft.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
