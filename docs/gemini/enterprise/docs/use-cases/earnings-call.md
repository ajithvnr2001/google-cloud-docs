---
url: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/earnings-call/
title: Summarize an earnings call transcript \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:34.807347+00:00
---

# Summarize an earnings call transcript  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/earnings-call/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Summarize an earnings call transcript Stay organized with collections  Save and categorize content based on your preferences. 

Stay on top of competitor and industry trends without spending hours reading dense transcripts. Paste in the text of an earnings call, and get the key takeaways in seconds.

**Note:** Verify every figure against the company's filed results release before using it. A transcript is a secondary source, and transcription errors in numbers are common.

## Before you begin

  * Attach the transcript rather than pasting it. A full call runs 10,000 words or more, and attaching keeps the whole document available to the model.
  * To compare earning calls across quarters, attach the prior quarter transcript in the same turn.
  * For a competitor's call that you don't have on file, use the second example prompt with the Deep Research agent, which cites its sources.



## Example prompt

To summarize an attached transcript, enter a prompt in the chat box such as the following:
    
    
    You are an equity analyst. Attached are the Q3 and Q2 earnings call transcripts
    for Cymbal Retail Group.
    
    Summarize the Q3 call:
    
    1. **Reported numbers**, quoted verbatim with the speaker named. Revenue,
    margin, EPS, and any segment figure management called out. Do not calculate
    anything that was not stated on the call.
    
    2. **Guidance**, quoted verbatim: what was given, and how it differs from what
    was given in Q2. If guidance was withdrawn, narrowed, or moved from a range to a
    point, say so explicitly.
    
    3. **Prepared remarks vs. Q&A.** Anything management raised in Q&A that did not
    appear in prepared remarks, and anything from prepared remarks that no analyst
    followed up on.
    
    4. **Analyst questions**, grouped by theme. For each: who asked, what they were
    getting at, and whether it was answered. Mark any question that was deflected,
    answered with a different metric than the one asked about, or promised as a
    follow-up.
    
    5. **Language shifts from Q2.** Phrases used in Q2 that are gone in Q3, and new
    hedging language. Quote both quarters side by side.
    
    6. **Not addressed:** subjects an analyst would expect on this call that nobody
    raised.
    
    Rules:
    - Quote verbatim for every number and every guidance statement, and name the
    speaker.
    - Do not derive ratios, growth rates, or margins that were not stated aloud.
    - Distinguish what management said from what an analyst asserted in a question.
    - If the transcript marks a passage as inaudible or uncertain, flag it rather
    than filling it in.
    

To summarize a competitor's call you don't have on file, select the Deep Research agent and enter a prompt such as the following:
    
    
    Find the most recent quarterly earnings call for Cymbal Retail Group and
    summarize it using the structure above. Link the transcript or webcast you used,
    and note the publisher. If you can only find secondary coverage rather than a
    transcript, say so and do not quote as though from the transcript itself.
    

## Example output

In response to the first prompt, Gemini Enterprise produces output similar to the following:

> ### Reported numbers
> 
> Metric | Quote | Speaker  
> ---|---|---  
> Revenue | "Total revenue for the third quarter was $1.24 billion, up 6% year over year." | CFO, prepared remarks  
> Gross margin | "Gross margin came in at 38.1%, down 120 basis points from a year ago." | CFO, prepared remarks  
> EPS | "Adjusted earnings per share of $1.50." | CFO, prepared remarks  
> Digital segment | "Digital grew 14%, and now represents just under a quarter of total revenue." | CEO, prepared remarks  
>   
> "Just under a quarter" was not given as a precise figure on the call and is not calculated here.
> 
> ### Guidance
> 
> **Q3 call, CFO:**
>
>> "We now expect full-year revenue growth of 4% to 5%."
> 
> **Q2 call, CFO:**
>
>> "We continue to expect full-year revenue growth of 5% to 7%."
> 
> The range was lowered and narrowed. The CFO characterized this as "recalibrating for a promotional environment," not as a reduction.
> 
> ### Prepared remarks vs. Q&A
> 
>   * **Raised only in Q &A:** the delayed distribution center opening. It appeared in no part of prepared remarks and came up when an analyst asked about capacity.
>   * **In prepared remarks, never followed up:** the new loyalty program. The CEO spent roughly two minutes on it and no analyst asked a single question about it.
> 

> 
> ### Analyst questions by theme
> 
> Theme | Who asked | Getting at | Answered?  
> ---|---|---|---  
> Promotional intensity and margin | Analyst 1, Analyst 4 | Whether the margin decline is structural or cyclical | **Deflected.** Asked about margin trajectory; answered with full-year revenue guidance  
> Inventory position | Analyst 2 | Whether excess inventory is driving the promotions | Answered. Gave units on hand and weeks of supply  
> Distribution center delay | Analyst 3 | Timing and cost impact | **Partially.** Timing given; cost impact promised as a follow-up  
> Digital profitability | Analyst 5 | Whether digital growth is margin-dilutive | **Answered with a different metric.** Asked about digital contribution margin; answered with digital revenue growth  
>   
> ### Language shifts from Q2
> 
> Q2 | Q3  
> ---|---  
> "We are confident in our full-year outlook." | "We feel good about our positioning as we head into the fourth quarter."  
> "Promotional activity has normalized." | "The promotional environment remains dynamic."  
> (not used in Q2) | "assuming the consumer environment holds" - used three times in Q3  
>   
> The Q2 phrase "normalized" is gone. The new conditional on the consumer environment appears only in Q3 and always attached to a forward-looking statement.
> 
> ### Not addressed
> 
>   * No question about the CFO transition announced two weeks before the call.
>   * Nobody asked about the buyback, despite the release stating the authorization was materially drawn down this quarter.
>   * Nobody asked what "dynamic" means for Q4 margin, which is the obvious follow-up to the deflection in the first theme above.
> 

> 
> ### Verification
> 
> Confirm the four figures in the first table against the filed results release. One passage in the Q&A is marked "[inaudible]" in the transcript where the CFO appears to give a store-count figure; that number is not reported here.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
