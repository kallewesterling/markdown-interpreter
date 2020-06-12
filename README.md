# markdown-interpreter

## How to import

Import whatever parts of the package you need in your Python script:

```python
from MarkdownInterpreter import split_md_into_sections, get_raw_content
```

`split_md_into_sections` is the most useful function here but depends on markdown data that we will download directly from a GitHub source, using `get_raw_content`.

To get the data, we will run:

```python
data = get_raw_content(
  repo="https://github.com/kallewesterling/dhri-test-repo",
  branch="master"
)
```

Make sure the `repo` variable points to the base directory of a _public_ repository, and that the branch points to the correct branch that you want to use.

Since this function is created for the [DHRI-Curriculum](https://www.github.com/DHRI-Curriculum/), the repository must be also contain the following three files:
- frontmatter.md
- theory-to-practice.md
- assessment.md

In order to get the nicely shaped data output, you can run:

```python
sections = {}

sections['frontmatter'] = split_md_into_sections(data['content']['frontmatter'])

sections['theory-to-practice'] = split_md_into_sections(data['content']['theory-to-practice'])

sections['assessment'] = split_md_into_sections(data['content']['assessment'])
```

Note that the `split_md_into_sections` can take two optional variables (that are not provided here):

- `remove_empty_headings` which determines whether empty dictionary keys (headings) should be removed from the dictionary (bool; defaults to `True`)

- `bulletpoints_to_lists` which determines whether sections that contain ONLY bulletpoints should be converted into python lists with each bullet point as an element in the list (bool; defaults to `True`)
