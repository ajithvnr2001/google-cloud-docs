---
url: https://docs.cloud.google.com/data-studio/data-governance-in-an-overview/
title: Data governance in Data Studio: An overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:27.142527+00:00
---

# Data governance in Data Studio: An overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/data-governance-in-an-overview/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Data governance in Data Studio: An overview Stay organized with collections  Save and categorize content based on your preferences. 

Effective data governance policies, procedures, and technology help ensure that your data is secure, private, accurate, available, and usable. This article outlines the features of Data Studio that can help you to control access to your organization's sensitive information, while still promoting data democratization—giving more people access to more data.

**Note:** This article applies to both the no-cost version of Data Studio and to Data Studio Pro.

## The need for controlling access to your data

Implementing strong data governance policies and controlling access to your data helps you achieve the following benefits:

  * Protect sensitive information
  * Ensure data integrity
  * Meet compliance requirements
  * Maintain stakeholder trust



### Protecting sensitive information

Data Studio reports often leverage data that contains confidential information such as personally identifiable information (PII), financial data, and proprietary business strategies. Controlling who can access this data is paramount in preventing data breaches and unauthorized disclosures.

### Ensuring data integrity

Restricting data modification privileges to authorized personnel helps safeguard the accuracy and reliability of the data. This is particularly crucial for reports that are used in decision-making processes.

### Meeting compliance requirements

Many industries operate under strict data privacy regulations, such as GDPR and HIPAA. Data Studio's access control features help you to adhere to these regulations, mitigating legal risks.

### Maintaining stakeholder trust

Demonstrating a commitment to data security through robust access controls fosters trust with your clients and partners. It assures them that their data is handled responsibly and securely.

## Recommendations

To implement the strongest data governance features in Data Studio, consider the following recommendations:

  * Use **Viewer's Credentials** or **Service Account Credentials** (if possible) for your data sources.
  * Use **reusable data sources** in your reports.
  * **Hide or remove sensitive fields** from the data source.
  * **Restrict sharing and downloading** of sensitive reports to limit access to specific individuals or groups.
  * As a report owner, **prevent editors from changing access** and adding new people.
  * Apply **row-level security** to the data.
  * For Google Workspace and Cloud Identity organizations, utilize **administrator settings** to enforce default policies for data access controls.



The rest of this article elaborates on these recommendations.

## Use data credentials to control who can access the data

Data credentials determine who can see the data that is provided by a data source. Data Studio uses several types of data credentials:

  * **Owner's Credentials** let other users access the data by using the credential owner's authorization. This option means that other people can view or create reports that use this data without requiring them to have their own access to the dataset.
  * **Viewer's Credentials** rely on each individual report viewer's credentials to access the data. This option restricts the ability to view the data in the data source to people who also have access to the underlying dataset.
  * **Service Account Credentials** rely on a special type of Google account that represents a non-human user, which can be authenticated and authorized to access data.

**Tip:** For maximum data access control, use Viewer's Credentials or Service Account Credentials (if possible) for your data sources.

[Learn more about data credentials](https://docs.cloud.google.com/data-studio/data-credentials).

## Use reusable data sources to prevent editor access

Data sources can be either embedded in a report or be a separate reusable asset _._ The type of data source is significant from the viewpoint of restricting access to the data.

Data sources that you create when editing a report are embedded in it. Anyone who can edit the report can also edit the data source and its connection. Sharing or copying the report also shares or copies any embedded data sources. While embedded data sources simplify collaboration, they can also let viewers access data and metadata by copying the report. You can prevent this by configuring the report's sharing settings.

Data sources that you [create from the Data Studio home page](https://docs.cloud.google.com/data-studio/add-data-to-a-report) are reusable. Access to these reusable data sources is restricted. Only users with explicit access can edit these sources. Additionally, modifications to the data source connection are limited to the owner of the data source credentials.

**Tip:** For maximum data access control, use reusable data sources in your reports. If necessary, you can [convert an embedded data source into a reusable data source](https://docs.cloud.google.com/data-studio/embedded-data-sources).

## Hide or remove sensitive fields

If your dataset includes fields that you don't want exposed in your reports, you can hide or remove them from the data source.

### Hide fields

Data source editors can selectively hide fields from the report's field list, preventing report editors from seeing those fields. Data source editors can still see and unhide hidden fields.

### Remove fields

Data source editors can remove fields entirely from the data source, making them inaccessible to report and data source editors and viewers. Reconnecting the data source or refreshing fields will add removed fields back to the data source.

**Note:** Hiding or removing a field may break charts and calculated fields that rely on the hidden or removed field.

[Learn more about hiding and removing fields](https://docs.cloud.google.com/data-studio/create-rename-copy-hide-and-remove-fields).

## Restrict sharing and downloading of sensitive reports and data sources

As a report owner or editor, you can limit who can view or edit your reports. You can also prevent viewers from downloading, printing, and copying a report or data source, and you can restrict viewer access to other features that can potentially reveal sensitive information.

### Limit the people with whom you share

When you share a report or data source, you can choose to limit access to specific individuals, to Google Groups, or to your entire domain. This helps you balance your need to share information broadly while ensuring that sensitive data is accessible only to authorized personnel.

As the owner of a report or data source, you can prevent editors from changing access and adding new people.

### Prevent downloading, printing, and copying reports

Report editors can disable the download, print, and copy functions for viewers, preventing them from easily disseminating the data.

### Additional viewer restrictions

Report editors can prevent viewers from doing the following:

  * Viewing and creating alerts
  * Generating Google Slides with Gemini assistance
  * Viewing advanced applied filters



[Learn more about sharing restrictions](https://docs.cloud.google.com/data-studio/stop-sharing-your-reports-and-data-sources).

## Apply row-level security to the data

If your data can be associated with individual user email addresses, consider implementing the filter by email feature in the data source. This feature requests report viewers to allow Data Studio to access their email address and use that to filter the data coming from the data source to only those rows that they are allowed to see.

[Learn more about filtering by email](https://docs.cloud.google.com/data-studio/filter-by-email-address).

## Set organization level sharing and access options

If you're using Data Studio in a Google Workspace organization, your administrator can set default policies for the following data access controls within your org:

  * Prevent report editors from setting Owner's Credentials for data sources. This prevents editors from accessing data that they wouldn't typically have permission to see.
  * Restrict where scheduled email deliveries can be sent, including limiting email delivery to internal domains or disabling Google Chat delivery to external recipients.
  * Set downloading restrictions for viewers.
  * Set policies for how users add or create data sources from third-party connectors.
  * Set policies for how users grant access to new and existing third-party visualizations.



[Learn more about Data Studio's enterprise administrator features](https://docs.cloud.google.com/data-studio/enterprise-administrator-feature-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
