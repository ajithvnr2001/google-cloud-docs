---
url: https://docs.cloud.google.com/architecture/framework/security/implement-preemptive-cyber-defense/
title: Implement preemptive cyber defense \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:53.257314+00:00
---

# Implement preemptive cyber defense  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/security/implement-preemptive-cyber-defense/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Implement preemptive cyber defense Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-02-05 UTC

This principle in the security pillar of the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) provides recommendations to build robust cyber-defense programs as part of your overall security strategy.

This principle emphasizes the use of threat intelligence to proactively guide your efforts across the core cyber-defense functions, as defined in [The Defender's Advantage: A guide to activating cyber defense](https://cloud.google.com/security/resources/defenders-advantage).

## Principle overview

When you defend your system against cyber attacks, you have a significant, underutilized advantage against attackers. As [the founder of Mandiant states](https://cloud.google.com/security/mandiant), "You should know more about your business, your systems, your topology, your infrastructure than any attacker does. This is an incredible advantage." To help you use this inherent advantage, this document provides recommendations about proactive and strategic cyber-defense practices that are mapped to the Defender's Advantage framework.

## Recommendations

To implement preemptive cyber defense for your cloud workloads, consider the recommendations in the following sections:

  * Integrate the functions of cyber defense
  * Use the Intelligence function in all aspects of cyber defense
  * Understand and capitalize on your defender's advantage
  * Validate and improve your defenses continuously
  * Manage and coordinate cyber-defense efforts



### Integrate the functions of cyber defense

This recommendation is relevant to all of the [focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security).

The Defender's Advantage framework identifies six critical functions of cyber defense: _Intelligence_ , _Detect_ , _Respond_ , _Validate_ , _Hunt_ , and _Mission Control._ Each function focuses on a unique part of the cyber-defense mission, but these functions must be well-coordinated and work together to provide an effective defense. Focus on building a robust and integrated system where each function supports the others. If you need a phased approach for adoption, consider the following suggested order. Depending on your current cloud maturity, resource topology, and specific threat landscape, you might want to prioritize certain functions.

  1. **Intelligence** : The Intelligence function guides all the other functions. Understanding the threat landscape—including the most likely attackers, their tactics, techniques, and procedures (TTPs), and the potential impact—is critical to prioritizing actions across the entire program. The Intelligence function is responsible for stakeholder identification, definition of intelligence requirements, data collection, analysis and dissemination, automation, and the creation of a cyber threat profile.
  2. **Detect and Respond** : These functions make up the core of active defense, which involves identifying and addressing malicious activity. These functions are necessary to act on the intelligence that's gathered by the intelligence function. The Detect function requires a methodical approach that aligns detections to attacker TTPs and ensures robust logging. The Respond function must focus on initial triage, data collection, and incident remediation.
  3. **Validate** : The Validate function is a continuous process that provides assurance that your security control ecosystem is up-to-date and operating as designed. This function ensures that your organization understands the attack surface, knows where vulnerabilities exist, and measures the effectiveness of controls. Security validation is also an important component of the detection engineering lifecycle and must be used to identify detection gaps and create new detections.
  4. **Hunt** : The Hunt function involves proactively searching for active threats within an environment. This function must be implemented when your organization has a baseline level of maturity in the Detect and Respond functions. The Hunt function expands the detection capabilities and helps to identify gaps and weaknesses in controls. The Hunt function must be based on specific threats. This advanced function benefits from a foundation of robust intelligence, detection, and response capabilities.
  5. **Mission Control** : The Mission Control function acts as the central hub that connects all of the other functions. This function is responsible for strategy, communication, and decisive action across your cyber-defense program. It ensures that all of the functions are working together and that they're aligned with your organization's business goals. You must focus on establishing a clear understanding of the purpose of the Mission Control function before you use it to connect the other functions.



### Use the Intelligence function in all aspects of cyber defense

This recommendation is relevant to all of the [focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security).

This recommendation highlights the Intelligence function as a core part of a strong cyber-defense program. Threat intelligence provides knowledge about threat actors, their TTPs, and indicators of compromise (IOCs). This knowledge should inform and prioritize actions across all cyber-defense functions. An intelligence-driven approach helps you align defenses to meet the threats that are most likely to affect your organization. This approach also helps with efficient allocation and prioritization of resources.

The following Google Cloud products and features help you take advantage of threat intelligence to guide your security operations. Use these features to identify and prioritize potential threats, vulnerabilities, and risks, and then plan and implement appropriate actions.

  * [Google Security Operations (Google SecOps)](https://cloud.google.com/security/products/security-operations) helps you store and analyze security data centrally. Use Google SecOps to map logs into a common model, enrich the logs, and link the logs to timelines for a comprehensive view of attacks. You can also create detection rules, set up IoC matching, and perform threat-hunting activities. The platform also provides curated detections, which are predefined and managed rules to help identify threats. Google SecOps can also integrate with [Mandiant frontline intelligence](https://cloud.google.com/security/products/threat-intelligence). Google SecOps uniquely integrates industry-leading AI, along with [threat intelligence from Mandiant](https://docs.cloud.google.com/chronicle/docs/detection) and [Google VirusTotal](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/virustotal). This integration is critical for threat evaluation and understanding who is targeting your organization and the potential impact.

  * [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview) , which is powered by Google AI, enables security professionals to efficiently assess, investigate, and respond to security issues across multiple cloud environments. The security professionals who can benefit from Security Command Center include security operations center (SOC) analysts, vulnerability and posture analysts, and compliance managers. Security Command Center enriches security data, assesses risk, and prioritizes vulnerabilities. This solution provides teams with the information that they need to address high-risk vulnerabilities and to remediate active threats.

  * [Chrome Enterprise Premium](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview) offers threat and data protection, which helps to protect users from exfiltration risks and prevents malware from getting onto enterprise-managed devices. Chrome Enterprise Premium also provides visibility into unsafe or potentially unsafe activity that can happen within the browser.

  * Network monitoring, through tools like [Network Intelligence Center](https://docs.cloud.google.com/network-intelligence-center), provides visibility into network performance. Network monitoring can also help you detect unusual traffic patterns or detect data transfer amounts that might indicate an attack or data exfiltration attempt.




### Understand and capitalize on your defender's advantage

This recommendation is relevant to all of the [focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security).

As mentioned earlier, you have an advantage over attackers when you have a thorough understanding of your business, systems, topology, and infrastructure. To capitalize on this knowledge advantage, utilize this data about your environments during cyberdefense planning.

Google Cloud provides the following features to help you proactively gain visibility to identify threats, understand risks, and respond in a timely manner to mitigate potential damage:

  * Chrome Enterprise Premium helps you enhance security for enterprise devices by protecting users from exfiltration risks. It extends [Sensitive Data Protection services](https://cloud.google.com/security/products/sensitive-data-protection) into the browser, and prevents malware. It also offers features like protection against malware and phishing to help prevent exposure to unsafe content. In addition, it gives you control over the installation of extensions to help prevent unsafe or unvetted extensions. These capabilities help you establish a secure foundation for your operations.

  * Security Command Center provides a continuous [risk engine](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn) that offers comprehensive and ongoing risk analysis and management. The risk engine feature enriches security data, assesses risk, and prioritizes vulnerabilities to help fix issues quickly. Security Command Center enables your organization to proactively identify weaknesses and implement mitigations.

  * Google SecOps centralizes security data and provides enriched logs with timelines. This enables defenders to proactively identify active compromises and adapt defenses based on attackers' behavior.

  * Network monitoring helps identify irregular network activity that might indicate an attack and it provides early indicators that you can use to take action. To help proactively protect your data from theft, continuously monitor for data exfiltration and use the provided tools.




### Validate and improve your defenses continuously

This recommendation is relevant to all of the [focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security).

This recommendation emphasizes the importance of targeted testing and continuous validation of controls to understand strengths and weaknesses across the entire attack surface. This includes validating the effectiveness of controls, operations, and staff through methods like the following:

  * [Penetration tests](https://cloud.google.com/security/resources/datasheets/penetration-testing#penetration-testing)
  * [Red-blue team](https://services.google.com/fh/files/blogs/google_ai_red_team_digital_final.pdf) and [purple team](https://cloud.google.com/security/resources/datasheets/consulting-services-continuous-purple-team-assessment) exercises
  * [Tabletop exercises](https://cloud.google.com/security/resources/datasheets/consulting-services-tabletop-exercise)



You must also actively search for threats and use the results to improve detection and visibility. Use the following tools to continuously test and validate your defenses against real-world threats:

  * Security Command Center provides a continuous risk engine to evaluate vulnerabilities and prioritize remediation, which enables ongoing evaluation of your overall security posture. By prioritizing issues, Security Command Center helps you to ensure that resources are used effectively.

  * Google SecOps offers threat-hunting and curated detections that let you proactively identify weaknesses in your controls. This capability enables continuous testing and improvement of your ability to detect threats.

  * Chrome Enterprise Premium provides threat and data protection features that can help you to address new and evolving threats, and continuously update your defenses against exfiltration risks and malware.

  * Cloud Next Generation Firewall (Cloud NGFW) provides network monitoring and data-exfiltration monitoring. These capabilities can help you to validate the effectiveness of your current security posture and identify potential weaknesses. Data-exfiltration monitoring helps you to validate the strength of your organization's data protection mechanisms and make proactive adjustments where necessary. When you integrate threat findings from Cloud NGFW with Security Command Center and Google SecOps, you can optimize network-based threat detection, optimize threat response, and automate playbooks. 




### Manage and coordinate cyber-defense efforts

This recommendation is relevant to all of the [focus areas](https://docs.cloud.google.com/architecture/framework/security#focus_areas_of_cloud_security).

As described earlier in Integrate the functions of cyber defense, the Mission Control function interconnects the other functions of the cyber-defense program. This function enables coordination and unified management across the program. It also helps you coordinate with other teams that don't work on cybersecurity. The Mission Control function promotes empowerment and accountability, facilitates agility and expertise, and drives responsibility and transparency.

The following products and features can help you implement the Mission Control function:

  * Security Command Center acts as a central hub for coordinating and managing your cyber-defense operations. It brings tools, teams, and data together, along with the built-in Google SecOps response capabilities. Security Command Center provides clear visibility into your organization's security state and enables the identification of security misconfigurations across different resources.
  * Google SecOps provides a platform for teams to respond to threats by mapping logs and creating timelines. You can also define detection rules and search for threats.
  * [Google Workspace](https://workspace.google.com/security/) and Chrome Enterprise Premium help you to manage and control end-user access to sensitive resources. You can define granular access controls based on user identity and the context of a request.
  * Network monitoring provides insights into the performance of network resources. You can import network monitoring insights into Security Command Center and Google SecOps for centralized monitoring and correlation against other timeline based data points. This integration helps you to detect and respond to potential network usage changes caused by nefarious activity.
  * Data-exfiltration monitoring helps to identify possible data loss incidents. With this feature, you can efficiently mobilize an incident response team, assess damages, and limit further data exfiltration. You can also improve current policies and controls to ensure data protection.



### Product summary

The following table lists the products and features that are described in this document and maps them to the associated recommendations and security capabilities.

Google Cloud product | Applicable recommendations  
---|---  
Google SecOps |  **Use the Intelligence function in all aspects of cyber defense** : Enables threat hunting and IoC matching, and integrates with Mandiant for comprehensive threat evaluation.  **Understand and capitalize on your defender's advantage** : Provides curated detections and centralizes security data for proactive compromise identification.  **Validate and improve your defenses continuously** : Enables continuous testing and improvement of threat detection capabilities.  **Manage and coordinate cyber-defense efforts through Mission Control** : Provides a platform for threat response, log analysis, and timeline creation.   
Security Command Center |  **Use the Intelligence function in all aspects of cyber defense** : Uses AI to assess risk, prioritize vulnerabilities, and provide actionable insights for remediation.  **Understand and capitalize on your defender's advantage** : Offers comprehensive risk analysis, vulnerability prioritization, and proactive identification of weaknesses.  **Validate and improve your defenses continuously** : Provides ongoing security posture evaluation and resource prioritization.  **Manage and coordinate cyber-defense efforts through Mission Control** : Acts as a central hub for managing and coordinating cyber-defense operations.   
Chrome Enterprise Premium |  **Use the Intelligence function in all aspects of cyber defense** : Protects users from exfiltration risks, prevents malware, and provides visibility into unsafe browser activity.  **Understand and capitalize on your defender's advantage** : Enhances security for enterprise devices through data protection, malware prevention, and control over extensions.  **Validate and improve your defenses continuously** : Addresses new and evolving threats through continuous updates to defenses against exfiltration risks and malware.  **Manage and coordinate cyber-defense efforts through Mission Control** : Manage and control end-user access to sensitive resources, including granular access controls.   
Google Workspace |  **Manage and coordinate cyber-defense efforts through Mission Control** : Manage and control end-user access to sensitive resources, including granular access controls.   
Network Intelligence Center |  **Use the Intelligence function in all aspects of cyber defense** : Provides visibility into network performance and detects unusual traffic patterns or data transfers.   
Cloud NGFW |  **Validate and improve your defenses continuously** : Optimizes network-based threat detection and response through integration with Security Command Center and Google SecOps.   
  
[ Previous arrow_back  Implement shift-left security  ](https://docs.cloud.google.com/architecture/framework/security/implement-shift-left-security)

[ Next Use AI securely and responsibly  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/security/use-ai-securely-and-responsibly)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-02-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-02-05 UTC."],[],[]] 
