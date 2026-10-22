---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/aws-waf/
title: Integrate AWS WAF with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:24.772345+00:00
---

# Integrate AWS WAF with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/aws-waf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate AWS WAF with Google SecOps

This document describes how to integrate AWS WAF with Google Security Operations (Google SecOps).

## Use cases

The **AWS WAF** integration helps you secure your web applications by allowing you to:

  * **Automate IP blocking** : Automatically add malicious IP addresses detected by Google SecOps to AWS WAF IP Sets to block traffic at the network edge.
  * **Manage access control lists (ACLs)** : Dynamically create and update Web ACLs to respond to emerging threats.
  * **Orchestrate global and regional security** : Manage rules for both regional resources (like ALBs) and global resources (Amazon CloudFront) from a single interface.



## Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
AWS Access Key ID | String | N/A | Yes | AWS Access Key ID to use in integration.  
AWS Secret Key | Password | N/A | Yes | AWS Secret Key to use in integration.  
AWS Default Region | String | N/A | Yes | AWS default region to use in integration, for example us-west-2. The `Regional` scope in AWS WAF corresponds to the region set here. The `CloudFront` scope is global and does not rely on this region, but resources created under `Regional` are scoped to this value. To manage AWS WAF resources across multiple AWS regions, you must configure a separate integration instance for each region.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Test the connectivity to AWS WAF.

**Important:** This action verifies connectivity only to the `Regional` AWS WAF service endpoint corresponding to the `AWS Default Region` set in the integration parameters. Successful execution confirms that the `AWS Access Key ID` and `AWS Secret Key` are valid for that region. It does not test connectivity to the global `CloudFront` scope. 

To verify connectivity to the `CloudFront` scope, configure the integration and run the List Web ACLs action with `Scope` set to `CloudFront`.

#### Parameters

N/A

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful:_ "Successfully connected to the AWS WAF server with the provided connection parameters!" **The action should fail and stop a playbook execution:** _If not successful:_ "Failed to connect to the AWS WAF server! Error is {0}".format(exception.stacktrace) | General  
  
### Create IP Set

Create an IP Set in AWS WAF, based on entities.

IP Set is created in the following format:
    
    
    Siemplify_NAME_IP Type`
    

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Name | String | N/A | Yes | Specify the name of the IP set. Note: action will create an IP set in the following format: Siemplify_{Name}_{IP Type}. The name must have 1-128 characters. Valid characters: A-Z, a-z, 0-9, - (hyphen), and _ (underscore).  
Scope | DDL | CloudFront Possible values:

  * CloudFront
  * Regional
  * Both

| Yes | Specify the scope for the creation of IP sets. If "Both" is selected, the action will create an IP set in Regional and Amazon CloudFront scopes. `CloudFront` is a global scope for resources used with Amazon CloudFront. `Regional` refers to the specific AWS region configured in the `AWS Default Region` integration parameter.  
Description | String | N/A | No | Specify the description for the IP set.  
Tags | CSV | N/A | No | Specify additional tags that should be added to the IP set. Format: key_1:value_1,key_2:value_1.  
  
#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
    "Regional": ["IPv4_set", "IPv6_set"]
    "Cloudfront":  ["IPv4_set", "IPv6_set"]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful and at least one of the provided entities were used to create an IP set (is_success = true):_ "Successfully created {0} {1} IP Set '{2}' in AWS WAF with the following IPs: \n {3}".format("Regional"/"Cloudfront", "IPv4"/"IPv6", full_name, entity.identifier list) _If fail to use specific entities(is_success = true):_ "Action was not able to use the following IPs in order to create AWS WAF IP Set\n: {0}".format([entity.identifier]) _If fail to use all entities (is_success = false):_ "No IP Sets were created. Reason: None of the provided IP entities were valid." _If All Sets Already exist (is_success=false) or if only partially sets already exist (is_success=true):_ "The following {0} IP Pattern Sets '{1}' already exist: \n.".format("Regional/CloudFront", list_of_full_names) **The action should fail and stop a playbook execution:** _If fatal error, like wrong credentials, no connection to server, other:_ "Error executing action "Create IP Set". Reason: {0}''.format(error.Stacktrace) |   
  
### Add IP To IP Set

Add IP addresses to the IP Set in AWS WAF.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
IP Set Names | CSV | N/A | Yes | Specify the comma-separated list of IP set names. Example: name_1,name_2  
Scope | DDL | CloudFront Possible values:

  * CloudFront
  * Regional
  * Both

| Yes | Specify the scope of the IP set. If "Both" is selected, the action will add IP addresses to IP sets in `Regional` and `CloudFront` scopes. `CloudFront` is a global scope for resources used with Amazon CloudFront. `Regional` refers to the specific AWS region configured in the `AWS Default Region` integration parameter.  
  
#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful and at least one IP addresses was added to one IP set(is_success = true):_ "Successfully added the following IPs to the {0} IP Set '{1}' in AWS WAF: \n {2}".format("Regional"/"Cloudfront", full_name, entity.identifier list) _If fail to add specific entities to one of the IP Sets(is_success = true):_ "Action was not able to add the following IPs to the {0} IP Set '{1}' in AWS WAF\n: {2}".format("Regional"/"Cloudfront", full_name,[entity.identifier]) _If fail to find one of the IP sets (is_success = true):_ "Action wasn't able to find the following '{0}' IP Sets in the AWS WAF:\n {1}".format("Regional"/Cloudfront",list of IP sets that were not found in that scope) _If fail to find all of the provided IP sets in the selected scope or scopes (is_success=false):_ "Action didn't find the provided IP sets." **The action should fail and stop a playbook execution:** _if fatal error, SDK error, like wrong credentials, no connection to server, other:_ "Error executing action "Add IP To IP Set". Reason: {0}''.format(error.Stacktrace) | General  
  
### Create Regex Pattern Set

Create a regular expression pattern set in AWS WAF based on entities.

The regular expression pattern set can only contain 10 patterns for every set and there can only be 10 regular expression pattern sets in total.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Name | String | N/A | Yes | Specify the name of the regular expression pattern set. Note: The name must have 1-128 characters. Valid characters: A-Z, a-z, 0-9, - (hyphen), and _ (underscore).  
Scope | DDL | CloudFront Possible values:

  * CloudFront
  * Regional
  * Both

| Yes | Specify the scope for the creation of regular expression pattern sets. If "Both" is selected, the action creates a regular expression pattern set in `Regional` and `CloudFront` scopes. `CloudFront` is a global scope for resources used with Amazon CloudFront. `Regional` refers to the specific AWS region configured in the `AWS Default Region` integration parameter.  
Description | String | N/A | No | Specify the description for the regular expression pattern set.  
Tags | CSV | N/A | No | Specify additional tags that should be added to the regular expression pattern set. Format: key_1:value_1,key_2:value_1.  
Domain Pattern | Checkbox | Checked | No | If enabled, the action retrieves the domain part out of URLs and create a regular expression pattern based on them, such as `http://test.com/folder` is converted to `^(http|https)(:\/\/)(\Qtest.com\E).*".format(entity)`.   
IP Pattern | Checkbox | Checked | No | If enabled, the action constructs a proper regular expression pattern out of IP address instead of using raw value, such as `10.0.0.1` is converted into `^(http|https)(:\/\/)(\Q10.0.1\E).*".format(entity)`.   
  
#### Run On

This action runs on the following entities:

  * IP Address
  * URL



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
    "Regional": "Regex_set"
    "Cloudfront": "Regex_set"
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _if successful and at least one of the provided entities were used to create an regular expression set (is_success = true):_ "Successfully created {0} Regex Pattern Set '{1}' in AWS WAF with the following entities: \n {2}".format("Regional"/"Cloudfront", name, entity.identifier list) _If more than 10 entities are going to be used to create a regular expression pattern set:_ "Action wasn't able to create regular expression pattern sets with all of the provided entities, because the limit is exceeded. The following entities were skipped: {0}".format(entity.identifier) _If Set Already exists (is_success=false):_ "{0} Regex Pattern Set '{1}' already exists.".format("Regional/CloudFront", name) **The action should fail and stop a playbook execution:** _If fatal error, SDK error, like wrong credentials, no connection to server, other:_ "Error executing action "Create Regex Pattern Set". Reason: {0}''.format(error.Stacktrace) | General  
  
### Create Web ACLs

Create a Web ACL in AWS WAF.

**Note:** You can have only 100 Web ACLs per region.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Name | String | N/A | Yes | Specify the name of the Web ACL. Note: The name must have 1-128 characters. Valid characters: A-Z, a-z, 0-9, - (hyphen), and _ (underscore).  
Rule Source Type | DDL | IP SetPossible valueIP SetRule Group | Yes | Specify what rule type should be used.  
Rule Source Name | String | N/A | Yes | Specify the name of the source, which should be used for Web ACL. If "Rule Source Type" is "IP Set", the action will search for IP Sets with that name. If "Rule Source Type" is "Rule Group", the action will search for Rule Groups with that name.  
Scope | DDL | CloudFront Possible values:

  * CloudFront
  * Regional
  * Both

| Yes | Specify the scope for the creation of the Web ACL. If "Both" is selected, the action will create a Web ACL in `Regional` and `CloudFront` scopes. `CloudFront` is a global scope for resources used with Amazon CloudFront. `Regional` refers to the specific AWS region configured in the `AWS Default Region` integration parameter.  
Enable Sampled Requests | Checkbox | Unchecked | Yes | If enabled, AWS WAF will store a sampling of the web requests that match the rules.  
Enable CloudWatch Metrics | Checkbox | Unchecked | Yes | If enabled, the associated resource sends metrics to CloudWatch.  
CloudWatch Metric Name | Checkbox | Unchecked | Yes | Specify the name of the CloudWatch Metric. Note: The name must have 1-128 characters. Valid characters: A-Z, a-z, 0-9, - (hyphen), and _ (underscore).  
Default Action | DDL | Allow Possible values:

  * Allow
  * Block

| Yes | Specify the default action for requests that don't match any rules.  
IP Set Action | DDL | Block Possible value:

  * Allow
  * Block
  * Count

| No | Specify the action for rules that are based on the IP set.  
Rule Priority | Integer | N/A | Yes | Specify the priority of the rule. Priorities in Web ACL should be unique.  
Description | String | N/A | No | Specify the description for the Web ACL.  
Tags | CSV | N/A | No | Specify additional tags that should be added to the Web ACL. Format: key_1:value_1,key_2:value_1.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
    "Regional": "Web_Acl_name"
    "Cloudfront": "Web_Acl_name"
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successfully listed available IP Sets(is_success = true) and "Scope" == "Both":_ "Successfully created Web ACL {0} in `Regional` and `CloudFront` scopes.".format(name) _If successfully listed available IP Sets(is_success = true) and "Scope" == "Regional":_ "Successfully created Web ACL {0} in Regional.".format(name) _If successfully listed available IP Sets(is_success = true) and "Scope" == "Cloudfront":_ "Successfully created Web ACL {0} in Cloudfront scope.".format(name) If the Web ACL exists:Print "The Web ACL {} already exists in {} scope.".format(web ACL name, scope). _If IP Set / Rule Group wasn't found:_ "Action wasn't able to create Web ACL. Reason: {0} {1} wasn't found in AWS WAF".format("IP Set/Rule Group", Rule Source Name) **The action should fail and stop a playbook execution:** _if fatal error, SDK error, like wrong credentials, no connection to server, other:_ "Error executing action "Create Web ACL". Reason: {0}''.format(error.Stacktrace) |   
  
### Add Rule To Web ACL

Add a rule based on IP Sets or Rule Groups to Web ACL in AWS WAF. The Web ACL can contain a maximum of 1,500 rule.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Web ACL Names | CSV | N/A | Yes | Specify the comma-separated list of Web ACL names. Example: name_1,name_2  
  
  
Rule Source Type | DDL | IP SetPossible values:

  * IP Set
  * Rule Group

| Yes | Specify what rule type should be used.  
Rule Source Name | String | N/A | Yes | Specify the name of the source, which should be used for Web ACL. If "Rule Source Type" is "IP Set", the action will search for IP Sets with that name. If "Rule Source Type" is "Rule Group", the action will search for Rule Groups with that name.  
Scope | DDL | CloudFront Possible values:

  * CloudFront
  * Regional
  * Both

| Yes | Specify the scope for the new rules. If "Both" is selected, the action will add a Rule to a Web ACL in `Regional` and `CloudFront` scopes. `CloudFront` is a global scope for resources used with Amazon CloudFront. `Regional` refers to the specific AWS region configured in the `AWS Default Region` integration parameter.  
Rule Priority | Integer | N/A | Yes | Specify the priority of the rule. Priorities in Web ACL should be unique.  
IP Set Action | DDL | BlockPossible value:

  * Allow
  * Block
  * Count

| No | Specify the action for rules that are based on the IP set.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _if successful and at least one rule was added to one Web ACL(is_success = true):_ "Successfully added a rule to the following {0} Web ACLs '{1}' in AWS WAF.".format("Regional"/"Cloudfront", list of name) _If fail to find one of the Web ACLs(is_success = true):_ "Action wasn't able to find the following '{0}' Web ACLs in the AWS WAF:\n {1}".format("Regional"/Cloudfront", list of Web ACLs that were not found in that scope) _If rule with name already exists per Web ACL in Scope (is_success=true):_ "Action wasn't able to add {0} rules to the Web ACL in AWS WAF. Reason: {0} with name '{1}' already exists in the following Web ACLs:\n{2}".format( rule source type, rule source name, list Web ACL with scope - structure {0} - {1}.format(scope, web acl name)) **The action should fail and stop a playbook execution:** _If fatal error, SDK error, like wrong credentials, no connection to server, other:_ "Error executing action "Add Rule To Web ACL". Reason: {0}''.format(error.Stacktrace) | General  
  
### Create Rule Group

Create a rule group in AWS WAF.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Name | String | N/A | Yes | Specify the name of the rule group. Note: The name must have 1-128 characters. Valid characters: A-Z, a-z, 0-9, - (hyphen), and _ (underscore).  
Scope | DDL | CloudFront Possible values:

  * CloudFront
  * Regional
  * Both

| Yes | Specify the scope for the creation of the rule group. If "Both" is selected, the action will create a Rule Group in `Regional` and `CloudFront` scopes. `CloudFront` is a global scope for resources used with Amazon CloudFront. `Regional` refers to the specific AWS region configured in the `AWS Default Region` integration parameter.  
Capacity | Integer | 100 | Yes | Specify the capacity of the rule group. Note: you can't change the capacity after the group is created. Maximum is 1500.  
Enable Sampled Requests | Checkbox | Unchecked | Yes | If enabled, AWS WAF will store a sampling of the web requests that match the rules.  
Enable CloudWatch Metrics | Checkbox | Unchecked | Yes | If enabled, the associated resource sends metrics to CloudWatch.  
CloudWatch Metric Name | Checkbox | Unchecked | Yes | Specify the name of the CloudWatch Metric. Note: The name must have 1-128 characters. Valid characters: A-Z, a-z, 0-9, - (hyphen), and _ (underscore).  
Description | String | N/A | No | Specify the description for the Rule Group.  
Tags | CSV | N/A | No | Specify additional tags that should be added to the Rule Group. Format: key_1:value_1,key_2:value_1.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successfully listed available IP Sets(is_success = true) and "Scope" == "Both":_ "Successfully created Rule Group {0} in `Regional` and `CloudFront` scopes.".format(name) >_If successfully listed available IP Sets(is_success = true) and "Scope" == "Regional":_ "The Rule Group {} already exists in {} scope.".format(web ACL name, scope). _If successfully listed available IP Sets(is_success = true) and "Scope" == "Cloudfront":_ "Successfully created Rule Group {0} in Cloudfront scope.".format(name) _If the Rule Group exists:_ "Successfully created Rule Group {0} in Cloudfront scope.".format(name) _If the creation of the Rule Group Fails_ "Action was not able to create Rule Group {} in {} scope".format(web ACL name, scope). **The action should fail and stop a playbook execution:** _If fatal error, SDK error, like wrong credentials, no connection to server, other:_ "Error executing action "Create Rule Group". Reason: {0}''.format(error.Stacktrace) | General  
  
### Add Entity To Regex Pattern Set

Add string patterns based on entities to the regular expression pattern set in AWS WAF.

The regular expression pattern set can only contain 10 patterns in every set.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Regex Pattern Set Names | CSV | N/A | Yes | Specify the comma-separated list of regular expression pattern set names, such as `name_1,name_2`.  
Scope | DDL | CloudFront Possible values:

  * CloudFront
  * Regional
  * Both

| Yes | Scope of the regular expression pattern set. If "Both" is selected, the action adds patterns based on entities to regular expression pattern sets in both `Regional` and `CloudFront` scopes. `CloudFront` is a global scope for resources used with Amazon CloudFront. `Regional` refers to the specific AWS region configured in the `AWS Default Region` integration parameter.  
Domain Pattern | Checkbox | Checked | No | If enabled, the action retrieves the domain part out of URLs and creates a regular expression pattern based on them, such as `http://test.com/folder` is converted to `^(http|https)(:\/\/)(\Qtest.com\E).*".format(entity)`.   
IP Pattern | Checkbox | Checked | No  
| If enabled, the action constructs a proper regular expression pattern out of IP address instead of using raw value, such as `10.0.0.1` is converted into `^(http|https)(:\/\/)(\Q10.0.1\E).*".format(entity)`.   
  
#### Run On

This action runs on the following entities:

  * IP Address
  * URL



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _if successful and at least one entity was added to one regular expression pattern set(is_success = true):_ "Successfully added the following entity patterns to the {0} Regex Pattern Set '{1}' in AWS WAF: \n {2}".format("Regional"/"Cloudfront", name, list of entity patterns) _If more than 10 entities are going to be used to create a regular expression pattern set:_ "Action wasn't able to add patterns to {0} Regex Pattern Set {1} based on all of the provided entities, because the limit is exceeded. The following entities were skipped: {2}".forma("Regional"/"Cloudfront", name, entity.identifier) _If fail to find one of the sets (is_success = true):_ "Action wasn't able to find the following '{0}' Regex Pattern Sets in the AWS WAF:\n {1}".format("Regional"/Cloudfront",list of regular expression pattern sets that were not found in that scope) _If fail to find all of the provided sets in the selected scope or scopes (is_success=false):_ "Action didn't find the provided Regex Pattern sets." **The action should fail and stop a playbook execution:** _if fatal error, SDK error, like wrong credentials, no connection to server, other:_ "Error executing action "Add Entity To Regex Pattern Set". Reason: {0}''.format(error.Stacktrace) | General  
  
### Add Pattern To Regex Pattern Set

Add string patterns to the regular expression pattern set in AWS WAF.

The regular expression pattern set can only contain 10 patterns for every set.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Regex Pattern Set Names | CSV | N/A | Yes | Specify the comma-separated list of regular expression pattern set names, such as `name_1,name_2`.  
Patterns | CSV | N/A | Yes | Specify the comma-separated list of patterns to add to the regular expression pattern set, such as `pattern_1,pattern_2`.  
Scope | DDL | CloudFront Possible values:

  * CloudFront
  * Regional
  * Both

| Yes | Scope of the regular expression pattern set. If "Both" is selected, the action adds patterns based on entities to regular expression pattern sets in both `Regional` and `CloudFront` scopes. `CloudFront` is a global scope for resources used with Amazon CloudFront. `Regional` refers to the specific AWS region configured in the `AWS Default Region` integration parameter.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful and at least one pattern was added to one regular expression pattern set(is_success = true):_ "Successfully added the following patterns to the {0} Regex Pattern Set '{1}' in AWS WAF: \n {2}".format("Regional"/"Cloudfront", name, list of patterns) _If fail to find one of the sets (is_success = true):_ t "Action wasn't able to find the following '{0}' Regex Pattern Sets in the AWS WAF:\n {1}".format("Regional"/Cloudfront",list of regular expression pattern sets that were not found in that scope). _If fail to find all of the provided sets in the selected scope or scopes (is_success=false):_ "Action didn't find the provided Regex Pattern sets." **The action should fail and stop a playbook execution:** _if fatal error, SDK error, like wrong credentials, no connection to server, other:_ "Error executing action "Add Pattern To Regex Pattern Set". Reason: {0}''.format(error.Stacktrace) | General  
  
### Remove Rule From Web ACL

Remove a rule from Web ACL in AWS WAF.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Web ACL Names | CSV |  | Yes | Specify the comma-separated list of Web ACL names. Example: name_1,name_2  
  
  
Scope | DDL | CloudFront Possible values:

  * CloudFront
  * Regional
  * Both

| Yes | Specify the scope for the removal of the web acl. If "Both" is selected, the action will remove a Web ACL in `Regional` and `CloudFront` scopes. `CloudFront` is a global scope for resources used with Amazon CloudFront. `Regional` refers to the specific AWS region configured in the `AWS Default Region` integration parameter.  
Rule Name | String | N/A  
| Yes | Specify the name of the rule that should be deleted.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **if successful and at least one rule was removed from one Rule Group:** print "Successfully removed a rule from the following {0} Web ACLs '{1}' in AWS WAF.".format("Regional"/"Cloudfront", list of names) **if unsuccessful for one Rule Group:** print "Action wasn't able to remove a rule from the following {0} Web ACLs '{1}' in AWS WAF.".format("Regional"/"Cloudfront", list of names) **if unsuccessful for one Web ACL, because rule wasn't found in one ACL:** print "Action wasn't able to find the specified rule in the following {0} Web ACLs '{1}' in AWS WAF.".format("Regional"/"Cloudfront", list of names Web ACL) **If fail to find one of the Rule Group:** Print "Action wasn't able to find the following '{0}' Web ACLs in the AWS WAF:\n {1}".format("Regional"/Cloudfront", list of Rule Group that were not found in that scope) **If fail to find all of the provided sets in the desired scope or scopes:** Print "Action didn't find the provided Web ACLs." **The action should fail and stop a playbook execution:** **if fatal error, SDK error, like wrong credentials, no connection to server, other:** print "Error executing action "Remove Rule From Web ACL". Reason: {0}''.format(error.Stacktrace) | General  
  
### List Web ACLs

List available Web ACLs in AWS WAF.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Scope | DDL | CloudFront Possible values:

  * CloudFront
  * Regional
  * Both

|  | Specify the scope for the listing of Web ACLs. `CloudFront` is a global scope for resources used with Amazon CloudFront. `Regional` refers to the specific AWS region configured in the `AWS Default Region` integration parameter.  
Max Web ACLs To Return | Integer | 50 | No | Specify how many Web ACLs to return. Default is 50. Maximum is 100.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    [
        {
            "Name": "example",
            "Id": "ID",
            "Description": "example",
            "LockToken": "7e76581b-f152-4448-aafe-b733a33c8fa2",
            "ARN": "arn:aws:wafv2:us-east-1:regional/ipset/example/ID"
        }
    ]
    "CloudFront": [
        {
            "Name": "example",
            "Id": "ID",
            "Description": "example",
            "LockToken": "7e76581b-f152-4448-aafe-b733a33c8fa2",
            "ARN": "arn:aws:wafv2:us-east-1:regional/ipset/example/ID"
        }
    ]
    

##### Case Wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If successfully listed available IP Sets and "Scope" == "Both":** "Successfully listed available Web ACLs in Regional and Cloudfront scopes." **If successfully listed available IP Sets(is_success = true) and "Scope" == "Regional":** "Successfully listed available Web ACLs in Regional scope." **If successfully listed available IP Sets(is_success = true) and "Scope" == "Cloudfront":** "Successfully listed available Web ACLs in Cloudfront scope." **If no available values(is_success = false) and "Scope" == "Both":** "No available Web ACLs were found in Regional and Cloudfront scopes." **If no available values (is_success = false) and "Scope" == "Regional":** "No available Web ACLs were found in Regional scope." **If no available values(is_success = false) and "Scope" == "Cloudfront":** "No available Web ACLs were found in Cloudfront scope."  
**The action should fail and stop a playbook execution:** **if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "List Web ACLs". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table  (if "Scope" == "Regional" or "Both") | **Table Name:** Regional Rule ACLs **Table Columns:**

  * Name
  * ID
  * Description
  * Lock Token
  * ARN

| General  
Case Wall Table (if "Scope" == "CloudFront" or "Both") | **Table Name:** CloudFront Rule ACLs **Table Columns:**

  * Name 
  * ID
  * Description
  * Lock Token
  * ARN

| General  
  
### Remove Rule From Rule Group

Remove a rule from the rule group in AWS WAF.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Rule Group Names | CSV |  | Yes | Specify the comma-separated list of Rule Group names. Example: name_1,name_2  
Scope | DDL | CloudFront Possible values:

  * CloudFront
  * Regional
  * Both

| Yes | Specify the scope for the removal of the rule group. If "Both" is selected, the action will remove a Rule Group in `Regional` and `CloudFront` scopes. `CloudFront` is a global scope for resources used with Amazon CloudFront. `Regional` refers to the specific AWS region configured in the `AWS Default Region` integration parameter.  
Rule Name | String | N/A  
| Yes | Specify the name of the rule that should be deleted.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If successful and at least one rule was removed from one Rule Group:** "Successfully removed a rule from the following {0} Rule Groups '{1}' in AWS WAF.".format("Regional"/"Cloudfront", list of names) **If unsuccessful for one Rule Group:** "Action wasn't able to remove a rule from the following {0} Rule Groups '{1}' in AWS WAF.".format("Regional"/"Cloudfront", list of names) **If unsuccessful for one Rule Group, because rule wasn't found in one Rule Group:** "Action wasn't able to find the specified rule in the following {0} Rule Groups '{1}' in AWS WAF.".format("Regional"/"Cloudfront", list of rule group names) **If fail to find one of the Rule Group:** "Action wasn't able to find the following '{0}' Rule Groups in the AWS WAF:\n {1}".format("Regional"/Cloudfront", list of Rule Group that were not found in that scope) **If fail to find all of the provided sets in the desired scope or scopes:** "Action didn't find the provided Rule Groups." **The action should fail and stop a playbook execution:** **If a fatal error, SDK error, like wrong credentials, no connection to the server, other is reported:** "Error executing action "Remove Rule From Rule Group". Reason: {0}''.format(error.Stacktrace) | General  
  
### List Rule Groups

List available rule groups in AWS WAF.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Scope | DDL | CloudFront Possible values:

  * CloudFront
  * Regional
  * Both

|  | Specify the scope for the listing of Rule Groups. `CloudFront` is a global scope for resources used with Amazon CloudFront. `Regional` refers to the specific AWS region configured in the `AWS Default Region` integration parameter.  
Max Rule Groups To Return | Integer | 50 | No | Specify how many Rule Groups to return. Default is 50. Maximum is 100.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    [
        {
            "Name": "example",
            "Id": "ID",
            "Description": "example",
            "LockToken": "7e76581b-f152-4448-aafe-b733a33c8fa2",
            "ARN": "arn:aws:wafv2:us-east-1:regional/ipset/example/ID"
        }
    ]
    "CloudFront": [
        {
            "Name": "example",
            "Id": "ID",
            "Description": "example",
            "LockToken": "7e76581b-f152-4448-aafe-b733a33c8fa2",
            "ARN": "arn:aws:wafv2:us-east-1:regional/ipset/example/ID"
        }
    ]
    

##### Case Wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If successfully listed available IP Sets and "Scope" == "Both":** "Successfully listed available Rule groups in Regional and Cloudfront scopes." **If successfully listed available IP Sets and "Scope" == "Regional":** "Successfully listed available Rule groups in Regional scope." **If successfully listed available IP Sets and "Scope" == "Cloudfront":** "Successfully listed available Rule groups in Cloudfront scope."> **If no available values and "Scope" == "Both":** "No available Rule groups were found in Regional and Cloudfront scopes." **If no available values and "Scope" == "Regional":** "No available Rule groups were found in Regional scope." **If no available values and "Scope" == "Cloudfront":** "No available Rule groups were found in Cloudfront scope." **The action should fail and stop a playbook execution:** **If a fatal error, SDK error, like wrong credentials, no connection to the server, other is reported:** "Error executing action "List Rule Groups". Reason: {0}''.format(error.Stacktrace) | General  
**Case Wall Table** **(if "Scope" == "Regional" or "Both")** | **Table Name:** Regional Rule Groups **Table Columns:**

  * Name
  * ID
  * Description
  * Lock Token
  * ARN

| General  
**Case Wall Table** **(if "Scope" == "CloudFront" or "Both")** | **Table Name:** CloudFront Rule Groups **Table Columns:**

  * Name
  * ID
  * Description
  * Lock Token
  * ARN

| General  
  
### List IP Sets

List available IP Sets in AWS WAF.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Scope | DDL | CloudFront Possible values:

  * CloudFront
  * Regional
  * Both

|  | Specify the scope for the listing of IP sets. `CloudFront` is a global scope for resources used with Amazon CloudFront. `Regional` refers to the specific AWS region configured in the `AWS Default Region` integration parameter.  
Max IP Sets To Return | Integer | 50 | No | Specify how many IP sets to return. Default is 50. Maximum is 100.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    [
        {
            "Name": "example",
            "Id": "ID",
            "Description": "example",
            "LockToken": "7e76581b-f152-4448-aafe-b733a33c8fa2",
            "ARN": "arn:aws:wafv2:us-east-1:regional/ipset/example/ID"
        }
    ]
    "CloudFront": [
        {
            "Name": "example",
            "Id": "ID",
            "Description": "example",
            "LockToken": "7e76581b-f152-4448-aafe-b733a33c8fa2",
            "ARN": "arn:aws:wafv2:us-east-1:regional/ipset/example/ID"
        }
    ]
    

##### Case Wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If successfully listed available IP Sets and "Scope" == "Both":** "Successfully listed available IP sets in Regional and Cloudfront scopes." **If successfully listed available IP Sets and "Scope" == "Regional":** "Successfully listed available IP sets in Regional scope." **If successfully listed available IP Sets and "Scope" == "Cloudfront":** "Successfully listed available IP sets in Cloudfront scope." **If no available values and "Scope" == "Both":** Print "No available IP Sets were found in Regional and Cloudfront scopes." **If no available values and "Scope" == "Regional":** "No available IP Sets were found in Regional scope." **If no available values and "Scope" == "Cloudfront":** "No available IP Sets were found in Cloudfront scope." **The action should fail and stop a playbook execution:** **If a fatal error, SDK error, like wrong credentials, no connection to the server, other is reported:** "Error executing action "List IP Sets". Reason: {0}''.format(error.Stacktrace) | General  
**Case Wall Table** **(if "Scope" == "Regional" or "Both")** | **Table Name:** Regional Rule Groups **Table Columns:**

  * Name
  * ID
  * Description
  * Lock Token
  * ARN

| General  
**Case Wall Table** **(if "Scope" == "CloudFront" or "Both")** | **Table Name:** CloudFront Rule Groups **Table Columns:**

  * Name
  * ID
  * Description
  * Lock Token
  * ARN

| General  
  
### Remove Pattern From Regex Pattern Set

Remove patterns from the regular expression set in AWS WAF.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Regex Pattern Set Names | CSV |  | Yes | Specify the comma-separated list of regular expression set names, such as `name_1,name_2`.  
Patterns | CSV |  | Yes | Specify the comma-separated list of patterns that should be removed from the regular expression set, such as `pattern_1,pattern_2`.  
Scope | DDL | CloudFront Possible values:

  * CloudFront
  * Regional
  * Both

| Yes | Scope of the set. If "Both" is selected, the action removes patterns from regular expression sets in both `Regional` and `CloudFront` scopes. `CloudFront` is a global scope for resources used with Amazon CloudFront. `Regional` refers to the specific AWS region configured in the `AWS Default Region` integration parameter.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If successful and at least one pattern set was removed from one regex set:** "Successfully removed the following patterns from the {0} Regex Pattern Set '{1}' in AWS WAF: \n {2}".format("Regional"/"Cloudfront", full_name, list of entity patterns) **If pattern never existed in that Pattern Set:** "The following patterns were not found in the {0} Regex Pattern Set '{1}' in AWS WAF: \n {2}".format("Regional"/"Cloudfront", full_name, list of patterns) **If fail to remove all patterns on all Regex Pattern Sets:** "No patterns were removed from the provided Regex Pattern Sets." **If fail to find one of the Pattern sets:** "Action wasn't able to find the following '{0}' Regex Pattern Sets in the AWS WAF:\n {1}".format("Regional"/Cloudfront",list of sets that were not found in that scope) **If fail to find all of the provided Regex Pattern sets in the desired scope or scopes:** "Action didn't find the provided Regex Pattern sets." **The action should fail and stop a playbook execution:** **If a fatal error, SDK error, like wrong credentials, no connection to server, other is reported:** "Error executing action "Remove Pattern From Regex Pattern Set". Reason: {0}''.format(error.Stacktrace) | General  
  
### Remove IP From IP Set

Remove IP addresses from the IP Set in AWS WAF.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
IP Set Names | CSV |  | Yes | Specify the comma-separated list of IP set names. Example: name_1,name_2  
Scope | DDL | CloudFront Possible values:

  * CloudFront
  * Regional
  * Both

| Yes | Specify the scope of the IP set. If "Both" is selected, the action will remove IP addresses from IP sets in `Regional` and `CloudFront` scopes. `CloudFront` is a global scope for resources used with Amazon CloudFront. `Regional` refers to the specific AWS region configured in the `AWS Default Region` integration parameter.  
  
#### Run On

This action runs on IP entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If successful and at least one IP addresses was removed from one IP set:** "Successfully removed the following IPs from the {0} IP Set '{1}' in AWS WAF: \n {2}".format("Regional"/"Cloudfront", full_name, entity.identifier list) **If IPs never existed in that IP Set:** "The following IPs were not a part of the {0} IP Set '{1}' in AWS WAF: \n {2}".format("Regional"/"Cloudfront", full_name, entity.identifier list) **If fail to remove all entities on all IP sets:** "No IPs were removed from the provided IP Sets." **If fail to find one of the IP sets:** P "Action wasn't able to find the following '{0}' IP Sets in the AWS WAF:\n {1}".format("Regional"/Cloudfront",list of IP sets that were not found in that scope) **If fail to find all of the provided IP sets in the desired scope or scopes:** "Action didn't find the provided IP sets." **The action should fail and stop a playbook execution:** **If a fatal error, SDK error, like wrong credentials, no connection to the server, other is reported:** "Error executing action "Remove IP From IP Set". Reason: {0}''.format(error.Stacktrace) | General  
  
### List Regex Pattern Sets

List available regular expression sets in AWS WAF.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Scope | DDL | CloudFront Possible values:

  * CloudFront
  * Regional
  * Both

|  | Specify the scope for the listing of IP sets.  
Max Regex Pattern Sets To Return | Integer | 5 | No | Specify how many regular expression sets to return. Default is 5. Maximum is 10. `CloudFront` is a global scope for resources used with Amazon CloudFront. `Regional` refers to the specific AWS region configured in the `AWS Default Region` integration parameter.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    [
        {
            "Name": "example",
            "Id": "ID",
            "Description": "example",
            "LockToken": "7e76581b-f152-4448-aafe-b733a33c8fa2",
            "ARN": "arn:aws:wafv2:us-east-1:regional/ipset/example/ID"
        }
    ]
    "CloudFront": [
        {
            "Name": "example",
            "Id": "ID",
            "Description": "example",
            "LockToken": "7e76581b-f152-4448-aafe-b733a33c8fa2",
            "ARN": "arn:aws:wafv2:us-east-1:regional/ipset/example/ID"
        }
    ]
    

##### Case Wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If successfully listed available Regex Sets and "Scope" == "Both":** "Successfully listed available Regex Pattern sets in Regional and Cloudfront scopes." **If successfully listed available IP Sets and "Scope" == "Regional":** "Successfully listed available Regex Pattern sets in Regional scope." **If successfully listed available IP Sets and "Scope" == "Cloudfront":** "Successfully listed available Regex Pattern sets in Cloudfront scope." **If no available values and "Scope" == "Both":** "No available Regex Pattern sets were found in Regional and Cloudfront scopes." **If no available values and "Scope" == "Regional":** "No available Regex Pattern sets were found in Regional scope." **If no available values and "Scope" == "Cloudfront":** "No available Regex Pattern sets were found in Cloudfront scope." **The action should fail and stop a playbook execution:** **If a fatal error, SDK error, like wrong credentials, no connection to the server, other is reported:** "Error executing action "List Regex Pattern Sets". Reason: {0}''.format(error.Stacktrace) | General  
**Case Wall Table** **(if "Scope" == "Regional" or "Both")** | **Table Name:** Regional Rule Groups **Table Columns:**

  * Name
  * ID
  * Description
  * Lock Token
  * ARN

| General  
**Case Wall Table** **(if "Scope" == "CloudFront" or "Both")** | **Table Name:** CloudFront Rule Groups **Table Columns:**

  * Name
  * ID
  * Description
  * Lock Token
  * ARN

| General  
  
### Remove Entity From Regex Pattern Set

Remove string patterns based on entities from the regular expression set in AWS WAF.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Regex Pattern Set Names | CSV |  | Yes | Specify the comma-separated list of regular expression set names, such as `name_1,name_2`.  
Scope | DDL | CloudFront Possible values:

  * CloudFront
  * Regional
  * Both

| Yes | Scope of the set. If "Both" is selected, the action removes patterns based on entities from regular expression sets in `Regional` and `CloudFront` scopes. `CloudFront` is a global scope for resources used with Amazon CloudFront. `Regional` refers to the specific AWS region configured in the `AWS Default Region` integration parameter.  
Domain Pattern | Checkbox | True | No | If enabled, the action retrieves the domain part from URLs and searches for a regular expression based on them in the regular expression set, such as `http://test.com/folder` turns to `^(http|https)(:\/\/)(\Qtest.com\E).*`.  
IP Pattern | Checkbox | True | No | If enabled, the action searches for a regular expression out of IP address instead of the raw value, such as `10.0.0.1` turns to `^(http|https)(:\/\/)(\Q10.0.1\E).*`.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * URL



#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If successful and at least one entity was removed from one IP set:** "Successfully removed the following entity patterns from the {0} Regex Pattern Set '{1}' in AWS WAF: \n {2}".format("Regional"/"Cloudfront", full_name, list of entity patterns) **If entity never existed in that Regex Pattern Set:** "The following patterns were not found in the {0} Regex Pattern Set '{1}' in AWS WAF: \n {2}".format("Regional"/"Cloudfront", full_name, list of entity patterns) **If fail to remove all entities on all IP sets:** "No patterns were removed from the provided Regex Pattern Sets." **If fail to find one of the IP sets:** "Action wasn't able to find the following '{0}' Regex Pattern Sets in the AWS WAF:\n {1}".format("Regional"/Cloudfront",list of IP sets that were not found in that scope) **If fail to find all of the provided Regex Pattern sets in the desired scope or scopes:** "Action didn't find the provided Regex Pattern sets." **The action should fail and stop a playbook execution:** **If a fatal error, SDK error, like wrong credentials, no connection to the server, other is reported:** "Error executing action "Remove Entity From Regex Pattern Set". Reason: {0}''.format(error.Stacktrace) | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
