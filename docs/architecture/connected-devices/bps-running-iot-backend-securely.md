---
url: https://docs.cloud.google.com/architecture/connected-devices/bps-running-iot-backend-securely/
title: Best practices for running an IoT backend on Google Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:40.105329+00:00
---

# Best practices for running an IoT backend on Google Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/connected-devices/bps-running-iot-backend-securely/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Best practices for running an IoT backend on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-12-06 UTC

This document provides security best practices for managing and running an Internet of Things (IoT) backend on Google Cloud. In an IoT solution, an IoT backend connects edge devices to other resources. This document focuses on the following IoT backends: Message Queuing Telemetry Transport (MQTT) broker and the IoT platform.

This document is part of a series of documents that provide information about IoT architectures on Google Cloud and about migrating from IoT Core. The other documents in this series include the following:

  * [Connected device architectures on Google Cloud overview](https://docs.cloud.google.com/architecture/connected-devices)
  * [Standalone MQTT broker architecture on Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/mqtt-broker-architecture)
  * [IoT platform product architecture on Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/iot-platform-product-architecture)
  * Best practices for running an IoT backend on Google Cloud (this document)
  * [Device on Pub/Sub architecture to Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/device-pubsub-architecture)
  * [Best practices for automatically provisioning and configuring edge and bare metal systems and servers](https://docs.cloud.google.com/architecture/connected-devices/best-practices-provisioning-configuring-bare-metal)



This document provides best practices for provisioning and managing device credentials, authenticating and accessing control edge devices, and letting IoT edge devices access Google Cloud resources.

## IoT architecture

An IoT architecture includes services that let you provision and manage device credentials, authenticate and access control edge devices, and let edge devices access Google Cloud resources. This document discusses two IoT backend architectures: one using MQTT broker and the other using an IoT platform. The main security differences between these two backends are device identity and device management. IoT platforms provide these capabilities as part of their system, whereas MQTT brokers require you to provide these capabilities.

The following diagram describes the IoT architecture.

![IoT backend architecture.](https://docs.cloud.google.com/architecture/images/iot-security.svg)

The architecture shows the services that are required for the following three processes:

  1. Certificate provisioning, which is the process that you must complete to prepare an edge device for configuration.

  2. Authentication and authorization, which include the authentication scheme that the edge device and the MQTT broker or IoT platform use to authenticate with each other.

  3. Connections between edge devices and Google Cloud services, which are tasks that the edge device completes to connect to cloud resources and upload or download data.




This document focuses primarily on security best practices for provisioning and authentication.

The architecture uses a combination of the following services and features:

  * An edge device (such as a medical device) that you deploy at the [edges of your environment](https://www.lfedge.org/2020/08/18/breaking-down-the-edge-continuum/) and that is geographically close to the data that you want to process. The edge devices connect bi-directionally with your IoT backend, which means that they can send messages to and receive messages from the IoT backend.
  * An IoT backend that can be an MQTT broker or an IoT platform. 
    * An MQTT broker provides a secure interface for edge devices to connect using the [MQTT protocol](https://mqtt.org/mqtt-specification/). MQTT brokers lack capabilities for device identity and device management and rely on external systems to provide them.
    * An IoT platform is a cloud application that edge devices connect and communicate with. IoT platforms provide a secure interface for edge devices to connect using the MQTT protocol. Each IoT platform has its own security implementation that determines how it authenticates and authorizes edge devices and how it manages device identities.
  * A central certificate store that hosts the certificates for all edge devices.
  * Cloud resources that edge devices must access.



## Provisioning an edge device

Before an edge device can connect with your backend workloads, you must provision a certificate for the edge device. There are two main scenarios that decide how you provision the certificate:

  * If your solution is based on commercial, generic devices, you have full control over the provisioning process after purchasing the device.

  * If you use custom-built devices, the initial provisioning process happens during the manufacturing of the devices and you must integrate the provisioning process with your vendors and manufacturers.




In either scenario, you must create device certificates with a chain of trust that links to a root certificate authority (CA). These certificates authenticate the device identity and help ensure that updates and modifications done on the device are by trusted actors. Use a CA such as [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service) to complete the following tasks:

  * [Generate and store the root CA certificate](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-authorities#create-root-ca) in a secure manner.
  * [Generate and store subordinate CA certificates](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-authorities#subordinate-internal) for signing of your device certificates, if necessary.
  * [Request and sign device certificates.](https://docs.cloud.google.com/certificate-authority-service/docs/requesting-certificates)
  * Configure and distribute [permissions to subordinate CAs](https://docs.cloud.google.com/certificate-authority-service/docs/reference/permissions-and-roles) to your vendors and manufacturers, if necessary.
  * [Revoke device certificates](https://docs.cloud.google.com/certificate-authority-service/docs/revoking-certificates) when they aren't required any longer or you suspect the device has been compromised.



To provision a device certificate, you must complete the following tasks:

  * If your device has a hardware-based, tamper-proof security solution, such as a [secure element (SE)](https://encyclopedia.kaspersky.com/glossary/secure-element/) or a [hardware secure module (HSM)](https://en.wikipedia.org/wiki/Hardware_security_module) that stores the private keys locally and the private keys are never exposed externally, do the following:

    1. Generate the public-private key pair using the hardware-based security solution that's supported by your device.
    2. [Request a certificate](https://docs.cloud.google.com/certificate-authority-service/docs/requesting-certificates#use-csr) by using a [certificate signing request (CSR)](https://wikipedia.org/wiki/Certificate_signing_request).
  * If you aren't using a hardware-based security solution to generate a public-private key pair, use the CA to generate the keys and the certificate instead. For more information, see [Using an auto-generated key](https://docs.cloud.google.com/certificate-authority-service/docs/requesting-certificates#auto-generated-key). The certificate that you download by using this method is already signed.




After you generate and sign a device certificate, you then install the signed device certificate on the edge device and store the certificate in a central certificate repository, such as [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview).

For more information, see [How to deploy a secure and reliable public key infrastructure with Google Cloud CA Service (PDF)](https://services.google.com/fh/files/misc/deploying_public_key_infrastructure_with_cas.pdf).

For information about other provisioning best practices, see [Best practices for automatically provisioning and configuring edge and bare metal systems and servers](https://docs.cloud.google.com/architecture/best-practices-provisioning-configuring-bare-metal#provisioning_and_configuration_processes_best_practicesactices).

Three types of certificates are used to help secure an IoT solution:

  * The root CA certificate provides the root for the chain of trust of all the other certificates in your system. The backend workloads use the root certificate to validate the client certificates and the edge devices use the root certificate to validate the server certificate. You must distribute the root certificate to both the IoT backend and to the edge devices.

  * The intermediate CAs certificates provide a chain of trust that is rooted into the root CA. You can use intermediate CAs for provisioning, or for operational needs, such as granting access to intermediate CAs to manufacturers, or to implement flexible CA management processes.

  * The server certificates are used to secure the endpoints that are exposed by the IoT backend. You have server certificates for the different encryption algorithms that your endpoints need to support. Server certificates are linked to the root CA. A secret manager manages and stores both the private and public portions of the server certificates. You must configure your IoT backend with the server certificates and their corresponding private keys.

  * The client certificates are used to identify edge devices. Each edge device has at least one client certificate, which means that the number of certificates that you have increases with the number of edge devices in your environment. Client certificates are linked to the root CA. You must distribute client certificates to your edge devices and to the IoT backend.




### Process for generating a device certificate using an HSM or SE

The following diagram shows how a device certificate is provisioned when using an HSM or SE.

![Process for generating a device certificate.](https://docs.cloud.google.com/architecture/images/iot-provisioning-1.svg)

In this diagram, the following steps occur:

  1. The edge device generates the public key pair in the hardware.
  2. You download the public key and create the certificate signing request (CSR) for it.
  3. You send the CSR to the CA to request a certificate.
  4. The CA completes the following actions: 
     1. Signs the certificate.
     2. Returns the signed certificate to the provisioner.
  5. The provisioner completes the following actions: 
     1. Sends the signed certificate to the edge device.
     2. Stores the signed certificate in the central certificate store.
  6. The edge device stores the certificate in a secure location.



### Process for generating a device certificate using the CA

The following diagram shows how a device certificate is provisioned when using a CA.

![Process for generating a device certificate.](https://docs.cloud.google.com/architecture/images/iot-provisioning-2.svg)

In this diagram, the following steps occur:

  1. The provisioner requests that the CA send a signed certificate for the device.
  2. The CA completes the following actions: 
     1. Generates a public-private key pair and signs the public key.
     2. Returns the device certificate and the private key to the provisioner.
  3. The provisioner completes the following actions: 
     1. Sends the certificate and private key to the edge device.
     2. Stores the certificate and private key in the central certificate store.
  4. The edge device stores the certificate and the private key in a secure location.



If you want to store the private key in a single place (the device), you should avoid storing the private key in the central secret store. However, if you store the private key outside the central secret store and you lose access to the private key, the device has to go through the provisioning process again.

### Authenticate devices before signing certificates

The process to generate a device certificate (either on the device, or by using a CA) requires that the device and the CA communicate and authenticate one another.

Without proper authentication, your CA might mistakenly trust a malicious device. For example, an attacker with knowledge about how to reach the certificate signing infrastructure of your CA might deploy a malicious device that asks your CA to sign a certificate. If you don't have device authentication in place, your CA might sign the certificate that the malicious device presents. If your CA does sign the certificate, the malicious device can then communicate with your backend as a trusted device.

To help you prevent malicious devices from communicating with your CA, we recommend that you take the following actions:

  * Implement an authentication mechanism for devices that aren't yet trusted.
  * Establish the authenticity of any device requesting authentication.
  * Establish device authenticity before a device asks the CA to generate a new certificate or sign an existing certificate.



Implementing an authentication mechanism at this point of the provisioning process is challenging. You cannot rely on device certificates to authenticate devices because the device doesn't yet have a signed certificate from the CA. This lack of a signed certificate can occur for the following reasons:

  * The device didn't yet generate a certificate.
  * The device didn't yet send a CSR to the CA.
  * The CA didn't yet send the signed certificate back to the device.



One way to solve this problem is to extend your device provisioning process to do the following for each device that you want to authenticate or need to authenticate:

  1. Generate a provisioning certificate that you use only to authenticate the device against the certificate signing infrastructure.
  2. Sign the provisioning certificate with your CA.
  3. Store the signed provisioning certificate in the SE or HSM on the device.
  4. Store the signed provisioning certificate in your Google Cloud backend.



Before the device is granted access to the certificate signing infrastructure of your CA, the device has to present the provisioning certificate. It has to present the certificate so that you can verify its integrity and authenticity, and determine whether the certificate matches one of the provisioning certificates stored in your Google Cloud backend. If the verification is successful, the device can access the certificate signing infrastructure of your CA and the certificate provisioning process can continue.

There are differences between a provisioning certificate and a fully-trusted certificate. A provisioning certificate only grants access to a minimal amount of services and infrastructure. Creating a provisioning certificate lets the CA verify that the device is genuine before considering it fully trusted and issuing a fully-trusted certificate.

An extension to this process is that you can use subordinate CAs that device manufacturers have access to, together with your CA, to sign provisioning certificates. For example, a manufacturer might sign the provisioning certificates of a device after it completes the manufacturing process for that device. You can then verify these signatures to help you validate that the device is genuine.

If a device is compromised before it's provisioned, we recommend that you remove the corresponding provisioning certificate from your Google Cloud backend, so that the device can't initiate the process to obtain a fully-trusted certificate because it won't be able to authenticate against your CA.

## Best practices for device identity

This section describes the best practices for device identities.

### Use an identity provider with MQTT brokers

MQTT brokers authenticate edge devices by using device credentials provided by [plugins](https://www.hivemq.com/docs/hivemq/3.4/plugins/authentication-and-permissions.html#client-authentication), [databases](https://docs.vernemq.com/configuring-vernemq/db-auth), and [files](https://mosquitto.org/documentation/authentication-methods/). To manage your device identities in a systematic and scalable manner, use an [identity provider (IdP)](https://wikipedia.org/wiki/Identity_provider). The IdP manages the identities and credentials for all devices and acts as the primary source of truth for device identities.

To keep the device identity updated in the MQTT broker, implement a system-specific integration layer. For more information about managing device credentials, see Provisioning an edge device.

### Use the digital identities of the IoT platform as the source of truth

The IoT platform has security features that manage the device identities and device credentials, and authenticate and authorize devices trying to access the platform. These security features help ensure that only authorized devices are allowed to access the IoT platform and help ensure data integrity.

Verify that the device identities managed by the IoT platform represent the primary source of truth of all the devices the IoT platform manages. Other components in an IoT solution that need device identity information should rely on the security system of the IoT platform. The IoT platform grants access rights to devices and propagates any security changes throughout the IoT solution.

## Best practices for network connectivity

Securing network connectivity is important for the following reasons:

  * Secure networks help ensure that a device connects to the right backend. For example, a secure network can prevent [DNS spoofing](https://wikipedia.org/wiki/DNS_spoofing), which is an attack that tries to divert devices to connect to a rogue backend that is controlled by attackers.
  * Secure networks help ensure third parties can't read your data traffic. For example, a secure network can prevent an [attacker-in-the-middle attack](https://wikipedia.org/wiki/Man-in-the-middle_attack), where attackers read the traffic between your device and the backend.



Use [Transport Layer Security (TLS)](https://wikipedia.org/wiki/Transport_Layer_Security) to protect network communication between your edge devices and backend workloads.

Extend TLS with [mTLS](https://wikipedia.org/wiki/Mutual_authentication#mTLS) to implement a mutual authentication scheme that enables both connecting parties to establish the identity of each other.

For instructions on using TLS, see [Standalone MQTT broker architecture on Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/mqtt-broker-architecture) and [IoT platform product architecture on Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/iot-platform-product-architecture).

## Best practices for certificate management for MQTT brokers

This section describes best practices for managing certificates when using MQTT brokers.

### Store certificates centrally

Store and manage server certificates and device certificates in a central location. Specifically, ensure that you have the following controls in place:

  * An inventory of all your devices and their certificates and the server endpoints and their certificates.
  * Additional information about the certificates such as their validity.
  * The ability to add and remove certificates for devices so that devices can connect using new certificates.
  * Access rights to your central certificate store, to limit what the different roles in your backend can do with the certificates.



Use a secret storage and management solution such as Secret Manager or HashiCorp Vault. Secret Manager lets you version, update, and invalidate device credentials, and to [manage access policies](https://docs.cloud.google.com/secret-manager/docs/access-control) to your credentials.

For an IoT platform, implement access to the credentials using [Secret Manager API access](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api).

### Protect certificates on edge devices

To store certificates and keys on the edge devices, use a local [trusted execution environment](https://wikipedia.org/wiki/Trusted_execution_environment) or certificate store to protect the credential and block unauthorized accesses. If you need to store secret material on your devices, encrypt that material using techniques such as [flash encryption](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/flash-encryption.html), and store it on tamper-proof elements to help prevent unauthorized data extraction.

### Synchronize the central certificate store with the MQTT broker certificate store

MQTT brokers must access client certificates for certificate-based authentication, so you must synchronize the certificate stores of MQTT brokers with the central certificate store. Verify that changes on the central certificate store, such as add, update, and delete certificates, are synchronized with the MQTT broker certificate store. MQTT brokers use certificate stores such as MySQL, PostgresDB, and Java Key Store. Depending on which certificate store your MQTT broker uses, ensure that the following processes exist:

  * A process that monitors for changes in the central certificate store and notifies the synchronization process.
  * A process that takes changes in the central certificate store and synchronizes the changes in the central certificate store with the certificate store used by the MQTT broker.



When you use Secret Manager as your certificate store, you can use [event notifications](https://docs.cloud.google.com/secret-manager/docs/event-notifications) as the monitoring process. You can implement the synchronization process as a listener of the event notifications.

### Distribute certificates to edge devices securely

When using MQTT brokers, distribute the root certificate and client certificates to your edge devices. When you distribute certificates, you must secure your communication channels so that the traffic doesn't get intercepted.

The main communication channels for certificate distribution are the following:

  * A direct path from the IoT backend to the edge devices over existing communication channels.
  * An indirect path in which edge devices request and download the certificates.



During certificate distribution, you require the following components:

  * A _certificate store_ where certificates are centrally managed.
  * A _distribution coordinator_ which sends the certificates and tracks the distribution process for each edge device.
  * An _update handler_ on the edge device that receives or downloads the certificates and stores them on the device.



Distribute certificates during the provisioning processes for edge devices, and when you need to rotate certificates.

During the provisioning process, ensure that the provisioner has direct access to edge devices over encrypted channels such as [SSH](https://wikipedia.org/wiki/Secure_Shell) and uses tools such as [SCP](https://wikipedia.org/wiki/Secure_copy_protocol). Because the devices are not in operation, you can push certificates directly to the edge devices.

When rotating certificates, use the MQTT broker as the communication channel between the distribution coordinator and the edge devices. Use other channels to download certificates onto the device. To minimize disruption of the edge devices in operation, use an indirect certificate distribution path. The process would consist of the following logical steps:

  1. The distribution coordinator acquires access credentials from the certificate store.
  2. The distribution coordinator pushes the certificate access credentials to the edge devices together with additional information, such as the download URL.
  3. The on-device update handler receives the access credentials and temporarily stores the information and acknowledges receipt back.
  4. The update handler coordinates the certificate download when the device is not active. The update handler uses the access credentials to download certificates from the credential store.
  5. After the certificates are downloaded, the update handler continues with the certificate rotation process which is described in the certificate rotation section.



When you use Secret Manager as the central certificate store, you can generate [short-lived access tokens](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#authenticating) to grant and restrict access to certificates. For more information, see Distribute access tokens to devices securely.

To help prevent the certificates from being exposed during transit, encrypt the connection between your edge devices and the MQTT broker. For more information, see Best practices for network connectivity.

### Rotate certificates automatically

To limit the damage an exposed certificate can cause, generate certificates with a finite valid period and rotate the certificates before they expire. For large-scale IoT deployments, implement an automatic certificate rotation procedure to consistently update your devices with new certificates before the old ones expire. Deployed devices without valid certificates means that the devices can stop functioning, which can be costly to fix and negatively affect the overall functionality of your IoT solution.

Your edge devices must connect bi-directionally with your MQTT broker to ensure that they can send messages to the MQTT broker and that they can receive messages from the MQTT broker.

During certificate rotation, you require the following components:

  * A monitoring process that recurrently scans through your certificate inventory and looks for certificates that are about to expire. The monitoring process triggers certificate rotation for expiring certificates.
  * A rotation process that initializes and oversees certificate rotation.
  * A device certificate rotation handler on the edge device that communicates with the MQTT broker and executes certificate rotation steps on the device.



To rotate certificates, the IoT solution completes the following steps:

  1. The rotation process sends an initialization message to the edge device to start certificate rotation.
  2. The device certificate rotation handler acknowledges the initialization message by sending a response back to the rotation job.
  3. The rotation process requests a new certificate from the CA. This request is similar to the certificate provisioning request, except that the keys and CSR are sent as MQTT broker messages.
  4. After receiving the new certificate from the CA, the rotation job distributes the certificate to the central certificate store and to the edge device. It also synchronizes the certificate to the certificate store of the MQTT broker.
  5. The device certificate rotation handler stores the new certificate and initializes a new connection with the MQTT broker using the new certificate.
  6. After the new connection is established, the device certificate rotation handler sends a completed message to the MQTT broker.
  7. After receiving the completed message, the rotation process invalidates the old certificate in the central certificate store.



To help protect the certificates that are being sent during the rotation process, use dedicated MQTT topics for certificate rotation. Limit access to these topics to only the rotation job and the edge device.

To help protect the certificate rotation process from runtime failures, enable persistence for the changes and progress.

For more information about rotating secrets using Secret Manager, see [Rotation of secrets](https://docs.cloud.google.com/secret-manager/docs/rotation-recommendations).

## Best practices for certificate management for IoT platforms

If you're using an IoT platform, use the certificate update and distribution mechanisms provided by the platform. For backup purposes, you can regularly export the credentials from your IoT platform to a secondary secret storage, such as Secret Manager.

## Best practices for authentication with an MQTT broker

During the mutual authentication process, backend workloads verify the identity of edge devices, and edge devices verify the identity of backend workloads. After the backend workloads confirm the identity of the edge device, the backend workloads authorize the device access to resources.

The following sections provide best practices for authentication methods when using MQTT brokers.

**Note:** Most commercial IoT platform applications support their own set of authentication schemes.

### Choose the authentication method for MQTT brokers

Different IoT backends support different authentication methods. The commonly used methods are the following:

  * **Username and password authentication** , where the edge device presents its username and password to verify its identity.
  * **Token-based authentication** , where encrypted security tokens are used to verify the edge device's identity.
  * **Customized authentication schemes** , where you implement a custom mechanism to verify the identity of the edge device.



As part of the [MQTT standard](http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html#_Toc398718116), MQTT brokers support username and password authentication as the default for [`MQTT CONNECT`](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901033) packets.

The `MQTT CONNECT` packet also contains a [`Client Identifier`](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901058) field that you can use to uniquely identify the client to the MQTT broker. Edge devices send the `MQTT CONNECT` packet to the MQTT broker when they establish a connection.

Besides the username, password, and client identifier fields in the `MQTT CONNECT` packet, MQTT 5.0 supports [enhanced authentication](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901256) that lets you build [challenge-response](https://wikipedia.org/wiki/Challenge%E2%80%93response_authentication) authentication flows. MQTT 5.0 allows for multiple [`AUTH`](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901217) packet exchanges between the edge device and the MQTT broker.

### Use password stores with username and password authentication

For username and password authentication, configure the MQTT broker to use a password store. The password store provides a centralized location for managing passwords for all the edge devices that connect to the MQTT broker. By default, the username, password, and client identifier fields are optional in the MQTT specification. Therefore, design your authentication mechanism to verify that the username, password, and client identifier fields are present in the `MQTT CONNECT` packet.

Ensure that the passwords are encrypted at rest and in transit, as follows:

  * At rest, store a cryptographically strong hash of the password that cannot be reversed. For more information about hashing passwords, see [Account authentication and password management best practices](https://cloud.google.com/blog/products/identity-security/account-authentication-and-password-management-best-practices).

  * In transit, encrypt the connection between your edge devices and the MQTT broker. For more information, see Best practices for network connectivity.




### Consider token-based authentication

With token-based authentication, edge devices send a token to the MQTT broker to authenticate. Devices can generate the token themselves or get the token from other authentication services. Compared to passwords, tokens are short-lived: tokens are only valid for a period with an explicit expiration date. Always check for expiration when validating tokens.

[JSON Web Tokens (JWT)](https://wikipedia.org/wiki/JSON_Web_Token) are a way to implement token-based authentication. Edge devices can generate the JWT and authenticate with the MQTT broker. The JWT is embedded into the MQTT CONNECT packet as the password field.

The advantages of JWT are the following:

  * JWT gives you choices on the encryption algorithm used for signing of the token. JWT works well with constrained edge devices, where you can use a less resource-intensive encryption algorithm such as ECC for signing of the token.
  * Using public key cryptography, the private key is used only on the edge device and never shared with other parties. A private key helps make this method more secure than username and password authentication, where the credentials are sent over the connection and requires encryption of the data.



### Consider custom authentication schemes

Some MQTT brokers support different authentication mechanisms and protocols. For example, if your MQTT broker supports customized authentication schemes, you can configure it to support the following:

  * **Industry-standard authentication protocols** such as [OpenID Connect](https://openid.net/connect/), [Security Assertion Markup Language (SAML)](https://wikipedia.org/wiki/Security_Assertion_Markup_Language), [LDAP](https://wikipedia.org/wiki/Lightweight_Directory_Access_Protocol), [Kerberos](https://wikipedia.org/wiki/Kerberos_\(protocol\)), and [Simple Authentication and Security Layer (SASL)](https://wikipedia.org/wiki/Simple_Authentication_and_Security_Layer). These protocols delegate device authentication to your existing identity providers. Some MQTT brokers support enhanced authentication and extensible authentication mechanisms that you can use to extend the MQTT broker to support new protocols and identity providers.
  * **Certificate-based mutual authentication**. Some MQTT brokers support a mutual authentication scheme, such as mTLS-based authentication.



## Best practices for device access control and authorization

Because of the publisher and subscriber communication pattern of the MQTT protocol, device access control is defined using MQTT topics. MQTT topics control how a device can communicate with your IoT backend. Each IoT backend has different implementations for access control and authorization, so refer to your IoT backend documentation for options on how to set up MQTT topics.

### Use single-purpose service accounts to access Google Cloud resources

[Access to Google Cloud resources](https://docs.cloud.google.com/iam/docs/manage-access-other-resources) are managed by IAM allow policies that bind the resource access allowance with a set of principals. Typical principals are user accounts, service accounts, and groups. [Service accounts](https://docs.cloud.google.com/iam/docs/service-accounts#what_are_service_accounts) are typically used by an application or compute workload to make authorized API calls for cloud resources. Service accounts let IoT edge devices access cloud resources.

Because the device identity is managed by the IoT backend, you must map an identity between the IoT backend and IAM so that the edge device can access Google Cloud resources.

If you're managing a large set of devices, the [limit](https://docs.cloud.google.com/iam/quotas#quotas) on the number of service accounts for each Google Cloud project makes it infeasible to have direct one-to-one mapping between device and service account.

Instead, create service accounts that are linked to the cloud resources that your IoT solution needs to access, as described in [creating single-purpose service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#single-purpose). For example, create a unique service account for each of the following use cases:

  * Downloading software update packages
  * Uploading large media files
  * Ingesting data from a latency stream



To implement [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege), ensure that each service account only has sufficient access rights to support its use case. For example, for a service account that is used to download software packages, only grant read access to the Cloud Storage bucket.

### Distribute access tokens to devices securely

Usually, your edge devices communicate with your IoT platform using MQTT. However, for specific use cases, your devices might require direct access to Google Cloud resources. For example, consider the following:

  * To download content, an edge device requires read-only access to a Cloud Storage bucket during the download process only.
  * To upload data to a Cloud Storage bucket, an edge device requires write access to the bucket.



For these use cases, use [workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation), where access to Google Cloud resources is granted through [access tokens](https://docs.cloud.google.com/docs/authentication/token-types#access-tokens). Workload identity federation eliminates the need of provisioning any cloud-specific credentials on the edge devices and access distribution is done dynamically based on demand.

To distribute access tokens for cloud resources to your devices, configure workload identity federation between your device identity provider and Google Cloud. To support workload identity federation, ensure that your IoT backend meets the [workload identity federation requirements](https://docs.cloud.google.com/iam/docs/use-workload-identity-federation-to-let-customers-access-their-cloud-resources#requirements) and follows the [security best practices](https://docs.cloud.google.com/iam/docs/use-workload-identity-federation-to-let-customers-access-their-cloud-resources#best_practices) that match your use cases.

To access Google Cloud resources using workload identity federation, your edge devices must implement the [OAuth 2.0 Token Exchange](https://tools.ietf.org/html/rfc8693) workflow, which involves the following steps:

  * The device calls the [Security Token Service](https://docs.cloud.google.com/iam/docs/reference/sts/rest) and provides its own device credentials.
  * The Security Token Service verifies the identity of the edge device by validating the credentials that the edge device provided with the device identity provider.
  * If the identity verification is successful, the Security Token Service returns an access token back to the edge device.
  * The edge device uses that token to impersonate the single-purpose service account and obtains a [short-lived OAuth 2.0 access token](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials#sa-credentials-oauth).
  * The device uses the short-lived OAuth 2.0 access token to authenticate with Google Cloud APIs and get access to the required cloud resources.



To restrict the access of the short-lived access token to specific buckets and objects in Cloud Storage, use [Credential Access Boundaries](https://docs.cloud.google.com/iam/docs/downscoping-short-lived-credentials#how-it-works). Credential Access Boundaries lets you limit the access of the short-lived credential and minimize the number of resources that are exposed in your Cloud Storage buckets when an access token gets compromised.

Workload identity federation is a scalable way of securely distributing cloud access to edge devices. For more information about authentication, see [Authentication at Google](https://docs.cloud.google.com/docs/authentication).

### Monitor and audit access to cloud resources

Enable Cloud Audit Logs to create log entries when your edge devices access cloud resources through authenticated API requests. Cloud Audit Logs lets you monitor critical actions that are done by your edge devices on Google Cloud. In addition, Cloud Audit Logs creates the audit traces and logs that you need to investigate any issues. For more information, see [Impersonating a service account to access Google Cloud](https://docs.cloud.google.com/iam/docs/audit-logging/examples-service-accounts#auth-as-service-account).

## What's next

  * Learn more about a [Technical overview of Internet of Things](https://docs.cloud.google.com/architecture/iot-overview).
  * Read the remaining documents in the series:

    * [Standalone MQTT broker architecture on Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/mqtt-broker-architecture)

    * [IoT platform product architecture on Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/iot-platform-product-architecture)

  * Learn more [best practices for working with service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts)




## Contributors

Authors: 

  * Charlie Wang | Cloud Solutions Architect
  * [Marco Ferrari](https://www.linkedin.com/in/ferrarimark) | Cloud Solutions Architect



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-12-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-12-06 UTC."],[],[]] 
