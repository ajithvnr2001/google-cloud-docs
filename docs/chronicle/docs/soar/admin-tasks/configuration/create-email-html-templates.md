---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/configuration/create-email-html-templates/
title: Create email HTML templates \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:00.708121+00:00
---

# Create email HTML templates  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/configuration/create-email-html-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create email HTML templates

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

You can define HTML templates for recurring emails, so that they can be sent by scripts or used by playbooks. 

To create a new HTML email template, follow these steps: 

  1. Go to **Settings > Environments > Email HTML Templates**.
  2. Click add **Add**. 
  3. In the **Add Email Template** dialog, edit the HTML information, making sure to add in the required body text. 
  4. Click **Add**. 



### Supported HTML tags and attributes

Google SecOps SOAR supports a specific, restricted list of HTML tags and attributes for security purposes. The platform prevents the use of certain elements to protect against malicious code. 

To ensure your template is valid, use only the tags and attributes listed in the following table: 

Supported HTML Tags | Supported HTML Attributes  
---|---  
  
  * `a`
  * `abbr`
  * `acronym`
  * `address`
  * `area`
  * `b`
  * `big`
  * `blockquote`
  * `br`
  * `button`
  * `caption`
  * `center`
  * `cite`
  * `code`
  * `col`
  * `colgroup`
  * `dd`
  * `del`
  * `dfn`
  * `dir`
  * `div`
  * `dl`
  * `dt`
  * `em`
  * `fieldset`
  * `font`
  * `form`
  * `h1`
  * `h2`
  * `h3`
  * `h4`
  * `h5`
  * `h6`
  * `hr`
  * `i`
  * `img`
  * `input`
  * `ins`
  * `kbd`
  * `label`
  * `legend`
  * `li`
  * `map`
  * `menu`
  * `ol`
  * `optgroup`
  * `option`
  * `p`
  * `pre`
  * `q`
  * `s`
  * `samp`
  * `select`
  * `small`
  * `span`
  * `strike`
  * `strong`
  * `sub`
  * `sup`
  * `table`
  * `tbody`
  * `td`
  * `textarea`
  * `tfoot`
  * `th`
  * `thead`
  * `tr`
  * `tt`
  * `u`
  * `ul`
  * `var`
  * `section`
  * `nav`
  * `article`
  * `aside`
  * `header`
  * `footer`
  * `main`
  * `figure`
  * `figcaption`
  * `data`
  * `time`
  * `mark`
  * `ruby`
  * `rt`
  * `rp`
  * `bdi`
  * `wbr`
  * `datalist`
  * `keygen`
  * `output`
  * `progress`
  * `meter`
  * `details`
  * `summary`
  * `menuitem`
  * `html`
  * `head`
  * `body`
  * `style`

| 

  * `abbr`
  * `accept`
  * `accept-charset`
  * `accesskey`
  * `action`
  * `align`
  * `alt`
  * `axis`
  * `bgcolor`
  * `border`
  * `cellpadding`
  * `cellspacing`
  * `char`
  * `charoff`
  * `charset`
  * `checked`
  * `cite`
  * `clear`
  * `cols`
  * `colspan`
  * `color`
  * `compact`
  * `coords`
  * `datetime`
  * `dir`
  * `disabled`
  * `enctype`
  * `for`
  * `frame`
  * `headers`
  * `height`
  * `href`
  * `hreflang`

  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
