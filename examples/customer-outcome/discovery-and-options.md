# Discover the work before selecting the interface

## Intended outcome

Staff should be able to identify an appropriate available item and explain the basis of that answer without creating incorrect commitments. Establish how they do this today, which source is authoritative, how freshness is represented, and what happens when sources disagree.

## Three interventions to compare

A conversational assistant may help when requests are naturally expressed in varied language and the underlying information is reliable. A structured search view may be simpler when the criteria are well defined. A data-quality intervention may be the priority when neither interface can produce a trustworthy answer from the existing inputs.

Use Make Clear to show the current journey, the information source at each step, and what each alternative changes. A polished chatbot mockup alone does not answer whether the data is reliable. Include an example with stale inventory and show how the user recognizes uncertainty.

## High-leverage decisions

Define the authoritative source, freshness and conflict semantics, who may see which inventory, and whether the system can make a commitment or only assist a person. These decisions matter regardless of interface choice. They are stronger candidates for early engineering attention than the styling of a chat bubble.

## Bounded experiment

Use synthetic or approved sample queries and inspect how each proposed workflow handles ordinary and uncertain cases. Record task success, incorrect answers, clarification effort, and user understanding. Do not claim production value from a demo. If the source is unreliable, the next approved task may be a data integration rather than a conversational UI.
