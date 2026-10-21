---
url: https://docs.cloud.google.com/spectrum-access-system/docs/iot-troubleshoot/
title: Troubleshoot interoperability testing \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:43.573924+00:00
---

# Troubleshoot interoperability testing  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/iot-troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Troubleshoot interoperability testing Stay organized with collections  Save and categorize content based on your preferences. 

Use these instructions to troubleshoot issues with interoperability testing between Spectrum Access System (SAS) and a Citizens Broadband Radio Service Device (CBSD).

To troubleshoot issues with the Google SAS Portal, see [Troubleshoot SAS issues](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).

## Certificate issues when testing

You might see the following certificate issues when you test the interoperability between SAS and a CBSD:

  * **SSL certificate problem when connecting with the provided CBSD or Domain Proxy (DP) certificate.**

Make sure that you have the Google Testing Certificate Authority (CA) listed as a root of trust in your device. If that's not the case, send an email to [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support) to get a copy.

  * **A`please-use-sni.invalid` error in the SAS certificate.**

A device connecting to the SAS Portal without Server Name Indication (SNI) sees a server certificate for the domain name `please-use- sni.invalid`. Proper implementation of Transport Layer Security (TLS) requires that the CBSD advertises the target hostname, such as `www.google-sas.com`, through the [TLS SNI extension](https://https.cio.gov/sni/).

  * **Modify the test certificates provided by Google before using SAS.**

You do not need to modify the test certificates because SAS verifies that a client sends the entire certificate chain. This chain is formed through the file concatenation of the CBSD's leaf certificate file and the corresponding intermediate CA file. The certificates that you receive from Google for testing purposes have the full chain already included.

  * **Include the intermediate CA file when testing SAS.**

Although SAS verifies that a client sends the entire certificate chain, no extra work is required when testing with Google SAS. This is because the certificates that you receive from Google for testing purposes have the full chain already included.

  * **Problems when trying to connect to the SAS Portal.**

To bypass checking the SAS certificate, use the `k` flag with the `curl` command, as follows: 
        
        curl -v -k -H "Host: www.google-sas.com" -H "content-type: application/json" -
        -cert /path/to/cert/file.cert --key /path/to/key/file.key -X POST
        https://www.google-sas.com/vendor/v1.2/registration --data
        @/path/to/example/registration_req.json
        

**Important:** Use the `-k` flag only for testing purposes because it's not secure.

If the connection is established:

    * Verify that you have the Google testing CA listed as a root of trust.
    * Make sure that you use Server Name Indication (SNI).

If no connection is established, then there might be a network issue that prevents your request from going through. If you see an HTTP status code `403` error, there is a problem with the certificates that the device provides to the SAS.

  * **Get CBSD or DP certificates for use with the test SAS environment.**

Google provides testing certificates as part of your onboarding process. These certificates contain everything that you need to get started. The test SAS environment also accepts official certificates issued by [WInnForum-approved CBRS CA operators](https://cbrs.wirelessinnovation.org/cbrs-root-ca-operators).

  * **Get CBSD or DP certificates for use with SAS.**

SAS supports CBSD and DP certificates from any of the WInnForum-approved CA operators. If you're connecting to a test instance, you need testing certificates.




## CBSD certificate errors when testing with SAS

You might see the following errors when you are testing with SAS:

  * **SSL certificate problem.**

You receive an SSL certificate error when you try to connect to `https://test.sas.goog` from your CBSD or DP. Make sure that you have the testing CA provided by Google SAS Support listed as a root of trust in your CBSD or DP. If you don't already have it, contact [SAS Support](https://docs.cloud.google.com/spectrum-access-%20system/docs/getting-support) to get a copy.

  * **Debug SAS certificate issues.**

**Important:** Use the `-k` flag only for testing purposes because it's not secure.

To bypass inspection of the SAS certificate in the SAS test environment, use the `-k` flag with the `curl` command as follows: 
        
        curl -v -k -H "Host: test.sas.goog" -H "content-type: application/json" --cert
        /path/to/cert/file.cert --key /path/to/key/file.key -X POST
        https://test.sas.goog/v1.2/registration --data
        @/path/to/example/registration_req.json
        

If the connection is established, verify that the Google testing CA is listed as a root of trust.

If no connection is established, then there is a network issue that prevents your request from going through. If you get an HTTP status code `403` error, then there is a problem with the CBSD or DP certificate that the device provides to SAS.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
