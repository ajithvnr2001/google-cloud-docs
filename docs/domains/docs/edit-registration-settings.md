---
url: https://docs.cloud.google.com/domains/docs/edit-registration-settings/
title: Edit registration settings for a domain \u00a0|\u00a0 Cloud Domains \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:40.372721+00:00
---

# Edit registration settings for a domain  |  Cloud Domains  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/domains/docs/edit-registration-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Domains ](https://docs.cloud.google.com/domains/docs)
  * [ Guides ](https://docs.cloud.google.com/domains/docs/buy-register-domain)



Send feedback 

#  Edit registration settings for a domain Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** On September 7, 2023 Squarespace acquired all domain registrations and related customer accounts from Google Domains. For more information about how this change affects Cloud Domains, see [Cloud Domains feature deprecations](https://docs.cloud.google.com/domains/docs/deprecations/feature-deprecations), [Renew an expired domain registration](https://support.google.com/a/answer/6152355), and [Squarespace purchase of Google Domains FAQ](https://docs.cloud.google.com/domains/docs/faq). 

This page describes how to edit registration settings—including contact settings, privacy settings, and DNS settings—for an existing domain in Cloud Domains.

## Before you begin

Before you complete the tasks, review the following information on the Cloud Domains overview and Troubleshooting pages:

  * [Contact information](https://docs.cloud.google.com/domains/docs/overview#contact-info)

**Note** : Starting in August 2025: For generic TLD domains, the [ICANN Registration Data Policy](https://www.icann.org/en/contracted-parties/consensus-policies/registration-data-policy) no longer requires both administrative and technical registrant contact information. If you submit administrative and technical contact information, it is ignored for generic TLD domains.

There are no changes for country-code TLD domains and all contact information continues to be required.

  * [Privacy protection](https://docs.cloud.google.com/domains/docs/overview#privacy-protection)

  * [Contact details while registering or transferring a domain for a company](https://docs.cloud.google.com/domains/docs/troubleshooting#contact-configuration)




## Edit contact and privacy settings

When you register a domain, you must submit contact information for that domain.

To edit a registration's contact settings, such as email, phone number, and postal address, and to choose privacy settings for the contact information, complete the following steps.

**Caution:** Changes to contact information are not atomic. If you change a contact privacy setting from `REDACTED_CONTACT_DATA` to `PUBLIC_CONTACT_DATA` while also updating your contact information, existing registrant contact information might become public because changes to the registrant contact information can take longer to publish.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `domains.registrations.configureContact`



**Roles**

  * `roles/domains.admin`



###  Console 

  1. In the Google Cloud console, go to the **Cloud Domains** page.

[Go to Cloud Domains](https://console.cloud.google.com/net-services/domains/registrations/list)

  2. Click the domain name that you want to edit. You can also click more_vert**More** next to the domain name to see the edit menu.

  3. To edit contact details, including the name, address, and email associated with the domain, click **Edit contact details**.

  4. Make the required changes.

  5. Choose or edit the privacy settings. The privacy options available for the domain that you selected might vary.

  6. Click **Save**.


**Note:** These updates might require a confirmation through a verification email sent to the registrant before they take effect.

###  gcloud 

Use the [`gcloud domains registrations configure contacts` command](https://docs.cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/contacts):
    
    
    gcloud domains registrations configure contacts DOMAIN_NAME
    

Replace `DOMAIN_NAME` with the name of the registered domain—for example, `example.app`.

The following example shows the output when you change the privacy settings for the domain `example.com`:
    
    
    Contact data not provided using the --contact-data-from-file flag.
    
    Do you want to enter it interactively (y/N)?  y
    
    Which contact do you want to change?
     [1] all the contacts to the same value
     [2] registrant contact
     [3] admin contact
     [4] technical contact
     [5] cancel
    Please enter your numeric choice (1):  1
    
    Full name:  NAME
    Organization (if applicable):  ORGANIZATION
    Email (darcy@gmail.com):  EMAIL_ADDRESS
    Enter phone number with country code, e.g. "+1.8005550123".
    Phone number:  PHONE_NUMBER
    Enter fax number with country code, e.g. "+1.8005550123".
    Fax number (if applicable):  FAX_NUMBER
    Enter two-letter country code, e.g. "US" or "PL".
    Refer to the guidelines for entering address field information at https://support.google.com/business/answer/6397478.
    Country / Region code:  COUNTRY_CODE
    Postal / ZIP code:  ZIP_CODE
    State / Administrative area (if applicable):  STATE
    City / Locality:  CITY
    Address Line 1:  ADDRESS_LINE_1
    Address Line 2 (if applicable):  ADDRESS_LINE_2
    Address Line 3 (if applicable):
    Your current contact privacy is REDACTED_CONTACT_DATA.
    
    Do you want to change it (y/N)?  y
    
    Specify contact privacy
     [1] private-contact-data
     [2] redacted-contact-data
     [3] public-contact-data
    Please enter your numeric choice (2):  1
    
    Waiting for 'operation-1596738116518-5ac39903c0348-5391fe45-78f57284' to
    complete...done.
    Updated registration [example.com] Note:
    The contact settings are currently pending.
    In order to finalize the update you need to confirm the change.
    An email with instructions has been sent to the registrant.
    

Replace the following:

  * `NAME`: your full name—for example, `Alice Smith`
  * `ORGANIZATION`: (optional) your organization—for example, `Doe Corp`
  * `EMAIL_ADDRESS`: your email address for verification—for example, `alice@example.net`
  * `PHONE_NUMBER`: the phone number of the contact in international format—for example, `+1-800-555-0123`
  * `FAX_NUMBER`: the fax number of the contact in international format—for example, `+1-800-555-0123`
  * `COUNTRY_CODE`: the country or region code of the address—for example, `US` for United States
  * `ZIP_CODE`: the postal code or ZIP code of the address—for example, `94043`
  * `STATE`: the state or administrative area of the address—for example, `CA`
  * `CITY`: the city or locality of the address—for example, `Mountain View`
  * `ADDRESS_LINE_1`: the first address line of the registrant—for example, `1599 Bayview Parkway`

You can have up to 5 address lines, but only the first one is required.

  * `ADDRESS_LINE_2`: (optional) the second address line of the registrant—for example, `APT. 123`

**Note:** You must enter the address accurately because it is used for domain recovery in case you lose access to your registration. Refer to these [guidelines for entering address field information](https://support.google.com/business/answer/6397478).

**Note:** These updates might require a confirmation through a verification email sent to the registrant before they take effect.

###  API 

Use the [`registrations.configureContactSettings` method](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/configureContactSettings):
    
    
    POST https://domains.googleapis.com/v1/projects/PROJECT_ID/locations/global/registrations/DOMAIN_NAME:configureContactSettings
    

Replace the following:

  * `PROJECT_ID`: the name of your project
  * `DOMAIN_NAME`: the domain for which you want to change contact settings



The request body can be one of the following:

  * To change the registrant contact's email address:
        
        {
          "contactSettings": {
            "registrantContact": {
              "email": "new-registrant@example.com",
            },
          },
          "updateMask": "registrantContact.email",
        }
        

  * To change the privacy setting to public:
        
        {
          "contactSettings": {
            "privacy": "PUBLIC_CONTACT_DATA",
          },
          "updateMask": "privacy",
          "contactNotices": ["PUBLIC_CONTACT_DATA_ACKNOWLEDGEMENT"],
        }
        

  * To change the entire registrant contact and the privacy setting:
        
        {
          "contactSettings": {
            "privacy": "CONTACT_PRIVACY",
            "registrantContact": {
              "postalAddress": {
                "regionCode": "REGION_CODE",
                "postalCode": "POSTAL_CODE",
                "administrativeArea": "SUBDIVISION",
                "locality": "CITY",
                "addressLines": [
                  "ADDRESS"
                ],
                "recipients": [
                  "CONTACT_NAME"
                ],
                "organization": "ORGANIZATION"
              },
              "email": "EMAIL_ADDRESS",
              "phoneNumber": "PHONE_NUMBER",
              "faxNumber": "FAX_NUMBER"
            }
          },
          "updateMask": "privacy,registrantContact",
        }
        

Replace the following values for the `registrantContact`, `adminContact`, or the `technicalContact` that you want to change. For detailed information about each type of contact, see [Contact privacy](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations#ContactPrivacy).

**Note:** Depending on the country of registration, some of the following fields might be optional. Refer to the [guidelines for entering address field information ](https://support.google.com/business/answer/6397478).
    * `CONTACT_PRIVACY`: the preferred privacy setting for the contact data
    * `REGION_CODE`: the region code of the address—for example, `US` for United States
    * `POSTAL_CODE`: the postal code of the address—for example, `94043`
    * `SUBDIVISION`: the highest administrative subdivision of an address, like a state, a province, an oblast, or a prefecture—for example, `CA` for the state of California
    * `CITY`: the name of the city or town of the address—for example, `Mountain View`
    * `ADDRESS`: the lower levels of an address—for example, `1599 Amphitheater Parkway`
    * `CONTACT_NAME`: the name of the contact
    * `ORGANIZATION`: (optional) the name of the organization that is registering the domain—for example, `Doe Corporation`
    * `EMAIL_ADDRESS`: the email address of the contact—for example, `john@example.com`
    * `PHONE_NUMBER`: the phone number of the contact in international format—for example, `+1-800-555-0123`
    * `FAX_NUMBER`: (optional) the fax number of the contact in international format—for example, `+1-800-555-0123`
**Note:** These updates might require a confirmation through a verification email sent to the registrant before they take effect.



## Edit DNS settings

To edit or configure the DNS settings of a registration, including authoritative name servers for the domain, complete the following steps.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `domains.registrations.configureDns`



**Roles**

  * `roles/domains.admin`



###  Console 

  1. In the Google Cloud console, go to the **Cloud Domains** page.

[Go to Cloud Domains](https://console.cloud.google.com/net-services/domains/registrations/list)

  2. Click the domain name that you want to edit. You can also click more_vert**More** next to the domain name to see the edit menu.

  3. To edit the DNS details, including the DNS provider option and the DNSSEC settings, click **Edit DNS details**. Choose one of the options in the following table. 

DNS provider | Description | Cost  
---|---|---  
**Cloud DNS** | Google recommends that you use Cloud DNS as your DNS provider for all your name servers. | Additional Cloud DNS charges apply. For details, see [ the Cloud DNS pricing page.](https://docs.cloud.google.com/dns/pricing)  
**Custom name servers** | If you choose this option, you can use Cloud Domains to configure your name servers, and then use a third-party DNS provider to configure your DNS resource records.  | Check with your DNS provider.  
  4. Click **Save**.




###  gcloud 

Use the [`gcloud domains registrations configure dns` command](https://docs.cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/dns):
    
    
    gcloud domains registrations configure dns DOMAIN_NAME
    

Replace `DOMAIN_NAME` with the name of the registered domain—for example, `example.app`.

The following example shows the output when you change the DNS provider from Google Domains to Cloud DNS for the domain `example.com`:
    
    
    Your current DNS settings are:
    googleDomainsDns:
     dsState: DS_RECORDS_UNPUBLISHED
     nameServers:
     ‐ ns-cloud-b1.googledomains.com
     ‐ ns-cloud-b2.googledomains.com
     ‐ ns-cloud-b3.googledomains.com
     ‐ ns-cloud-b4.googledomains.com
    You can provide your DNS settings by specifying name servers or Cloud DNS
    Managed Zone name
     [1] Provide name servers list
     [2] Provide Cloud DNS Managed Zone name
     [4] cancel
    Please enter your numeric choice (4):  2
    
    Cloud DNS Managed Zone name:  example-app
    
    Waiting for 'operation-1596738623568-5ac39ae74fa6f-1025c18d-9d3a4872' to
    complete...done.
    Updated registration [example.com].
    

###  API 

Use the [`registrations.configureDnsSettings` method](https://docs.cloud.google.com/domains/docs/reference/rest/v1/projects.locations.registrations/configureDnsSettings):
    
    
    POST https://domains.googleapis.com/v1/projects/PROJECT_ID/locations/global/registrations/DOMAIN_NAME:configureDnsSettings
    

Replace the following:

  * `PROJECT_ID`: the name of your project
  * `DOMAIN_NAME`: the domain that you want to change contact settings for



The request body can be one of the following:

  * To update or switch to custom name servers: 
        
        {
          "dnsSettings": {
            "customDns": {
              "nameServers": [
                "ns-cloud-a1.googledomains.com",
                "ns-cloud-a2.googledomains.com",
                "ns-cloud-a3.googledomains.com",
                "ns-cloud-a4.googledomains.com"
              ]
            }
          },
          "updateMask": "customDns"
        }
        




## Edit automatic renewal settings

All domains renew automatically. Changes to your automatic renewal settings must be made at least 15 days before the expiration date.

For domains that use a country-code TLD: When these domains expire, there is a 72 hours waiting period before you can renew a domain or change the automatic renewal settings.

### Turn off automatic renewal

To disable automatic domain renewal:

###  Console 

  1. In the Google Cloud console, go to the **Cloud Domains** page.
[Go to Cloud Domains](https://console.cloud.google.com/net-services/domains/registrations/list)
  2. Click the domain name for which you want to turn off automatic renewal.
  3. Click **Disable auto-renewal**.
  4. On the **Disable auto-renewal** dialog, click **Disable**.



###  gcloud 

Use the [`gcloud domains registrations configure management` command](https://docs.cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/management):
    
    
    gcloud domains registrations configure management DOMAIN_NAME \
        --preferred-renewal-method=renewal-disabled
    

Replace `DOMAIN_NAME` with the name of the registered domain—for example, `example.app`.

### Turn on automatic renewal

To enable automatic domain renewal:

###  Console 

  1. In the Google Cloud console, go to the **Cloud Domains** page.
[Go to Cloud Domains](https://console.cloud.google.com/net-services/domains/registrations/list)
  2. Click the domain name for which you want to turn on automatic renewal.
  3. Click **Enable auto-renewal**.
  4. On the **Enable auto-renewal** dialog, click **Enable**.



###  gcloud 

Use the [`gcloud domains registrations configure management` command](https://docs.cloud.google.com/sdk/gcloud/reference/domains/registrations/configure/management):
    
    
    gcloud domains registrations configure management DOMAIN_NAME \
        --preferred-renewal-method=automatic-renewal
    

Replace `DOMAIN_NAME` with the name of the registered domain—for example, `example.app`.

## What's next

  * To view a list of your registered domains, see [List registered domains](https://docs.cloud.google.com/domains/docs/list-registrations).
  * To delete a domain, see [Delete a registered domain](https://docs.cloud.google.com/domains/docs/delete-domain).
  * To access API information, see the [Cloud Domains API](https://docs.cloud.google.com/domains/docs/reference/rest).
  * To find solutions for common issues that you might encounter when using Cloud Domains, see [Troubleshooting](https://docs.cloud.google.com/domains/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
