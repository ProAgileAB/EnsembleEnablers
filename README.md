
# Ensemble Enablers - what is this repo?

This repo documents patterns we've found useful while
coaching teams in Ensemble Programming


## How to add an enabler?

Update the enablers.json file, then run this command:

    python build.py

This will update README.md if no obvious errors were
found in enablers.json.

# ENSEMBLE ENABLERS BELOW

# No decisions at the keyboard

*Also known has: More listening at the keyboard*

## Symptoms

 * Typist is talking as much or more than the navigator
 * Navigator is quiet or uncertain
 * Typist writes code that the navigator didn’t talk about


## Proposal

The typist is not supposed to have their own ideas, they should be channeling the ideas from the navigator and the rest of the ensemble into the codebase.

"For an idea to go from your head into the computer it MUST go through someone else's hands"

That’s Llewellyn Falco’s description of “strong-style” pair programming. For an ensemble, this is even more important. Every idea should be spoken: expressed in a form so that it can be discussed and analyzed as it makes its way into the code. The typist has the hardest job here, because they have to break their habit of both thinking and typing themselves. Instead they need to put more effort into listening - in particular to the navigator, and translating their ideas into code.

If you notice the typist is rushing ahead writing code for an idea that hasn’t been discussed, you should probably intervene straight away. Kindly suggest “more listening, less thinking at the keyboard”. Perhaps also bring it up at the retrospective.
