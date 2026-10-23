---
url: https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/errors-grant-suspension/
title: Troubleshoot errors and grant suspension \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:15.477554+00:00
---

# Troubleshoot errors and grant suspension  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/errors-grant-suspension/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Troubleshoot errors and grant suspension Stay organized with collections  Save and categorize content based on your preferences. 

Use these instructions to troubleshoot issues with Citizens Broadband Radio Service Device (CBSD) errors and grant suspension.

To troubleshoot issues with interoperability testing between Spectrum Access System (SAS) and a [CBSD](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cbsd), see [Troubleshoot interoperability testing issues](https://docs.cloud.google.com/spectrum-access-system/docs/topics/iot-troubleshoot).

To troubleshoot issues when using the SAS Portal, see [Troubleshoot SAS issues](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).

## Review CBSD history

To troubleshoot errors when you register a CBSD or request new spectrum grants, you can review the CBSD history log and device activity. Reviewing the CBSD history log also helps you to investigate why a spectrum grant lost transmission authorization.

To view CBSD history, follow these steps:

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/welcome).
  2. Click **View deployments**.
  3. Optional: If you are an administrator for multiple organizations, select the organization that contains the device whose history you want to review.
  4. Select the device, and then click **Open**.
  5. On the right, click the **History** tab.
  6. Enter the date range in MM-DD-YYYY format or click date_range **Calendar**. The CBSD history displays automatically unless there is no history available in the specified timeframe.
  7. To view the history for a new event, click refresh **Refresh**.
  8. To download a CSV of the CBSD history, at the top of the grant activity log, click file_download **Download file**.



## Understand CBSD events

The Google SAS Portal shows a log of all activity within the last 30 days for each CBSD registered with SAS. CBSD history is available in a **Registered** , **Granted** , or **Authorized** state. Devices that are in a **Draft** , **Ready for CPI** , or **Pending Registration** state only have a CBSD history if the CBSD attempted to connect with SAS.

The SAS Portal records the following events for each CBSD.

Events | Description  
---|---  
**Registered** | The CBSD configuration successfully registered with SAS.  
**New grant issued** | A grant is created.  
**First heartbeat** | The CBSD completed its first successful heartbeat.  
**Unsuspended** | The grant was suspended on the last heartbeat, but is now authorized.  
**Suspended** | The grant wasn't suspended on the last heartbeat, but is now suspended.  
**Unsync op param** | The heartbeat response code sent to the CBSD was `UNSYNC_OP_PARAM`. For more information, see the SAS error code troubleshooting matrix.   
**Renewed** | The CBSD requested renewal of the grant.  
**Terminated** | SAS terminated the grant.  
**Relinquished** | The CBSD asked to relinquish the grant.  
**Auto-relinquished** | The CBSD requested de-registration or re-registration, which requires SAS to relinquish the grant.  
**Deregistered** | The CBSD asked to deregister its CBSD configuration from SAS and relinquish all of its grants.  
**Failed request** | An error occurred when processing the CBSD's request. This event contains a more specific error message. For more information, see [Error messages](https://docs.cloud.google.com/spectrum-access-system/docs/support/error-messages).  
  
## Error code 103 for a CBSD

If you receive an `Error code 103 Invalid field: installationParam` error when registering a CBSD with [Certified Professional Installer (CPI)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cpi)-signed parameters, include the `cpiSignatureData` field and take out the `installationParam` field in your registration request.

If both fields are included, the registration request is not approved. This happens even if the values in the `installationParam` field are the same as the values provided by the CPI.

## Resend (106) response code

SAS sends the `Resend (106)` response code for retryable errors. If the CBSD receives this response code, it resends the original request until it succeeds. We recommend an exponential backoff between requests.

A CBSD is most likely to see this response code when sending a grant request during [Coordinated Periodic Activities among SASs (CPAS)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cpas).

A Domain Proxy (DP) might see this response code when sending a batch request for more than 120 CBSDs. Only the first 120 entries are processed; subsequent devices in the batch receive a `Resend (106)` response code. However, there is no limit to the number of simultaneous batch requests that can be made to SAS.

**Important:** The `Resend (106)` response code is not included in the current [SAS-CBSD Protocol v1.2](https://winnf.memberclicks.net/assets/CBRS/WINNF-TS-0016.pdf).

## SAS error code troubleshooting matrix

The following matrix helps a CBSD operator to determine the root cause for each SAS response code returned to the CBSD or DP. It contains the following four columns:

  * **Response code.** The WInnForum SAS-CBSD protocol response code value and name returned by SAS.
  * **What it means.** A summary of the cause of the response code.
  * **Action required.** The actions needed to unblock the CBSD when you receive the corresponding response code.
  * **Support.** We recommend that you contact the support team listed for the error and then continue to the others in order.

Response code | What it means | Action required | Support  
---|---|---|---  
`100-VERSION` | SAS doesn't support the SAS-CBSD protocol version requested by the CBSD. For example, `https://sas.goog/v0.5/` instead of `https://sas.goog/v1.2/`. | Determine the protocol versions that SAS supports and set up the CBSD or DP to use a supported protocol version. In most CBSDs or DPs, change the SAS-CBSD base URL to determine the version. | For information about supported SAS-CBSD protocols, contact [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support). For instructions to change the device to use a different SAS URL or version, contact the CBSD or DP vendor.  
`101-BLACKLISTED` | This CBSD is not permitted to connect to SAS. | Contact [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support). | Contact [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support).  
`102-MISSING_PARAM` | The CBSD does not provide a required parameter to SAS. | Make sure that you entered all the required parameters in the CBSD or DP or into the SAS Portal. Your device vendor can tell you where to enter each parameter. Contact the CBSD vendor and then mention which request was unsuccessful. | For instructions to set any missing parameters or to identify why the CBSD or DP sent an incomplete request, contact the CBSD or DP vendor.  
`103-INVALID_VALUE` | The CBSD provided all required parameters, but at least one of those parameters has an invalid value. | View the response message and response data for a list of the invalid fields. Correct those fields and then attempt the request again. Some common causes for the `103-INVALID_VALUE` error are as follows:

  * `maxEirp` in the grant request is higher than the `eirpCapability` specified during registration.
  * The requested device height or power is not permitted by the CBSD category.
  * There's an unnecessary `installationParam` field in the device registration.

| For instructions to find the response message from SAS in the device logs, contact the CBSD or DP vendor. To make sure that the fields flagged by the response data have acceptable values, contact the CPI. Make sure that you account for unit conversions. For example, Effective Isotropic Radiated Power (EIRP) in the registration request is in dBm/10 MHz, while EIRP in every other message is in dBm/MHz. If you're unable to identify why the field listed in the response data is invalid, contact [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support).  
`104-CERT_ERROR` (Can occur as a standard HTTP `403` error) | There is an error with the certificate used to send a request to SAS. | Ask the device manufacturer to investigate. The device should use all [CBRS Root CA Certificates](https://cbrs.wirelessinnovation.org/cbrs-root-ca-operator) stored as roots of trust. The device must use a CBSD or DP type certificate that is:

  * Issued by a CBRS Root CA.
  * Not expired or revoked.
  * Sent with every request to SAS.
  * A **CBSD certificate only** , with a Federal Communications Commission (FCC) ID and serial number that matches the corresponding values in the registration request.

| To confirm that all required certificates are installed on the device and are not altered or revoked, contact the CBSD or DP vendor. To investigate why the certificates were rejected, after the vendor has confirmed that all certificates meet the specifications, contact [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support).  
`105-DEREGISTER` | SAS forcibly deregistered your device. Check the response message for an explanation. | Acquire the response message from the CBSD or DP. If the described reason is not clear, contact [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support). | For instructions to find the response message from SAS in the device logs, contact the CBSD or DP vendor. For information about the deregistration reason sent to the device, contact [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support).  
`106-RESEND` | SAS was temporarily unable to fulfill the request; see Resend 106 response code. | Resend the request. | If SAS is not in CPAS and continues to respond with this code after several attempts to resend the request, contact [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support).  
`200-REG_PENDING` | Some registration parameters are provided in the SAS Portal and others are provided by the CBSD or DP. However, at least one required parameter is still missing. A common cause of this error is a typo in one of the values when a device in the SAS Portal for multistep registration is created. | Make sure that the FCC ID and serial number on the device match the corresponding values in the SAS Portal. Make sure that there is no whitespace or characters that are similar—for example, uppercase (I) and lowercase (l). Make sure that all [required registration parameters](https://docs.cloud.google.com/spectrum-access-system/docs/portal#register-cbsd) that are not entered into the SAS Portal are included in the registration request sent by the CBSD or DP. | For instructions to have the CBSD send any parameters not entered into the SAS Portal, contact the CBSD or DP vendor. If you are unable to view or edit the device properties in the SAS Portal, contact your company SAS Portal Administrator. For a list of all the required registration parameters, review [SAS-CBSD Protocol Part 10.1.1](https://winnf.memberclicks.net/assets/CBRS/WINNF-TS-0016.pdf).  
`300-UNSUPPORTED_SPECTRUM` |  The CBSD requested a frequency range outside of the CBRS band less than 3550 MHz or greater than 3700 MHz. Check that the channel frequencies are expressed in the unit requested by your CBSD or DP vendor. | Request only spectrum in the CBRS band. | For instructions to set up the spectrum inquiry request parameters, contact the CBSD or DP vendor.  
`400-INTERFERENCE` | SAS cannot authorize transmission at any power for this device on this channel. This response code most often indicates that the device is deployed in an exclusion zone for the requested channel. | Attempt to reduce power or change the antenna azimuth. However, usually a grant request that returns this response code is not approved at any power. In that case, request a grant on a different channel. Check the response message for a description of the reason that the device might cause interference. | For instructions to find the grant response message and set up the grant request parameters, contact the CBSD or DP vendor. For more information about why the SAS reports interference, contact [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support).  
`401-GRANT_CONFLICT` | A single CBSD cannot have grants for overlapping frequency ranges from 3550 MHz to 3560 MHz and 3555 MHz to 3565 MHz. This code might occur when the CBSD power cycles or when you specifically request overlapping grants. Separately, a CBSD cannot hold grants with multiple SAS at the same time. | None, if overlapped frequencies caused the grant conflict. The device should be able to automatically recover. If it doesn't, contact the device vendor. If this device held any grants with another SAS during the last CPAS, it must relinquish all grants with that SAS. Then it must wait until the next CPAS to request a grant. | To identify why the device requests grants for overlapping frequencies, contact the CBSD or DP vendor.  
`500-TERMINATED_GRANT` | This grant is no longer authorized to transmit. A new grant with different operational parameters must be requested to receive new authorization to transmit. This response likely occurs for one of these reasons:

  * New incumbent or PAL activity
  * New grant parameters calculated after CPAS

| If the heartbeat response includes suggested operational parameters, the CBSD or DP should request a new grant with those parameters. If the heartbeat response does not include suggested operational parameters, request a new grant on a different channel. | For assistance if the CBSD or DP does not request a new grant by using the operational parameters provided by SAS, contact the CBSD or DP vendor. For more information, see [Why a grant is suspended](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/overview#grant-suspended) and [SAS sync](https://docs.cloud.google.com/spectrum-access-system/docs/sas-sync).  
`501-SUSPENDED_GRANT` | [Understand why a grant is suspended](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/overview#grant-suspended) and how to [operate CBSDs near the coast](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/overview#cbsd-near-coast). | 

  * **Interference Calculations Pending:** no action needed. Wait for the SAS to complete calculations. It typically takes only a few minutes.
  * **IAP Pending:** the grant cannot be authorized before CPAS. Do not relinquish the grant or re-register the device before CPAS. SAS suggests new operational parameters after CPAS.
  * **DPA Activation:** SAS must protect higher-priority users from interference if authorized to transmit. Do not relinquish the grant or re-register the device before CPAS because there's a chance the grant won't affect higher-priority users after CPAS. If the grant is still suspended after CPAS, request a new grant at lower power for a chance of authorization on this channel.
  * **By FCC Request:** the FCC requested that we suspend the grant. The FCC's request might be specific to a device or it might include a set of devices, possibly grouped by geography or frequency. The suspension might last any length of time.

| For assistance in identifying if a grant is held through CPAS, contact the CBSD or DP vendor. If interference calculations take longer than a few minutes, or if your device holds on to a grant through CPAS but is still suspended, contact [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support).  
`502-UNSYNC_OP_PARAM` | The CBSD improperly sent a heartbeat in the **Authorized** state in one of these scenarios:

  * Immediately after a grant was issued
  * Before a suspension was lifted
  * After too much time had passed since the last heartbeat request

In all cases, the heartbeat should have been in the **Granted** state, but the device reported **Authorized** instead. WInnForum requires that a CBSD automatically relinquishes the grant when you receive this error code. | Check network latency from your device to the SAS. If the CBSD requests or SAS responses experience high latency, it is possible that the CBSD and SAS can get out of sync. Contact the device manufacturer to understand why the device sent an **Authorized** heartbeat request instead of a **Granted** heartbeat request. | To verify network latency and identify its root cause, contact your network provider. For assistance in determining why the device sends **Authorized** heartbeat requests when they should be **Granted** , contact the CBSD or DP vendor. For assistance when network latency is potentially due to SAS, contact [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
