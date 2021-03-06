from MarkdownInterpreter import split_md_into_sections, get_raw_content
from pprint import pprint

data = get_raw_content(repo = "https://github.com/kallewesterling/dhri-test-repo", branch = "v2.0")

sections = {}
sections['frontmatter'] = split_md_into_sections(data['content']['frontmatter'])
sections['theory-to-practice'] = split_md_into_sections(data['content']['theory-to-practice'])
sections['assessment'] = split_md_into_sections(data['content']['assessment'])

pprint(sections)


# Manually added meta-data here:

sections['frontmatter']['Name'] = 'Test Repository'
sections['frontmatter']['Parent backend'] = "Github"
sections['frontmatter']['Parent repo'] = "kallewesterling/dhri-test-repo"
sections['frontmatter']['Parent branch'] = "v2.0"


# Added part about saving:

from pathlib import Path
import json

Path("./workshop.json").write_text(json.dumps(sections))