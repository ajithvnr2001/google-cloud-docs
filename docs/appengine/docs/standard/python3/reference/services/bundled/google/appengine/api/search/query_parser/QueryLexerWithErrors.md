---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/query_parser/QueryLexerWithErrors/
title: google.appengine.api.search.query_parser.QueryLexerWithErrors \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:50:22.411590+00:00
---

# google.appengine.api.search.query_parser.QueryLexerWithErrors  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/query_parser/QueryLexerWithErrors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.search.query_parser.QueryLexerWithErrors Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/query_parser.py#L53-L71) An overridden Lexer that raises exceptions. Inherits From: `QueryLexer`, [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.search.query_parser.QueryLexerWithErrors(
        input=None, state=None
    )
    

| 

## Attributes  
  
---  
  
`text` |  Return the text matched so far for the current token or any text override.   
  
## Child Classes

`class DFA10`

`class DFA7`

`class DFA9`

## Methods

### `ExclamationNotFollowedByEquals`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L122-L127)
    
    
    ExclamationNotFollowedByEquals()
    

### `alreadyParsedRule`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L926-L948)
    
    
    alreadyParsedRule(
        input, ruleIndex
    )
    

Has this rule already parsed input at the current index in the input stream? Return the stop token index or MEMO_RULE_UNKNOWN. If we attempted but failed to parse properly before, return MEMO_RULE_FAILED.

This method has a side-effect: if we have seen this input for this rule and successfully parsed before, then seek ahead to 1 past the stop token matched for this rule last time.

### `beginResync`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L494-L500)
    
    
    beginResync()
    

A hook to listen in on the token consumption during error recovery. The DebugParser subclasses this to fire events to the listenter.

### `combineFollows`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L663-L679)
    
    
    combineFollows(
        exact
    )
    

### `computeContextSensitiveRuleFOLLOW`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L606-L661)
    
    
    computeContextSensitiveRuleFOLLOW()
    

Compute the context-sensitive FOLLOW set for current rule. This is set of token types that can follow a specific rule reference given a specific call chain. You get the set of viable tokens that can possibly come next (lookahead depth 1) given the current call chain. Contrast this with the definition of plain FOLLOW for rule r:

FOLLOW(r)={x | S=>*alpha r beta in G and x in FIRST(beta)}

where x in T* and alpha, beta in V*; T is set of terminals and V is the set of terminals and nonterminals. In other words, FOLLOW(r) is the set of all tokens that can possibly follow references to r in _any_ sentential form (context). At runtime, however, we know precisely which context applies as we have the call chain. We may compute the exact (rather than covering superset) set of following tokens.

For example, consider grammar:

stat : ID '=' expr ';' // FOLLOW(stat){EOF} | "return" expr '.' ; expr : atom ('+' atom)* ; // FOLLOW(expr){';','.',')'} atom : INT // FOLLOW(atom)=={'+',')',';','.'} | '(' expr ')' ;

The FOLLOW sets are all inclusive whereas context-sensitive FOLLOW sets are precisely what could follow a rule reference. For input input "i=(3);", here is the derivation:

stat => ID '=' expr ';' => ID '=' atom ('+' atom)* ';' => ID '=' '(' expr ')' ('+' atom)* ';' => ID '=' '(' atom ')' ('+' atom)* ';' => ID '=' '(' INT ')' ('+' atom)* ';' => ID '=' '(' INT ')' ';'

At the "3" token, you'd have a call chain of

stat -> expr -> atom -> expr -> atom

What can follow that specific nested ref to atom? Exactly ')' as you can see by looking at the derivation of this specific input. Contrast this with the FOLLOW(atom)={'+',')',';','.'}.

You want the exact viable token set when recovering from a token mismatch. Upon token mismatch, if LA(1) is member of the viable next token set, then you know there is most likely a missing token in the input stream. "Insert" one by just not throwing an exception.

### `computeErrorRecoverySet`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L510-L604)
    
    
    computeErrorRecoverySet()
    

Compute the error recovery set for the current rule. During rule invocation, the parser pushes the set of tokens that can follow that rule reference on the stack; this amounts to computing FIRST of what follows the rule reference in the enclosing rule. This local follow set only includes tokens from within the rule; i.e., the FIRST computation done by ANTLR stops at the end of a rule.

EXAMPLE

When you find a "no viable alt exception", the input is not consistent with any of the alternatives for rule r. The best thing to do is to consume tokens until you see something that can legally follow a call to r _or_ any rule that called r. You don't want the exact set of viable next tokens because the input might just be missing a token--you might consume the rest of the input looking for one of the missing tokens.

#### Consider grammar:

a : '[' b ']' | '(' b ')' ; b : c '^' INT ; c : ID | INT ;

At each rule invocation, the set of tokens that could follow that rule is pushed on a stack. Here are the various "local" follow sets:

FOLLOW(b1_in_a) = FIRST(']') = ']' FOLLOW(b2_in_a) = FIRST(')') = ')' FOLLOW(c_in_b) = FIRST('^') = '^'

Upon erroneous input "[]", the call chain is

a -> b -> c

and, hence, the follow context stack is:

depth local follow set after call to rule 0 <EOF> a (from main()) 1 ']' b 3 '^' c

Notice that ')' is not included, because b would have to have been called from a different context in rule a for ')' to be included.

For error recovery, we cannot consider FOLLOW(c) (context-sensitive or otherwise). We need the combined set of all context-sensitive FOLLOW sets--the set of all tokens that could follow any reference in the call chain. We need to resync to one of those tokens. Note that FOLLOW(c)='^' and if we resync'd to that token, we'd consume until EOF. We need to sync to context-sensitive FOLLOWs for a, b, and c: {']','^'}. In this case, for input "[]", LA(1) is in this set so we would not consume anything and after printing an error rule c would return normally. It would not find the required '^' though. At this point, it gets a mismatched token error and throws an exception (since LA(1) is not in the viable following token set). The rule exception handler tries to recover, but finds the same recovery set and doesn't consume anything. Rule b exits normally returning to rule a. Now it finds the ']' (and with the successful match exits errorRecovery mode).

So, you cna see that the parser walks up call chain looking for the token that was a member of the recovery set.

Errors are not generated in errorRecovery mode.

ANTLR's error recovery mechanism is based upon original ideas:

"Algorithms + Data Structures = Programs" by Niklaus Wirth

and

"A note on error recovery in recursive descent parsers": http://portal.acm.org/citation.cfm?id=947902.947905

Later, Josef Grosch had some good ideas:

"Efficient and Comfortable Error Recovery in Recursive Descent Parsers": ftp://www.cocolab.com/products/cocktail/doca4.ps/ell.ps.zip

Like Grosch I implemented local FOLLOW sets that are combined at run-time upon error to avoid overhead during parsing.

### `consumeUntil`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L810-L824)
    
    
    consumeUntil(
        input, tokenTypes
    )
    

Consume tokens until one matches the given token or token set

tokenTypes can be a single token type or a set of token types

### `displayRecognitionError`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/query_parser.py#L56-L58)
    
    
    displayRecognitionError(
        tokenNames, e
    )
    

### `emit`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L1136-L1161)
    
    
    emit(
        token=None
    )
    

The standard method called to automatically emit a token at the outermost lexical rule. The token object should point into the char buffer start..stop. If there is a text override in 'text', use that to set the token's text. Override this method to emit custom Token objects.

If you are building trees, then you should also override Parser or TreeParser.getMissingSymbol().

### `emitErrorMessage`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/query_parser.py#L60-L71)
    
    
    emitErrorMessage(
        msg
    )
    

Raise an exception if the input fails to parse correctly.

Overriding the default, which normally just prints a message to stderr.

Arguments  
---  
  
`msg` |  the error message   
  
Raises  
---  
  
`QueryException` |  always.   
  
### `endResync`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L502-L508)
    
    
    endResync()
    

A hook to listen in on the token consumption during error recovery. The DebugParser subclasses this to fire events to the listenter.

### `getBacktrackingLevel`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L886-L887)
    
    
    getBacktrackingLevel()
    

### `getCharErrorDisplay`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L1271-L1274)
    
    
    getCharErrorDisplay(
        c
    )
    

### `getCharIndex`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L1207-L1210)
    
    
    getCharIndex()
    

What is the index of the current character of lookahead?

### `getCharPositionInLine`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L1204-L1205)
    
    
    getCharPositionInLine()
    

### `getCurrentInputSymbol`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L756-L768)
    
    
    getCurrentInputSymbol(
        input
    )
    

Match needs to return the current input symbol, which gets put into the label for the associated token ref; e.g., x=ID. Token and tree parsers need to return different objects. Rather than test for input stream type or change the IntStream interface, I use a simple method to ask the recognizer to tell me what the current input symbol is.

This is ignored for lexers.

### `getErrorHeader`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L438-L443)
    
    
    getErrorHeader(
        e
    )
    

What is the error header, normally line/character position information?

### `getErrorMessage`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L1245-L1269)
    
    
    getErrorMessage(
        e, tokenNames
    )
    

What error message should be generated for the various exception types?

Not very object-oriented code, but I like having all error message generation within one method rather than spread among all of the exception classes. This also makes it much easier for the exception handling because the exception classes do not have to have pointers back to this object to access utility routines and so on. Also, changing the message for an exception type would be difficult because you would have to subclassing exception, but then somehow get ANTLR to make those kinds of exception objects instead of the default. This looks weird, but trust me--it makes the most sense in terms of flexibility.

For grammar debugging, you will want to override this to add more information such as the stack frame with getRuleInvocationStack(e, this.getClass().getName()) and, for no viable alts, the decision description and state etc...

Override this to change the message generated for one or more exception types.

### `getGrammarFileName`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L889-L895)
    
    
    getGrammarFileName()
    

For debugging and other purposes, might want the grammar name.

Have ANTLR generate an implementation for this method.

### `getLine`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L1201-L1202)
    
    
    getLine()
    

### `getMissingSymbol`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L770-L791)
    
    
    getMissingSymbol(
        input, e, expectedTokenType, follow
    )
    

Conjure up a missing token during error recovery.

The recognizer attempts to recover from single missing symbols. But, actions might refer to that missing symbol. For example, x=ID {f($x);}. The action clearly assumes that there has been an identifier matched previously and that $x points at that token. If that token is missing, but the next token in the stream is what we want we assume that this token is missing and we keep going. Because we have to return some token to replace the missing token, we have to conjure one up. This method gives the user control over the tokens returned for missing tokens. Mostly, you will want to create something special for identifier tokens. For literals such as '{' and ',', the default action in the parser or tree parser works. It simply creates a CommonToken of the appropriate type. The text will be the token. If you change what tokens must be created by the lexer, override this method to create the appropriate tokens.

### `getNumberOfSyntaxErrors`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L427-L436)
    
    
    getNumberOfSyntaxErrors()
    

Get number of recognition errors (lexer, parser, tree parser). Each recognizer tracks its own number. So parser and lexer each have separate count. Does not count the spurious errors found between an error and next valid token match

See also reportError()

### `getRuleInvocationStack`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L826-L848)
    
    
    getRuleInvocationStack()
    

Return List of the rules in your parser instance leading up to a call to this method. You could override if you want more details such as the file/line info of where in the parser java code a rule is invoked.

This is very useful for error messages and for context-sensitive error recovery.

You must be careful, if you subclass a generated recognizers. The default implementation will only search the module of self for rules, but the subclass will not contain any rules. You probably want to override this method to look like

def getRuleInvocationStack(self): return self._getRuleInvocationStack(.__module_ _)

where  is the class of the generated recognizer, e.g. the superclass of self.

### `getRuleMemoization`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L911-L924)
    
    
    getRuleMemoization(
        ruleIndex, ruleStartIndex
    )
    

Given a rule number and a start token index number, return MEMO_RULE_UNKNOWN if the rule has not parsed input starting from start index. If this rule has parsed input starting from the start index before, then return where the rule stopped parsing. It returns the index of the last token matched by the rule.

### `getSourceName`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L1133-L1134)
    
    
    getSourceName()
    

### `getText`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L1212-L1221)
    
    
    getText()
    

Return the text matched so far for the current token or any text override.

### `getTokenErrorDisplay`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L445-L463)
    
    
    getTokenErrorDisplay(
        t
    )
    

How should a token be displayed in an error message? The default is to display just the text, but during development you might want to have a lot of information spit out. Override in that case to use t.toString() (which, for CommonToken, dumps everything about the token). This is better than forcing you to override a method in your token objects because you don't have to go modify your lexer so that it creates a new Java type.

### `mAND`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L183-L201)
    
    
    mAND()
    

### `mBACKSLASH`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L454-L472)
    
    
    mBACKSLASH()
    

### `mCOMMA`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L429-L447)
    
    
    mCOMMA()
    

### `mDIGIT`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L988-L1001)
    
    
    mDIGIT()
    

### `mEQ`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L604-L622)
    
    
    mEQ()
    

### `mESC`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L283-L341)
    
    
    mESC()
    

### `mESCAPED_CHAR`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L1178-L1241)
    
    
    mESCAPED_CHAR()
    

### `mEXCLAMATION`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L1248-L1264)
    
    
    mEXCLAMATION()
    

### `mFIX`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L258-L276)
    
    
    mFIX()
    

### `mGE`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L529-L547)
    
    
    mGE()
    

### `mGT`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L504-L522)
    
    
    mGT()
    

### `mHAS`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L133-L151)
    
    
    mHAS()
    

### `mHEX_DIGIT`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L1008-L1027)
    
    
    mHEX_DIGIT()
    

### `mLE`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L554-L572)
    
    
    mLE()
    

### `mLESSTHAN`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L479-L497)
    
    
    mLESSTHAN()
    

### `mLPAREN`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L379-L397)
    
    
    mLPAREN()
    

### `mMID_CHAR`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L1122-L1171)
    
    
    mMID_CHAR()
    

### `mMINUS`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L629-L647)
    
    
    mMINUS()
    

### `mNE`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L579-L597)
    
    
    mNE()
    

### `mNOT`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L208-L226)
    
    
    mNOT()
    

### `mNUMBER_PREFIX`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L768-L794)
    
    
    mNUMBER_PREFIX()
    

### `mOCTAL_ESC`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L879-L981)
    
    
    mOCTAL_ESC()
    

### `mOR`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L158-L176)
    
    
    mOR()
    

### `mQUOTE`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L654-L672)
    
    
    mQUOTE()
    

### `mREWRITE`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L233-L251)
    
    
    mREWRITE()
    

### `mRPAREN`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L404-L422)
    
    
    mRPAREN()
    

### `mSTART_CHAR`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L1034-L1115)
    
    
    mSTART_CHAR()
    

### `mTEXT`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L679-L761)
    
    
    mTEXT()
    

### `mTEXT_ESC`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L801-L847)
    
    
    mTEXT_ESC()
    

### `mTokens`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L1270-L1397)
    
    
    mTokens()
    

This is the lexer entry point that sets instance var 'token'

### `mUNICODE_ESC`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L854-L872)
    
    
    mUNICODE_ESC()
    

### `mWS`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/QueryLexer.py#L348-L372)
    
    
    mWS()
    

### `match`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L1163-L1185)
    
    
    match(
        s
    )
    

Match current input symbol against ttype. Attempt single token insertion or deletion error recovery. If that fails, throw MismatchedTokenException.

To turn off single token insertion or deletion error recovery, override mismatchRecover() and have it call plain mismatch(), which does not recover. Then any error in a rule will cause an exception and immediate exit from rule. Rule would recover by resynchronizing to the set of symbols that can follow rule ref.

### `matchAny`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L1187-L1188)
    
    
    matchAny()
    

Match the wildcard: in a symbol

### `matchRange`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L1190-L1199)
    
    
    matchRange(
        a, b
    )
    

### `memoize`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L950-L962)
    
    
    memoize(
        input, ruleIndex, ruleStartIndex, success
    )
    

Record whether or not this rule parsed the input at this position successfully.

### `mismatch`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L279-L294)
    
    
    mismatch(
        input, ttype, follow
    )
    

Factor out what to do upon token mismatch so tree parsers can behave differently. Override and call mismatchRecover(input, ttype, follow) to get single token insertion and deletion. Use this to turn of single token insertion and deletion. Override mismatchRecover to call this instead.

### `mismatchIsMissingToken`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L256-L277)
    
    
    mismatchIsMissingToken(
        input, follow
    )
    

### `mismatchIsUnwantedToken`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L253-L254)
    
    
    mismatchIsUnwantedToken(
        input, ttype
    )
    

### `next`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L1024-L1035)
    
    
    next()
    

Return next token or raise StopIteration.

Note that this will raise StopIteration when hitting the EOF token, so EOF will not be part of the iteration.

### `nextToken`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L1075-L1107)
    
    
    nextToken()
    

Return a token from this source; i.e., match a token on the char stream.

### `recover`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L1276-L1284)
    
    
    recover(
        re
    )
    

Lexers can normally match any char in its vocabulary after matching a token, so do the easy thing and just kill a character and hope it all works out. You can instead use the rule invocation stack to do sophisticated error recovery if you are in a fragment rule.

### `recoverFromMismatchedSet`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L745-L754)
    
    
    recoverFromMismatchedSet(
        input, e, follow
    )
    

Not currently used

### `recoverFromMismatchedToken`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L681-L743)
    
    
    recoverFromMismatchedToken(
        input, ttype, follow
    )
    

Attempt to recover from a single missing or extra token.

EXTRA TOKEN

LA(1) is not what we are looking for. If LA(2) has the right token, however, then assume LA(1) is some extra spurious token. Delete it and LA(2) as if we were doing a normal match(), which advances the input.

MISSING TOKEN

If current token is consistent with what could come after ttype then it is ok to 'insert' the missing token, else throw exception For example, Input 'i=(3;' is clearly missing the ')'. When the parser returns from the nested call to expr, it will have call chain:

stat -> expr -> atom

and it will be trying to match the ')' at this point in the derivation:
    
    
     => ID '=' '(' INT ')' ('+' atom)* ';'
                        ^
    

match() will see that ';' doesn't match ')' and report a mismatched token error. To recover, it sees that LA(1)==';' is in the set of tokens that can follow the ')' token reference in rule atom. It can assume that you forgot the ')'.

### `reportError`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L1232-L1243)
    
    
    reportError(
        e
    )
    

Report a recognition problem.

This method sets errorRecovery to indicate the parser is recovering not parsing. Once in recovery mode, no errors are generated. To get out of recovery mode, the parser must successfully match a token (after a resync). So it will go:

  1. error occurs
  2. enter recovery mode, report error
  3. consume until token found in resynch set
  4. try to resume parsing
  5. next match() will reset errorRecovery mode



If you override, make sure to update syntaxErrors if you care about that.

### `reset`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L1055-L1073)
    
    
    reset()
    

reset the parser's state; subclasses must rewinds the input stream

### `setCharStream`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L1127-L1131)
    
    
    setCharStream(
        input
    )
    

Set the char stream and reset the lexer

### `setInput`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L198-L199)
    
    
    setInput(
        input
    )
    

### `setText`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L1223-L1228)
    
    
    setText(
        text
    )
    

Set the complete text of this token; it wipes any previous changes to the text.

### `skip`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L1110-L1119)
    
    
    skip()
    

Instruct the lexer to skip creating a token for current lexer rule and look for another token. nextToken() knows to keep looking when a lexer rule finishes with token set to SKIP_TOKEN. Recall that if token==null at end of any token rule, it creates one for you and emits it.

### `toStrings`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L900-L909)
    
    
    toStrings(
        tokens
    )
    

A convenience method for use most often with template rewrites.

Convert a List to List

### `traceIn`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L1286-L1290)
    
    
    traceIn(
        ruleName, ruleIndex
    )
    

### `traceOut`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L1292-L1296)
    
    
    traceOut(
        ruleName, ruleIndex
    )
    

### `__iter__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/_internal/antlr3/recognizers.py#L1014-L1022)
    
    
    __iter__()
    

The TokenSource is an iterator.

The iteration will not include the final EOF token, see also the note for the next() method.

## Class Variables  
  
---  
  
DEFAULT_TOKEN_CHANNEL  
DFA10_accept  
DFA10_eof  
DFA10_eot  
DFA10_max  
DFA10_min  
DFA10_special  
DFA10_transition  
DFA7_accept  
DFA7_eof  
DFA7_eot  
DFA7_max  
DFA7_min  
DFA7_special  
DFA7_transition  
DFA9_accept  
DFA9_eof  
DFA9_eot  
DFA9_max  
DFA9_min  
DFA9_special  
DFA9_transition  
HIDDEN  
MEMO_RULE_FAILED  
MEMO_RULE_UNKNOWN  
antlr_version  
antlr_version_str  
grammarFileName  
tokenNames  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
