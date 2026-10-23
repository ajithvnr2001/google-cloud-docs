---
url: https://docs.cloud.google.com/architecture/limiting-compliance-scope-pci-environments-google-cloud/
title: Limiting scope of compliance for PCI environments in Google Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:03.504925+00:00
---

# Limiting scope of compliance for PCI environments in Google Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/limiting-compliance-scope-pci-environments-google-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Limiting scope of compliance for PCI environments in Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-03-12 UTC

This document describes best practices for architecting your cloud environment for [Payment Card Industry (PCI) Security Standards Council](https://www.pcisecuritystandards.org/) compliance. These best practices are useful for organizations that are migrating or designing systems in the cloud that are subject to PCI compliance requirements. This document refers to the [PCI DSS 4.0 requirements](https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Standard/PCI-DSS-v4_0.pdf) where applicable.

## Understanding the PCI DSS assessment scope

If your organization engages in commerce over the internet, you need to support and maintain PCI compliance. The way that you design and manage your cloud environment affects how your systems are scoped for your [PCI Data Security Standard (DSS)](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard) assessment. Scoping has important implications for the security of your IT assets and your ability to support and maintain PCI compliance. To ensure that your PCI environment is scoped properly, you need to understand how your business processes and design decisions impact scope.

### What is scope?

All systems that store, process, or transmit cardholder data (CHD) are in scope for your PCI DSS assessment. Security is important for your entire cloud environment, but the compromise of in-scope systems can cause a data breach and exposure of CHD.

![What is within assessment scope compared to what is outside of assessment scope.](https://docs.cloud.google.com/static/architecture/images/limiting-compliance-scope-pci-environments-google-cloud-scope-definition.svg)Figure 1. Diagram of PCI DSS scope definition.

In figure 1, the cardholder data environment (CDE), connected-to systems, and security-impacting systems are inside the assessment scope boundary, while untrusted and out-of-scope systems are outside the assessment scope boundary.

According to PCI DSS, in-scope systems are _trusted_. In-scope systems include your CDE and any system that is connected to, or could impact, the security of your CDE.

A system is _connected-to_ if it's on the same network, shares databases or file storage, or otherwise has access or connectivity to any system or process that resides within the CDE, but doesn't have direct access to CHD.

A system is _security-impacting_ if it can, if compromised, allow an attacker to gain access to the CDE. All connected-to and security-impacting systems are always in scope.

Out-of-scope systems are _untrusted_ by definition in PCI DSS, and have zero value to an attacker who wants to gain access to CHD or sensitive authentication data (SAD). A system is out of scope if it can't have impact on the security of an in-scope system, even if the out-of-scope system is compromised. While out-of-scope systems aren't assessed directly, the [PCI Qualified Security Assessor (QSA)](https://www.pcisecuritystandards.org/assessors_and_solutions/qualified_security_assessors) verifies that your scoping is accurate and protects CHD according to PCI DSS. It's therefore important that your scope boundaries are strongly protected, continuously and thoroughly monitored, and clearly documented.

### Connections in the PCI context

Several PCI DSS requirements reference _connections_ but the PCI DSS [doesn't explicitly define connections](https://www.pcisecuritystandards.org/pci_security/glossary#C). You can interpret the meaning of connections in this context by understanding the scoping decision tree in the [PCI SSC Guidance for PCI DSS scoping and network segmentation (PDF)](https://www.pcisecuritystandards.org/documents/Guidance-PCI-DSS-Scoping-and-Segmentation_v1_1.pdf).

For purposes of evaluating your PCI scope, a connection is defined by the following:

  * An active information transport connecting two computers or systems
  * Which of the two parties initiates the call



When you document your environment, it's best to clearly indicate which party is authorized to initiate a connection. A firewall that is configured to only allow traffic in one direction can enforce a one-way connection. For example, an in-scope payment processing application can make queries to an out-of-scope database server without the out-of-scope server coming into scope if all of the following are true:

  * The connection and out-of-scope database don't store, process, or transmit CHD or SAD.
  * The database is on a separate network or is otherwise segmented from the CDE.
  * The database cannot initiate any calls into the CDE directly or indirectly.
  * The database doesn't provide security services to the CDE.
  * The database doesn't impact configuration or security of the CDE.
  * The database supports PCI DSS requirements.



The following diagram shows the factors that determine system scope:

![The decision making process that's used to determine scope.](https://docs.cloud.google.com/static/architecture/images/limiting-compliance-scope-pci-environments-google-cloud-scope-flowchart.svg)Figure 2. Flowchart for determining system scope.

In figure 2, system scope is determined as follows:

  * System components that are in scope for PCI DSS:

    * Systems that are in the CDE for which _one of_ the following is true: 
      * A system component stores, processes, or transmits CHD or SAD.
      * A system component is on the same network segment—for example in the same subnet or VLAN—as systems that store, process, or transmit CHD.
    * Systems that are connected-to or security-impacting systems for which _one of_ the following is true: 
      * A system component directly connects to CDE.
      * A system component impacts configuration or security of the CDE.
      * A system component segments CDE systems from out-of-scope systems and networks.
      * A system component indirectly connects to CDE.
      * A system component provides security services to the CDE.
      * A system component supports PCI DSS requirements.
  * System components can be considered untrusted and out of scope for PCI DSS when _all_ of the following are true:

    * A system component doesn't store, process, or transmit CHD or SAD.
    * A system component isn't the same network segment—for example in the same subnet or VLAN—as systems that store, process, or transmit CHD or SAD.
    * A system component can't connect to any system in the CDE.
    * A system component doesn't meet any criteria for connected-to or security-impacting systems.

Out-of-scope systems can include systems that connect to a connected-to or security-impacting system component, where controls are in place to prevent the out-of-scope system from gaining access to the CDE by using the in-scope system component.




In practical terms, the PCI DSS definition of system scope can mean that your web application's session store and ecommerce database might qualify as out-of-scope if segmentation is properly implemented and documented. The following diagram shows how read and write connections work between in-scope systems and out-of-scope systems:

![Identifies which connections between in-scope and out-of-scopes systems are read only, write only, or read and write.](https://docs.cloud.google.com/static/architecture/images/limiting-compliance-scope-pci-environments-google-cloud-app-capability.svg)Figure 3. In-scope applications that are capable of calling out-of-scope services and applications.

Figure 3 shows the following connections:

  * Read-only: 
    * An in-scope payment processing application reads a cart ID from an out-of-scope cart database and reads data from a DNS and NTP.
  * Write-only: 
    * An in-scope payment processing application writes to an out-of-scope application main database and to Cloud Logging.
    * The out-of-scope main web application writes data to a logging service. This data doesn't include CHD or SAD.
  * Read and write: 
    * A user on the public web reads and writes request metadata as follows: 
      * The user reads and writes to an in-scope payment processing application. This request metadata is the cart ID and cart authentication key that contain CHD and SAD.
      * The user reads and writes to the out-of-scope main web application. This request metadata is a session ID that doesn't contain CHD or SAD.
    * The out-of-scope main web application reads and writes data to an out-of-scope cart database, session store, and application main database. This data doesn't include CHD or SAD.
    * An in-scope payment processing application reads and writes data to an in-scope card tokenization service and to a credit card processor on the public web. This data includes CHD and SAD.



The architecture in figure 3 describes two discrete web applications: the main web application (main application), which is out of scope for PCI, and the payment processing application (checkout application), which is in scope. In this architecture, a connection can be initiated between two entities only in the directions described by the preceding list. Connections between entities can be read-only, read and write, or write-only from the caller's perspective. Any path or request direction that isn't explicitly described is blocked by segmentation. For example, the payment processing application can read from the cart database, and write to the logging service, which involves initiating a connection to those entities.

In-scope systems commonly call out-of-scope systems and services. These connections remain secure because segmentation prevents any remote caller (other than a cardholder) from initiating a connection into the CDE directly or indirectly. Figure 3 shows that the only ingress path to the checkout application is from the user.

In figure 3, no out-of-scope service or application provides any configuration or security data to the payment processing application. Data flows through the architecture as follows:

  1. The main application forwards the user to the checkout application and uses an HTTP `POST` to transmit the `CartID` and a validator called the `CartAuthKey`. The `CartAuthKey` is a hash of the `CartID` and a pre-shared secret known only to the main and checkout applications.
  2. The checkout application validates the user by hashing the `CartID` along with the secret and comparing that value to the `CartAuthKey`.
  3. After the user data is authenticated, the `CartID` is used to read the cart contents from the cart database. All cardholder data is sent from the user directly to the checkout application.
  4. If payment profiles are used, the cardholder data is stored in the tokenization service.
  5. After the payment is processed, the result is inserted into the main application's database with a write-only database service account.



### Scoping considerations

In the Guidance for PCI DSS scoping and network segmentation, the PCI Security Standards Council (SSC) recommends that you assume that everything is in-scope until verified otherwise. This SSC recommendation doesn't mean that you should make your scope as broad as possible. Rather, it means that the QSA assesses all systems as if they are trusted unless you can show that a system has no connectivity to, or security impact on your CDE. To meet regulatory compliance requirements and keep your IT assets safe, you should scope your environment in alignment with the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege) by trusting as few systems as possible.

Before your assessment, evaluate your environment to understand and document the boundary between your in-scope and out-of-scope systems. The QSA's first task is to confirm that your documented scope reasonably encapsulates the CDE and connected systems. As part of the overall assessment, the QSA then verifies that out-of-scope systems can't negatively affect any in-scope systems.

Make sure that you understand any special circumstances that are specific to your environment, such as the following:

  * If you collect cardholder data over the telephone or through a VOIP system, consider the additional scoping issues described in [Protecting telephone-based payment card data (PDF)](https://www.pcisecuritystandards.org/documents/Protecting_Telephone_Based_Payment_Card_Data_v3-0_nov_2018.pdf).
  * [If your service provider requires access to your CDE (PDF)](https://www.pcisecuritystandards.org/documents/PCI-SSC-Connected-to-Service-Providers-Guidance.pdf) in order to operate a point-of-sale system, then the system that your service provider uses might be regarded as a connected-to system. This might require additional scoping and due diligence considerations.



[Google's security best practices](https://docs.cloud.google.com/architecture/framework/security/compliance) can help you to establish and demonstrate a clear and defensible boundary between in-scope and untrusted systems which will assist in your assessment. When you manage access and security by [practicing the principle of least privilege](https://cloud.google.com/blog/products/identity-security/dont-get-pwned-practicing-the-principle-of-least-privilege), you help minimize the number of exposure points for cardholder data, minimize the attack surface of your CDE, and consequently reduce your scope. When you reduce the footprint of in-scope systems, you help reduce system complexity and streamline your PCI DSS assessment.

### Risks of incorrect scoping

An overly-broad scope can lead to costly assessments and increased compliance risks. To help keep a narrow scope, trust as few systems as possible and grant access to only a select few designated users. Through diligent evaluation and self-assessment, you can identify systems that shouldn't be in scope for PCI DSS, verify that they meet the guidelines for out-of-scope systems, and reduce scope accordingly. This process of elimination is the safest way to discover which systems are untrusted, and help ensure that they cannot impact the in-scope systems.

If you require a large infrastructure footprint to meet PCI DSS requirements, you can cause extraneous systems to be included in your assessment scope. When you include extraneous systems in your scope, it poses risks to your ability to attain compliance. It can also degrade your overall security posture by broadening the attack surface of your trusted in-scope environment.

A core principle of network security and PCI DSS is to assume that some or all of your network has already been compromised. This principle is enshrined in Google's [zero trust security model](https://cloud.google.com/beyondcorp), which rejects perimeter-only security in favor of a model wherein each system is responsible for securing itself. Google's security model is in alignment with PCI DSS, which recommends that the CDE and its connected systems are deployed in a small, trusted space that's segmented from your broader IT environment and not intermingled with it.

Within your in-scope PCI environment, don't place your CDE in a large, trusted space with a wide perimeter. Doing so can create a false sense of security and undermine a holistic defense-in-depth strategy. If an attacker breaches perimeter security, they can operate with ease inside a trusted, private intranet. Consider ways that you can tighten the trusted space to contain only what it needs to operate and secure itself, and avoid relying solely on perimeter security. By understanding and following these principles, you can design your cloud environment to help secure your critical systems and reduce risk of contamination from compromised systems.

A large, in-scope environment of trusted systems requires a similarly large management apparatus to maintain continuous monitoring, maintenance, auditing, and inventory of these systems. The complexity of the system architecture, change management processes, and access control policies can create security and compliance risks. Difficulty in maintaining these monitoring processes can lead to difficulties in meeting PCI DSS requirements [10](https://www.pcisecuritystandards.org/faq/articles/Frequently_Asked_Question/What-is-the-intent-of-PCI-DSS-requirement-10/) and [11](https://www.pcisecuritystandards.org/faq/articles/Frequently_Asked_Question/I-have-had-an-external-vulnerability-scan-completed-by-an-ASV-does-this-mean-I-am-PCI-DSS-compliant/). It's important to understand these risks, and implement strategies to limit the scope of your assessed environment. For more information, see Support continuous compliance later in this document.

### Google Cloud services in scope for PCI DSS

Before you start reducing the scope of your PCI environment, understand [which Google Cloud services are in-scope for PCI DSS](https://cloud.google.com/security/compliance/pci-dss/). These services provide infrastructure upon which you can build your own service or application that stores, processes, or transmits cardholder data.

## Strategies for reducing scope

This section discusses the following strategies for reducing assessment scope: resource hierarchy controls, [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls) segmentation, and tokenization. Rather than picking one approach, consider employing all of these strategies in order to maximize your potential scope reduction.

There isn't a universal solution for PCI scoping. You might have existing segmentation in place in an on-premises network, or a card processing solution that can cause your infrastructure design to look somewhat different than described here. Use these strategies as principles that you can apply to your own environment.

### Establish resource hierarchy controls

Google Cloud resources are organized hierarchically as follows:

  * The [Organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) resource is the root node in the Google Cloud resource hierarchy. Organization resources contain folder and project resources. [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) access control policies applied to the Organization resource apply throughout the hierarchy on all resources in the organization.
  * [Folders](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#folders) can contain projects and other folders, and control access to their resources using folder-level IAM permissions. Folders are commonly used to group similar projects.
  * [Projects](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects) are a trust boundary for all of your resources and is an IAM enforcement point.



To help reduce your assessment scope, follow Google's best practices for [defining your resource hierarchy](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy). The following image shows an example resource hierarchy for PCI compliance:

![Example resource hierarchy that shows how to group PCI-related resources to be within assessment scope.](https://docs.cloud.google.com/static/architecture/images/limiting-compliance-scope-pci-environments-google-cloud-resource-hierarchy.svg)Figure 4. An example resource hierarchy for PCI compliance.

In figure 4, all projects that are in PCI scope are grouped within a single folder to isolate at the folder level. The PCI-scoped folder contains the CDE and another project that contains shared services. When you implement a similar resource hierarchy, the PCI scoped folder forms a logical root of your PCI compliance scope. By ensuring that only designated users have access to this folder and its projects, you can exclude other folders, projects, and resources in your hierarchy from your assessment scope.

When you grant users access to only the folders and projects they require on an as-needed basis, you ensure that only designated users have access to your in-scope components. This supports [PCI DSS requirements 7.2 and 7.3 (PDF)](https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Supporting%20Document/PCI_DSS-QRG-v4_0.pdf), and others. To make sure that permissions for the parent Organization and folders are set appropriately, understand the [implications of policy inheritance](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control). To support [PCI DSS requirement 8.4.1](https://www.pcisecuritystandards.org/faq/articles/Frequently_Asked_Question/In-what-circumstances-is-multi-factor-authentication-required/), make sure to implement [2-Step verification](https://knowledge.workspace.google.com/admin/security/protect-your-business-with-2-step-verification) for designated users, and see the [PCI DSS supplement on guidance for multi-factor authentication (PDF)](https://www.pcisecuritystandards.org/pdfs/Multi-Factor-Authentication-Guidance-v1.pdf). In order to enforce compliance in your resource hierarchy, make sure that you understand how to set [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints). These constraints support continuous compliance and can help protect your trusted environments from privilege escalation.

As with all PCI compliance, adequate logging and monitoring of your environment and its scoped components are required to establish a clear scope boundary. The resource hierarchy is inextricably linked with identity and access management, and effective [logging, auditing, and monitoring of user actions](https://docs.cloud.google.com/logging/docs/audit) is necessary to enforce and maintain separation.

### Implement network segmentation

Network segmentation is an important architecture pattern to help secure your CDE and connected systems, as described by the PCI SSC supplemental [guide on network segmentation (PDF)](https://www.pcisecuritystandards.org/documents/Guidance-PCI-DSS-Scoping-and-Segmentation_v1.pdf). When implemented properly, network segmentation narrows your assessment scope by removing network routes that untrusted systems might use to access your CDE or its connected components. Define only the [routes](https://docs.cloud.google.com/vpc/docs/using-routes) needed to allow communication between trusted components. When untrusted systems don't have a route by which to send or receive packets from trusted systems, the untrusted systems are out-of-scope and can't impact the security of your in-scope components.

To implement network segmentation, place your CDE in a dedicated [Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc) with [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls) enabled. Create this VPC in [custom mode](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network) to ensure that no extraneous subnets or routes are created that might enable default access to trusted networks. Implement [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) to make sure that this VPC cannot be shared with other projects, and can only be peered with other trusted networks.

The following diagram shows how your network segmentation strategy relates closely to your resource hierarchy. This diagram assumes a resource hierarchy with a single folder for your in-scope PCI environment, and two projects in that folder for the CDE and shared services.

![CDE shown in a dedicated VPC with a network connection to the shared services project.](https://docs.cloud.google.com/static/architecture/images/limiting-compliance-scope-pci-environments-google-cloud-network-segmentation.svg)Figure 5. Resource hierarchy that uses network segmentation for PCI compliance.

In figure 5, the shared services project isn't part of the CDE, but it is a _connected-to_ system and therefore it is in-scope for PCI. Access into the CDE is restricted at the network level by the load balancer and [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) or [firewall policies](https://docs.cloud.google.com/firewall/docs/network-firewall-policies) to protect these networks and meet [PCI DSS requirements 1.2 and 1.3](https://www.pcisecuritystandards.org/faq/articles/Frequently_Asked_Question/What-is-meant-by-adequate-network-segmentation-in-the-PCI-DSS/). The tokenization system and payment system are placed in separate subnets, and their communication is governed by firewall rules between each subnet to allow only necessary communications. The necessary logging, monitoring, and alerting functions that satisfy [PCI DSS Requirements 10.2, 10.4, and 10.5](https://www.pcisecuritystandards.org/faq/articles/Frequently_Asked_Question/What-is-the-intent-of-PCI-DSS-requirement-10/) are in a separate project. The shared services and the CDE are inside a [VPC Service Controls security perimeter](https://docs.cloud.google.com/vpc-service-controls) in order to safeguard against accidental misconfiguration or compromise of IAM access controls.

If your deployment is on [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine), the following are more ways that you can segment your CDE and protect cardholder data from untrusted systems:

  * [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) offer an additional layer of access control isolation whereby users can be given access to only certain Pods, services, and deployments within your Kubernetes cluster. This is useful for providing more fine-grained access to designated users.
  * [Network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy) can isolate Pods and services from one another to restrict data flows, and can provide an additional layer of network segmentation within your cluster.
  * [PodSecurity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/podsecurityadmission) is a Kubernetes admission controller that lets you apply Pod Security Standards to Pods running on your GKE cluster.



Each of these layers forms an important part of your defense-in-depth security posture, and helps narrow your scope by further isolating and protecting your trusted components from the surrounding environment. If you are deploying all or part of your CDE with Kubernetes, learn in more detail how to [run your PCI-compliant environment on GKE](https://docs.cloud.google.com/solutions/pci-dss-and-gke-guide).

### Implement tokenization

Tokenization is the process of irreversibly obscuring a primary account number (PAN). A tokenized PAN, or _token_ , cannot be redeemed for a PAN through mathematical means. PCI SSC offers guidance on the scoping impact of tokenization in Chapter 3 of the [tokenization guidelines supplement (PDF)](https://www.pcisecuritystandards.org/documents/Tokenization_Guidelines_Info_Supplement.pdf). PCI DSS scope is influenced heavily by the set of components that store and transmit cardholder data. When implemented properly, tokenization can help reduce your assessment scope by minimizing the occurrence and transmission of primary account numbers.

Tokenization is also a form of segmentation by data flow, because it separates systems that store and transmit cardholder data from those that can perform operations using only tokens. For example, systems that analyze consumer activity for fraud might not need PANs, but instead can perform these analyses using tokenized data. Tokenization also adds a layer of separation between systems that store and transmit PANs and your ecommerce web application. When your web application only interacts with systems that use tokens, the web application can potentially be removed from the set of connected-to systems, thus reducing scope.

The following diagram shows how CHD, a PAN, and tokenized data are handled in a typical tokenization system:

![Shows the flow of CHD, PAN, and tokenized data throughout the CDE project and shared services project of a tokenization system.](https://docs.cloud.google.com/static/architecture/images/limiting-compliance-scope-pci-environments-google-cloud-tokenization-architecture.svg)Figure 6. A typical architecture for a tokenization system.

In figure 6, a PAN and other cardholder data is received from the user, and then the data is immediately sent to the tokenization service. The tokenization service encrypts the PAN, generates a token, and then stores them both in a secure token vault. Only designated services, such as the settlement service, can access the vault on the network, and are authorized to redeem a PAN using a generated token. The settlement service only uses the PAN to send it to the payments processor. Neither the PAN nor any other cardholder data ever occurs outside this tightly controlled data flow. As part of a defense-in-depth strategy, the architecture also uses [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection) as another layer of defense against unintended leakage of PANs or other cardholder data.

In figure 6, the tokenization system uses [Hashicorp Vault](https://www.vaultproject.io/), a tightly-guarded secret store, to manage the PAN-to-token mappings. Only authorized users and services can redeem a PAN from a token using a lookup process. Components that are authorized to access the token vault can be given time-restricted access so that the component can only redeem a PAN during the specific time window it needs to carry out its function. Other datastores can be appropriate as well, depending on your business requirements. For more information on securely implementing tokenization in your environment, see [Tokenizing sensitive cardholder data for PCI DSS](https://docs.cloud.google.com/solutions/tokenizing-sensitive-cardholder-data-for-pci-dss).

#### Example architecture

The following diagram illustrates an example architecture for processing tokenized transactions using [Pub/Sub](https://docs.cloud.google.com/pubsub) and [Dataflow](https://docs.cloud.google.com/dataflow), and storing tokenized transaction records in [Spanner](https://docs.cloud.google.com/spanner).

![Shows the transaction processing project where Pub/Sub receives the tokenized data before sending it to Dataflow for processing.](https://docs.cloud.google.com/static/architecture/images/limiting-compliance-scope-pci-environments-google-cloud-transaction-architecture.svg)Figure 7. An example architecture for processing tokenized transactions.

In figure 7, the transaction processing project is a _connected-to_ system, and it's in-scope for PCI. It isn't _security-impacting_ , because compromise of any component in the transaction processing project cannot provide an attacker with access to CHD. The webapp project is out-of-scope, because it doesn't connect to the CDE, and only interacts with sanitized data.

The tokenized data is sent from the CDE to Pub/Sub. Before the tokenized data is published to other subscribers, Sensitive Data Protection verifies that it doesn't contain CHD. Tokenized data is processed by Dataflow and stored in the Spanner transaction database. Transactions can be associated with specific users by tokens without accessing PANs. The Spanner transaction database can also be used for reporting and analysis using business intelligence (BI) tools such as [Looker](https://docs.looker.com/setup-and-management/database-config/google-spanner).

### Support continuous compliance

Security and compliance are more than correct architecture and good engineering. A correct architecture can show that your environment is designed securely _in theory_. You also need effective auditing, logging, monitoring, and remediation processes in order to help ensure that your environment remains secure _in practice_.

To support compliance with each of the 12 PCI DSS requirement categories, you must monitor your implementation of that requirement on an ongoing basis. You must prove to yourself and your assessor that any in-scope component will remain secure in the future, long after the PCI DSS assessment is complete. Proper oversight paired with swift remediation action is called _continuous compliance_. Continuous compliance is a requirement of PCI DSS, and when implemented properly, it can help maximize the effect of the other scope reduction strategies.

Google Cloud lets you log everything that is happening in your network using [Firewall Rules Logging](https://docs.cloud.google.com/vpc/docs/using-firewall-rules-logging), [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs), [VPC Service Controls logs](https://docs.cloud.google.com/vpc-service-controls/docs/audit-logging), and [Cloud Load Balancing logs](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring). You can monitor the activity of your systems and users using [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit). Regularly monitoring these logs helps you comply with [PCI DSS Requirement 10.4](https://www.pcisecuritystandards.org/faq/articles/Frequently_Asked_Question/What-is-the-intent-of-PCI-DSS-requirement-10/), and lets you quickly respond to and remediate potential security threats. For more information, see the [PCI DSS supplement on effective daily log monitoring (PDF)](https://www.pcisecuritystandards.org/documents/Effective-Daily-Log-Monitoring-Guidance.pdf).

[Security Command Center](https://docs.cloud.google.com/security-command-center) lets you understand your security and data attack surface by providing asset inventory, discovery, search, and management. Security Command Center can analyze [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection) scan results to help identify leaked cardholder data and help verify that your tokenization system isn't being misused to maliciously redeem PANs. Using [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview), Security Command Center can help you proactively detect threats and unusual activity on your network and in your VMs, which could indicate that an attacker might be probing your system to identify its defensive capabilities. Security Command Center also lets you [create custom security sources](https://docs.cloud.google.com/security-command-center/docs/how-to-api-create-manage-security-sources) that are specific to your environment.

[Google Cloud Armor](https://docs.cloud.google.com/armor/docs) can provide additional protection for your public-facing Google Cloud web applications and help you comply with PCI DSS Requirement 6.4. Cloud Armor evaluates incoming requests for a variety of common web attacks and can help you avoid labor-intensive manual code reviews specified in requirement 6.4. Having a WAF in place helps you maintain continuous compliance while reducing your ongoing compliance costs and risks.

## What's next

  * Review [best practices for managing compliance obligations](https://docs.cloud.google.com/architecture/framework/security/compliance).
  * Read [PCI data security standard compliance on Google Cloud](https://docs.cloud.google.com/solutions/pci-dss-compliance-in-gcp).
  * [PCI Council guidance for PCI DSS scoping and network segmentation (PDF)](https://www.pcisecuritystandards.org/documents/Guidance-PCI-DSS-Scoping-and-Segmentation_v1_1.pdf).
  * Try the [PCI on GKE blueprint](https://docs.cloud.google.com/architecture/blueprints/gke-pci-dss-blueprint).
  * [Secure your Kubernetes workloads for PCI DSS](https://docs.cloud.google.com/solutions/pci-dss-and-gke-guide).
  * [Tokenizing sensitive cardholder data for PCI DSS](https://docs.cloud.google.com/solutions/tokenizing-sensitive-cardholder-data-for-pci-dss).
  * Deploy the [PCI Starter Terraform project](https://github.com/GoogleCloudPlatform/terraform-pci-starter#pci-starter).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-03-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-12 UTC."],[],[]] 
