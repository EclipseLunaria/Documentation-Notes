### Specification Used
All of the following examples will be using the [[Schema.org Specification]]
## Installation

The RDFlib package may be installed with the [[Pip Package Management Tool]]:
```sh
pip install rdflib
```

Some features require additional dependencies which may be install with [[Pip Extras]]:
```sh
pip install rdflib[berkelydb,networkx,html,lxml]
```


## Getting Started

Below is an example of RDFlibs fundamental data type the Graph. The graph composes of a 3-value tuple with the respective fields:
- Subject
- Predicate
- Object
We will use the following code to further explore the different fields of [[Exploring the schema.org Graph|Schema.org Graph]]:
```python
from rdflib import Graph
g = Graph()
# The Schema.org schema may be found at: https://schema.org/docs/developers.html
g.parse('https://schema.org/version/latest/schemaorg-current-https.jsonld')
for s, p, o in g:
    print(s, p, o)
```

