from setuptools import setup

setup(
    name='lektor-markdown-excerpt',
    description='Adds filter for Markdown body excerpt.',
    author='Luka Zakrajsek',
    author_email='luka@bancek.net',
    url='http://github.com/bancek/lektor-markdown-excerpt',
    version='0.1',
    license='BSD',
    py_modules=['lektor_markdown_excerpt'],
    entry_points={
        'lektor.plugins': [
            'markdown-excerpt = lektor_markdown_excerpt:MarkdownExcerptPlugin',
        ]
    }
)
