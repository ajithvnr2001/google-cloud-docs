---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-ldaps/
title: Enable LDAPS \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:38:22.621998+00:00
---

# Enable LDAPS  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-ldaps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Enable LDAPS Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to enable LDAP over SSL/TLS (LDAPS) for Managed Service for Microsoft Active Directory (Managed Microsoft AD) to make your LDAP traffic confidential and secure. By default, the communication between Managed Microsoft AD and client applications is not encrypted for simple LDAP binds.

To enable LDAPS, you must have a certificate. This page also describes the specifications for the required certificate and how to verify and monitor it.

## Request a certificate

You can request a certificate from a Public Certificate Authority (CA), Enterprise CA, Google Cloud [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service/docs) or use a self-signed certificate. If you use a self-signed certificate, follow the Microsoft documentation linked to the PowerShell commands in the following sections.

You can create a self-signed certificate with the `New-SelfSignedCertificate` command on Windows, OpenSSL, or MakeCert.

### Certificate requirements

Your certificate must meet the following requirements:

  * The following table outlines the requirements for creating a self-signed certificate and lists the associated parameters used in the [`New-SelfSignedCertificate` command](https://learn.microsoft.com/en-us/powershell/module/pki/new-selfsignedcertificate). Note that the parameter or field names can vary based on how you create the certificate.

Parameter | Description  
---|---  
`Subject` (subject name) | It must be the wildcard-prefixed name of your Managed Microsoft AD domain to ensure that the service remains available during an upgrade or restore process. This is because domain controllers use random names that change during an upgrade or restore process. For example, if the domain name is `ad.mycompany.com`, the subject name must be `CN=*.ad.mycompany.com`  
`DnsName` (DNS name or subject alternative name) | It must include only the following:  

* Wildcard name of your Managed Microsoft AD domain
* Managed Microsoft AD domain name
For example, `"CN=*.ad.mycompany.com","CN=.ad.mycompany.com"`  
`KeySpec` | It must be set to `1`, which denotes that it can be used for both digital signature and key exchange.   
`KeyLength` | The minimum key size depends on the cryptographic algorithm.  

* **RSA:** At least 2048 bits
* **ECDSA:** At least 256 bits
* **ED25519:** 512 bits (Fixed length)  
`KeyUsage` | It must include "digital signatures" and "key encipherment".   
`TextExtension` or `EnhancedKeyUsageExtension` | It must have `OID=1.3.6.1.5.5.7.3.1` for server authentication.   
`NotBefore` | The time from which the certificate is valid. The certificate must be valid when enabling LDAPS.   
`NotAfter` | The time after which the certificate is not valid. The certificate must be valid when enabling LDAPS.   
`KeyAlgorithm` (signature algorithm) | Weak signature algorithms like SHA-1, MD2, MD5 are not supported.   
  
  * **Issuing chain:** The entire certificate chain must be uploaded and must be valid. The chain must be linear and cannot have multiple chains.

  * **Certificate format:** The format must meet Public-Key Cryptography Standards (PKCS) #12. You must use a PFX file.




### Request from a Public CA or Enterprise CA

To request a certificate from a Public CA or Enterprise CA, follow [these steps](https://docs.microsoft.com/en-us/troubleshoot/windows-server/identity/enable-ldap-over-ssl-3rd-certification-authority#create-the-certificate-request).

Accept the certificate on the same VM where the request is generated.

## Export the certificate in PKCS #12 format

To export the certificate in PKCS #12 format (as a PFX file), complete the following steps:

  1. In Windows, navigate to your certificates in the [Microsoft Management Console (MMC)](https://docs.microsoft.com/en-us/dotnet/framework/wcf/feature-details/how-to-view-certificates-with-the-mmc-snap-in#view-certificates-in-the-mmc-snap-in).

  2. Expand **Local Computer Certificates** , and navigate to **Personal > Certificates**.

  3. Right-click the certificate you created to enable LDAPS, and select **All Tasks > Export**.

  4. In the **Certificate Export Wizard** dialog that appears, click **Next**.

  5. On the **Export Private Key** page, select **Yes** to export the private key.

  6. On the **Export File Format** page, select **Personal Information Exchange - PKCS #12 (.PFX)** and **Include all certificates in the certification path if possible** checkbox. Click **Next**.

**Note:** If you are using Windows 10, version 1709 or later, we strongly recommend exporting the PFX chain with AES256-SHA256 encryption rather than TripleDES-SHA1.
  7. On the **Security** page, select the **Password** checkbox and enter a strong password to protect the certificate. Click **Next**. This password is required when configuring LDAPS on your Managed Microsoft AD domain.

  8. On the **File to Export** page, enter the destination name and path for the PFX file to export. Click **Next**.

  9. Click **Finish**.




To export a self-signed certificate with the private key in PKCS #12 format as a PFX file, use the [`Export-PfxCertificate` command](https://learn.microsoft.com/en-us/powershell/module/pki/export-pfxcertificate) and to export the self-signed certificate as a PEM file, use the [`Export-Certificate` command](https://learn.microsoft.com/en-us/powershell/module/pki/export-certificate).

## Distribute the issuer chain to client computers

For LDAPS to function, all client computers must trust the issuer of the LDAPS certificate. For a well-known Public CA, the client computers might already trust the issuer chain. If the chain is not trusted, complete the following steps to export the issuer chain:

  1. In Windows, navigate to your certificates in the [Microsoft Management Console (MMC)](https://docs.microsoft.com/en-us/dotnet/framework/wcf/feature-details/how-to-view-certificates-with-the-mmc-snap-in#view-certificates-in-the-mmc-snap-in).

  2. Expand **Local Computer Certificates** and navigate to **Personal > Certificates**. Double-click the LDAPS certificate.

  3. In the **Certificate** window, click **Certification Path** tab.

  4. On the **Certification Path** tab, select the root certificate in the path.

  5. Click **View Certificate**.

  6. Click **Details** tab, and then click **Copy to File...**

  7. In the **Certificate Export Wizard** dialog that appears, select **Base-64 encoded X.509** and click **Next**.

  8. Select the filename and location for the certificate chain, and click **Finish**.

  9. To copy the certificate to the client computer that establishes an LDAPS connection, use the **Certificate Import Wizard** dialog to import the certificate in the "Local Machine" store. Alternatively, you can distribute the certificate chain of issuing authorities to the [client computers using Group Policy](https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/deployment/distribute-certificates-to-client-computers-by-using-group-policy) in Windows.


**Note:** You can't add and manage these certificates using the Windows Certificate Manager tool or [Active Directory Certificate Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-cs/active-directory-certificate-services-overview) because the [delegated administrator account](https://docs.cloud.google.com/managed-microsoft-ad/docs/objects#delegated_administrator) doesn't have the `Domain Admins` and `Enterprise Admins` permissions.

To import a self-signed certificate into the trusted root store of the local machine, use the [`Import-Certificate` command](https://learn.microsoft.com/en-us/powershell/module/pki/import-certificate).

## Enable LDAPS on a Managed Microsoft AD domain

Before you enable LDAPS on your Managed Microsoft AD domain, do the following:

  1. Ensure that you have one of the following IAM roles:

     * Google Cloud Managed Identities Admin (`roles/managedidentities.admin`)
     * Google Cloud Managed Identities Domain Admin (`roles/managedidentities.domainAdmin`)

For more information about Managed Microsoft AD IAM roles, see [Access control](https://docs.cloud.google.com/managed-microsoft-ad/docs/access-control).




To enable LDAPS on your Managed Microsoft AD domain, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **Managed Microsoft AD** page.  
[Go to Managed Microsoft AD](https://console.cloud.google.com/security/cloud-ad)
  2. On the **Domains** page, select a domain from the list of instances to enable LDAPS.
  3. In the **LDAPS** section of the **Domain details** page, click **Configure LDAPS**.
  4. In the **Configure LDAPS** pane, enter the location of the PFX file and the password that you used to [export the certificate in PKCS #12 format](https://docs.cloud.google.com/managed-microsoft-ad/docs/how-to-use-ldaps#export-cert), and then click **Configure LDAPS**.



###  gcloud 

Run the following gcloud CLI command:
    
    
    gcloud active-directory domains update-ldaps-settings DOMAIN_NAME \
        --certificate-pfx-file=PFX_FILENAME \
        --certificate-password=PASSWORD
    

Replace the following:

  * DOMAIN_NAME: The [full resource name](https://docs.cloud.google.com/iam/docs/full-resource-names) of your Managed Microsoft AD domain. Full resource name format: `projects/PROJECT_ID/locations/global/domains/DOMAIN_NAME`.
  * PFX_FILENAME: The PKCS #12-formatted PFX file that specifies the certificate chain used to configure LDAPS.
  * PASSWORD: The password used to encrypt the PKCS #12 certificate. If you don't specify the password, it prompts for the password while running the command.



This operation can take up to 20 minutes to complete. To update the certificate, repeat these steps with the updated PFX file.

## Verify LDAPS

You can verify that LDAPS is enabled by performing an LDAPS bind. This process uses `LDP.exe`, which is one of the [RSAT tools](https://docs.cloud.google.com/managed-microsoft-ad/docs/manage-active-directory-objects#install-rsat) that you install when you join a VM to domain.

On a domain-joined Google Cloud Windows VM, complete the following steps in PowerShell:

  1. In PowerShell, start `LDP.exe` and navigate to **Connection > Connect**.

  2. In the **Connect** dialog, complete the following steps:

     1. In the **Server** field, enter your domain name.
     2. In the **Port** field, enter `636`.
     3. Select the **SSL** checkbox.
     4. Click **OK**.

If LDAPS is properly enabled, the connection succeeds.




## Monitor a certificate

You can view the Time to Live (TTL) for a certificate chain in Cloud Monitoring. The `cert_ttl` metric shows the number of valid days remaining for the certificate in the chain with the earliest expiration.

###  Console 

To view the metrics for a monitored resource by using the Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `LDAPS Certificate TTL` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select [**Microsoft Active Directory Domain**](https://docs.cloud.google.com/monitoring/api/resources#tag_microsoft_ad_domain).
     2. In the **Active metric categories** menu, select **Microsoft_ad**.
     3. In the **Active metrics** menu, select **LDAPS Certificate TTL**. 
     4. Click **Apply**.
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. To combine time series, use the menus on the [**Aggregation** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#select_display). For example, to display the CPU utilization for your VMs, based on their zone, set the first menu to **Mean** and the second menu to **zone**.

All time series are displayed when the first menu of the **Aggregation** element is set to **Unaggregated**. The default settings for the **Aggregation** element are determined by the metric type you selected.

  6. For quota and other metrics that report one sample per day, do the following: 
     1. In the **Display** pane, set the **Widget type** to **Stacked bar chart**.
     2. Set the time period to at least one week.



You can also click **Monitoring** in the **LDAPS** section of **Domain details** page to navigate to **Metrics Explorer**.

You can also [use the code editor for PromQL](https://docs.cloud.google.com/monitoring/promql/promql-in-monitoring) to find these metrics.

  1. On the **Metric** tab, select **Query Editor**.

  2. In the text field of the **Query Editor** , enter the following PromQL query and select **Run Query**.



    
    
    sum by (fqdn) (
      avg_over_time({
        "__name__"="managedidentities.googleapis.com/microsoft_ad/domain/ldaps/cert_ttl",
        "monitored_resource"="microsoft_ad_domain",
      }[${__interval}])
    )
    

## Disable LDAPS

To disable LDAPS, complete the following steps:

###  Console 

  1. In the Google Cloud console, go to the **Managed Microsoft AD** page.  
[Go to Managed Microsoft AD](https://console.cloud.google.com/security/cloud-ad)
  2. On the **Domains** page, select the domain from the list of instances for which you want to disable the certificate.
  3. In the **LDAPS** section of the **Domain details** page, click **Disable**.



###  gcloud 

Run the following gcloud CLI command:
    
    
    gcloud active-directory domains update-ldaps-settings DOMAIN_NAME \
        --clear-ldaps-certificate
    

Replace DOMAIN_NAME with the [full resource name](https://docs.cloud.google.com/iam/docs/full-resource-names) of your Managed Microsoft AD domain. Full resource name format: `projects/PROJECT_ID/locations/global/domains/DOMAIN_NAME`.

This operation can take up to 20 minutes to complete. To reenable LDAPS, you must reupload the certificates.

## What's next

  * [Best practices for automating certificate renewal](https://docs.cloud.google.com/managed-microsoft-ad/docs/automating-cert-updates)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
