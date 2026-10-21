---
url: https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/overview/
title: Citizens Broadband Radio Service Device overview \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:29.389487+00:00
---

# Citizens Broadband Radio Service Device overview  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Citizens Broadband Radio Service Device overview Stay organized with collections  Save and categorize content based on your preferences. 

A _[Citizens Broadband Radio Service Device (CBSD)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cbsd)_ is a transmitter device that operates in the [Citizens Broadband Radio Service (CBRS)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cbrs) spectrum, such as an Evolved NodeB (eNodeB).

The primary function of Spectrum Access System (SAS) is to control spectrum access for a CBSD. A CBSD transmits only _after_ it has received authorization from SAS. This control ensures the protection of higher-priority CBRS users by controlling the operating parameters such as channels or transmission power of lower-priority CBRS devices.

A CBSD initiates all the required communications with SAS by using standard protocols defined by WInnForum. SAS then issues short-term spectrum leases to these CBSDs, abstracting the complexity of facilitating coexistence among many disparate systems that compete for shared spectrum resources.

## How the CBSD knows what spectrum is available

To learn which spectrum is available at its location, a registered CBSD sends a spectrum inquiry request to SAS.

SAS responds with detailed information about which frequencies are available for the CBSD to use and additional information that is useful to the CBSD when it's selecting a frequency range to transmit on.

The term _channel_ is frequently used to describe a 10-MHz segment of the CBRS band. A channel is marked as unavailable to the CBSD if SAS is unable to authorize any transmissions on that channel at the CBSD's location. For example, SAS is not allowed to authorize transmissions inside of exclusion zones. Otherwise, SAS indicates that the channel is available for use.

If the spectrum inquiry request is incomplete, SAS rejects the request. Examples of incomplete requests include requests that have an invalid frequency range or an invalid CBSD ID.

**Note:** To meet operational security requirements from the U.S. Department of Defense (DoD), SAS does not indicate which channels are currently affected by naval operations.

## CBSD registration and deregistration

Before a new CBSD can transmit, it needs to register with SAS. To register, the CBSD sends a request to SAS containing information about its installation parameters such as the owner, location, and transmit characteristics. SAS responds with a registration response.

If SAS approves the registration request, SAS responds with a CBSD ID. If SAS rejects the registration request, it responds with an error message. The CBSD needs to correct the error and send another registration request.

### Register a CBSD that needs CPI validation

CBSDs that don't require [Certified Professional Installer (CPI)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cpi) validation can send a registration request directly to SAS. However, most CBSDs require CPI validation. There are two types of CBSD categories, **Category A CBSD** and **All Category B CBSD**.

Category A CBSDs that meet at least one of the following conditions require a CPI validation:

  * The CBSD does not automatically determine its location.
  * The CBSD operates outdoors with an antenna height above average terrain (HAAT) of more than six meters. This type of CBSD must be registered as a Category B device.



To register a CBSD that needs CPI validation, there are two options:

  * **Single-step registration.** The CPI provides the installation parameters of the CBSD signed with their own CPI certificate to the CBSD. Then, the CBSD sends a registration request to SAS that includes the signed installation parameters in the `cpiSignatureData` field.

  * **Multistep registration.** The CPI uses the Google SAS Portal (or another user interface that's integrated with the [Google SAS Portal API](https://docs.cloud.google.com/spectrum-access-system/docs/overview-api)) to send the installation parameters to SAS. For more information about CPI-provided parameters, see section 10.1 of the [WInnForum SAS to CBSD Technical Specification](https://winnf.memberclicks.net/assets/CBRS/WINNF-TS-0016.pdf). The CBSD then sends a registration request to SAS without installation parameters. SAS combines the information from the SAS Portal and the CBSD to process the registration request.


**Important:** To register the CBSD, do not include the `installationParam` field in the registration request, even if the information matches exactly with the information that the CPI provides.

If the CPI uses a combination of single and multistep registration procedures, it's important to know which information SAS uses. The following table shows information about the CBSD configuration of `cpiSignatureData` sent by the CBSD.

CBSD data | CPI-signed CBSD configuration exists in the SAS Portal | No CPI-signed CBSD configuration exists in the SAS Portal  
---|---|---  
`cpiSignatureData` sent by CBSD | `cpiSignatureData` information is used | `cpiSignatureData` information is used  
No `cpiSignatureData` sent by CBSD | CBSD configuration in the SAS Portal is used | Registration fails  
  
The data from two different sources is not merged. Whichever source is being used must be completed, or the registration fails.

For more information about CBSD registration and deregistration, see [Register and deregister a CBSD](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/register-deregister).

## DPA move lists when you re-request grants

To reduce the risk of suspension because of [Dynamic Protection Area (DPA)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#dpa) activation, SAS can request a new grant with parameters similar to those of a recently relinquished grant. The grant reservations must be claimed on the same day that they are created. As a result, the following steps must be completed before the next [Coordinated Periodic Activities among SASs (CPAS)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cpas).

To claim a grant reservation, follow these steps:

  1. Get the frequency range and [Effective Isotropic Radiated Power (EIRP)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#eirp) of your CBSD's current grant. 
     1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas).
     2. To select the CBSD, do one of the following: 
        * In _map_ **Map view** , click the CBSD location marker.
        * In _table_chart_ **Table view** , click the row of the CBSD.
     3. On the right, click the **Status** tab and find the frequency range and EIRP in the **Active grants** section.
  2. Claim a reservation.

     1. Relinquish your CBSD's grant or re-register the CBSD with the same installation parameters. SAS automatically creates a grant reservation for the frequency range and power.
     2. Request new grants, according to the following requirements:

        * **Frequency range:** New grants must be for the same frequency range, or for any valid 5-MHz subset of that frequency range. You can request multiple new grants on frequencies that do not overlap within the previous frequency range. New grants that contain any frequencies outside the range from step 1, even if there's partial overlap, cannot claim the reservation.

        * **EIRP:** All new grants within the reserved frequency range must use equal or lower EIRP than the grant.

**Tip:** When a reservation is claimed, the new grants are on the same move lists as the previous grant.



A CBSD loses all grant reservations and can't claim previous grant reservations if the following occurs:

  * A deregistration request is sent.
  * A registration request is sent with different parameters than it previously used to register.
  * CPAS occurs before the CBSD requests new grants for the previously granted frequencies.



## Operate CBSDs near the coast

Most high-priority users operate continuously at a well-known location. However, naval radar operations can happen at different places and times.

To maximize the amount of spectrum available for commercial use, SAS uses specialized sensors ([Environmental Sensing Capability (ESC)](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#esc) devices) to detect when and where the navy is using the band. When they use the band, SAS must adjust the operation of the CBSDs under its control to ensure that they do not disrupt the navy's operations.

When SAS learns that [incumbent](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#incubment) activity has been detected in a DPA, it activates protections for that DPA. When a DPA is activated, all grants that cause too much interference to navy operations are suspended.

SAS uses a DPA move list to keep track of which grants must be suspended during incumbent activity. As the following table shows, the grant only needs to be suspended if it's on the move list and incumbent activity is detected.

| Grant is on the move list | Grant is not on the move list  
---|---|---  
**DPA is active** | Suspended | Not suspended  
**DPA is not active** | Not suspended | Not suspended  
  
### When a grant is added to a move list

Every night SAS recalculates which grants must be suspended during incumbent activity and updates the DPA move lists.

This is done by ranking grants on the corresponding channel according to the interference they cause to the DPA. SAS removes the low-interference grants from the move list but adds the high-interference grants to the move list. This means that a grant's membership on the move list is determined by both its own characteristics and the characteristics of other nearby grants.

As per [WInnForum](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#winforum) rules, all new grants inside a DPA's neighborhood must be added to the move list on the first day of the grant. This means that if the DPA is active or activates at any time on the first day, the grant is suspended regardless of where it's located within the DPA neighborhood. The size of each DPA neighborhood is based on data provided by the [National Telecommunications and Information Administration (NTIA)](https://www.ntia.gov/spectrum-frequency-bands/3550-3650-mhz).

There are 6 DPA neighborhoods:

  * Category A Indoor ≤ 6 meters
  * Category A Indoor > 6 meters 
  * Category A Outdoor ≤ 6 meters
  * Category A Outdoor > 6 meters
  * Category B ≤ 6 meters
  * Category B > 6 meters



To check if a device falls within a DPA neighborhood, see [DPA neighborhood borders](https://docs.cloud.google.com/spectrum-access-system/docs/cbrs-availability#dpa-neighborhood) or [download a map of DPAs](https://www.ntia.gov/files/ntia/publications/e-dpas.kml).

## Operate CBSDs in the NRQZ

You can use the Google SAS Portal to register and operate devices in the [National Radio Quiet Zone (NRQZ)](https://greenbankobservatory.org/about/national-radio-quiet-zone/). If a device is located within the NRQZ, coordination with the NRQZ office must be confirmed before registration and operation.

**Important:** Google reserves the right to revoke the registration and deny SAS services to any devices that are not compliant with NRQZ coordination requirements.

### Sign a CBSD configuration in the NRQZ (CPI only)

**Important:** Single-step registration of devices in the NRQZ isn't supported.

To sign the CBSD configuration of a device located in the NRQZ, a CPI is prompted to confirm successful coordination and enter the [NRQZ Case ID](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#nrqz) furnished by the NRQZ office. You must be a CPI to edit the NRQZ Case ID and confirm successful coordination. For more information, contact the [NRQZ office](mailto:%20nrqz@gb.nrao.edu).

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas).
  2. Select a CBSD located in the NRQZ.
  3. Click _settings_ **CBSD configuration settings** and do one of the following: 
     * In _map_ **Map view** , click the CBSD location marker.
     * In _table_chart_ **Table view** , click the row of the CBSD.
  4. Review the configuration to make sure that all the required fields are complete and correct.
  5. To verify that the device has been successfully coordinated with the NRQZ office and will be installed and operated in accordance with the parameters of the coordination, select the **Confirm coordination** option.
  6. Enter the **NRQZ Case ID**.
  7. Click **Sign**.



## Understand why a grant is suspended

The heartbeat response from SAS provides information about why a grant is suspended. To view the heartbeat response, see the `responseMessage` and `responseData` fields when the `responseCode` is equal to `501`. The following table describes the heartbeat parameters with their values.

Parameter | Values | Description  
---|---|---  
NAME: `responseCode` DATA TYPE: number | `501` |   
NAME: `responseData` DATA TYPE: array |  **Interference Calculations Pending** **IAP Pending** | The grant is suspended because it is in the move list of a [DPA](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#dpa) that is activated by an [FCC](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#fcc) request.   
NAME: `responseMessage` DATA TYPE: string | **Suspended_Grant: Interference Calculations Pending** | The grant is suspended while SAS calculates how much interference the new grant might cause to protected entities. Calculations might take up to a few minutes. After SAS completes the calculations, it waits for the next heartbeat request from the CBSD to provide a final response as **Authorized** or **Suspended_Grant: IAP Pending**.  
**Suspended_Grant: IAP Pending** | SAS completes the initial interference calculations and doesn't have enough interference budget to authorize a grant. SAS includes this grant in its [CPAS](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms#cpas) calculations and offers new operating parameters (which can be authorized) after CPAS completes.   
**Suspended_Grant** | The grant is suspended because it is in the move list of a DPA that has been activated. A DPA activation can cause a grant to be suspended.  
**Suspended_Grant: By FCC Request** | The FCC requests to suspend the grant. The FCC's request might be specific to a device, or it might include a set of devices, possibly grouped by geography or frequency. The suspension might last any length of time.  
  
Following are some examples of heartbeat parameters.

  * **Example 1:** `responseMessage = "SUSPENDED_GRANT: Interference Calculations Pending" responseData = ["Interference Calculations Pending"]`

The grant is suspended while SAS is calculating the interference impact of a new grant. If the interference impact is within the SAS interference budget for the day, it authorizes the grant. The CBSD might heartbeat every few seconds to get updates from SAS more quickly.

  * **Example 2:** `responseMessage = "SUSPENDED_GRANT: IAP Pending" responseData = ["IAP Pending"]`

The interference calculations have completed, but SAS does not have enough interference budget available to authorize transmission with the grant. After CPAS, the CBSD should expect to see the grant terminated and a lower power suggested. The CBSD is expected to request a grant with the suggested operation parameters from the terminating heartbeat response.

  * **Example 3:** `responseMessage = "SUSPENDED_GRANT: IAP Pending, The grant is suspended because it is in the move list of a DPA that has been activated."`

`responseData = ["IAP Pending", "The grant is suspended because it is in the move list of a DPA that has been activated."]`

SAS provided this response because the grant is suspended while waiting for IAP, and the grant is on the move list of an activated DPA.

  * **Example 4:** `responseMessage = "SUSPENDED_GRANT: Interference Calculations Pending, The grant is suspended because it is in the move list of a DPA that has been activated."`

`responseData = ["Interference Calculations Pending", "The grant is suspended because it is in the move list of a DPA that has been activated."]`

SAS is still calculating the interference resulting from this new grant, and the grant is on the move list of an activated DPA. Even after the interference calculations are complete, the grant remains suspended until the DPA is deactivated or the grant is removed from the DPA move list, which happens after CPAS and never happens outside of CPAS.




## CBSD statuses and states

The following table shows the different statuses of a CBSD.

Status | Description  
---|---  
error_outline **Unregistered** | The CBSD has not yet registered with SAS or has deregistered.  
access_time **Registered** | The CBSD is registered with SAS but doesn't have any grants.  
check_circle_outline **Authorized** | The CBSD is authorized to transmit on at least one grant.  
access_time **Granted** | The CBSD received at least one grant but isn't currently heartbeating on any grants.  
pause_circle **Suspended** | The CBSD can't transmit on any of its grants. All grants are temporarily suspended by SAS.  
  
If the SAS Portal shows the device state as **stale** , it means that the CBSD was previously **Authorized** , **Granted** , or **Suspended**. To get the latest status, refresh the device state after the CBSD resumes heartbeating.

Following are the different states of the CBSD:

  * **Authorized (stale):** The CBSD was authorized, but the transmit expiration time has passed since SAS last received a heartbeat from the CBSD. The status is updated when the CBSD resumes heartbeating.
  * **Granted (stale):** The CBSD was granted, but the grant expiration time has passed without SAS having received a heartbeat from the CBSD. The status is updated when the CBSD begins heartbeating.
  * **Suspended (stale):** The CBSD was suspended, but the transmit expiration time has passed since SAS last received a heartbeat from the CBSD. The status is updated when the CBSD resumes heartbeating.



## What's next

  * Learn about [Spectrum Access System](https://docs.cloud.google.com/spectrum-access-system/docs/overview).
  * Learn about [key SAS terms](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms).
  * [Troubleshoot SAS issues](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
