# John Ousterhout

The inspected primary source is the author's page for *A Philosophy of Software Design*, not the complete book. The page also identifies disagreements with some Clean Code advice. [S15](index.md#s15)

The deep-module concept is a lens used in this investigation: callers should obtain meaningful capability without coordinating internal complexity. Our assignment example is an original illustration, not a case study from the book. The detailed red-flag treatment is separately supported by the inspected PStack reference. [S09](index.md#s09)

We do not claim that fewer methods, more hidden code, or longer call chains automatically create depth. The usefulness of the interface and clarity of responsibility must be examined in context.
