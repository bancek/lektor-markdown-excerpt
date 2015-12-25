from lektor.pluginsystem import Plugin
from lektor.markdown import Markdown


class MarkdownExcerptPlugin(Plugin):
    name = u'Markdown Excerpt'
    description = u'Adds filter for Markdown body excerpt.'

    def on_setup_env(self, **extra):
        def excerpt(value, separator='\n\n'):
            excerpt_source = value.source.split(separator)[0]

            return Markdown(excerpt_source)

        self.env.jinja_env.filters['excerpt'] = excerpt
