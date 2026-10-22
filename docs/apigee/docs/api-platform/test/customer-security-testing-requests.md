---
url: https://docs.cloud.google.com/apigee/docs/api-platform/test/customer-security-testing-requests/
title: Customer security testing requests \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:56.372106+00:00
---

# Customer security testing requests  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/test/customer-security-testing-requests/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Customer security testing requests Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

## Customer-requested testing of Apigee

Apigee allows and even encourages our customers to scan or test their own endpoints in Apigee. We ask for notification of the scan only so that we are aware of the scanning in the event the scanning causes an issue for your services. To notify Apigee of your planned testing, open a support ticket at least one business day prior to the start of testing and provide the following details:

  * Date of tests (start date and projected end date including time zone)
  * Name of person/company performing the testing
  * Contact info for person performing the testing
  * Source IP addresses of the testing
  * Target/Destination IPs and names of the systems being tested (API endpoint names)



Testing is specifically not prohibited in customer agreements. Approval emails will not be sent, nor will authorization letters be signed, because there is no prohibition against the customer testing their own end points and configurations in Apigee.

If customers find vulnerabilities during their testing that they believe are because of the Apigee platform itself, we ask them to submit this information to Apigee using a standard support ticket. By opening a support ticket, the issue can be tracked, escalated, and resolved as appropriate. 

Once customers submit a vulnerability report through the standard Apigee support process, the Support team will review the ticket and escalate to security and engineering teams as appropriate. Customers should expect a response in the ticket, although follow-up could come directly from Google security or engineering if more information is needed about the reported vulnerability. 

## Google scanning of Apigee

Apigee scans Apigee weekly. However, these scans are for internal purposes and not shared with customers. The Google scans look at publicly exposed endpoints and the internal infrastructure. These scans are looking for missing patches, vulnerabilities, misconfigured hosts, poor TLS configurations, and so on. They are part of the Google commitment to "secure the platform."

If something was identified that directly related to a customer and was obviously incorrectly configured, we would notify the customer. But, since customers use both clear text and TLS configurations, and since some customers use Apigee for public data while others use Apigee for PCI or healthcare or other PII types of data, we are not in a position to determine what is always appropriate for all of our customers.

These Google scans may not be used by customers as fulfilling their own due diligence in testing their endpoints and verifying secure configurations such as are required by PCI and other industry or regulatory standards.

Customers are encouraged to perform their own testing of endpoints in Apigee for security or compliance needs. See the Customer-requested testing of Apigee section of this document for instructions.

## Customer testing of Apigee hybrid

Because Apigee hybrid customers have Apigee software within their own networks, customers are permitted to test the software. There are no limitations on testing of systems or services that are managed by the customer directly.

As a result, however, Apigee does not provide testing reports to Apigee hybrid customers. Apigee _does_ perform malware scanning of Apigee code before it is released to customers.

For Hybrid customers, the API processing services are within the customer's network, while the management interface is in Apigee Cloud. Please review the Customer-requested testing of Apigee Cloud section of this document for details on management interface testing restrictions.

## Customer testing of Apigee-sponsored developer portals hosted at Pantheon or Acquia

Customers can perform penetration testing on their portals hosted by Pantheon or Acquia. Apigee and Pantheon (or Acquia) need to be notified first, and customers can do this by opening a support ticket with Apigee.

Customers must provide the Support team with following details of the planned testing:

  * Date of tests (start date and projected end date including time zone)
  * Name of person/company performing the testing
  * Contact info for person performing the testing
  * Source IP addresses of the testing
  * Pantheon Site Names and URLs being tested



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
