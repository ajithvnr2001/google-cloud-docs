---
url: https://docs.cloud.google.com/architecture/security/confidential-computing-analytics-ai/
title: Confidential computing for data analytics, AI, and federated learning \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:06.657081+00:00
---

# Confidential computing for data analytics, AI, and federated learning  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/security/confidential-computing-analytics-ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Confidential computing for data analytics, AI, and federated learning Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-12-20 UTC

This document provides a general overview of confidential computing, including how you can use it for secure data collaboration, AI model training, and federated learning. The document also provides information about the Confidential Computing services in Google Cloud and architecture references for different use cases.

This document is intended to help technology executives understand the business potential of confidential computing with generative AI and applied AI across various industries, including financial services and healthcare.

## What is confidential computing?

Data security practices have conventionally centered on protecting data at rest and in transit through encryption. Confidential computing adds a new layer of protection by addressing the vulnerability of data during its active use. This technology ensures that sensitive information remains confidential even as it is being processed, thus helping to close a critical gap in data security.

A confidential computing environment implements the protection of data in use with a hardware-based [trusted execution environment (TEE)](https://en.wikipedia.org/wiki/Trusted_execution_environment). A TEE is a secure area within a processor that protects the confidentiality and integrity of code and data loaded inside it. TEE acts as a safe room for sensitive operations, which mitigates risk to data even if the system is compromised. With confidential computing, data can be kept encrypted in memory during processing.

For example, you can use confidential computing for data analytics and machine learning to help achieve the following:

  * **Enhanced privacy:** Perform analysis on sensitive datasets (for example, medical records or financial data) without exposing the data to the underlying infrastructure or the parties that are involved in the computation.
  * **Secure collaboration:** Jointly train machine learning models or perform analytics on the combined datasets of multiple parties without revealing individual data to each other. Confidential computing fosters trust and enables the development of more robust and generalizable models, particularly in sectors like healthcare and finance.
  * **Improved data security:** Mitigate the risk of data breaches and unauthorized access, ensuring compliance with data protection regulations — such as the General Data Protection Regulation (GDPR) or the Health Insurance Portability and Accountability Act (HIPAA).
  * **Increased trust and transparency:** Provide verifiable proof that computations are performed on the intended data and in a secure environment, increasing trust among stakeholders.



## How a confidential computing environment works

Confidential computing environments have the following properties:

  * **Runtime encryption:** The processor keeps all confidential computing environment data encrypted in memory. Any system component or hardware attacker that attempts to read confidential computing environment data directly from memory only sees encrypted data. Likewise, encryption prevents the modification of confidential computing environment data through direct access to memory.
  * **Isolation:** The processor blocks software-based access to the confidential computing environment. The operating system and other applications can only communicate with the confidential computing environment over specific interfaces.
  * **Attestation:** In the context of confidential computing, attestation verifies the trustworthiness of the confidential computing environment. Using attestation, users can see the evidence that confidential computing is safeguarding their data because attestation lets you authenticate the TEE instance.

During the attestation process, the CPU chip that supports the TEE produces a cryptographically signed report (known as an _attestation report_) of the measurement of the instance. The measurement is then sent to an attestation service. An attestation for process isolation authenticates an application. An attestation for VM isolation authenticates a VM, the virtual firmware that is used to launch the VM, or both.

  * **Data lifecycle security:** Confidential computing creates a secure processing environment to provide hardware-backed protection for data in use.




## Confidential computing technology

The following technologies enable confidential computing:

  * Secure enclaves, also known as _application-based confidential computing_
  * Confidential VMs and GPUs, also known as _VM-based confidential computing_



Google Cloud uses Confidential VM to enable confidential computing. For more information, see Implement confidential computing on Google Cloud.

### Secure enclaves

A secure enclave is a computing environment that provides isolation for code and data from the operating system using hardware-based isolation or isolating an entire VM by placing the hypervisor within the trusted computing base (TCB). Secure enclaves are designed to ensure that even users with physical or root access to the machines and operating system can't learn the contents of secure enclave memory or tamper with the execution of code inside the enclave. An example of a secure enclave is Intel Software Guard Extension (SGX).

### Confidential VMs and confidential GPUs

A confidential VM is a type of VM that uses hardware-based memory encryption to help protect data and applications. Confidential VM offers isolation and attestation to improve security. Confidential VM computing technologies include AMD SEV, AMD SEV-SNP, Intel TDX, Arm CCA, IBM Z, IBM LinuxONE, and Nvidia Confidential GPU.

Confidential GPUs help protect data and accelerate computing, especially in cloud and shared environments. They use hardware-based encryption and isolation techniques to help protect data while it's being processed on the GPU, ensuring that even the cloud provider or malicious actors cannot access sensitive information.

## Confidential data analytics, AI, and federated learning use cases

The following sections provide examples of confidential computing use cases for various industries.

### Healthcare and life sciences

Confidential computing enables secure data sharing and analysis across organizations while preserving patient privacy. Confidential computing lets healthcare organizations participate in collaborative research, disease modeling, drug discovery, and personalized treatment plans.

The following table describes some example uses for confidential computing in healthcare.

Use case | Description  
---|---  
Disease prediction and early detection | Hospitals train a federated learning model to detect cancerous lesions from medical imaging data (for example, MRI scans or CT scans across multiple hospitals or hospital regions) while maintaining patient confidentiality.  
Real-time patient monitoring | Health care providers analyze data from wearable health devices and mobile health apps for real-time monitoring and alerts. For example, wearable devices collect data on glucose levels, physical activity, and dietary habits to provide personalized recommendations and early warnings for blood sugar fluctuations.  
Collaborative drug discovery | Pharmaceutical companies train models on proprietary datasets to accelerate drug discovery, enhancing collaboration while protecting intellectual property.  
  
### Financial services

Confidential computing lets financial institutions create a more secure and resilient financial system.

The following table describes some example uses for confidential computing in financial services.

Use case | Description  
---|---  
Financial crimes | Financial institutions can collaborate on anti-money laundering (AML) or general fraud model efforts by sharing information about suspicious transactions while protecting customer privacy. Using confidential computing, institutions can analyze this shared data in a secure manner, and train the models to identify and disrupt complex money laundering schemes more effectively.  
Privacy-preserving credit risk assessment | Lenders can assess credit risk using a wider range of data sources, including data from other financial institutions or even non-financial entities. Using confidential computing, lenders can access and analyze this data without exposing it to unauthorized parties, enhancing the accuracy of credit scoring models while maintaining data privacy.  
Privacy-preserving pricing discovery | In the financial world, especially in areas like over-the-counter markets or illiquid assets, accurate pricing is crucial. Confidential computing lets multiple institutions calculate accurate prices collaboratively, without revealing their sensitive data to each other.  
  
### Public sector

Confidential computing lets governments create more transparent, efficient, and effective services, while retaining control and sovereignty of their data.

The following table describes some example uses for confidential computing in the public sector.

Use case | Description  
---|---  
Digital sovereignty | Confidential computing ensures that data is always encrypted, even while being processed. It enables secure cloud migrations of citizens' data, with data being protected even when hosted on external infrastructure, across hybrid, public, or multi-cloud environments. Confidential computing supports and empowers digital sovereignty and digital autonomy, with additional data control and protection for data in use so that encryption keys are not accessible by the cloud provider.  
Multi-agency confidential analytics | Confidential computing enables multi-party data analytics across multiple government agencies (for example, health, tax, and education), or across multiple governments in different regions or countries. Confidential computing helps ensure that trust boundaries and data privacy are protected, while enabling data analytics (using data loss prevention (DLP), large-scale analytics, and policy engines) and AI training and serving.  
Trusted AI | Government data is critical and can be used to train private AI models in a trusted way to improve internal services as well as citizen interactions. Confidential computing allows for trusted AI frameworks, with confidential prompting or confidential retrieval augmented generation (RAG) training to keep citizen data and models private and secure.  
  
### Supply chain

Confidential computing lets organizations manage their supply chain and sustainability collaborate and share insights while maintaining data privacy.

The following table describes some example uses for confidential computing in supply chains.

Use case | Description  
---|---  
Demand forecasting and inventory optimization | With confidential computing, each business trains their own demand forecasting model on their own sales and inventory data. These models are then securely aggregated into a global model, providing a more accurate and holistic view of demand patterns across the supply chain.  
Privacy-preserving supplier risk assessment | Each organization involved in supplier risk assessment (for example, buyers, financial institutions, and auditors) trains their own risk-assessment model on their own data. These models are aggregated to create a comprehensive and privacy-preserving supplier risk profile, thereby enabling early identification of potential supplier risks, improved supply-chain resilience, and better decision making in supplier selection and management.  
Carbon footprint tracking and reduction | Confidential computing offers a solution for tackling the challenges of data privacy and transparency in carbon footprint tracking and reduction efforts. Confidential computing lets organizations share and analyze data without revealing its raw form, which empowers organizations to make informed decisions and take effective action towards a more sustainable future.  
  
### Digital advertising

Digital advertising has moved away from third-party cookies and towards more privacy-safe alternatives, like [Privacy Sandbox](https://privacysandbox.com/). Privacy Sandbox supports critical advertising use cases while limiting cross-site and application tracking. Privacy Sandbox uses TEEs to ensure secure processing of users' data by advertising firms.

You can use [TEEs](https://github.com/googleads/conf-data-processing-architecture-reference/blob/main/docs/TrustedExecutionEnvironmentsArchitecturalReference.md) in the following digital advertising use cases:

  * **Matching algorithms:** Finding correspondences or relationships within datasets.
  * **Attribution:** Linking effects or events back to their likely causes.
  * **Aggregation:** Calculating summaries or statistics from the raw data.



## Implement confidential computing on Google Cloud

Google Cloud includes the following services that enable confidential computing:

  * **Confidential VM:** Enable encryption of data in use for workloads that use VMs
  * **Confidential GKE:** Enable encryption of data in use for workloads that use containers
  * **Confidential Dataflow:** Enable encryption of data in use for streaming analytics and machine learning
  * **Confidential Dataproc:** Enable encryption of data in use for data processing
  * **Confidential Space:** Enable encryption of data in use for joint data analysis and machine learning



These services let you reduce your [trust boundary](https://en.wikipedia.org/wiki/Trust_boundary) so that fewer resources have access to your confidential data. For example, in a Google Cloud environment without Confidential Computing, the trust boundary includes the Google Cloud infrastructure (hardware, hypervisor, and host OS) and the guest OS. In a Google Cloud environment that includes Confidential Computing (without Confidential Space), the trust boundary includes only the guest OS and the application. In a Google Cloud environment with Confidential Space, the trust boundary is just the application and its associated memory space. The following table shows how the trust boundary is reduced with Confidential Computing and Confidential Space.

Elements | Within trust boundary without using Confidential Computing | Within trust boundary when using Confidential Computing | Within trust boundary when using Confidential Space  
---|---|---|---  
Cloud stack and administrators | Yes | No | No  
BIOS and firmware | Yes | No | No  
Host OS and hypervisor | Yes | No | No  
VM guest admin | Yes | Yes | No  
VM guest OS | Yes | Yes | Yes, measured and attested  
Applications | Yes | Yes | Yes, measured and attested  
Confidential data | Yes | Yes | Yes  
  
[Confidential Space](https://docs.cloud.google.com/docs/security/confidential-space) creates a secure area within a VM to provide the highest level of isolation and protection for sensitive data and applications. The main security benefits of Confidential Space include the following:

  * **Defense in depth:** Adds an extra layer of security on top of existing confidential computing technologies.
  * **Reduced attack surface:** Isolates applications from potential vulnerabilities in the guest OS.
  * **Enhanced control:** Provides granular control over access and permissions within the secure environment.
  * **Stronger trust:** Offers higher assurance of data confidentiality and integrity.



Confidential Space is designed for handling highly sensitive workloads, especially in regulated industries or scenarios involving multi-party collaborations where data privacy is paramount.

## Architecture references for confidential analytics, AI, and federated learning

You can implement confidential computing on Google Cloud to address the following use cases:

  * Confidential analytics
  * Confidential AI
  * Confidential federated learning



The following sections provide more information about the architecture for these use cases, including examples for financial and healthcare businesses.

### Confidential analytics architecture for healthcare institutions

The confidential analytics architecture demonstrates how multiple healthcare institutions (such as providers, biopharmaceutical, and research institutions) can work together to accelerate drug research. This architecture uses confidential computing techniques to create a digital clean room for running confidential collaborative analytics.

This architecture has the following benefits:

  * **Enhanced insights:** Collaborative analytics lets health organizations gain broader insights and decrease time to market for enhanced drug discovery.
  * **Data privacy:** Sensitive transaction data remains encrypted and is never exposed to other participants or the TEE, ensuring confidentiality.
  * **Regulatory compliance:** The architecture helps health institutions comply with data protection regulations by maintaining strict control over their data.
  * **Trust and collaboration:** The architecture enables secure collaboration between competing institutions, fostering a collective effort to discover drugs.



The following diagram shows this architecture.

![Diagram of confidential analytics architecture for healthcare institutions.](https://docs.cloud.google.com/static/architecture/security/images/confidential-computing-analytics-architecture.svg)

The key components in this architecture include the following:

  * **TEE OLAP aggregation server:** A secure, isolated environment where machine learning model training and inference occur. Data and code within the TEE are protected from unauthorized access, even from the underlying operating system or cloud provider.
  * **Collaboration partners:** Each participating health institution has a local environment that acts as an intermediary between the institution's private data and the TEE.
  * **Provider-specific encrypted data:** Each healthcare institution stores its own private, encrypted patient data that includes electronic health records. This data remains encrypted during the analytics process, which ensures data privacy. The data is only released to the TEE after validating the attestation claims from the individual providers.
  * **Analytics client:** Participating health institutions can run confidential queries against their data to gain immediate insights.



### Confidential AI architecture for financial institutions

This architectural pattern demonstrates how financial institutions can collaboratively train a fraud detection model while using fraud labels to preserve the confidentiality of their sensitive transaction data. The architecture uses confidential computing techniques to enable secure, multi-party machine learning.

This architecture has the following benefits:

  * **Enhanced fraud detection:** Collaborative training uses a larger, more diverse dataset, leading to a more accurate and effective fraud detection model.
  * **Data privacy:** Sensitive transaction data remains encrypted and is never exposed to other participants or the TEE, ensuring confidentiality.
  * **Regulatory compliance:** The architecture helps financial institutions comply with data protection regulations by maintaining strict control over their data.
  * **Trust and collaboration:** This architecture enables secure collaboration between competing institutions, fostering a collective effort to combat financial fraud.



The following diagram shows this architecture.

![Diagram of confidential analytics architecture for financial institutions.](https://docs.cloud.google.com/static/architecture/security/images/confidential-computing-financial-architecture.svg)

The key components of this architecture include the following:

  * **TEE OLAP aggregation server:** A secure, isolated environment where machine learning model training and inference occur. Data and code within the TEE are protected from unauthorized access, even from the underlying operating system or cloud provider.
  * **TEE model training:** The global fraud base model is packaged as containers to run the ML training. Within the TEE, the global model is further trained using the encrypted data from all participating banks. The training process employs techniques like federated learning or secure multi-party computation to ensure that no raw data is exposed.
  * **Collaborator partners:** Each participating financial institution has a local environment that acts as an intermediary between the institution's private data and the TEE.
  * **Bank-specific encrypted data:** Each bank holds its own private, encrypted transaction data that includes fraud labels. This data remains encrypted throughout the entire process, ensuring data privacy. The data is only released to the TEE after validating the attestation claims from individual banks.
  * **Model repository:** A pre-trained fraud detection model that serves as the starting point for collaborative training.
  * **Global fraud trained model and weights (symbolized by the green line):** The improved fraud detection model, along with its learned weights, is securely exchanged back to the participating banks. They can then deploy this enhanced model locally for fraud detection on their own transactions.



### Confidential federated learning architecture for financial institutions

Federated learning offers an advanced solution for customers who value stringent data privacy and data sovereignty. The confidential federated learning architecture provides a secure, scalable, and efficient way to use data for AI applications. This architecture brings the models to the location where the data is stored, rather than centralizing the data in a single location, thereby reducing the risks associated with data leakage.

This architectural pattern demonstrates how multiple financial institutions can collaboratively train a fraud detection model while preserving the confidentiality of their sensitive transaction data with fraud labels. It uses federated learning along with confidential computing techniques to enable secure, multi-party machine learning without training data movement.

This architecture has the following benefits:

  * **Enhanced data privacy and security:** Federated learning enables data privacy and data locality by ensuring that sensitive data remains at each site. Additionally, financial institutions can use privacy preserving techniques such as homomorphic encryption and differential privacy filters to further protect any transferred data (such as the model weights).
  * **Improved accuracy and diversity:** By training with a variety of data sources across different clients, financial institutions can develop a robust and generalizable global model to better represent heterogeneous datasets.
  * **Scalability and network efficiency:** With the ability to perform training at the edge, institutions can scale federated learning across the globe. Additionally, institutions only need to transfer the model weights rather than entire datasets, which enables efficient use of network resources.



The following diagram shows this architecture.

![Diagram of confidential federated learning architecture.](https://docs.cloud.google.com/static/architecture/security/images/confidential-computing-fl-architecture.svg)

The key components of this architecture include the following:

  * **Federated server in the TEE cluster:** A secure, isolated environment where the federated learning server orchestrates the collaboration of multiple clients by first sending an initial model to the federated learning clients. The clients perform training on their local datasets, then send the model updates back to the federated learning server for aggregation to form a global model.
  * **Federated learning model repository:** A pre-trained fraud detection model that serves as the starting point for federated learning.
  * **Local application inference engine:** An application that executes tasks, performs local computation and learning with local datasets, and submits results back to federated learning server for secure aggregation.
  * **Local private data:** Each bank holds its own private, encrypted transaction data that includes fraud labels. This data remains encrypted throughout the entire process, ensuring data privacy.
  * **Secure aggregation protocol (symbolized by the dotted blue line):** The federated learning server doesn't need to access any individual bank's update to train the model; it requires only the element-wise weighted averages of the update vectors, taken from a random subset of banks or sites. Using a secure aggregation protocol to compute these weighted averages helps ensure that the server can learn only that one or more banks in this randomly selected subset wrote a given word, but not which banks, thereby preserving the privacy of each participant in the federated learning process.
  * **Global fraud-trained model and aggregated weights (symbolized by the green line):** The improved fraud detection model, along with its learned weights, is securely sent back to the participating banks. The banks can then deploy this enhanced model locally for fraud detection on their own transactions.



## What's next

  * Read [Confidential AI: Intel seeks to overcome AI's data protection problem](https://www.thinkdigitalpartners.com/news/2024/07/18/confidential-ai-intel-seeks-to-overcome-ais-data-protection-problem/).

  * Read [The Present and Future of Confidential Computing](https://www.darkreading.com/cloud-security/the-present-and-future-of-confidential-computing).

  * View [Enabling secure multi-party collaboration with confidential computing by Keith Moyer (Google) | OC3](https://youtu.be/FGJeP2-PDnQ) (YouTube).

  * View [What's new in confidential computing?](https://www.youtube.com/watch?v=NFvrcPc0aX0) (YouTube).

  * Implement [Confidential Computing](https://docs.cloud.google.com/confidential-computing/docs/confidential-computing-overview) and [Confidential Space](https://docs.cloud.google.com/confidential-computing/confidential-space/docs/confidential-space-overview) in your environment.

  * Learn more about the [fundamentals of Confidential Computing on Google Cloud](https://codelabs.developers.google.com/codelabs/confidential-space#0).

  * Learn more about [enabling more private generative AI](https://developers.googleblog.com/en/enabling-more-private-gen-ai/).




## Contributors

  * [Arun Santhanagopalan](https://www.linkedin.com/in/arunneoz) | Head of Technology and Incubation, Google Cloud
  * [Pablo Rodriguez](https://www.linkedin.com/in/pablorr/) | Technical Director, Office of CTO
  * [Vineet Dave](https://www.linkedin.com/in/vineet-dave/) | Head of Technology and Incubation, Google Cloud



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-12-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-12-20 UTC."],[],[]] 
