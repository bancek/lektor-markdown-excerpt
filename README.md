# lektor-markdown-excerpt

This plugin adds filter for Markdown body excerpt.

## Enabling the Plugin

To enable the plugin run this command:

```ini
$ lektor plugins add markdown-excerpt
```

## In Templates

Plugin provides the `|excerpt` filter that can be used to render first
paragraph of Markdown:

```jinja
{{ post.body|excerpt }}
```

It takes one optional argument which is the separator for the excerpt:

```jinja
{{ post.body|excerpt:'\n\n##' }}
```
