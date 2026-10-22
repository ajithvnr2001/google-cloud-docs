---
url: https://docs.cloud.google.com/architecture/pci-dss-compliance-in-gcp/
title: PCI Data Security Standard compliance \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:03.065191+00:00
---

# PCI Data Security Standard compliance  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/pci-dss-compliance-in-gcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  PCI Data Security Standard compliance Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-03-12 UTC

This guide helps you learn how to implement the [Payment Card Industry Data Security Standard (PCI DSS)](https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Standard/PCI-DSS-v4_0.pdf) for your business on Google Cloud. The guide goes beyond [the PCI SSC Cloud Computing Guidelines](https://www.pcisecuritystandards.org/pdfs/PCI_SSC_Cloud_Guidelines_v3.pdf) (PDF) to provide background about the standard, explain your role in cloud-based compliance, and then give you the guidelines to design, deploy, and configure a payment-processing app using PCI DSS. The tutorial also discusses methods for monitoring, logging, and validating your app.

This document refers to the [PCI DSS 4.0 requirements](https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Standard/PCI-DSS-v4_0.pdf) where applicable.

The PCI Data Security Standard, created by the [PCI Security Standards Council](https://www.pcisecuritystandards.org/), is an information security standard for businesses that handle payment card (both credit and debit) information. The PCI Security Standards Council includes every major payment card company. Businesses that take Visa, MasterCard, Discover, American Express, JCB, or UnionPay are expected to comply with PCI DSS, and they can be fined or penalized if they don't.

PCI DSS includes classifications for several merchant types, from merchants that collect payment information in person to merchants that outsource payment processing entirely. This guide covers the [SAQ A](https://docs-prv.pcisecuritystandards.org/SAQ%20\(Assessment\)/SAQ/PCI-DSS-v4-0-SAQ-A-r2.pdf), [SAQ A-EP](https://docs-prv.pcisecuritystandards.org/SAQ%20\(Assessment\)/SAQ/PCI-DSS-v4-0-SAQ-A-EP-r2.pdf), and [SAQ D](https://docs-prv.pcisecuritystandards.org/SAQ%20\(Assessment\)/SAQ/PCI-DSS-v4-0-SAQ-D-Merchant-r1.pdf) merchant types.

## Objectives

  * Review the payment-processing app architecture.
  * Set up your payment-processing environment.
  * Deploy and configure your app servers.
  * Set up logging and monitoring.
  * Validate your payment-processing environment.



## Definitions

This guide uses many unique phrases. Here are several of the most common. For more information, refer to the [PCI DSS glossary](https://www.pcisecuritystandards.org/pci_security/glossary).

**CDE** : Acronym for _cardholder data environment_. This acronym refers to any part of your app that holds or transfers any cardholder data, including the payment account number or any personally identifiable information related to the card.

**Compensating controls** : Alternative solutions that can be considered if an entity cannot meet a requirement explicitly as stated, due to legitimate technical or documented business constraints. Entities must sufficiently mitigate the risk associated with the requirement when they implement these other controls. See "Compensating Controls" Appendixes B and C in [PCI DSS Requirements and Security Assessment Procedures](https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Standard/PCI-DSS-v4_0.pdf) for guidance on the use of compensating controls.

**PAN** : Acronym for _primary account number_ and also referred to as an account number. It is the unique payment card number that identifies the issuer and the cardholder account.

**QSA** : Acronym for _Qualified Security Assessor_. QSAs are qualified by the PCI Security Standards Council (SSC) to perform PCI DSS on-site assessments. The [Qualification Requirements for Qualified Security Assessors (QSA)](https://docs-prv.pcisecuritystandards.org/Programs%20and%20Certification/Qualified%20Security%20Assessor%20\(QSA\)/QSA_Qualification_Requirements_v4.1.pdf) provides details about requirements for QSA companies and employees.

**SAQ:** Acronym for _Self-Assessment Questionnaire_ , the reporting tool that is used to document self-assessment results from an entity's PCI DSS assessment. This only applies for entities that are eligible for self-assessment.

**Scope** : The systems, procedures, and people to be included in a PCI DSS assessment.

**Tokenization** : A process that replaces the primary account number (PAN) with a surrogate value called a token. The PAN is then stored in a secure lookup. De-tokenization is the reverse process of looking up a PAN by its token. A token can either be a [hash or an assigned value](https://www.pcisecuritystandards.org/documents/Tokenization_Guidelines_Info_Supplement.pdf).

## Background

PCI DSS provides a [list of requirements](https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Supporting%20Document/Prioritized-Approach-For-PCI-DSS-v4-0.pdf) designed to enhance cardholder security. These requirements are divided into twelve major numbered parts and many subparts. This document references these part numbers to add context, but the section references are not an exhaustive list of applicable requirements.

Your PCI DSS compliance requirements vary depending on how your company handles payment card transactions (type) and how many transactions it performs each year (level).

As your number of transactions increases, your PCI DSS merchant level increases, and the PCI DSS compliance guidelines become stricter. At the highest merchant level, Level 1, PCI DSS requires an audit. Levels vary by the card brand. Level 1 is defined by American Express as 2.5 million annual transactions, and by Visa, Mastercard, and Discover as 6 million annual transactions. Each card brand has additional level requirements that are beyond the scope of this document. Ensure that your payment-processing environment is audited to support your merchant level.

Because Google Cloud is a Level 1 PCI DSS 4.0–compliant service provider, it can support your PCI DSS compliance needs no matter what your company's merchant level is. The Committed to compliance section lays out which areas are covered for you by Google.

The other fundamental variable is your SAQ type. The SAQ outlines criteria that you must address to comply with PCI DSS if you are eligible for self-assessment. Your SAQ type is determined by your app architecture and the precise way you handle payment card data. Most merchants in the cloud are one of the following:

SAQ type | Description  
---|---  
A | Merchants that have fully outsourced payment card processing to a third-party site. Customers leave your domain (including through an `<iframe>` web form), complete payment, and then return to your app.  
  
In other words, your company can't touch customer card data in any way.  
A-EP | Merchants that outsource payment processing to a third-party provider, but who can access customer card data at any point in the process. Merchants that can access card data include merchant-controlled page elements such as JavaScript or CSS that are embedded in the third-party payment page.  
  
In other words, your payment processing app forwards card data to a processor on the client side, or the processor renders any content hosted by you.  
D | Merchants that accept payments online and don't qualify for SAQ A or SAQ A-EP. This type includes all merchants that call a payment processor API from their own servers, regardless of tokenization.   
  
In other words, if you are not SAQ A or SAQ A-EP, you are SAQ D.  
  
SAQ D differentiates between [merchants and service providers](https://www.pcisecuritystandards.org/pci_security/glossary). Service providers are not discussed in this document, and all SAQ D references address merchants as defined in PCI DSS.  
![SAQ requirements. SAQ A-EP is a superset of SAQ A, and SAQ D is a superset of SAQ A-EP.](https://docs.cloud.google.com/static/architecture/images/pci-dss-venn-saq.svg)Figure 1. Venn diagram of SAQ requirements. SAQ A-EP is a superset of SAQ A, and SAQ D is a superset of SAQ A-EP.

## Committed to compliance

Google uses a variety of technologies and processes to secure information that is stored on Google servers. Google independently validated PCI DSS requirements that apply to Google Cloud technologies and infrastructure that are managed by Google. You can download Google's PCI DSS compliance reports from [Compliance Reports Manager](https://cloud.google.com/security/compliance/compliance-reports-manager). While Google offers merchants a great deal of control over their compute instances that run on Google infrastructure, Google doesn't control security for the operating system, packages, or apps that merchants deploy on Google Cloud. It is your responsibility to comply with PCI DSS requirements for operating system packages and apps that you deploy, in addition to other customizations required by your architecture.

Google Cloud follows the PCI DSS requirements set forth for a Level 1 Service Provider and all applicable service provider requirements. The Google Cloud [Shared Responsibility Matrix](https://services.google.com/fh/files/misc/gcp_pci_dss_v4_responsibility_matrix.pdf) outlines the compliance obligations of PCI DSS. The responsibility matrix can be a helpful reference as you pursue PCI DSS compliance and conduct your own PCI DSS audits.

## Product guidance

This section contains guidance for commonly-used Google Cloud services in architectures used for PCI DSS environments.

### App Engine

Use App Engine [ingress firewall rules](https://docs.cloud.google.com/appengine/docs/flexible/go/creating-firewalls) and [egress traffic controls](https://docs.cloud.google.com/appengine/docs/standard/python3/connecting-vpc#egress).

### Cloud Run

Use Cloud Run [ingress settings](https://docs.cloud.google.com/run/docs/securing/ingress), [VPC Service Controls](https://docs.cloud.google.com/run/docs/securing/using-vpc-service-controls), and [egress controls on VPC connectors](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc#egress). If needed, [configure a static outbound IP address](https://docs.cloud.google.com/run/docs/configuring/static-outbound-ip).

### Cloud Run functions

Use Cloud Run functions [ingress and egress network settings](https://docs.cloud.google.com/functions/docs/networking/network-settings).

### Cloud Logging

Log interactions with [Cloud Logging](https://docs.cloud.google.com/logging/docs).

### Cloud Monitoring

Monitor interactions with [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs).

### Google Kubernetes Engine

For information about using Google Kubernetes Engine for PCI DSS environments, see [PCI DSS compliance on GKE](https://docs.cloud.google.com/architecture/pci-dss-and-gke-guide).

### Cloud Storage

Requirement 3.5 stipulates that a primary account number (PAN) is secured wherever it is stored. While Google automatically offers encryption at rest, it doesn't automatically perform the one-way hashes, truncation, or tokenization that the rules also require.

## Example architectures

This section illustrates the approaches to implementing an environment that complies with SAQ A, SAQ A-EP, and SAQ D.

### Architecture overview

### SAQ A

SAQ A is the most basic payment-processing architecture. Payments are processed by a third party, and no card data is accessed by merchant apps or pages.

At a high level, the payment-processing flow is as follows:

  1. The customer makes their selections and proceeds to check out.

  2. The checkout app redirects the customer to a third-party payment processor.

  3. The customer enters their payment card information into a payment form that the third-party processor owns and maintains.

  4. The third-party payment processor checks the payment card information and then charges or declines the card.

  5. After processing the transaction, the third-party payment processor sends the customer back to the merchant app along with transaction details.

  6. The merchant app sends a verification request to the payment processor to confirm the transaction.

  7. The payment processor responds to verify the transaction details.


![Processing information between the customer's browser, the merchant's site, the payment processor, and the payment gateway.](https://docs.cloud.google.com/static/architecture/images/pci-dss-architecture-saq-a.svg)Architecture of an SAQ A third-party payment-processing environment.**Important:** PCI DSS supports third-party payment processors in an `<iframe>` under SAQ A, based on the security provided by a browser's same-origin policy. This policy restricts DOM access to the `<iframe>` from the parent page.

### SAQ A-EP

The SAQ A-EP payment-processing architecture is centered around a payment-processing app that runs on Compute Engine virtual machine instances. These instances are in a secure private network, and they use secure channels to communicate with services that are outside the network.

At a high level, the payment-processing flow is as follows:

  1. The customer enters their payment card information into a payment form that your company owns and maintains.

  2. When the customer submits their information, the form information is securely passed on to a third-party payment processor.

  3. The third-party payment processor checks the payment card information and then charges or declines the card.

  4. The payment processor sends a response back to your payment app, which then passes a message to your core app.




All of these interactions are logged and monitored with [Cloud Logging](https://docs.cloud.google.com/logging/docs) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs).

![Architecture of an SAQ A-EP payment-processing environment](https://docs.cloud.google.com/static/architecture/images/pci-dss-architecture-saq-aep.svg)Architecture of an SAQ A-EP payment-processing environment.

### SAQ D

The SAQ D payment–processing architecture centers around a payment-processing app that runs on Compute Engine virtual machine instances. These instances are in a secure private network and use secure channels to communicate with services that are outside the network.

At a high level, the payment-processing flow is as follows:

  1. The customer enters their payment card information into a payment form that your company owns and maintains.

  2. When the customer submits their information, your payment app receives the form information.

  3. Your payment app validates the payment information and securely passes it on to a third-party payment processor through a backend API.

  4. The third-party payment processor checks the payment card information and then charges or declines the card.

  5. The payment processor sends a response back to your payment app, which then passes a message to your core app.




All of these interactions are logged and monitored with [Logging](https://docs.cloud.google.com/logging/docs) and [Monitoring](https://docs.cloud.google.com/monitoring/docs).

![Architecture of a SAQ D payment-processing environment](https://docs.cloud.google.com/static/architecture/images/pci-dss-architecture-saq-d.svg)Architecture of a SAQ D payment-processing environment.

### Payment processing customer-facing flow

### SAQ A

This section describes the third-party payment processing flow from the perspective of the customers using your app.

![Customer-facing flow of SAQ A third-party payment processing](https://docs.cloud.google.com/static/architecture/images/pci-dss-third-party-payment-flow.svg)Customer-facing flow of SAQ A third-party payment processing.

When your customer accesses your payment form, the app presents an `<iframe>` hosted by the payment processor. Your app cannot access or monitor the contents of the `<iframe>` because of [cross-origin resource sharing limitations](https://wikipedia.org/wiki/Cross-origin_resource_sharing). When the customer submits their payment card information, the payment processor accepts or declines the card, then sends the customer back to your app. Your app then checks the transaction response from the payment processor and acts accordingly. Your app didn't access or handle any payment card information.

### SAQ A-EP

This section describes the same internal payment processing flow as previously described, but from the perspective of the customers using your app.

![Customer-facing flow of SAQ A-EP third-party payment processing](https://docs.cloud.google.com/static/architecture/images/pci-dss-saq-aep-processing.svg)Customer-facing flow of SAQ A-EP third-party payment processing.

When your customer accesses the URL for your payment form, the site presents a form hosted by your payment app. When the customer submits their payment card information, the form goes directly to the payment processor. The processor accepts or declines the card, then sends the customer back to your app. Your app then checks the transaction response from the payment processor and acts accordingly. The customer might not see the third-party payment processor, but your app didn't access any payment card information on the server side.

### SAQ D

This section describes the internal payment processing flow from the perspective of the customers using your app.

![Customer-facing flow of SAQ D third-party payment processing](https://docs.cloud.google.com/static/architecture/images/pci-dss-saq-d-processing.svg)Customer-facing flow of SAQ D third-party payment processing.

When your customer accesses the URL for your payment form, they are securely routed to the form through an HTTPS load balancer. When the customer submits their payment card information, your payment-processing app securely sends the information to a third-party payment processor. The third-party payment processor accepts or declines the card, then returns a response to your payment-processing app.

### Payment-processing internal flow

### SAQ A & A-EP

This section describes the payment-processing flow from the perspective of the servers running your app.

![SAQ A and SAQ A-EP internal flow](https://docs.cloud.google.com/static/architecture/images/pci-dss-saq-a-aep-internal-flow.svg)SAQ A and SAQ A-EP internal flow.

Your payment-processing app receives and parses the response returned by the third-party payment processor, and then sends some or all of the response data to the core app. At this point, your payment-processing app is finished with the transaction. The core app handles the task of notifying your customers.

### SAQ D

This section describes the internal payment processing flow from the perspective of the servers running your app.

![SAQ D internal flow](https://docs.cloud.google.com/static/architecture/images/pci-dss-saq-d-internal-flow.svg)SAQ D internal flow.

Your payment-processing app validates the payment card information submitted by the customer, and then sends it to the payment processor through a backend API. The processor attempts the charge and responds with transaction details. Your app receives and processes the response and then sends some or all of the response data to the core app. At this point, your payment-processing app is finished with the transaction. The core app handles the task of notifying your customer and delivering product.

### Monitoring and logging data flow

The monitoring and logging flow is designed as follows:

![Monitoring and logging flow](https://docs.cloud.google.com/static/architecture/images/pci-dss-monitoring-logging.svg)Monitoring and logging flow.

## Setting up your payment-processing environment

This section describes how to set up your payment-processing environment. Setup includes the following:

  * Creating a new Google Cloud account to isolate your payment-processing environment from your production environment.
  * Restricting access to your environment.
  * Setting up your virtual resources.
  * Designing the base Linux image that you will use to set up your app servers.
  * Implementing a secure package management solution.

**Important:** SAQ A and SAQ A-EP don't strictly require some of the actions indicated later in this document, but Google recommends them as a baseline for secure online operations.

### Setting up a new account

To simplify access restriction and compliance auditing, create a production-quality, payment-processing environment that is fully isolated from your standard production environment and any dev and QA environments (requirement 6.5.3). To ensure isolation, create and use a Google Cloud account that is separate from your core production environment account. Users experienced with Identity and Access Management (IAM) configuration can accomplish equivalent isolation by using [separate projects](https://docs.cloud.google.com/resource-manager/docs/access-control-proj) for in-scope work.

### Restricting access to your environment

Allow payment-processing environment access only to individuals who deploy your payment system code or manage your payment system machines (section 7.2 and requirement 8.2.1). This is known as the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege). Use IAM [roles](https://docs.cloud.google.com/iam/docs/understanding-roles) to restrict access. Best practices include using roles wherever possible, granting only the permissions required to perform expected work, and only granting the Owner role to principals who legitimately need full root access to your services. Refer to the [IAM security guide](https://docs.cloud.google.com/iam/docs/using-iam-securely) for more information.

Automated access to any managed service should rely on [service accounts](https://docs.cloud.google.com/iam/docs/service-accounts). Service accounts simplify the app management lifecycle by giving you a way to manage app authentication and authorization. These accounts give you a flexible, yet secure way to group virtual machine instances with similar apps and functions that have a common identity. You can enforce security and access control at the service-account level through IAM roles and VPC firewall rules.

IAM rules that you apply to folders are inherited by all items contained in that folder. Default permissions are deny-all (requirement 7.2.3), and every rule that you apply only adds permissions.

**Important:** Access rights granted to a parent IAM folder cannot be taken away from a child folder.

Requirement 8.3.6 provides some basic rules for user passwords. The National Institute of Standards and Technology (NIST) defines a more secure set of rules for secure passwords in [section 5.1.1 of NIST SP800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html#-511-memorized-secrets). Google recommends following the NIST Digital Identity guidelines whenever possible.

PCI DSS SAQ D section 12.7 requires individuals with access to your in-scope environment to pass a background check, in compliance with local laws, before they are granted access to the environment. To reduce the risk of compliance violations, consider performing these criminal background checks and reference checks on each individual regardless of your compliance type.

### Securing your network

To secure inbound and outbound traffic to and from your payment-processing app network, you need to create the following:

  * Cloud Next Generation Firewall policies or Compute Engine firewall rules
  * A Cloud VPN tunnel
  * An External Application Load Balancer



For creating your VPC, we also recommend [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) for an additional layer of network security. There are many powerful options available to secure networks of both Compute Engine and GKE instances.

#### Creating firewall rules

Use Cloud Next Generation Firewall [policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview) or VPC [firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) to restrict inbound traffic to each of your Compute Engine instances (requirements 1.3 and 1.4). Allow inbound traffic only from the following three sources:

  * Public HTTPS, so that customers can reach your payment page.
  * Your app network, so that your payment-processing app can receive responses from your third-party payment processor.
  * Your internal office network, so that you can access the instances for auditing and management purposes.



Use firewall rules on individual instances to restrict outbound traffic. You can implement these rules locally with iptables or, more broadly, by using VPC firewall rules and [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags). Allow outbound traffic only from your payments form to the third-party payment processor. This connection must be HTTPS-only. To test your work, see the section on Firewall Rules Logging later in this document.

Cloud DNS offers [private DNS zones](https://docs.cloud.google.com/dns/zones#create-private-zone) so you can securely name hosts within your CDE without the potential of leaking sensitive network topology data to the public.

Restrict traffic as follows:

Source | Destination | Port | Direction and reason  
---|---|---|---  
Public load balancer | Third-party payments form | tcp:443 | Inbound  
Public access to the payment-processing app  
Third-party payment form | Third-party payment processor | tcp:443 | Outbound  
Forwarding AUTH requests to payment service provider  
Third-party payment processor | Your payment-processing app | tcp:5480 | Inbound  
Accepting AUTH requests from payment systems (does not contain any cardholder data)  
Your company's office network | vpn-gateway | tcp:8000 | Inbound  
Access to payment-processing environment for access to logs and development machines  
  
In addition, the following traffic occurs securely in your payment-processing app internal network:

Source | Destination | Port | Reason  
---|---|---|---  
Card form | PCI proxy | tcp:5480 | Exchange of encrypted card data for payment instrument token  
All hosts | Google NTP servers | udp:123 | Time synchronization  
VPN gateway | All hosts | tcp:22 | Secure Shell (SSH) connections  
  
#### Establishing a secure VPN tunnel

You can use [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) to establish a secure VPN tunnel between your on-premises environment and your payment-processing environment (sections 2.2.7 and 4.2).

#### Creating an External Application Load Balancer

You can help ensure that incoming customer traffic is secure by creating an [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/application-load-balancer) (sections 2.2.7 and 4.2). To create an external Application Load Balancer, you need the following:

  * A subdomain of your website that is used for your payment processing form, for example, `payments.your-domain-name.com`.
  * A valid, signed SSL certificate that has been registered for your subdomain.



Ensure that your domain is valid by looking at its DNS settings in your web registrar domain configuration interface.

**Important:** Although it's possible to configure an external Application Load Balancer to allow HTTP traffic, HTTPS traffic, or both, you must configure your load balancer to allow HTTPS traffic only.

### Creating a base Linux image

The PCI DSS contains requirements that describe how to set up machines that are part of a compliant payment-processing architecture. You can implement these requirements in several ways, but the easiest approach is as follows:

  1. Create a list of the software and libraries that must be installed on each server that is in scope for your payment-processing app. To avoid introducing unnecessary vulnerabilities to your system (requirement 2.2.4), include only the minimum of software and libraries that you need to run your app. Candidates might include the [Google Cloud CLI](https://docs.cloud.google.com/sdk), language-specific runtimes and libraries, or a web server.

  2. Create a Compute Engine instance that uses one of the Compute Engine [preconfigured operating system images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  3. Install the libraries and software you listed earlier.

  4. Install and configure `ntp` to keep system clocks in sync. Managing server clocks with the Network Time Protocol ensures the integrity of timestamps in logs (section 10.6).

  5. Ensure that the image follows the [best practices](https://docs.cloud.google.com/compute/docs/images/configuring-imported-images#security) for creating a secure Compute Engine image (all of section 2.2).

  6. After you've configured your base image, [create a custom Compute Engine disk image](https://docs.cloud.google.com/compute/docs/creating-custom-image) from your image. This image lets you use your base Linux image when you create virtual machine instances.




### Using secure package management

Package management is a key component of a security-hardened hosting environment. Per section 2.2, you must implement industry-accepted hardening standards. Unless you use [Container-Optimized OS from Google](https://docs.cloud.google.com/container-optimized-os/docs/resources), you likely have a package manager installed such as RPM, Yum, or Apt. Your app might use its own programming language-specific package manager such as NPM, PyPi, or Composer, and download dependencies upon first run.

If your app can fetch updates from the internet, you must treat update sources as a potential security risk. Supply-side, or upstream attacks, that are maliciously included in publicly hosted packages are becoming more common. Imagine the effects of installing an update to SSH that contains malicious code.

You can mitigate the risk of supply-side attacks by creating a safe recipients list for your packages and verifying that they match the list. Keep a list of tested and approved version numbers for each package that you use. Record the version number along with its hash or signature. Ensure that the package manager validates the hash or signature before installing or updating an app.

Most package management systems allow for private hosting. If possible, launch your own private package management server and only host tested and approved software. Lock down the package manager so that it cannot reach out to other servers for updates.

Ideally, your app build process fetches and validates all packages, and then creates a revision of the custom disk image that includes everything that the container needs. This way, your servers launch and scale up with no installer delay, and there is a reduced chance of random errors at launch time. You can also revisit any previous version of your app exactly as it was in production by launching its image, which can be helpful for diagnostics and forensics.

## Deployment and configuration

Next, set up the deployment and configuration of your instances from your base image.

### Deploying your environment

To meet the PCI DSS requirements, ensure that you're deploying the correct app every time, that you're deploying the app securely, and that you aren't installing any other software packages during the deployment. To simplify the deployment process, consider creating an automated deployment for your app by using [Terraform](https://docs.cloud.google.com/docs/terraform). Terraform lets you describe your entire payment-processing environment, including its firewall rules, gateways, load balancers, and instances in code.

In an automated deployment, you must verify the integrity of the software being deployed, whether it's from a third party or it's your own. You can verify your software by running an automated hash against each package as the package is installed. After a hash is verified, you can then use an automated testing framework to run security and other tests, and to verify that the tests have passed.

Finally, when deploying Compute Engine instances, design a recovery plan in the event that your instances fail. If your window for acceptable downtime is large enough, a manual recovery plan might be sufficient; if not, you must design an automated recovery plan. See the [Disaster recovery planning guide](https://docs.cloud.google.com/solutions/disaster-recovery-cookbook), [Designing robust systems](https://docs.cloud.google.com/compute/docs/tutorials/robustsystems), and [Building scalable and resilient web apps](https://docs.cloud.google.com/solutions/scalable-and-resilient-apps) for guidance.

### Configuring your environment

After your instances have been deployed, ensure that they're configured correctly. Install additional software and libraries on top of each instance base image as needed. To avoid the complexity, overhead, and overall risk of manual configuration, use an automated configuration management tool such as [Skaffold](https://github.com/GoogleContainerTools/skaffold), [Chef](https://www.chef.io/chef/), [Puppet](https://puppetlabs.com/), [Ansible](http://www.ansible.com/), or [Salt](http://saltstack.com/).

### Implementing immutable audit logging

Logging produces [audit logs](https://docs.cloud.google.com/logging/docs/audit) automatically for a wide variety of activities [across many products](https://docs.cloud.google.com/logging/docs/audit/services). Long-term, you can securely store immutable logs by using Cloud Storage [bucket locks](https://docs.cloud.google.com/storage/docs/bucket-lock) (section 10.3). Bucket locks let you set a policy to make all objects immutable and non-deletable for an amount of time that you specify, from seconds to years.

### Implementing Virtual Private Cloud Flow Logs

The [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) service is designed to record network flows sent from or received by virtual machine instances. You can use these logs for network monitoring, forensics, and real-time security analysis (section 10.2).

#### Installing the Logging agent

After you set up iptables on your servers, each server logs every activity to the server's block storage. Check out the [Logging](https://cloud.google.com/stackdriver/pricing#logging-costs) pricing page for details on the free allotment and data transfer pricing. To retain these logs and to generate alerts based on suspicious activity, stream them to Logging and Monitoring by installing the [Logging agent](https://docs.cloud.google.com/logging/docs/agent) on each server (section 10.3).

#### Integrating an intrusion detection system

To help ensure the security of your payment-processing environment, described in section 11.5, use an [intrusion detection system (IDS)](https://en.wikipedia.org/wiki/Intrusion_detection_system), so you know when bad actors try to attack the system. There are two ways to place an IDS in a payment-processing environment: place an IDS at every entry point, or install an IDS on every server.

To reduce the complexity of your environment architecture and to simplify compliance with 11.5, install an IDS on each server. After you research and choose the IDS software to use, make IDS installation part of the startup installation script for each server.

[Cloud Intrusion Detection System (Cloud IDS)](https://docs.cloud.google.com/intrusion-detection-system/docs/overview), an intrusion detection service, provides threat detection for intrusions, malware, spyware, and command-and-control attacks on your network. Cloud IDS provides full visibility into network traffic, including both north-south and east-west traffic, letting you monitor VM-to-VM communication to detect lateral movement. You can also use Cloud IDS to simplify compliance with requirement 11.5.

IDS logs fall in the scope of PCI DSS compliance, and must be sent to Logging and Monitoring for reporting, alerting, and auditing.

### Implementing Security Command Center

[Security Command Center](https://docs.cloud.google.com/security-command-center) helps security teams gather data, identify threats, and respond to threats before they result in business damage or loss. It offers deep insight into app and data risk so that you can quickly mitigate threats to your cloud resources and evaluate overall health. With Security Command Center, you can view and monitor an inventory of your cloud assets, scan storage systems for sensitive data, detect common web vulnerabilities, and review access rights to your critical resources, all from a single, centralized dashboard. It can help you comply with several requirements, including sections 5 and 6.4.

#### Automating your app deployment

Build your configuration management tool to securely retrieve and launch the latest version of your app. Your app can be retrieved from any location, such as [Cloud Storage](https://docs.cloud.google.com/storage/docs), as long as that location is secure.

Many of the configuration management tools mentioned earlier support continuous integration and deployment (CI/CD) workflows, which can also be used to perform automated scanning (section 11.3) and to ensure that code is reviewed (requirement 6.2.3).

#### Capturing configuration manager logs

When setting up your configuration manager, ensure that it logs all installation details. After completing the configuration process, ensure that it delivers the logs to Logging and Monitoring.

## Logging and monitoring

To ensure PCI DSS compliance under section 10, ensure that every step taken in your payment-processing environment is monitored and recorded. Every server activity on every instance must be logged, and every user action must be able to be examined at a later time.

### Enabling Access Transparency

Through [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview), Logging now offers near real-time logs when Google Cloud admins access your content. Cloud Audit Logs logs already provide visibility into the actions of your own admins. However, this audit trail typically excludes actions taken by your cloud provider's support or engineering team. For example, before Access Approval logging, if you opened a ticket with Google Support that required data access, it wouldn't have been tracked in Cloud Audit Logs. Access Approval closes that gap, capturing near real-time logs of manual, targeted access by either support or engineering.

[Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview) lets you explicitly approve access to your data or configurations on Google Cloud before that access occurs. Access Approval also provides insight into accesses by Google Support and Engineering.

### Enabling Firewall Rules Logging

[Firewall Rules Logging](https://docs.cloud.google.com/vpc/docs/firewall-rules-logging) lets you enable logging at the individual rule level. It can record TCP and UDP connections inside a VPC for any rules you create yourself. These can be useful for auditing network access or providing early warning that the network is being used in an unapproved manner.

### Using VPC Service Controls

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls) lets you define a security perimeter around Google Cloud resources such as Cloud Storage buckets, Bigtable instances, and BigQuery datasets to constrain data in a VPC network and help mitigate data exfiltration risks (requirements 1.3.1 and 1.3.2). With VPC Service Controls, you can keep your sensitive data private as you take advantage of the fully managed storage and data processing capabilities of Google Cloud.

### Setting up VPC Flow Logs

[VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) record network traffic flows sent or received by VM instances. The logs are useful under PCI DSS for monitoring, auditing, forensics, and real-time security analysis. Each VPC network subnet can have Flow Logs enabled or disabled independently. You can minimize the amount of log data by only enabling Flow Logs on your in-scope CDE. Flow Logs, combined with egress firewall rules, enable you to limit outbound traffic to authorized endpoints in a way that is auditable and difficult to circumvent (requirements 1.2.1 and 1.3.4).

The following diagram shows how VPC Flow Logs record network traffic flows sent or received by VM instances."

![Cardholder Data Environment with VPC Flow Logs enabled](https://docs.cloud.google.com/static/architecture/images/pci-dss-cde-withvpc-flow-logs.svg)Figure 2. CDE with VPC Flow Logs enabled.

If you require more detailed data than Flow Logs can provide, such as individual HTTP request logging, you can implement controls in your app or proxy outbound requests. You do this through your own reverse proxy server configured to forward access logs to Logging. For instructions on setting up a Squid proxy server on Compute Engine, see [Setting up a network proxy](https://docs.cloud.google.com/compute/docs/vpc/special-configurations#proxyvm). To avoid bottlenecks, set up at least two redundant proxy servers.

### Logging internal access data

In addition to logging external threats, also monitor and log the activity of individuals who have administrator access to your payment-processing environment (section 10.2). To do this, you can log shell commands. Several open source tools can audit shell commands and send them to logging. Popular choices for this task include [OSSEC](https://www.ossec.net/) or [Tripwire](https://www.tripwire.com/).

### Setting up monitoring alerts

Configure Monitoring to send alerts if something goes wrong in your payment-processing environment (section 10.6). Ensure that your alerts cover environmental, audit, and internal app events. Base your alerting strategy on the potential risk or attack vectors for each component of your payment-processing app. For example, trigger Monitoring alerts if your IDS detects any intrusion attempts, whether they are successful or unsuccessful. You can also use Firewall Rules Logging to trigger alerts in response to attempts to violate specific network policies.

### Streaming logs to BigQuery

![Logging streaming logs to both
Cloud Storage and BigQuery](https://docs.cloud.google.com/static/architecture/images/pci-dss-streaming-logs.svg)Figure 3. Logging streaming logs to both Cloud Storage and BigQuery.

Optionally, you can route Logging logs to BigQuery to analyze later; see [Routing and storage overview: Sinks](https://docs.cloud.google.com/logging/docs/routing/overview#sinks) for details. Because BigQuery is optimized to query large datasets, it is an ideal tool for large-scale logs analysis. Logging can even [log directly to BigQuery](https://docs.cloud.google.com/logging/docs/export/configure_export_v2) for logs that require near real-time analysis (requirement 10.4.1).

### Using Sensitive Data Protection to sanitize data

There are many reasons to use parts of the data contained in your in-scope app that are not themselves in scope, such as for analytics or development. Grant apps access to PCI data only after it has been sanitized with [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection) (requirement 6.5.1).

## App security

To help secure your app, you first need to evaluate the administrator interface. You might also want to use Cloud Key Management Service.

### Evaluating the administrator interface

Most ecommerce apps have their own non-console administrator interface, such as a customer service billing portal. Such a tool must have robust access controls; it must have individualized access that uses multi-factor authentication (section 8.4); and it must be instrumented with audit logging (section 10.2).

Any logs you create should answer these questions: Who did what? Where did they do it? When did they do it? According to section 2.2.7, all access to such a tool must use strong transport encryption. Use Sensitive Data Protection to filter sensitive information before displaying it in any administration tool.

### Using Cloud Key Management Service (Cloud KMS)

[Cloud KMS](https://docs.cloud.google.com/kms) is a service that lets you manage encryption keys. It can generate, use, rotate, and destroy AES-256, RSA 2048, RSA 3072, RSA 4096, EC P256, and EC P384 encryption keys. Cloud KMS lets you remove plain-text passwords stored in code or config files, which simplifies compliance with sections 2.2.2, 3.6, 3.7, and 8.2.

## Validating your environment

After your environment is implemented, but before any production traffic flows through it, you must have the environment validated:

  * If you're a Level 1 merchant, your environment must be validated by a [Qualified Security Assessor (QSA)](https://www.pcisecuritystandards.org/assessors_and_solutions/qualified_security_assessors). A QSA is a firm or an individual that is approved by the PCI Security Standards Council to validate PCI environments and give the seal of approval.
  * If you're a Level 2 merchant or lower, you can validate your environment by filling out the [Self-Assessment Questionnaire](https://www.pcisecuritystandards.org/document_library?category=saqs#results).



## What's next

  * [PCI DSS document library](https://www.pcisecuritystandards.org/document_library)
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-03-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-03-12 UTC."],[],[]] 
