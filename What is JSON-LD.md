Json-LD combines the concept of linked data with the JSON structure in order to better communicate data in a human and computer readable format.

## Linked Data
Linked data that is interlinked with other data making it easier to semantically query said data. It is Build upon Web Technologies such as [[HTTP]], [[Resource Description Framework|RDF]], and [[Uniform Resource Identifiers|URIs]]. instead of presenting the data for solely human readers, linked data structures in a way that can be shared with other computers.

### Linked Data Guiding Principals
1. [[Uniform Resource Identifiers]] (URIs) should be used to identify individual things (**Identifiable**)
2. [[HTTP]] URIs should allow the data to be looked, interpreted, and subsequently "dereferenced" (Quarriable)
3. What the data identifies should be defined through open standards such as: [[Resource Description Framework|RDF]], [[SPARQL]], Etc.
4. When publishing to the web, use the HTTP URI when referencing other resources

### Essential Components
1. URIs
2. HTTP
3. Structured data with controlled vocabulary expressed in [[Resource Description Framework]] serialization formats such as [[RDFa]], [[RDF/XML]], [[N3]], [[Turtle]], or [[JSON LD Overview|Json-LD]]
4. [[Linked Data Platform]]

## JSON LD
JSON-LD is a light weight linked data format that is easy for humans to read and help provide a way Json Data to interoperate at a Web-Scale

### Example
```JSON
{
"@type": "Organization",
"name": "Allrecipes",
"url": "https://www.allrecipes.com",
"logo": {
"@type": "ImageObject",
"url": "https://www.allrecipes.com/thmb/Z9lwz1y0B5aX-cemPiTgpn5YB0k=/112x112/filters:no_upscale():max_bytes(150000):strip_icc()/allrecipes_logo_schema-867c69d2999b439a9eba923a445ccfe3.png",
"width": 112,
"height": 112
}
```

## Developers

### Playground
The JSON-LD Playground allows developers to view and debug JSON-LD data in a web based environment