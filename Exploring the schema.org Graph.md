```python
from rdflib import Graph
g = Graph()
# The Schema.org schema may be found at: https://schema.org/docs/developers.html
g.parse('https://schema.org/version/latest/schemaorg-current-https.jsonld')
for s, p, o in g:
    print(s, p, o)
```

The code above will be used to get the various endpoints for schema.org

# Types of Fields
## [[Schema.org Predicate Vocabulary|Predicate Vocabulary]]
Using the following code we may find the number of predicates using the following code:
```python
from rdflib import Graph
from pprint import pprint

g = Graph()

  

# The Schema.org schema may be found at: https://schema.org/docs/developers.html

g.parse('https://schema.org/version/latest/schemaorg-current-https.jsonld')

predicate_set = set()

for s, p, o in g:
        predicate_set.add(str(p))

print("Predicate Set")
pprint(predicate_set)
print(f"Set Lengths: predicate set {len(predicate_set)}") #, object set: {len(object_set)}, subject set: {len(subject_set)}")
```

