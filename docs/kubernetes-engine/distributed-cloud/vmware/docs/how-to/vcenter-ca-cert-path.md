---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-ca-cert-path/
title: Getting your vCenter CA root certificate \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:36.341559+00:00
---

# Getting your vCenter CA root certificate  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-ca-cert-path/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Getting your vCenter CA root certificate Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to get the root certificate for your vCenter server. This page is for IT administrators and Operators who manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

When a client, like Google Distributed Cloud, sends a request to your vCenter server, the server must prove its identity to the client by presenting a certificate or a certificate bundle. To verify the certificate or bundle, Google Distributed Cloud (software only) for VMware must have the root certificate in the chain of trust.

When you fill in an [admin workstation configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-workstation-configuration-file), you provide the path of the root certificate in the `vCenter.caCertPath` field.

Your VMware installation has a certificate authority (CA) that issues a certificate to your vCenter server. The root certificate in the chain of trust is a self-signed certificate created by VMware.

If you do not want to use the VMWare CA, which is the default, you can configure VMware to [use a different certificate authority](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-authentication/vsphere-security-certificates/certificate-management-overview/certificate-replacement-options.html).

If your vCenter server uses a certificate issued by the default VMware CA, download the certificate as follows:
    
    
    curl -k "https://[SERVER_ADDRESS]/certs/download.zip" > download.zip
    

Replace [SERVER_ADDRESS] with the address of your vCenter server.

Install the `unzip` command and unzip the certificate file:
    
    
    sudo apt-get install unzip
    unzip download.zip
    

If the unzip command doesn't work the first time, enter the command again.

Find the certificate file and a revocation file in `certs/lin`. For example:
    
    
    457a65e8.0
    457a65e8.r0
    

In the preceding example, `457a65e8.0` is the certificate file, and `457a65e8.r0` is the revocation file.

You can rename the certificate file to any name of your choice. The file extension can be `.pem`, but it doesn't have to be `.pem`.

For example, suppose you rename the certificate file to `vcenter-ca-cert.pem`.

View the contents of `vcenter-ca-cert.pem`:
    
    
    cat vcenter-ca-cert.pem
    

The output shows the base64-encoded certificate. For example:
    
    
    -----BEGIN CERTIFICATE-----
    MIIEGTCCAwGgAwIBAgIJAPW1akYrS5L6MA0GCSqGSIb3DQEBCwUAMIGXMQswCQYD
    VQQDDAJDQTEXMBUGCgmSJomT8ixkARkWB3ZzcGhlcmUxFTATBgoJkiaJk/IsZAEZ
    FgVsb2NhbDELMAkGA1UEBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExGTAXBgNV
    ...
    0AaWpaT9QCTS31tbBgBYB1W+IS4qeMK5dz5Tko5460GgbSNLuz5Ml+spW745RbGA
    76ePS+sXL0WYqZa1iyAb3x8E3xn5cVGtJlxXu4PkJa76OtdDjqWAlqkNvVZB
    -----END CERTIFICATE-----
    

View the decoded certificate:
    
    
    openssl x509 -in vcenter-ca-cert.pem -text -noout
    

The output shows the decoded certificate For example:
    
    
    Certificate:
        Data:
            Version: 3 (0x2)
            Serial Number:
                f5:b5:6a:46:2b:4b:92:fa
            Signature Algorithm: sha256WithRSAEncryption
            Issuer: CN = CA, DC = vsphere, DC = local, C = US, ST = California, O = uphc-vc01.anthos, OU = VMware Engineering
            Validity
                ...
            Subject: CN = CA, DC = vsphere, DC = local, C = US, ST = California, O = uphc-vc01.anthos, OU = VMware Engineering
            Subject Public Key Info:
                Public Key Algorithm: rsaEncryption
                    RSA Public-Key: (2048 bit)
                    Modulus:
                        00:e0:39:28:9d:c1:f5:ac:69:04:3f:b0:a0:31:9e:
                        89:0b:6e:f7:1e:2b:3b:94:ac:1c:47:f0:52:2e:fa:
                        6d:52:2c:de:66:3e:4e:40:6a:58:c7:cc:99:46:81:
                        ...
                        5c:d6:a9:ab:a9:87:26:0f:d2:ef:9e:a1:61:3d:38:
                        18:bf
                    Exponent: 65537 (0x10001)
            X509v3 extensions:
                ...
        Signature Algorithm: sha256WithRSAEncryption
             58:24:57:36:a4:66:fa:16:e1:82:b1:ee:a7:1a:77:db:77:6c:
             0a:b7:2e:7a:11:ca:0b:38:21:d2:d2:ab:3c:30:82:3f:ae:22:
             ...
             ad:26:5c:57:bb:83:e4:25:ae:fa:3a:d7:43:8e:a5:80:96:a9:
             0d:bd:56:41
    

Copy your certificate file to a location of your choice.

Then when you need to provide a value for `caCertPath` in a configuration file, enter the path of your certificate file.

For example, in your admin workstation configuration file:
    
    
    gcp:
      ...
    vCenter:
      ...
      caCertPath: "/path/to/vcenter-ca-cert.pem"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
