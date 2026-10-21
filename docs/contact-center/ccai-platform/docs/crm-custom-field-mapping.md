---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-custom-field-mapping/
title: Custom CRM field mapping (Salesforce, Zendesk, Kustomer) \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:53:40.929360+00:00
---

# Custom CRM field mapping (Salesforce, Zendesk, Kustomer)  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-custom-field-mapping/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Custom CRM field mapping (Salesforce, Zendesk, Kustomer) Stay organized with collections  Save and categorize content based on your preferences. 

To allow metadata from CRM records to be analyzed quickly, the Contact Center AI Platform (CCAI Platform) Web & Mobile SDKs can push data into CRM custom fields.

Custom CRM field mapping provides the ability to fully customize the CRM fields and what data is pushed into those fields from the CCAI Platform Web & Mobile SDKs.

### Mobile SDK API example

The following sections outline an example specific to the mobile SDK.

#### Data from SDK to server
    
    
    {
        custom_data: { # same format with previous custom data from SDK
            data_name: {
                value: value,
                type: string,
                label: "Data Name",
            },
            device: { # example
                value: "iOS",
                type: "string",
                label: "Device Type"}
        }
    }
    

#### Data from server to CRM adaptor
    
    
    {
        key: {
            crm_field: "crm custom field name",
            type: "text", # text / checkbox ...,
            value: "value"
        },
        device: { # example
            crm_field: "device",
            type: "text", 
            value: "iOS"
        }
    }
    

#### API endpoint

The CRM custom field mapping can be accessed using an API. The following endpoints are available:

  * **Retrieve all fields** : HTTP POST or GET: `/crm_custom_fields`

  * **Update or delete a specific field** : HTTP PUT or DELETE `/crm_custom_fields/:id`




### Steps to configure

  1. Create the custom field and values in your CRM.

  2. Assign the new values to contacts in your CRM.

  3. Configure the setting in the CCAI Platform portal.

  4. Test.




### Zendesk configuration

The following sections outline the process to configure field mappings for the Zendesk CRM.

#### Create a custom field for User (Contact)

  1. Sign in to Zendesk as an Admin.

  2. Click the  settings  to access the Admin options.

  3. Select **User Fields.**

  4. Select the field type that you want to create.




  1. Add a field title and name within an agent's view.

**Note:** We recommend using the same value as the **crm_field** from the API.

**Field key** is filled automatically.

  2. Click **Create field**.




You can now see this new field in the **Active fields** list, and this new field appears in the left-side column when viewing a user.

![Active fields display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f23da0486.png)

#### Create a custom field for Ticket

  1. Sign in to Zendesk as an Admin.

  2. Click the  settings  icon to access the Admin options.

  3. Select **Ticket Fields.**

  4. Click the **add custom field** button.

  5. Select a field type that you want to create by clicking **select**.

  6. Add a **Field Title**. The **Field Title** will appear in your Agent's view.

We recommend using the same value as the **crm_field** from the API.

![Field title display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f23da700b.png)

  7. Click the **Add field** button.




You can now see this new field in the **Active fields** list, and this new field appears in the left side column when viewing a ticket.

### Salesforce configuration

  1. Go to **Setup.**

  2. Select **Object Manager**.

  3. Choose the object on which you want to append custom fields (Case or CCAI Platform Session).

  4. Click **Fields & Relationships**.

  5. Click **New**.

  6. Select **Text** as the Data Type.

  7. In **Field Label** , enter a name for the field.

  8. In **Length** , enter **255**.

**Field Name** should automatically populate after you enter **Field Label**.

![Field label display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f23daa480.png)

You may leave the rest of the variables at their default value.

  9. Click **Next**.

  10. Check the **Visible** box for any of the profiles that access the object (Case or CCAI Platform Session).

  11. Click **Next**.

  12. Click **Save**.

  13. This will take you back to the **Fields & Relationships** view. Find the field that you just created, and take note of the **Field Name**.

![Fields and relationship view](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f23dad8b7.png)

  14. The **Field Name** is what you will enter in **CRM Field Label** in the CCAI Platform Custom Field Mapping page.




The following example shows what a **New field** will look like when correctly set up and used on the case object:

![New field display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f23db13cf.png)

### Kustomer configuration

See the Kustomer Help Center for details and information regarding setting up Custom Fields.

### CCAI Platform configuration

The following sections outline the changes needed in the CCAI Platform portal to configure the Kustomer CRM field mapping.

#### Add CRM field mapping

  1. In the CCAI Platform portal, go to **Settings > Operation Management.**

  2. Go to the **CRM Custom Field Mapping** section and click **View All**.

  3. Click the + **Add CRM Field Mapping link.**

     * **Field Mapping Title:** CCAI Platform name for this custom field mapping used in the CCAI Platform Portal

     * **CRM Field Label:** Label within your CRM of the CRM field to which you are mapping

     * **Custom Data Field Label:** Label of the SDK data field from which you are mapping




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
