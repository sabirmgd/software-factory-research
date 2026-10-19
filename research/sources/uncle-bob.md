# Robert C. Martin / Uncle Bob

The primary inspected source is the author's Clean Architecture article. It describes keeping business rules independent of framework and infrastructure details through dependency direction. [S14](index.md#s14)

Our application is a design lens: keep transport and persistence mechanics from unnecessarily determining business behavior. We do not interpret this as a requirement for a particular number of classes or layers. The specific NestJS module layout and agent workflow are our proposals.

The conversation also referenced an interview with Matt Pocock. That recording and transcript were not independently verified for this edition. We therefore do not attribute detailed claims about current habits, mutation testing, or planning preferences to that interview. A future correction can add a checked timestamp and precise scope.

The author supplies a body of engineering ideas, not an endorsement of the software-factory synthesis in this repository.
