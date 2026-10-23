---
url: https://docs.cloud.google.com/recaptcha/docs/best-practices-oat/
title: Best practices for protection from automated threats \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:44:12.661057+00:00
---

# Best practices for protection from automated threats  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/best-practices-oat/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Best practices for protection from automated threats Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the recommended implementations of Google Cloud Fraud Defense and fraud mitigation strategies to defend against the critical automated threats ([OWASP Automated Threats (OAT) to Web Applications](https://owasp.org/www-project-automated-threats-to-web-applications/)). Enterprise architects and technology stakeholders can review this information to make an informed decision about the Fraud Defense implementation and fraud mitigation strategy for their use case.

This document contains the following information for each type of threat:

  * Optimal implementation of Fraud Defense. This implementation is designed with the relevant features of Fraud Defense for the best fraud protection.

  * Minimal implementation of Fraud Defense. This implementation is designed for a bare minimum of fraud protection.

  * Recommended fraud mitigation strategies.




Choose the implementation and fraud mitigation strategy that best fits your use case. The following factors might influence the implementation and fraud mitigation strategy that you choose:

  * Organization's anti-fraud needs and capabilities.
  * Organization's existing environment.

**Note:** We recommend choosing either the optimal implementation or minimal implementation depending on your organization's anti-fraud needs.

For more information about the fraud mitigation strategies for your use case, [contact our sales team](https://go.chronicle.security/recaptcha-enterprise).

## Carding

Carding is an automated threat where attackers make multiple payment authorization attempts to verify the validity of bulk-stolen payment card data.

### Minimum implementation

  1. Install checkbox site keys on all pages where end users need to enter their credit card information. To learn how to install checkbox site keys, see [Install checkbox site keys (checkbox challenge) on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages-with-checkbox). 

**Note:** Checkbox site keys increase user friction and might affect conversion rates. 

  2. Create assessments for all tokens. To learn how to create assessments, see [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment). 




### Optimal implementation

  1. Install score-based site keys on all pages where end users need to enter their credit card information. Specify an action in the `action` parameter such as `card_entry`. To learn how to install score-based site keys, see [Install score-based site keys (no challenge) on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages). 

  2. Install reCAPTCHA for the payment workflow on your website. To learn how to protect your payment workflow, see [Protect payment workflows](https://docs.cloud.google.com/recaptcha/docs/payment-flows). 

  3. Create assessments for all tokens, and set `expectedAction` to match the value of `action` that you specified when installing the score-based site keys. To learn how to create assessments, see [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment). 

  4. Save all assessment IDs and annotate the assessments that turn into fraudulent purchases or chargebacks as `fraudulent`. To learn how to annotate assessments, see [Annotate an assessment](https://docs.cloud.google.com/recaptcha/docs/annotate-assessment). 




### Fraud mitigation strategy

After you implement Fraud Defense, use one of the following fraud mitigation strategies to protect your website from carding:

  * Install reCAPTCHA for the payment workflow on your website. To learn how to protect your payment workflow, see [Protect payment workflows](https://docs.cloud.google.com/recaptcha/docs/payment-flows). 

  * Configure card management APIs to ensure that the reCAPTCHA tokens are valid and the scores are greater than their threshold value. 

If the scores do not meet or exceed the specified threshold value, do not run a card authorization or allow the end user to use the card. When possible, allow the transaction to proceed at time of purchase, but cancel the transaction later to avoid tipping off the attacker. 

  * When creating assessments, ensure that your assessments meet the following criteria for a successful transaction: 

    * All assessed tokens are valid and have a score greater than a specified threshold value.
    * The value of `expectedAction` matches the value of `action` that you specified when installing the score-based site keys on your web pages. To learn how to verify actions, see [verify actions](https://docs.cloud.google.com/recaptcha/docs/interpret-assessment#verify_action).

If a transaction does not meet these criteria, do not run a card authorization or allow the end user to use the card. When possible, allow the transaction to proceed at time of purchase, but cancel the transaction later to avoid tipping off the attacker. 




## Card cracking

Card cracking is an automated threat where attackers identify missing values for start date, expiration date, and security codes for stolen payment card data by trying different values.

### Minimum implementation

  1. Install checkbox site keys on all pages where end users need to enter their payment details, including both **checkout** and **add payment method** functions. To learn how to install checkbox site keys, see [Install checkbox site keys (checkbox challenge) on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages-with-checkbox). 

**Note:** Checkbox site keys increase user friction and might affect conversion rates. 

  2. Create assessments for all tokens. To learn how to create assessments, see [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment). 




### Optimal implementation

  1. Install score-based site keys on all pages where end users need to enter their payment details. Specify an action in the `action` parameter such as `checkout` or `add_pmtmethod`. To learn how to install score-based site keys, see [Install score-based site keys (no challenge) on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages). 

  2. Install reCAPTCHA for the payment workflow on your website. To learn how to protect your payment workflow, see [Protect payment workflows](https://docs.cloud.google.com/recaptcha/docs/payment-flows). 

  3. Create assessments for all tokens, and set `expectedAction` to match the value of `action` that you specified when installing the score-based site keys. To learn how to create assessments, see [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment). 

  4. Save all assessment IDs and annotate the assessments that turn into fraudulent purchases or chargebacks as `fraudulent`. To learn how to annotate assessments, see [Annotate an assessment](https://docs.cloud.google.com/recaptcha/docs/annotate-assessment). 




### Fraud mitigation strategy

After you implement Fraud Defense, use one of the following fraud mitigation strategies to protect your website from card cracking:

  * Install reCAPTCHA for the payment workflow on your website. To learn how to protect your payment workflow, see [Protect payment workflows](https://docs.cloud.google.com/recaptcha/docs/payment-flows). 

  * Implement a response model and create assessments:

    1. Create and implement a response model that is adjusted for score-based risk.

The following example shows a sample response model: 

       * For low to intermediate score threshold (0.0-0.5), use context-based risk management, such as limiting the number of attempts, and blocking purchases over a specified value.
       * For the highest score threshold (> 0.5), allow the end user to proceed without any challenge.
**Note:** Your score thresholds might vary depending on your users and attackers. We recommend using the reCAPTCHA analytics dashboard to determine the best scores to take action on. 
    2. When creating assessments, ensure that the value of `expectedAction` matches the value of `action` that you specified when installing the score-based site keys on your web pages. If they do not match, do not run a card authorization or allow the end user to use the card. When possible, allow the transaction to proceed at time of purchase, but cancel the transaction later to avoid tipping off the attacker. 




## Credential cracking

Credential cracking is an automated threat where attackers identify valid login credentials by trying different values for usernames and passwords.

### Minimum implementation

  1. Install checkbox site keys on all pages where end users need to enter their credentials, including both **login** and **forgot my password** functions. To learn how to install checkbox site keys, see [Install checkbox site keys (checkbox challenge) on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages-with-checkbox). 

**Note:** Checkbox site keys increase user friction and might affect conversion rates. 

  2. Create assessments for all tokens. To learn how to create assessments, see [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment). 




### Optimal implementation

  1. Install score-based site keys on all pages where end users need to enter their credentials. Specify an action in the `action` parameter such as `login` or `authenticate`. To learn how to install score-based site keys, see [Install score-based site keys (no challenge) on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages). 
  2. Recommended: Implement reCAPTCHA Password defense for all authentication attempts. To learn how to use Password defense, see [Detect password leaks and breached credentials](https://docs.cloud.google.com/recaptcha/docs/check-passwords). 
  3. Optional: To enable blocking of high-volume and low-reCAPTCHA score interactions, integrate reCAPTCHA with a web application firewall (WAF). For example, you can use [reCAPTCHA for WAF and Google Cloud Armor integration](https://docs.cloud.google.com/recaptcha/docs/integration-overview). 
  4. Implement reCAPTCHA account defender to trend end-user behavior across logins and receive additional signals that can indicate an ATO. To learn how to use reCAPTCHA account defender, see [Detect and prevent account-related fraudulent activities](https://docs.cloud.google.com/recaptcha/docs/account-defender). 
  5. Create assessments for all tokens, and set `expectedAction` to match the value of `action` that you specified when installing the score-based site keys. To learn how to create assessments, see [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment). 
  6. Save all Assessment IDs and annotate the assessment that appears fraudulent, such as Account Takeovers (ATOs) or any other fraudulent activity. To learn how to annotate assessments, see [Annotate an assessment](https://docs.cloud.google.com/recaptcha/docs/annotate-assessment). 



### Fraud mitigation strategy

After you implement Fraud Defense, use the following fraud mitigation strategy to protect your website from credential cracking:

  1. Create and implement a response model that is adjusted for score-based risk.

The following example shows a sample response model: 

     * For low to intermediate score threshold (0.0-0.5), challenge the end user with multi-factor authentication through email or SMS.
     * For the highest score threshold (> 0.5), allow the end user to proceed without any challenge.
**Note:** Your score thresholds might vary depending on your users and attackers. We recommend using the reCAPTCHA analytics dashboard to determine the best scores to take action on. 
  2. End or interrupt sessions for end users who successfully authenticate but receive a `credentialsLeaked: true` response from reCAPTCHA Password defense, and send an email to the end users to change their password. 
  3. When creating assessments, ensure that the value of `expectedAction` matches the value of `action` that you specified when installing the score-based site keys on your web pages. If they do not match, do not permit authentication.



## Credential stuffing

Credential stuffing is an automated threat where attackers use mass log-in attempts to verify the validity of stolen username/password pairs.

### Minimum implementation

  1. Install checkbox site keys on all pages where end users need to enter their credentials, including both **login** and **forgot my password** functions. To learn how to install checkbox site keys, see [Install checkbox site keys (checkbox challenge) on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages-with-checkbox). 

**Note:** Checkbox site keys increase user friction and might affect conversion rates. 

  2. Create assessments for all tokens. To learn how to create assessments, see [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment). 




### Optimal implementation

  1. Install score-based site keys on all pages where end users need to enter their credentials. Specify an action in the `action` parameter such as `login` or `authenticate`. To learn how to install score-based site keys, see [Install score-based site keys (no challenge) on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages). 
  2. Recommended: Implement reCAPTCHA Password defense for all authentication attempts. To learn how to use Password defense, see [Detect password leaks and breached credentials](https://docs.cloud.google.com/recaptcha/docs/check-passwords). 
  3. Implement reCAPTCHA account defender to trend end-user behavior across logins and receive additional signals that can indicate an ATO. To learn how to use reCAPTCHA account defender, see [Detect and prevent account-related fraudulent activities](https://docs.cloud.google.com/recaptcha/docs/account-defender). 
  4. Optional: To enable blocking of high-volume and low-reCAPTCHA score interactions, integrate reCAPTCHA with a web application firewall (WAF). For example, you can use [reCAPTCHA for WAF and Google Cloud Armor integration](https://docs.cloud.google.com/recaptcha/docs/integration-overview). 

  5. Create assessments for all tokens, and set `expectedAction` to match the value of `action` that you specified when installing the score-based site keys. To learn how to create assessments, see [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment). 

  6. Save all assessment IDs and annotate the assessments that turn into fraudulent purchases or chargebacks as `fraudulent`. To learn how to annotate assessments, see [Annotate an assessment](https://docs.cloud.google.com/recaptcha/docs/annotate-assessment). 




### Fraud mitigation strategy

After you implement Fraud Defense, use the following fraud mitigation strategy to protect your website from credential stuffing:

  1. Create and implement a response model that is adjusted for score-based risk.

The following example shows a sample response model: 

     * For the lowest reCAPTCHA score threshold (0.0), inform the end user that their password is incorrect.
     * For the intermediate score threshold (0.1-0.5), challenge the end user with multi-factor authentication through email or SMS.
     * For the highest score threshold (> 0.5), allow the end user to proceed without any challenge.
**Note:** Your score thresholds might vary depending on your users and attackers. We recommend using the reCAPTCHA analytics dashboard to determine the best scores to take action on. 
  2. End or interrupt sessions for end users who successfully authenticate but receive a `credentialsLeaked: true` response from reCAPTCHA Password defense, and send an email to the end users to change their password. 
  3. When creating assessments, ensure that the value of `expectedAction` matches the value of `action` that you specified when installing the score-based site keys on your web pages. If they do not match, do not permit authentication.
  4. In your assessment, if `accountDefenderAssessment`=`PROFILE_MATCH`, allow the end user to proceed without any challenge.



## Cashing out

Cashing out is an automated threat where attackers obtain currency or high value items through the utilization of stolen, previously validated payment cards.

### Minimum implementation

  1. Install score-based site keys on all pages where checkout is possible. To learn how to install score-based site keys, see [Install score-based site keys (no challenge) on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages). 
  2. Create assessments for all tokens. To learn how to create assessments, see [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment). 



### Optimal implementation

  1. Install score-based site keys on all pages where end users enter their gift card information. Specify an action such as `add_gift_card`. To learn how to install score-based site keys, see [Install score-based site keys (no challenge) on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages). 
  2. Create assessments for all tokens, and set `expectedAction` to match the value of `action` that you specified when installing the score-based site keys. To learn how to create assessments, see [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment). 

  3. Save all assessment IDs and annotate the transactions that were fraudulent. 




### Fraud mitigation strategy

After you implement Fraud Defense, use the following fraud mitigation strategy to protect your website from cashing out:

  * Install reCAPTCHA for the payment workflow on your website. To learn how to protect your payment workflow, see [Protect payment workflows](https://docs.cloud.google.com/recaptcha/docs/payment-flows). 

  * Implement a response model and create assessments:

    1. Create and implement a response model that is adjusted for score-based risk.

The following example shows a sample response model: 

       * For low to intermediate score threshold (0.0-0.5), use context-based risk management, such as limiting the number of attempts, and blocking purchases over a specified value.
       * For the highest score threshold (> 0.5), allow the end user to proceed without any challenge.
**Note:** Your score thresholds might vary depending on your users and attackers. We recommend using the reCAPTCHA analytics dashboard to determine the best scores to take action on. 
    2. When creating assessments, ensure that the value of `expectedAction` matches the value of `action` that you specified when installing the score-based site keys on your web pages. If they do not match, do not permit authentication. When possible, allow the transaction to proceed at time of purchase, but cancel the transaction later to avoid tipping off the attacker. 



## Account creation

Account creation is an automated threat where attackers create multiple accounts for subsequent misuse.

### Minimum implementation

  1. Install checkbox site keys on all pages where end users need to enter their credentials, including both **login** and **forgot my password** functions. To learn how to install checkbox site keys, see [Install checkbox site keys (checkbox challenge) on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages-with-checkbox). 

**Note:** Checkbox site keys increase user friction and might affect conversion rates. 

  2. Create assessments for all tokens. To learn how to create assessments, see [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment). 




### Optimal implementation

  1. Install score-based site keys on all pages where accounts are created. Specify an action in the `action` parameter such as `register`. To learn how to install score-based site keys, see [Install score-based site keys (no challenge) on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages). 
  2. Recommended: Implement reCAPTCHA Password defense for all authentication attempts. To learn how to use Password defense, see [Detect password leaks and breached credentials](https://docs.cloud.google.com/recaptcha/docs/check-passwords). 
  3. Implement Fraud Defense Account defense to receive additional signals that indicate fake account creations. To learn how to use reCAPTCHA account defender, see [Detect and prevent account-related fraudulent activities](https://docs.cloud.google.com/recaptcha/docs/account-defender). 
  4. Optional: To enable blocking of high-volume and low-reCAPTCHA score interactions, integrate reCAPTCHA with a web application firewall (WAF). For example, you can use [reCAPTCHA for WAF and Google Cloud Armor integration](https://docs.cloud.google.com/recaptcha/docs/integration-overview). 

  5. Create assessments for all tokens, and set `expectedAction` to match the value of `action` that you specified when installing the score-based site keys. To learn how to create assessments, see [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment). 

  6. Save all assessment IDs and annotate the transactions that were fraudulent. 




### Fraud mitigation strategy

After you implement Fraud Defense, use the following fraud mitigation strategy to protect your website from account creation:

  1. Create and implement a response model that is adjusted for score-based risk.

The following example shows a sample response model: 

     * For the lowest reCAPTCHA score threshold (0.0), limit the actions of the account until it undergoes further fraud checks.
     * For the intermediate score threshold (0.1-0.5), challenge the end user with multi-factor authentication through email or SMS.
     * For the highest score threshold (> 0.5), allow the end user to proceed without any challenge.
**Note:** Your score thresholds might vary depending on your users and attackers. We recommend using the reCAPTCHA analytics dashboard to determine the best scores to take action on. 
  2. End or interrupt sessions for end users who successfully authenticate but receive a `credentialsLeaked: true` response from Fraud Defense Password defense, and prompt the user to select a new password.
  3. When creating assessments, ensure that the value of `expectedAction` matches the value of `action` that you specified when installing the score-based site keys on your web pages. If they do not match, do not permit account registration or account creation.
  4. In your assessment, if `accountDefenderAssessment`=`SUSPICIOUS_ACCOUNT_CREATION`, restrict the account's access until further validation can be performed.



## Fraudulent account and address changes

Attackers might attempt to change account details, including email addresses, phone numbers, or mailing addresses as part of fraudulent activity or account takeovers.

### Minimum implementation

  1. Install checkbox site keys on all pages where end users need to enter their credentials, including both **login** and **forgot my password** functions. To learn how to install checkbox site keys, see [Install checkbox site keys (checkbox challenge) on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages-with-checkbox). 

**Note:** Checkbox site keys increase user friction and might affect conversion rates. 

  2. Create assessments for all tokens. To learn how to create assessments, see [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment). 




### Optimal implementation

  1. Install score-based site keys on all pages where accounts are created. Specify an action in the `action` parameter such as `change_telephone` or `change_physicalmail`. To learn how to install score-based site keys, see [Install score-based site keys (no challenge) on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages). 

  2. Create assessments for all tokens, and set `expectedAction` to match the value of `action` that you specified when installing the score-based site keys. To learn how to create assessments, see [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment). 

  3. Implement reCAPTCHA account defender to trend end-user behavior across logins and receive additional signals that can indicate an ATO. To learn how to use reCAPTCHA account defender, see [Detect and prevent account-related fraudulent activities](https://docs.cloud.google.com/recaptcha/docs/account-defender). 

  4. Save all assessment IDs and annotate the transactions that were fraudulent.




### Fraud mitigation strategy

After you implement Fraud Defense, use the following fraud mitigation strategy to protect your website from fraudulent account and address changes:

  1. Create and implement a response model that is adjusted for score-based risk.

The following example shows a sample response model: 

     * For low to intermediate score threshold (0.0-0.5), challenge the end user with multi-factor authentication through email or SMS.
     * For the highest score threshold (> 0.5), allow the end user to proceed without any challenge.
**Note:** Your score thresholds might vary depending on your users and attackers. We recommend using the reCAPTCHA analytics dashboard to determine the best scores to take action on. 
  2. When creating assessments, ensure that the value of `expectedAction` matches the value of `action` that you specified when installing the score-based site keys on your web pages. If they do not match, do not permit account changes.

  3. In your assessment, if `accountDefenderAssessment` does not have the `PROFILE_MATCH` label, challenge the end user with multi-factor authentication through email or SMS.




## Token cracking

Token cracking is an automated threat where attackers do mass enumeration of coupon numbers, voucher codes, discount tokens.

### Minimum implementation

  1. Install checkbox site keys on all pages where end users need to enter their gift card information. To learn how to install checkbox site keys, see [Install checkbox site keys (checkbox challenge) on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages-with-checkbox). 

**Note:** Checkbox site keys increase user friction and might affect conversion rates. 

  2. Create assessments for all tokens. To learn how to create assessments, see [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment). 




### Optimal implementation

  1. Install score-based site keys on all pages where end users need to enter their gift card information. Specify an action such as `gift_card_entry`. To learn how to install score-based site keys, see [Install score-based site keys (no challenge) on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages). 

  2. Optional: To enable blocking of high-volume and low-reCAPTCHA score interactions, integrate reCAPTCHA with a web application firewall (WAF). For example, you can use [reCAPTCHA for WAF and Google Cloud Armor integration](https://docs.cloud.google.com/recaptcha/docs/integration-overview). 

  3. Create assessments for all tokens, and set `expectedAction` to match the value of `action` that you specified when installing the score-based site keys. To learn how to create assessments, see [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment). 

  4. Save all assessment IDs and annotate the assessments that turn into fraudulent gift cards or coupons.




### Fraud mitigation strategy

After you implement Fraud Defense, use one of the following fraud mitigation strategies to protect your website from token cracking:

  * Configure card management APIs to ensure that the reCAPTCHA tokens are valid and the scores are greater than their threshold value. 

If the scores do not meet or exceed the specified threshold, do not run a gift card or credit card authorization, or allow the end user to use the coupon, gift card. When possible, allow the transaction to proceed at time of purchase, but cancel the transaction later to avoid tipping off the attacker. 

  * When creating assessments, ensure that your assessments meet the following criteria for a successful transaction: 

    * All assessed tokens are valid and have a score greater than a specified threshold value.
    * The value of `expectedAction` matches the value of `action` that you specified when installing the score-based site keys on your web pages. To learn how to verify actions, see [verify actions](https://docs.cloud.google.com/recaptcha/docs/interpret-assessment#verify_action).

If a transaction does not meet these criteria, do not run a gift card or credit card authorization, or allow the end user to use the coupon or gift card. When possible, allow the transaction to proceed at time of purchase, but cancel the transaction later to avoid tipping off the attacker. 




## Scalping

Scalping is an automated threat where attackers obtain limited-availability and preferred goods or services by unfair methods.

### Minimum implementation

  1. Install score-based site keys on all pages where end users need to enter their gift card information. Specify an action in the `action` parameter such as `add_to_cart`. To learn how to install score-based site keys, see [Install score-based site keys (no challenge) on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages). 
  2. Create assessments for all tokens, and set `expectedAction` to match the value of `action` that you specified when installing the score-based site keys. To learn how to create assessments, see [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment). 



### Optimal implementation

  1. Install score-based site keys on all pages where end users need to enter their gift card information. Specify an action in the `action` parameter such as `add_to_cart`. To learn how to install score-based site keys, see [Install score-based site keys (no challenge) on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages). 

  2. Optional: To enable blocking of high-volume and low-reCAPTCHA score interactions, integrate reCAPTCHA with a web application firewall (WAF). For example, you can use [reCAPTCHA for WAF and Google Cloud Armor integration](https://docs.cloud.google.com/recaptcha/docs/integration-overview). 

  3. Create assessments for all tokens, and set `expectedAction` to match the value of `action` that you specified when installing the score-based site keys. To learn how to create assessments, see [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment). 

  4. Save all assessment IDs and annotate the transactions that were fraudulent. 




### Fraud mitigation strategy

After you implement Fraud Defense, use the following fraud mitigation strategy to protect your website from scalping:

  1. Create and implement a response model that is adjusted for score-based risk.

The following example shows a sample response model: 

     * For low to intermediate score threshold (0.0-0.5), use context-based risk management, such as limiting the number of attempts, and blocking purchases over a specified value.
     * For the highest score threshold (> 0.5), allow the end user to proceed without any challenge.
**Note:** Your score thresholds might vary depending on your users and attackers. We recommend using the reCAPTCHA analytics dashboard to determine the best scores to take action on. 
  2. When creating assessments, ensure that the value of `expectedAction` matches the value of `action` that you specified when installing the score-based site keys on your web pages. If they do not match, do not run the gift card authorization.




## Skewing

Skewing is an automated threat where attackers use repeated link clicks, page requests, or form submissions to alter some metric.

### Minimum implementation

  1. Install score-based site keys on all pages where metric skewing is possible. To learn how to install score-based site keys, see [Install score-based site keys (no challenge) on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages). 
  2. Create assessments for all tokens. To learn how to create assessments, see [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment). 



### Optimal implementation

  1. Install score-based site keys on all pages where metric skewing is possible. To learn how to install score-based site keys, see [Install score-based site keys (no challenge) on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages). 

  2. Optional: To enable blocking of high-volume and low-reCAPTCHA score interactions, integrate reCAPTCHA with a web application firewall (WAF). For example, you can use [reCAPTCHA for WAF and Google Cloud Armor integration](https://docs.cloud.google.com/recaptcha/docs/integration-overview). 

  3. Create assessments for all tokens, and set `expectedAction` to match the value of `action` that you specified when installing the score-based site keys. To learn how to create assessments, see [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment). 

  4. Save all assessment IDs and annotate the transactions that were fraudulent.




### Fraud mitigation strategy

After you implement Fraud Defense, use the following fraud mitigation strategy to protect your website from skewing:

Create and implement a response model that is adjusted for score-based risk.

The following example shows a sample response model: 

  * For low to intermediate score threshold (0.0-0.5), use context-based risk management, such as tracking the number of times a user has clicked an ad, or number of times a user has reloaded the page. Use this data to determine whether to count the metric.
  * For the highest score threshold (> 0.5), allow the end user to proceed without any challenge.

**Note:** Your score thresholds might vary depending on your users and attackers. We recommend using the reCAPTCHA analytics dashboard to determine the best scores to take action on. 

## Scraping

Scraping is an automated threat where attackers collect website data or artifacts in an automated way.

### Minimum implementation

  1. Install score-based site keys on all pages where important information resides and on key common end-user interaction pages. To learn how to install score-based site keys, see [Install score-based site keys (no challenge) on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages). 
  2. Create assessments for all tokens. To learn how to create assessments, see [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment). 



### Optimal implementation

  1. Install score-based site keys on all pages where important information resides and on key common end-user interaction pages. To learn how to install score-based site keys, see [Install score-based site keys (no challenge) on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages). 

  2. Optional: To enable blocking of high-volume and low-reCAPTCHA score interactions, integrate reCAPTCHA with a web application firewall (WAF). For example, you can use [reCAPTCHA for WAF and Google Cloud Armor integration](https://docs.cloud.google.com/recaptcha/docs/integration-overview). 

  3. Create assessments for all tokens. To learn how to create assessments, see [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment). 

  4. Save all assessment IDs and annotate the transactions that were fraudulent.




### Fraud mitigation strategy

After you implement Fraud Defense, use the following fraud mitigation strategies to protect your website from scraping:

  * Enable blocking of high-volume and low-reCAPTCHA score interactions by integrating Fraud Defense with a web application firewall (WAF). For example, you can use [Fraud Defense for WAF and Google Cloud Armor integration](https://docs.cloud.google.com/recaptcha/docs/integration-overview)
  * If scraping involves APIs, use the [Apigee Management APIs](https://cloud.google.com/apigee) for additional mitigation.



## CAPTCHA defeat

CAPTCHA defeat is an automated threat where attackers use automation in an attempt to analyze and determine the answer to visual and/or aural CAPTCHA tests and related puzzles.

### Minimum implementation

  1. Install score-based site keys on all pages that involve end-user input, account creation, payment information, or end-user interactions with the potential for fraud. Specify a descriptive action in the `action` parameter. To learn how to install score-based site keys, see [Install score-based site keys (no challenge) on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages). 

  2. Create assessments for all tokens, and set `expectedAction` to match the value of `action` that you specified when installing the score-based site keys. To learn how to create assessments, see [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment). 




### Optimal implementation

  1. Install score-based site keys on all pages that involve end-user input, account creation, payment information, or end-user interactions with the potential for fraud. Specify a descriptive action in the `action` parameter. To learn how to install score-based site keys, see [Install score-based site keys (no challenge) on websites](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages). 
  2. Optional: To enable blocking of high-volume and low-reCAPTCHA score interactions, integrate reCAPTCHA with a web application firewall (WAF). For example, you can use [reCAPTCHA for WAF and Google Cloud Armor integration](https://docs.cloud.google.com/recaptcha/docs/integration-overview). 

  3. Create assessments for all tokens, and set `expectedAction` to match the value of `action` that you specified when installing the score-based site keys. To learn how to create assessments, see [Create an assessment](https://docs.cloud.google.com/recaptcha/docs/create-assessment). 

  4. Save all assessment IDs and annotate the assessments that turn into fraudulent purchases or chargebacks as `fraudulent`. To learn how to annotate assessments, see [Annotate an assessment](https://docs.cloud.google.com/recaptcha/docs/annotate-assessment). 




### Fraud mitigation strategy

After you implement Fraud Defense, use one of the following fraud mitigation strategies to protect your website from CAPTCHA defeat:

  * Implement a response model and create assessments:

    1. Create and implement a response model that is adjusted for score-based risk.

The following example shows a sample response model: 

       * For low to intermediate score threshold (0.0-0.5), challenge the end user with multi-factor authentication through email or SMS.
       * For the highest score threshold (> 0.5), allow the end user to proceed without any challenge.
**Note:** Your score thresholds might vary depending on your users and attackers. We recommend using the reCAPTCHA analytics dashboard to determine the best scores to take action on. 
    2. When creating assessments, ensure that the value of `expectedAction` matches the value of `action` that you specified when installing the score-based site keys on your web pages. If they do not match, do not permit authentication.
  * If end users use web browsers that have JavaScript disabled, do the following:

    1. Block those end users.
    2. Notify the end users that your website requires JavaScript to proceed.
  * Ensure that the `grecaptcha.enterprise.ready` promise is fulfilled to prevent end users' browsers that block Google's script from loading. This indicates that reCAPTCHA Javascript API is fully loaded and did not encounter an error.

  * For web-only APIs, we recommend passing the reCAPTCHA token or Fraud Defense assessment result to the backend API, and then only allowing the API action if the reCAPTCHA token is valid and meets a score threshold value. This ensures that the end user is not using the API without going through the website.




## What's next

  * [Install score-based site keys](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages).
  * [Install checkbox site keys](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages-with-checkbox).
  * [Create assessments](https://docs.cloud.google.com/recaptcha/docs/create-assessment).
  * [Annotate assessments](https://docs.cloud.google.com/recaptcha/docs/annotate-assessment).
  * [Implement Password defense](https://docs.cloud.google.com/recaptcha/docs/check-passwords).
  * [Implement Account defense](https://docs.cloud.google.com/recaptcha/docs/account-defender).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
