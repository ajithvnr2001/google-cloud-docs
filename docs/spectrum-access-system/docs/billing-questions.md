---
url: https://docs.cloud.google.com/spectrum-access-system/docs/billing-questions/
title: Spectrum Access System billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:59.378055+00:00
---

# Spectrum Access System billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/billing-questions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Spectrum Access System billing Stay organized with collections  Save and categorize content based on your preferences. 

Spectrum Access System (SAS) billing is set by SAS deployment, which is a collection of Citizens Broadband Radio Service Devices (CBSDs) with the same userID (UR ID), and based on the type of CBSD radio in each deployment. Pricing is specified in your SAS agreement. 

There are two billing modes:

  * **Fixed wireless pricing:** SAS services are billed per [Customer Premise Equipment (CPE)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cpe). Base stations that operate solely to connect to CPEs in a fixed wireless setup are free of charge. This pricing applies to SAS deployments that meet one of the following conditions: 

    * The number of CPE CBSDs is equal or more than the number of Base stations
    * The number of CBSDs less than ten and the number of CPEs greater than zero
  * **Mobility, IoT, or Private-LTE pricing:** SAS services are billed per [Citizens Broadband Radio Service Device (CBSD)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cbsd), based on CBSD category A or B. This pricing applies to any CBSD that is not used solely for CBSD-to-CBSD fixed wireless. This pricing applies to SAS deployments that meet the following conditions: 

    * CBSD type is the same as the base station for all the CBSDs
    * The number of CPEs is less than the number of base stations



**Note:** For customers who provisioned SAS prior to Nov 6 2023, the billing mode for each deployment is determined when the SAS organization is provisioned. The billing mode is visible in the SAS Portal. 

## How billing works

  * **Pay for CBSDs registered each day:** You're billed for the CBSDs that are registered for more than 30 minutes each day. The prices are quoted in monthly increments. The billing is prorated per day for each CBSD registered with Google SAS.
  * **Pay each month:** Google sends an invoice at the beginning of the month for the charges incurred during the previous month. Invoices are sent through email to the contact address you specified when you signed up with Google SAS.



## View your billing options

As an administrator, you can view the default and allowed billing modes associated with your SAS account on the SAS Portal.

**Important:** To change the billing mode on your account, you must contact SAS support.

To view the billing mode:

  1. Open the [SAS Portal](https://wirelessconnectivity.google.com/sas).
  2. Click **View deployments**.
  3. Select your organization.
  4. On the deployment page, view the billing mode.
  5. For the billing mode, select **Default billing mode** or **Allowed billing mode**.



## Determine if your CBSD operates as a base station

**Important:** SAS examines the [Federal Communications Commission (FCC) ID](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#fccid) in the FCC database specifications to determine if a CBSD operates as CPE.

To find your CBSD radio type:

  1. Open the [SAS Portal](https://wirelessconnectivity.google.com/sas).
  2. Click **View deployments** , and then open your organization.
  3. Click _table_chart_ **Table view**.
  4. On the **Device table** page, select a CBSD.
  5. On the **Config** tab, view the **Radio type** as **CPE** or **Basestation**.



## Understand and pay your SAS invoice

Invoices are sent by email at the beginning of the month for your previous month's activities, and payment terms are Net 30. Invoices are sent to the email address that you used to sign up. To change your billing email address, contact the [customer maintenance team](mailto:customer-maintenance@google.com).

### Review and pay charges

**Important:** Any request to send payment to an account other than what is listed on your invoice is fraudulent and should be reported to [collections@google.com](mailto:collections@google.com).

To review and pay charges:

  1. Open your monthly invoice and go to the second page.
  2. Review each column.
  3. Send your payment to the address or bank account listed on the Google invoice.



### Understand each column in the invoice

Invoice item | Description  
---|---  
Description | The Citizens Broadband Radio Service (CBRS) device type or category for which you're billed:

  * **Spectrum Access System FIXED_WIRELESS_CPE** : CPE device connected through fixed wireless
  * **Spectrum Access System MOBILE_A** : Category A CBSD
  * **Spectrum Access System MOBILE_B** : Category B CBSD

  
Quantity | The number of days that CBSDs are registered during the billing period. For example, if one CBSD is registered with the SAS for 30 days, it is equal to 30 in quantity.  
Unit price | The price per day for each device. For example, if the price per month is $2.25, the unit price displayed in the invoice is $2.25 multiplied by 12 months and then divided by 365 days, which is equal to $0.073972.  
  
### Download usage reports

To request your usage report by email, contact the [SAS support team](mailto:sas-support@google.com).

### Get more help

For questions about billing, email [collections@google.com](mailto:collections@google.com), or at the bottom of your invoice email, click **Contact us**.

## Billing information for nonprofits

If your organization is a nonprofit, sign up for SAS and enter your tax exemption documentation to exclude tax on your monthly SAS usage fees. Only administrators can upload tax exemption information.

To enter your tax exemption information for existing users:

  1. Open [payments.google.com](https://payments.google.com/gp/w/u/0/home/signup).
  2. Sign in with your company's administrator account.
  3. On the right, click **Settings** , and then click **Tax exemption info**.
  4. Select the following: 
     * State
     * Tax exemption number
     * The certificate start and end date, if applicable
     * The exemption type, if applicable
  5. To select your tax exemption certificate file, click **Upload File**.
  6. When the file is uploaded, click **Add** , and then click **Save**. After your certificate is accepted, the status of your account updates automatically.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
