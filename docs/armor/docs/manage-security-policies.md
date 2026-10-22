---
url: https://docs.cloud.google.com/armor/docs/manage-security-policies/
title: Manage Cloud Armor security policies \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:55.733831+00:00
---

# Manage Cloud Armor security policies  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/manage-security-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Manage Cloud Armor security policies Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage Google Cloud Armor security policies and filter incoming traffic to your application. Cloud Armor security policies help protect your web applications and services from distributed denial-of-service (DDoS) attacks and other threats from the internet. Enforcing a strong security posture requires managing your security policies through creation, testing, and consolidation. To create or view security policies, see [Create and view Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/configure-security-policies).

## Manage security policies

The following sections describe how you can list, update, delete, or test your security policies.

### List security policies

Follow the steps in this section to list Cloud Armor security policies in your project.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Armor policies** page.

[Go to Cloud Armor policies](https://console.cloud.google.com/net-security/securitypolicies/list)

  2. To view a policy, in the list of policies, click the name of that specific policy.




###  gcloud 
    
    
    gcloud compute security-policies list
    

For example:
    
    
    gcloud compute security-policies list
    

Output: 
    
    
    NAME: my-policy
    REGION: us-central1
    

For more information, see [`gcloud compute security-policies list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies/list).

### Update security policies

The steps in this section describe how you can update a Cloud Armor security policy. You can modify the policy's description, modify the default rule, change the target backend service, or add rules.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Armor policies** page.

[Go to Cloud Armor policies](https://console.cloud.google.com/net-security/securitypolicies/list)

  2. Find the name of the policy that you want to update in the list of policies and click more_vert**Menu** for that policy.

     * To update the description or the default rule action, select **Edit** , make your changes, and then click **Update**.
     * To add a rule, select **Add rule** , and then follow the steps in Add rules to a security policy.
     * To replace the target backend service, select **Apply policy to target** , click **Add Target** , select a target, and then click **Add**.



###  gcloud 

To update a security policy, use the following Google Cloud CLI steps:

  * To update a rule, see Update a single rule in a security policy.
  * To add a rule, see Add rules to a security policy.
  * To delete a rule, see Delete rules from a security policy.
  * To update multiple rules in a single atomic update, see Atomically update multiple rules in a security policy.
  * To update non-rule fields (such as the description), see Export security policies and Import security policies.



### Delete security policies

This section describes how you can delete a Cloud Armor security policy. Remove all backend services from the policy before you delete it.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Armor policies** page.

[Go to Cloud Armor policies](https://console.cloud.google.com/net-security/securitypolicies/list)

  2. Select the checkbox next to the policy that you want to delete.

  3. In the upper-right corner of the page, click delete**Delete**.




###  gcloud 

Use `gcloud compute security-policies delete NAME`. Replace `NAME` with the name of the security policy:
    
    
    gcloud compute security-policies delete NAME
    

### Test security policies

We recommend that you deploy all new rules in preview mode, then examine your [request logs](https://docs.cloud.google.com/armor/docs/request-logging), to verify that the policies and rules are behaving as expected.

## Manage security policy rules

The following sections describe how you can list, add, update, or delete security policy rules.

### List the rules in a security policy

Follow the steps in this section to list the rules in a Cloud Armor security policy.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Armor policies** page.

[Go to Cloud Armor policies](https://console.cloud.google.com/net-security/securitypolicies/list)

  2. Click the name of the specific security policy. The **Policy details** page shows the policy rules on the **Rules** tab.




###  gcloud 

Use the following `gcloud` command to list all of the rules in a security policy:
    
    
    gcloud compute security-policies describe NAME \
    

Use the following `gcloud` command to list all of the rules in a single security policy in a specified region along with a description of the policy:
    
    
    gcloud compute security-policies describe NAME \
      --region REGION
    

Use the following `gcloud` command to describe a rule:
    
    
    gcloud compute security-policies rules describe PRIORITY \
        --security-policy POLICY_NAME
    

For example, the following command describes the rule with a priority of 1000 in the security policy `my-policy`:
    
    
    gcloud compute security-policies rules describe 1000 \
        --security-policy my-policy
    

Output: 
    
    
    action: deny(403)
    description: block traffic from 192.0.2.0/24 and 198.51.100.0/24
    kind: compute#securityPolicyRule
    match:
      srcIpRanges:
      - '192.0.2.0/24'
      - '198.51.100.0/24'
    preview: false
    priority: 1000
    

For more information, see [`gcloud compute security-policies describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies/describe).

### Add rules to a security policy

Follow the steps in this section to add rules to a Cloud Armor security policy.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Armor policies** page.

[Go to Cloud Armor policies](https://console.cloud.google.com/net-security/securitypolicies/list)

  2. Click the name of the security policy to open the **Policy details** page.

  3. In the middle of the page, click the **Rules** tab.

  4. Click **Add rule**.

  5. Optional: Enter a description of the rule.

  6. Select the mode:

     * **Basic mode** : allow or deny traffic based on IP addresses or IP ranges.
     * **Advanced mode** : allow or deny traffic based on rule expressions.
  7. In the **Match** field, specify the conditions that the rule applies to:

     * **Basic mode** : enter from one (1) to 10 IP address ranges to match the rule. You can add a maximum of 10 IP address ranges. For limits, see [Cloud Armor quotas and limits](https://docs.cloud.google.com/armor/quotas#limits).

     * **Advanced mode** :

       * **Match condition builder** ([Preview](https://cloud.google.com/products#product-launch-stages)): use the visual builder to create expressions without writing raw CEL code. Combine and group conditions, and apply string transformations. See Use the match condition builder.
       * **Match condition editor** : enter an expression to evaluate against incoming requests. For more information, see the [custom rules language reference](https://docs.cloud.google.com/armor/docs/rules-language-reference).
     * The following expression matches requests from the IP address `1.2.3.4` that contain the string `example` in the `User-Agent` header:
           
           inIpRange(origin.ip, '1.2.3.4/32') && has(request.headers['user-agent']) && request.headers['user-agent'].contains('example')
           

     * The following expression matches requests that have a cookie with a specific value:
           
           has(request.headers['cookie']) && request.headers['cookie'].contains('cookie_name=cookie_value')
             

     * The following expression matches requests from the region `AU`:
           
           origin.region_code == 'AU'
             

     * The following expression matches requests from the region `AU` that aren't in the specified IP range:
           
           origin.region_code == "AU" && !inIpRange(origin.ip, '1.2.3.0/24')
             

     * The following expression matches requests if the URI matches a regular expression:
           
           request.path.matches('/example_path/')
             

     * The following expression matches requests if the `user-id` header contains a Base64-encoded value that, when decoded, contains a specific string:
           
           has(request.headers['user-id']) && request.headers['user-id'].base64Decode().contains('myValue')
             

     * The following expression uses a preconfigured expression set to match against SQLi attacks:
           
           evaluatePreconfiguredWaf('sqli-stable')
             

  8. In the **Action** list, select **Allow** or **Deny**.

  9. If you are configuring a deny rule, select a **Deny status** message.

  10. To enable preview mode for the rule, select **Enable**.

  11. In the **Priority** field, enter a positive integer.

  12. Click **Add**.




###  gcloud 

Use the command `gcloud compute security-policies rules create PRIORITY`. Replace `PRIORITY` with the priority of the rule in the policy:
    
    
    gcloud compute security-policies rules create PRIORITY \
        --security-policy POLICY_NAME \
        --description DESCRIPTION \
        --src-ip-ranges IP_RANGES | --expression EXPRESSION \
        --action=[ allow | deny-403 | deny-404 | deny-502 ] \
        --preview
    

For example, the following command adds a rule with a priority of 1000 to block traffic from IP address ranges 192.0.2.0/24 and 198.51.100.0/24:
    
    
    gcloud compute security-policies rules create 1000 \
        --security-policy my-policy \
        --description "block traffic from 192.0.2.0/24 and 198.51.100.0/24" \
        --src-ip-ranges "192.0.2.0/24","198.51.100.0/24" \
        --action "deny-403"
    

Use the `--expression` flag to specify a condition. The following command adds a rule to allow traffic from the IP address `1.2.3.4` that contains the string `example` in the `User-Agent` header:
    
    
    gcloud compute security-policies rules create 1000 \
        --security-policy my-policy \
        --expression "inIpRange(origin.ip, '1.2.3.4/32') && has(request.headers['user-agent']) && request.headers['user-agent'].contains('example')" \
        --action allow \
        --description "Block User-Agent 'example'"
    

The following command adds a rule to block requests if the request's cookie contains a specific value:
    
    
    gcloud compute security-policies rules create 1000 \
        --security-policy my-policy \
        --expression "has(request.headers['cookie']) && request.headers['cookie'].contains('80=BLAH')" \
        --action deny-403 \
        --description "Cookie Block"
    

The following command adds a rule to block requests from the region `AU`:
    
    
    gcloud compute security-policies rules create 1000 \
        --security-policy my-policy \
        --expression "origin.region_code == 'AU'" \
        --action deny-403 \
        --description "AU block"
    

The following command adds a rule to block requests from the region `AU` that are not in the specified IP range:
    
    
    gcloud compute security-policies rules create 1000 \
        --security-policy my-policy \
        --expression "origin.region_code == "AU" && !inIpRange(origin.ip, '1.2.3.0/24')" \
        --action deny-403 \
        --description "country and IP block"
    

The following command adds a rule to block requests with a URI that matches a regular expression:
    
    
    gcloud compute security-policies rules create 1000 \
        --security-policy my-policy \
        --expression "request.path.matches('/example_path/')" \
        --action deny-502 \
        --description "regex block"
    

The following command adds a rule to block requests if the Base64 decoded value of the `user-id` header contains a specific value:
    
    
    gcloud compute security-policies rules create 1000 \
        --security-policy my-policy \
        --expression "has(request.headers['user-id']) && request.headers['user-id'].base64Decode().contains('myValue')" \
        --action deny-403 \
        --description "country and IP block"
    

The following command adds a rule that uses a preconfigured expression set to mitigate SQLi attacks:
    
    
    gcloud compute security-policies rules create 1000 \
        --security-policy my-policy \
        --expression "evaluatePreconfiguredWaf('sqli-stable')" \
        --action deny-403
    

### Update a single rule in a security policy

This section describes how you can update a single rule in a Cloud Armor security policy. To atomically update multiple rules, see Atomically update multiple rules in a security policy.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Armor policies** page.

[Go to Cloud Armor policies](https://console.cloud.google.com/net-security/securitypolicies/list)

  2. Click the name of the security policy to open the **Policy details** page.

  3. In the middle of the page, click the **Rules** tab.

  4. Next to the rule that you want to update, click edit**Edit**. The **Edit rule** page is displayed.

  5. Make your changes, and then click **Update**.




###  gcloud 

Use the following command to update a rule. You can update only one security policy at a time:
    
    
    gcloud compute security-policies rules update PRIORITY [ \
        --security-policy POLICY_NAME  \
        --description DESCRIPTION  \
        --src-ip-ranges IP_RANGES  | --expression EXPRESSION \
        --action=[ allow | deny-403 | deny-404 | deny-502 ]  \
        --preview
      ]
      

For example, the following command updates a rule with a priority of 1111 to allow traffic from the IP address range 192.0.2.0/24:
    
    
    gcloud compute security-policies rules update 1111 \
        --security-policy my-policy \
        --description "allow traffic from 192.0.2.0/24" \
        --src-ip-ranges "192.0.2.0/24" \
        --action "allow"
    

For more information about the preceding command, see [`gcloud compute security-policies rules update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/update).

To update the priority of a rule, use the REST API. See [`securityPolicies.patchRule`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/securityPolicies/patchRule).

### Use the match condition builder

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The match condition builder is a visual interface in the Google Cloud console that helps you create complex Cloud Armor rule expressions without writing Common Expression Language (CEL) code. Instead of writing code, you can use the builder's structured UI to combine conditions and group logic, which can help you avoid syntax errors and better visualize your rule structure. The builder supports flat lists and nested logic up to five levels of expressions. Use this tool when you configure rules to help protect multi-cloud backends or hybrid deployments, where you might need to inspect specific request attributes before routing traffic.

#### Features of the match condition builder

The match condition builder includes the following features:

  * **Logic and nesting** : combine multiple conditions using `AND` and `OR` operators. The builder supports grouping and nesting up to five expressions.
  * **String transformations** : for string-based attributes (such as `request.path` or `request.headers`), apply transformations to normalize data before evaluation. Supported transformations include: 
    * Lowercase and Uppercase
    * Base64 Decode
    * URL Decode and URL Decode (Unicode)
    * UTF-8 to Unicode Convert
  * **Bidirectional parsing** : switch between the visual **Match condition builder** and the raw text **Match condition editor**. The UI parses raw CEL code into visual blocks automatically.
  * **Function support** : the builder provides UI controls for function-based expressions, such as preconfigured WAF rules, address groups, and Threat Intelligence.



#### Limitations

The match condition builder is the default interface for advanced rule creation. If an expression contains unsupported logic (such as unknown macros), the builder is disabled. In these cases, use the raw text in **Match condition editor** to edit the rule.

Additionally, the availability of certain expressions in the builder depends on your project's Google Cloud Armor Enterprise tier and the security policy type.

### Atomically update multiple rules in a security policy

You can use the atomic update feature to apply changes to multiple rules in a single update. Single-rule updates might cause unintended behavior like errors because old and new rules might overlap for a short period.

To atomically update multiple rules, export the current security policy to a JSON or YAML file, and then modify it. Use the modified file to create a security policy, and then switch the security policy for the backend services.

###  gcloud 

  1. Export the policy to update, as shown in the following example:
         
         gcloud compute security-policies export my-policy \
             --file-name my-file \
             --file-format yaml
         

The exported policy will look similar to the following example:
         
         description: my description
             fingerprint: PWfLGDWQDLY=
             id: '123'
             name: my-policy
             rules:
             - action: deny(404)
               description: my-rule-1
               match:
                 expr:
                   expression: evaluatePreconfiguredWaf('xss-stable')
                 versionedExpr: SRC_IPS_V1
               preview: false
               priority: 1
             - action: allow
               description: my-rule-2
               match:
                 config:
                   srcIpRanges:
                   - '1.2.3.4'
                 versionedExpr: SRC_IPS_V1
               preview: false
               priority: 2
             - action: deny
               description: default rule
               kind: compute#securityPolicyRule
               match:
                 config:
                   srcIpRanges:
                   - '*'
                 versionedExpr: SRC_IPS_V1
               preview: false
               priority: 2147483647
             selfLink: https://www.googleapis.com/compute/v1/projects/my-project/global/securityPolicies/my-policy
         

  2. Use a text editor to modify the policy. For example, you can modify the priorities of existing rules and add a rule:
         
         description: my description
             fingerprint: PWfLGDWQDLY=
             id: '123'
             name: my-policy
             rules:
             - action: deny(404)
               description: my-rule-1
               match:
                 expr:
                   expression: evaluatePreconfiguredWaf('xss-stable')
                 versionedExpr: SRC_IPS_V1
               preview: false
               priority: 1
             - action: allow
               description: my-new-rule
               match:
                 config:
                   srcIpRanges:
                   - '1.2.3.1'
                 versionedExpr: SRC_IPS_V1
               preview: false
               priority: 10
             - action: allow
               description: my-rule-2
               match:
                 config:
                   srcIpRanges:
                   - '1.2.3.4'
                 versionedExpr: SRC_IPS_V1
               preview: false
               priority: 11
             - action: deny
               description: default rule
               kind: compute#securityPolicyRule
               match:
                 config:
                   srcIpRanges:
                   - '*'
                 versionedExpr: SRC_IPS_V1
               preview: false
               priority: 2147483647
             selfLink: https://www.googleapis.com/compute/v1/projects/my-project/global/securityPolicies/my-policy
         

  3. Create a new Cloud Armor security policy and specify the modified filename and format, as shown in the following example:
         
         gcloud compute security-policies create new-policy \
             --file-name modified-policy \
             --file-format yaml
         

  4. Remove the old security policy from the relevant backend service, as shown in the following example:
         
         gcloud compute backend-services update my-backend \
             --security-policy ""
         

  5. Add the new security policy to the backend service, as shown in the following example:
         
         gcloud compute backend-services update my-backend \
             --security-policy new-policy
         

  6. If the old policy is unused, delete it:
         
         gcloud compute security-policies delete my-policy
         




### Delete rules from a security policy

Follow the steps in this section to delete rules from a Cloud Armor security policy.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Armor policies** page.

[Go to Cloud Armor policies](https://console.cloud.google.com/net-security/securitypolicies/list)

  2. Click the name of the security policy to open the **Policy details** page.

  3. In the middle of the page, on the **Rules** tab, select the checkbox next to the rule that you want to delete.

  4. Click delete**Delete**.




###  gcloud 

Use the following command to remove a rule. You can modify only one security policy at a time, but you can delete multiple rules at once:
    
    
    gcloud compute security-policies rules delete PRIORITY [...] [
        --security-policy POLICY_NAME \
      ]
    

For example:
    
    
    gcloud compute security-policies rules delete 1000 \
        --security-policy my-policy
    

## Attach and remove security policies

The following sections describe how you can attach and remove security policies.

### Attach a security policy to a backend service

Follow the steps in this section to attach a Cloud Armor security policy to a backend service. You can attach a security policy to multiple backend services, but a backend service can have only one of each type of security policy attached to it.

###  Console 

**Caution:** You cannot use the Google Cloud console to attach a security policy to an external proxy Network Load Balancer or classic proxy Network Load Balancer.

  1. In the Google Cloud console, go to the **Cloud Armor policies** page.

[Go to Cloud Armor policies](https://console.cloud.google.com/net-security/securitypolicies/list)

  2. Click the name of the security policy to open the **Policy details** page.

  3. In the middle of the page, click the **Targets** tab.

  4. Click **Apply policy to new target**.

  5. Click **Add Target**.

  6. In the **Target** list, select a target, and then click **Add**.




###  gcloud 

When you attach a backend security policy to a backend service, use the `gcloud compute backend-services` command and the `--security-policy` flag:
    
    
    gcloud compute backend-services update my-backend \
        --security-policy my-policy
    

When you attach an edge security policy to a backend service, use the `gcloud compute backend-services` command and the `--edge-security-policy` flag:
    
    
    gcloud compute backend-services update my-backend \
        --edge-security-policy my-policy
    

### Remove a security policy from a backend service

Follow the steps in this section to remove a Cloud Armor security policy from a backend service.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Armor policies** page.

[Go to Cloud Armor policies](https://console.cloud.google.com/net-security/securitypolicies/list)

  2. Click the name of the security policy to open the **Policy details** page.

  3. In the middle of the page, click the **Targets** tab.

  4. Select the target backend service that you're removing the policy from.

  5. Click **Remove**.

  6. In the **Remove target** message, click **Remove**.




###  gcloud 

When you remove a backend security policy, use the `gcloud compute backend-services` command and the `--security-policy` flag:
    
    
    gcloud compute backend-services update my-backend \
        --security-policy ""
    

When you remove an edge security policy, use the `gcloud compute backend-services` command and the `--edge-security-policy` flag:
    
    
    gcloud compute backend-services update my-backend \
        --edge-security-policy ""
    

### Attach a security policy to a backend bucket

Follow the steps in this section to attach a Cloud Armor edge security policy to a backend bucket. You can attach an edge security policy to multiple backend buckets.

**Note:** You can attach only edge security policies to backend buckets.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Armor policies** page.

[Go to Cloud Armor policies](https://console.cloud.google.com/net-security/securitypolicies/list)

  2. Click the name of the security policy to open the **Policy details** page.

  3. In the middle of the page, click the **Targets** tab.

  4. Click **Apply policy to new target**.

  5. Click **Add Target**.

  6. In the **Target** list, select a target, and then click **Add**.




###  gcloud 

When you attach an edge security policy to a backend bucket, use the `cloud compute backend-buckets` command and the `--edge-security-policy` flag:
    
    
    gcloud compute backend-services update my-bucket \
        --edge-security-policy my-edge-policy
    

### Remove a security policy from a backend bucket

Follow the steps in this section to remove a Cloud Armor edge security policy from a backend bucket.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Armor policies** page.

[Go to Cloud Armor policies](https://console.cloud.google.com/net-security/securitypolicies/list)

  2. Click the name of the security policy to open the **Policy details** page.

  3. In the middle of the page, click the **Targets** tab.

  4. Select the target backend service that you're removing the policy from.

  5. Click **Remove**.

  6. In the **Remove target** message, click **Remove**.




###  gcloud 

When you remove an edge security policy from a backend bucket, use the `cloud compute backend-buckets` command and the `--edge-security-policy` flag:
    
    
    gcloud compute backend-services update my-bucket \
        --edge-security-policy ""
    

## Import and export security policies

The following sections describe how you can import and export security policies.

### Export security policies

You can export a Cloud Armor security policy as a YAML or JSON file by using the Google Cloud CLI. This feature provides the following benefits:

  * **Save a copy for version control or backup** : exporting provides a local copy of your policy. Save this copy in source control systems as a backup or to track changes. You can re-import it later to restore a prior version.

  * **Modify and update policies locally** : modify exported policies offline using a text editor. After making changes, re-import the updated policy to apply your modifications to Cloud Armor.




###  gcloud 

  1. In the following command, `NAME` is the name of the security policy. Valid file formats are YAML and JSON. If you don't specify the file format, Cloud Armor uses YAML.
         
         gcloud compute security-policies export NAME \
             --file-name FILE_NAME  \
             --file-format FILE_FORMAT
         

The following example shows the command to export the `my-policy` security policy to the `my-file` file in the YAML format:
         
         gcloud compute security-policies export my-policy \
             --file-name my-file \
             --file-format yaml
          

The following example shows an exported security policy:
         
         description: my description
         fingerprint: PWfLGDWQDLY=
         id: '123'
         name: my-policy
         rules:
         - action: allow
           description: default rule
           match:
               config:
                 srcIpRanges:
                 - '*'
               versionedExpr: SRC_IPS_V1
             preview: false
             priority: 2147483647
           selfLink: https://www.googleapis.com/compute/v1/projects/my-project/global/securityPolicies/my-policy
           

  2. Modify the exported file with a text editor, and then import it back to Google Cloud by using the `import` command.




### Import security policies

You import Cloud Armor security policies from a YAML or JSON file by using the Google Cloud CLI. You can't use the `import` command to update an existing policy's rules. Instead, update rules individually by using the Update a single rule in a security policy procedure, or all at once by using the Atomically update multiple rules in a security policy procedure.

###  gcloud 

To import security policies, use the following `gcloud compute security-policies import NAME` command.
    
    
    gcloud compute security-policies import NAME \
        --file-name FILE_NAME  \
       [--file-format FILE_FORMAT]
    

For example, the following command updates the policy `my-policy` by importing the file `my-file`.
    
    
    gcloud compute security-policies import my-policy \
        --file-name my-file \
        --file-format json
    

Replace `NAME` with the name of the security policy. If you don't provide the file format, the correct format is assumed based on the file structure. If the structure is invalid, the gcloud CLI returns an error message.

If the policy's [fingerprint](https://docs.cloud.google.com/armor/docs/security-policy-overview#fingerprint) is out of date when you import it, Cloud Armor returns an error. This means the policy was modified since you last exported it. To fix this, use the `describe` command on the policy to get the latest fingerprint. You can use `--format=yaml` or `--format=json` with the `describe` command to make comparison easier. Compare the `rules` section of the `describe` output with the `rules` section in your policy file, merge any differences, and then replace the outdated fingerprint in your file with the latest one from the `describe` output.

**Note:** Exporting and importing security policies is useful for version control and local modification but not for migrating a policy from one project to another.

## List available preconfigured rules

In addition to rules that you configure yourself, Cloud Armor provides preconfigured rules that you can use in your security policies. You can list preconfigured rules to view the predefined application protection rules and signatures such as the [OWASP Core Rule Set](https://coreruleset.org/) that Cloud Armor provides. These rules contain built-in signatures that Cloud Armor evaluates against incoming requests. Add these preconfigured rules to new or existing rules by using the [custom rules language reference](https://docs.cloud.google.com/armor/docs/rules-language-reference).

For more information, see [preconfigured rules](https://docs.cloud.google.com/armor/docs/rules-language-reference#preconfigured-rules).

###  gcloud 

  1. Run the `gcloud compute security-policies list-preconfigured-expression-sets` command:
         
         gcloud compute security-policies list-preconfigured-expression-sets
         

The following example shows the form of the output from the command:
         
         EXPRESSION_SET
         expression-set-1
            RULE_ID                SENSITIVITY
            expression-set-1-id-1  sensitivity-value-1
            expression-set-1-id-2  sensitivity-value-2
         expression-set-2
            alias-1
            RULE_ID                SENSITIVITY
            expression-set-2-id-1  sensitivity-value-1
            expression-set-2-id-2  sensitivity-value-2
         

The following example includes a sample of the actual output from the command. Note that the actual output would include all of the rules that are listed in [Tuning Cloud Armor WAF rules](https://docs.cloud.google.com/armor/docs/rule-tuning).
         
         gcloud compute security-policies list-preconfigured-expression-sets
         
         
         EXPRESSION_SET
         sqli-canary
             RULE_ID                          SENSITIVITY
             owasp-crs-v042200-id942120-sqli  2
             …
         xss-canary
             RULE_ID                         SENSITIVITY
             owasp-crs-v042200-id941110-xss  1
             owasp-crs-v042200-id941120-xss  2
         …
         sourceiplist-fastly
         sourceiplist-cloudflare
         sourceiplist-imperva
         




## What's next

  * [Tune web application firewall (WAF) rules](https://docs.cloud.google.com/armor/docs/rule-tuning)
  * [Troubleshoot issues](https://docs.cloud.google.com/armor/docs/troubleshooting)
  * [Use the custom rules language reference](https://docs.cloud.google.com/armor/docs/rules-language-reference)
  * [Create and view security policies](https://docs.cloud.google.com/armor/docs/configure-security-policies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
