---
url: https://docs.cloud.google.com/billing/docs/resources/indonesia-wht/
title: PT Google Cloud Indonesia Withholding Tax (WHT) \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:58:55.532593+00:00
---

# PT Google Cloud Indonesia Withholding Tax (WHT)  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/resources/indonesia-wht/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Resources ](https://docs.cloud.google.com/billing/docs/resources)



Send feedback 

#  PT Google Cloud Indonesia Withholding Tax (WHT) Stay organized with collections  Save and categorize content based on your preferences. 

This document applies to Google Cloud Indonesia customers.

To comply with Indonesia legislation, starting January 1, 2025, Google charges 11% value-added tax (VAT) on digital services in Indonesia.

## Confirm your name and billing address

As part of local government requirements, before Google can issue you a valid Faktur Pajak, you must verify that the name and billing address in your Google payments profile exactly matches the information registered with the Indonesian tax authorities. Depending on your account type, this information applies to your NIK (population identification number or resident identity number), NPWP (tax identification number), or NITKU (business location ID number).

To confirm or edit your information, follow the steps in Update your tax information.

## Indonesia withholding tax

To have a 2% tax withheld from your payment and avoid an outstanding balance in your account, you must send us a withholding tax slip (Bukti Potong). You must send the withholding tax slip within the payment deadline indicated on your commercial invoice. Refer to the following section for mailing information.

## Send a withholding tax slip to Google

How you send your withholding tax slip depends on if it has a QR code.

### Your withholding slip has a QR code

Email your withholding tax slip to the correct email address for your payment method. For the subject line, enter "PTGCI Withholding Tax Slip".

Payment method | Email address  
---|---  
Credit or debit card or ATM transfer | eps-wht@google.com  
Invoice | collections@google.com  
  
### Your withholding slip doesn't have a QR code

Send the original hard copy of your withholding tax slip using POS Indonesia to the correct address for your payment method.

Payment method | Address  
---|---  
Credit or debit card or ATM transfer | PO BOX 176 Cibinong 16900  
Jl. Tegar Beriman No.7  
Pakansari, Cibinong, Bogor  
Jawa Barat 16914-Indonesia   
Invoice | PO BOX 188 Cibinong 16900  
Jl. Tegar Beriman No.7  
Pakansari, Cibinong, Bogor  
Jawa Barat 16914-Indonesia   
  
## VAT overview

When you set up billing for your service, your account type is automatically set to Business. With a Business account, you're responsible for self-assessing your organization's account and paying VAT.

You can't set up _new_ Cloud Billing accounts and Google payments accounts with the _Individual_ account type. However, if you already have this Google payments account type, you can keep using it. For Individual accounts, Google automatically adds VAT to invoices for services.

Service prices shown on the Google website _don't_ include VAT.

## Provide your tax ID

How you provide your tax ID or VAT ID to Google depends on how you pay:

  * If your payment is automatically deducted: Go to your payments profile settings and follow the steps in [Update your tax information](https://docs.cloud.google.com/billing/docs/resources/:#update-tax-info).
  * If you pay by monthly invoice: Contact [Cloud Billing Support](https://cloud.google.com/support/billing) to submit your tax ID.



## Update your tax information

To update your tax information, complete the steps for your account type.

### Individual accounts

If you have an Individual account and previously provided a NPWP, the NPWP is no longer valid for invoices issued after January 1, 2025. To avoid invoicing or service interruptions, update your payment settings with your NIK at your earliest convenience.

To access the Payment settings page in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Payment settings** page.

[Go to your Cloud Billing account](https://console.cloud.google.com/billing/profile)

  2. At the prompt, choose the Cloud Billing account connected to the payments profile that you want to update. The **Payment settings** page opens for the selected Cloud Billing account.

  3. In the **Address** section, click **Edit** edit.

  4. Update your address to match the address registered with the Indonesia tax authorities for your NIK.

  5. In the **Indonesia tax info** section, click **Edit** edit.

  6. For **Residential Identity Number (NIK)** , enter your NIK.

  7. Click **Save**.




### Organization accounts

As of January 1, 2025, the NPWP is 16 digits. If you've entered a 15-digit NPWP in your Google payments profile settings, you need to update it to the 16-digit format by adding the number "0" in front of the existing 15-digit NPWP.

To access the Payment settings page in the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Payment settings** page.

[Go to your Cloud Billing account](https://console.cloud.google.com/billing/profile)

  2. At the prompt, choose the Cloud Billing account connected to the payments profile that you want to update. The **Payment settings** page opens for the selected Cloud Billing account.

  3. In the **Organization Name and Address** section, click **Edit** edit and update your organization name and address to match the information registered with the Indonesian tax authorities.

  4. In the **Indonesia tax info** section, click **Edit** edit.

  5. Select if you're a **Branch Office** or **Home Office**.

  6. (Branch offices only) For **Nomor Identitas Tempat Kegiatan Usaha (NITKU)** , enter your 22-digit NITKU.

  7. For **Nomor Pokok Wajib Pajak (NPWP)** , enter your 16-digit NPWP.

  8. Click **Save**.




## Where to view your tax charges

The amount of tax charged on your purchase will show as separate line items on your Cloud Billing account **Transaction** page. Learn how to [View and understand your transactions](https://docs.cloud.google.com/billing/docs/how-to/view-history).

Your invoice or statement will show the amount of tax charged. You can view your tax charges on the [Cost table report](https://docs.cloud.google.com/billing/docs/how-to/cost-table) or when viewing a [Billing Report by invoice month](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-invoice-charges).

**Note:** Google can't advise you on tax matters. Contact your tax adviser for any questions about this tax.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
