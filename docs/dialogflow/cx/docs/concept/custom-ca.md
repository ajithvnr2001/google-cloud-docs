---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/custom-ca/
title: Custom CA certificates \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:55.705831+00:00
---

# Custom CA certificates  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/custom-ca/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Custom CA certificates Stay organized with collections  Save and categorize content based on your preferences. 

Dialogflow CX webhooks require HTTPS endpoints that present valid TLS certificates when they are verified using Google's default trust store. However, you may want to use custom CA certificates, which cannot be signed by a certificate authority recognized by Google's default trust store. For example, webhook servers that are inside Google's private VPC network have this issue. In this case, you can upload the custom certificates to Dialogflow CX when creating webhooks, and the uploaded certificates will override Google's default trust store.

Custom CA certificates can be self-signed certificates or custom root certificates. You can upload multiple certificates in case you want to rotate the certificates. The certificates must be in [DER format](https://en.wikipedia.org/wiki/X.509#Certificate_filename_extensions) and must be signed with [subject alternative name](https://en.wikipedia.org/wiki/Subject_Alternative_Name) matching the webhook URL. When the [keyUsage](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3) extension is present, its value needs to be `digitalSignature`.

## Demo self-signed server

The following is the configuration of a demo server:

  1. Prepare self-signed certificate files. We use www.example.com as the example domain. 
         
         openssl genrsa -out server.key 2048
         openssl req -nodes -new -sha256 -newkey rsa:2048 -key server.key -subj "/CN=www.example.com" -out server.csr
         openssl x509 -req -days 3650 -sha256 -in server.csr -signkey server.key -out server.crt -extfile <(printf "\nsubjectAltName='DNS:www.example.com'")
         openssl x509 -in server.crt -out server.der -outform DER

  2. Start your HTTPS server using the server certificate (`server.crt`) and private key (`server.key`) created in previous step. We assume the server is listening on port 443.
  3. Test to connect to the server locally. 
         
         curl --cacert server.crt https://www.example.com --resolve www.example.com:443:127.0.0.1




## Demo webhook with custom certificate

After you have setup the server with your custom certificate, you may [create a webhook resource](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#create) with the following extra instructions to use the custom certificate:

  * Set the URL matching the domain signed with the certificate (`https://www.example.com` in previous demo). It is your own responsibility to make sure that your domain will correctly resolve to the IP address of the server.
  * Upload the custom certificate in DER format. This is the `server.der` file in previous self-signed demo or the custom root certificate.
  * For webhooks integrated with [Service Directory private network access](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#sd), Setup your [Service Directory Endpoint](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory#configure_an_endpoint) with the IP address and port of your server, and provide the [Service Directory Service](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory#configure_a_service) when creating webhook.



[ Previous arrow_back  Regionalization and location settings  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region)

[ Next Access Transparency  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/access-transparency)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
