---
url: https://docs.cloud.google.com/access-context-manager/docs/example-yaml-file/
title: Example YAML for an access level \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T21:27:13.890569+00:00
---

# Example YAML for an access level  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/example-yaml-file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/access-context-manager/docs/apis)



Send feedback 

#  Example YAML for an access level Stay organized with collections  Save and categorize content based on your preferences. 

The following example includes all attributes that can be specified when you create a YAML file for an access level. A YAML file is only necessary if you are creating or modifying an access level using the `gcloud` command-line tool.

**Note:** Conditions must include at least one attribute. If they contain more than one attribute, the attributes can be combined as an **AND** operation (all must be true) or as a **NAND** operation (at least one must be false) to determine whether the condition is met. You can use any combination of attributes required for your use case. The comments provided for these attributes apply only if you include the attribute in your YAML file.

Although you can include identities in the `members` attribute, Google recommends against doing so. See `identities` in [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) for how to allow perimeters to communicate with each other.
    
    
    # Attributes can be included in any order in the condition
    - devicePolicy:
      # Must include at least one of the following:
        allowedEncryptionStatuses:
        # Must include at least one of the following:
          - ENCRYPTION_UNSUPPORTED
          - ENCRYPTED
          - UNENCRYPTED
        osConstraints:
        # Must include at least one of the following:
          - osType: DESKTOP_CHROME_OS
            minimumVersion: 11316.165.0
            # minimumVersion must be formatted as x.x.x
            requireVerifiedChromeOs: true
          - osType: DESKTOP_MAC
          - osType: DESKTOP_WINDOWS
            # minimumVersion is not required
        requireScreenlock: true
        # requireScreenlock defaults to false if not included
        requireAdminApproval: true
        # requireAdminApproval defaults to false if not included
        requireCorpOwned: true
        # requireCorpOwned defaults to false if not included
      ipSubnetworks:
      # Must include one or more IPv4 and IPv6 CIDRs
        - 252.0.2.0/24
        - 2001:db8::/32
      regions:
      # Must include one or more regions as ISO 3166-1 alpha-2 codes
        - US
        - CH
        - SG
      requiredAccessLevels:
      # Must include one or more existing access levels
      # Must be formatted as accessPolicies/policy-name/accessLevels/level-name
        - accessPolicies/247332951433/accessLevels/Device_Trust
      members:
      # Must include one or more valid IAM users or service accounts
        - user:exampleuser@example.com
        - serviceAccount:exampleaccount@example.iam.gserviceaccount.com
      negate: true
      # negate is not required and can only be included with other attributes
      # If negate is set to true, the condition is evaluated as a NAND operation
      # (at least one attribute in the condition must be false for the condition
      # to be met).
    
    # You can include more than one condition in the YAML file
    - ipSubnetworks:
        - 176.0.2.0/24
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
