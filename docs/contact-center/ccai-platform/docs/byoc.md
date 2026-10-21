---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/byoc/
title: Bring your own carrier (BYOC) \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:28:36.447143+00:00
---

# Bring your own carrier (BYOC)  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/byoc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Bring your own carrier (BYOC) Stay organized with collections  Save and categorize content based on your preferences. 

The Bring Your Own Carrier program lets you integrate your existing telephony infrastructure with Contact Center AI Platform (CCAI Platform). This means you can retain your current telephony carrier and phone numbers while leveraging the capabilities of CCAI Platform.

The CCAI Platform enterprise license comes with a quota of 5,000 minutes per agent per month, with the exception of IVA Only, which includes the BYOC costs. Additional BYOC minutes that exceed this quota are charged according to [CCAI Platform pricing](https://cloud.google.com/skus?currency=USD&filter=BYOC).

Because BYOC provides telephony service, legislation and regional limitations prevent CCAI Platform from operating in some locations. For more information, see [Telephony](https://docs.cloud.google.com/contact-center/ccai-platform/docs/localities#telephony).

This page explains how to enable BYOC and get optimal use of CCAI Platform capabilities. While BYOC is typically used with the [Interactive Virtual Assistant solution](https://docs.cloud.google.com/contact-center/ccai-platform/docs/iva-guide), you can also use it to simplify and accelerate migration from existing on-premise telephony platforms. You can use BYOC for both inbound and outbound calling.

**Important:** BYOC is only available for the voice channel. For the SMS channel, contact Google support to request Google SMS numbers. You can also port the SMS numbers to a Google telephony provider.

## BYOC integration with SIP

This section highlights the key benefits of adopting the BYOC integration.

You can integrate with an existing enterprise Session Border Controller (SBC) or telephony carrier by using Session Initiation Protocol (SIP) through the BYOC option provided by CCAI Platform.

The following diagram shows the SIP integration flow:

![Diagram of the SIP integration flow.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/byoc-sip-integration.png)

Here are the key benefits of integrating BYOC using SIP:

  * **Cost optimization** : Potentially save money by using existing carrier contracts and leveraging the BYOC fair use policy.

  * **Flexibility and control** : Retain existing telephony infrastructure while gaining access to CCAI Platform AI-powered capabilities.

  * **Seamless integration** : Get guidance and technical support for a smooth and efficient integration with minimal disruption.

  * **Highly available voice services** : Google recommends that you build redundancy into your BYOC connectivity design to help with disaster recovery across your carrier's infrastructure. For example, you can configure over-the-top (OTT) SIP trunks (using the public internet or private connectivity) to connect two or more points to CCAI Platform.


**Important:** If you implement BYOC telephony integration, you must manage high availability and call routing from the integration's carrier services to the CCAI Platform media layer's edge.

## Constraints

Some fields in the SIP headers, such as User-to-User (UUI) information, don't pass through to CCAI Platform session metadata by default. For example, `TO` and `FROM` fields are available in session metadata as DNIS and ANI. If UUI data must be [passed through SIP headers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-pass-data-parameters), then that payload must be mapped to X-header values. For example, SipHeader_X-UUI is available to the session metadata.

BYOC supports multiple simultaneous inbound carriers. However, for outbound calls, only a single outbound carrier is supported. You can request for Google telephony to be used as a fallback option for outbound calls.

## Implement BYOC

This section explains how to implement BYOC.

### Prepare for integration

Before you can create a BYOC integration, you must gather requirements and do some preliminary tasks.

To prepare for integration, do the following:

  1. Prepare a current-state topology diagram of your existing telephony network infrastructure and document the Session Border Controller (SBC) in use.

  2. Use your current-state topology diagram to design an end-state topology diagram for BYOC integration to CCAI Platform.

  3. Draft a strategy for high availability from your origination platform in the event of SIP options failure.

  4. Consider sequential and round-robin call distribution strategies.

  5. Determine your preferred authentication method between SBCs. Keep the following in mind:

     * SIP authentication is only supported for inbound calls. Outbound calls still require IP to IP handshakes. Therefore, Google recommends IP to IP handshakes.

     * IP to IP handshakes require an Access Control List (ACL) update on the SBCs to include the [CCaaS IP ranges](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-adapter-ip-allow-list#media_ip_ranges).

  6. Set up authentication.




### Fill out the BYOC questionnaire

Fill out the [Google Cloud CCaaS BYOC Questionnaire](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/Google%20CCaaS%20BYOC%20Information%20and%20Worksheet.pdf) so Google can help you integrate BYOC with your instance. While the questionnaire is for the most part self-explanatory, the following information can help you fill it out:

  * **Supported Audio Codecs** : G.711 µ-law (PCMU), G.711 A-law (PCMA)

  * **Google Cloud CCaaS Instance Name(s)** : You must create all required instances (Development, UAT, or Production) before submitting the CCaaS BYOC Questionnaire. Each subsequent BYOC instance activation requires a separate support ticket and CCaaS BYOC Questionnaire.

  * **Customer Contact Information** : This is used to schedule interop sessions and testing.

  * **Customer SIP Trunk Information (calls inbound)** : In the **Source IP(s)** field, enter one or more public IP addresses or a CIDR range.

  * **Customer SIP Trunk Information (calls outbound)** : Enter public IP addresses or FQDN. Leave the section empty if you're planning to use only Google telephony for outbound calls. In that case, for **Call Termination (Outbound calling)** , select **Google Cloud CCaaS**.

  * **Outbound Distribution Method** : Fill out this section only if you aren't planning to use Google telephony for outbound calls and you have multiple outbound destination IPs and FQDNs. You can specify the distribution method from the options provided. If you select the weighted option, ensure that the total weighting value doesn't exceed 100 and specify the destinations and weights in the provided field.




### Open a Google support case

Open a Google Cloud support case and include the following:

  * The CCAI Platform BYOC Questionnaire that you filled out in Fill out the BYOC questionnaire.

  * The end-state topology diagram that you created in Prepare for integration.




### Configure CCAI Platform for outbound BYOC calls

This procedure is for outbound calls only. For inbound BYOC calls, fill out the BYOC questionnaire and submit it to Google in a support case.

To configure CCAI Platform for outbound BYOC calls, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings > Developer Settings**.

  2. Go to the **Bring Your Own Carrier** section.

  3. Click the toggle to the on position.

  4. Under **Country** , select the country where you want to operate.

  5. Enter the trunk SID, the origination target URI, or both, depending on your carrier. Get these values from your system administrator.

  6. Click **Save**. Add and assign phone numbers to appropriate resources.




### Configure your customer telephony infrastructure

Your system integrator (SI) configures your telephony infrastructure. Your SI can be your telephony team, a Google Cloud integration partner, or your telephony carrier.

Your SI should perform the following tasks:

  1. Configure your Session Border Controller (SBC) and firewall for BYOC integration. Google Cloud support can provide the information required for this task.

  2. Confirm that your SBC sends the SIP invitation to the correct FQDN, and not to the IP address of the BYOC SIP endpoint.

**Note:** Google provides a unique SIP FQDN for each CCaaS instance (development, UAT, or production).
  3. Test end-to-end call flows to verify that they're working correctly.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
